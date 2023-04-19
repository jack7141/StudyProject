import json
import sys

from xlsxwriter import Workbook
from utils import get_today_file_name, SingletonClass


class XLSXWriter(SingletonClass):
    def __init__(self, output_file_name):
        self.wb = Workbook(output_file_name)
    
    def close(self):
        self.wb.close()
        
    def get_or_create_sheet(self, sheet_name):
        ws = self.wb.get_worksheet_by_name(sheet_name)
        if not ws:
            ws = self.wb.add_worksheet(sheet_name)
        
        return ws
    
    def json_to_xlsx(self, json, list_key_name, sheet_name):
        ws = self.get_or_create_sheet(sheet_name)
        
        dict_list = json[list_key_name]
        ordered_list = list(dict_list[0].keys())

        first_row = 0
        for header in ordered_list:
            col=ordered_list.index(header) 
            ws.write(first_row,col,header)

        row = 1
        for entry in dict_list:
            for _key,_value in entry.items():
                col=ordered_list.index(_key)
                ws.write(row,col,_value)
            row += 1
        
        
writer = XLSXWriter(output_file_name="/app/datas/" + get_today_file_name(prefix='hhl_statistics', extension='xlsx'))