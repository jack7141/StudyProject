import os
import datetime
import argparse

from hhl_es_requester import HhlESRequester
from hhl_db_requester import HhlDBRequester
from hhl_ssh_requester import HhlSSHRequester

from decorators import store_to_xlsx
from xlsx_writer import writer
from utils import SSHTunnel


class HHLDataManager:
    def __init__(self, api_url, api_token, db_host, db_port, db_user, db_passwd):
        self.es_requester = HhlESRequester(api_url=api_url, token=api_token)        
        self.db_requester = HhlDBRequester(
            db_user=db_user,
            db_passwd=db_passwd, 
            db_host=db_host,
            db_port=db_port
        )
    
    @store_to_xlsx(writer=writer, list_key_name='records', sheet_name='월별가입자수')
    def store_signup_counts_by_month(self):        
        return self.db_requester.get_signup_counts_by_month()
        
    @store_to_xlsx(writer=writer, list_key_name='records', sheet_name='월별방문자수')
    def store_visit_counts_by_month(self):        
        return self.db_requester.get_visit_counts_by_month()
        
    @store_to_xlsx(writer=writer, list_key_name='records', sheet_name='일별방문자수')
    def store_visit_counts_by_day(self):        
        return self.db_requester.get_visit_counts_by_day()        
        
    @store_to_xlsx(writer=writer, list_key_name='records', sheet_name='월별 펀드변경 수')
    def store_fund_change_counts_by_month(self):        
        return self.db_requester.get_fund_change_counts_by_month()
        
    @store_to_xlsx(writer=writer, list_key_name='records', sheet_name='월별 펀드변경 취소 수')
    def store_fund_change_cancel_counts_by_month(self):        
        return self.db_requester.get_fund_change_cancel_counts_by_month()   
        
    @store_to_xlsx(writer=writer, list_key_name='records', sheet_name='서비스별 호출 수')
    def store_hits_all_api(self):        
        return self.es_requester.get_hits_all_api()
    
    @staticmethod
    @store_to_xlsx(writer=writer, list_key_name='records', sheet_name='System')
    def store_system_report(remote_key_path, remote_host_list):
        report_list = list()
        for remote_host in remote_host_list:
            alias = remote_host[0]
            host = remote_host[1]
            username = remote_host[2]
            
            with HhlSSHRequester(
                ssh_host=host, ssh_username=username, remote_key_path=remote_key_path, host_alias=alias
            ) as ssh_requester:       
                report = ssh_requester.get_system_report()
                report_list.append(report)
            
        
        return report_list
    
    @staticmethod
    @store_to_xlsx(writer=writer, list_key_name='records', sheet_name='AWS Redis')
    def store_redis_report(redis_host, redis_passwd):
        command = f'redis-cli -h {redis_host} -p 6379 -a {redis_passwd} INFO'
        output = os.popen(command).readlines()
        
        used_memory = 0
        max_memory = 0
        used_cpu_sys = 0
        used_cpu_user = 0
        uptime_in_seconds = 0
        
        for row in output:
            splits = row.split(':')
            if len(splits) < 2:
                continue 
            
            name = splits[0]
            value = splits[1]
            if name == 'used_memory':
                used_memory = int(value)
            elif name == 'maxmemory':
                max_memory = int(value)
            elif name == 'used_cpu_sys':
                used_cpu_sys = float(value)
            elif name == 'used_cpu_user':
                used_cpu_user = float(value)
            elif name == 'uptime_in_seconds':
                uptime_in_seconds = int(value)
            
        
        if max_memory == 0:
            raise ValueError('redis max_memory is 0')
            
        if uptime_in_seconds == 0:
            raise ValueError('redis uptime_in_seconds is 0')
            
        cpu_usage = round((used_cpu_sys + used_cpu_user) / uptime_in_seconds * 100, 2)
        memory_usage = round(used_memory / max_memory * 100, 2)
        
        return [{
            'NAME': 'AWS-REDIS',
            'HOST': redis_host,
            'CPU': str(cpu_usage) + '%',
            'MEM': str(memory_usage) + '%'
        }]
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='hhl statistics generator')

    parser.add_argument("-v", "--verbosity", type=str,
                        choices=['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL'],
                        help="increase output verbosity", default='INFO')

    parser.add_argument('-dh', '--db-host', help='db host', required=True)
    parser.add_argument('-du', '--db-user', help='db user', required=True)
    parser.add_argument('-dp', '--db-passwd', help='db password', required=True)
    parser.add_argument('-eu', '--es-url', help='es domain', required=True)
    parser.add_argument('-et', '--es-api-token', help='es domain', required=True)
    parser.add_argument('-rh', '--redis-host', help='redis host', required=True)
    parser.add_argument('-rp', '--redis-passwd', help='redis passwd', required=True)
    
    
    args = parser.parse_args()
            
    es_api_url = f"{args.es_url}/hwl-dev-*/_search"
    es_api_token = args.es_api_token
        
    db_host = args.db_host
    db_user = args.db_user
    db_passwd = args.db_passwd
    
    redis_host = args.redis_host
    redis_passwd = args.redis_passwd
    
    remote_key_path = '/app/fount-ssh-key.pem'
    remote_host_list = [
        ('WAS-A', '10.10.40.238', 'ubuntu'),
        ('WAS-C', '10.10.50.100', 'ubuntu'),
        ('WEB-A', '10.10.20.7', 'ubuntu'),
        ('WEB-C', '10.10.30.61', 'ubuntu'),
        ('ELK', '10.10.50.172', 'ubuntu'),
    ]
        
    try:    
        manager = HHLDataManager(
            api_url=es_api_url, 
            api_token=es_api_token, 
            db_host=db_host,
            db_port=3306,
            db_user=db_user,
            db_passwd=db_passwd
        )
        
        manager.store_signup_counts_by_month()
        manager.store_visit_counts_by_day()
        manager.store_visit_counts_by_month()
        manager.store_fund_change_counts_by_month()
        manager.store_fund_change_cancel_counts_by_month()
        manager.store_hits_all_api()
        
        HHLDataManager.store_system_report(remote_key_path=remote_key_path, remote_host_list=remote_host_list)
        HHLDataManager.store_redis_report(redis_host=redis_host, redis_passwd=redis_passwd)
        
        writer.close()
        
    except Exception as e:
        print(e)
