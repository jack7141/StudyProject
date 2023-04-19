import os
import paramiko


class HhlSSHRequester:
    def __init__(self, ssh_host, ssh_username, remote_key_path, host_alias=None):
        # key = paramiko.RSAKey.from_private_key_file(remote_key_path)
        # self.client = paramiko.SSHClient()
        # self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # self.client.connect(hostname=ssh_host, username=ssh_username, pkey=key)
        
        self.ssh_host = ssh_host
        self.ssh_username = ssh_username
        self.remote_key_path = remote_key_path
        self.host_alias = host_alias
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return None
        #return self.client.close()
        
    def _command(self, command):
        return os.popen(command).readlines()
        #stdin, stdout, stderr = self.client.exec_command(command)        
        # lines = stdout.readlines()
        # return lines
        
    def _get_memory_usage(self):
        command = f'ssh -oStrictHostKeyChecking=accept-new -i {self.remote_key_path} {self.ssh_username}@{self.ssh_host} free -m'
        output = self._command(command = command)
                
        mem_row = [entry for entry in output[1].split(' ') if entry != '']
            
        total_memory = float(mem_row[1])
        used_memory = float(mem_row[2])
        
        used_percent = round(used_memory / total_memory * 100, 2)
        used_percent = str(used_percent) + '%'
        return used_percent
    
    def _get_volume_usage(self):
        command = f'ssh -oStrictHostKeyChecking=accept-new -i {self.remote_key_path} {self.ssh_username}@{self.ssh_host} df -hT'
        output = self._command(command = command)
        
        output_table = []
        for row in output:
            output_table.append([entry for entry in row.split(' ') if entry != ''])
        
        root_mount_row = -1
        for idx, row in enumerate(output_table):
            if row[-1] == '/\n':
                root_mount_row = idx
                break
        
        if root_mount_row == -1:            
            raise ValueError('not found root mount point')
        
        return output_table[root_mount_row][-2]
    
    def _get_cpu_usage(self):
        command = f'ssh -oStrictHostKeyChecking=accept-new -i {self.remote_key_path} {self.ssh_username}@{self.ssh_host} mpstat'
        output = self._command(command = command)
        output_table = []
        for row in output:
            output_table.append([entry for entry in row.split(' ') if entry != ''])
        
        
        cpu_col = -1
        usage_col = -1
        for row in output_table:
            for idx, col in enumerate(row):
                if(col == "%usr"):
                    usage_col = idx
                if(col == "CPU"):
                    cpu_col = idx
                    
            if cpu_col != -1 and usage_col != -1:
                break
        
        for row in output_table:
            if len(row) <= max(cpu_col, usage_col):
                continue
            
            if row[cpu_col] == 'all':
                return str(row[usage_col]) + '%'                           
        
        print('COMMAND : ' + command)
        print('OUTPUT : ' + str(output))
        raise ValueError('not found cpu usage')
    
    def get_system_report(self):
        usage_list = list()
        cpu_usage = self._get_cpu_usage()
        memory_usage = self._get_memory_usage()
        volume_usage = self._get_volume_usage()
        
        return {
            'NAME': self.host_alias,
            'HOST': self.ssh_host,
            'CPU': cpu_usage,
            'MEM': memory_usage,
            'DISK': volume_usage
        }
