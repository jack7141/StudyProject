import pymysql

from utils import SSHTunnel


class HhlDBRequester(object):
    def __init__(self, db_user, db_passwd, db_host, db_port):
        self.conn = pymysql.connect(
            host=db_host, user=db_user, passwd=db_passwd, db=None,
            charset='utf8', port=db_port, 
            cursorclass=pymysql.cursors.DictCursor        
        )
        
        self.cursor = self.conn.cursor()
 
    def get_signup_counts_by_month(self):        
        query = """
            SELECT SUBSTRING(activated_at, 1, 7) as MONTH, COUNT(id) as COUNT
            FROM customer.customer WHERE is_active = 1
            GROUP BY SUBSTRING(activated_at, 1, 7) 
            ORDER BY activated_at ASC;
        """
        
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def get_visit_counts_by_month(self):
        query = """
            SELECT SUBSTRING(timestamp, 1, 7) as MONTH, SUM(count) as COUNT
            FROM dashboard.log_count_accessered_customer 
            GROUP BY SUBSTRING(timestamp, 1, 7)
            ORDER BY timestamp ASC;
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
        
    def get_visit_counts_by_day(self):
        query = """
            SELECT SUBSTRING(timestamp, 1, 10) as DAY, SUM(count) as COUNT
            FROM dashboard.log_count_accessered_customer 
            GROUP BY SUBSTRING(timestamp, 1, 10)
            ORDER BY timestamp ASC;
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results        

    def get_fund_change_counts_by_month(self):
        query = """
            SELECT SUBSTRING(created_at, 1, 7) as MONTH, COUNT(id) as COUNT
            FROM dashboard.log_change_portfolio
            WHERE is_success = 0
            GROUP BY SUBSTRING(created_at, 1, 7)
            ORDER BY created_at ASC
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
                
    def get_fund_change_cancel_counts_by_month(self):
        query = """
            SELECT SUBSTRING(created_at, 1, 7) as MONTH, COUNT(id) as COUNT
            FROM dashboard.log_cancel_portfolio
            WHERE is_success = 0
            GROUP BY SUBSTRING(created_at, 1, 7)
            ORDER BY created_at ASC
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results    