# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:01:29 2015

@author: Taikor
"""


import xlrd
from .lib import retrive_basename, retrive_dirname


class converter:
    
    EXCEL = 'excel'
    TXT = 'txt'
    CSV = 'csv'
    # define Marcos here
    
    def __init__(self, file_path, from_, to_):
        self.file_path = file_path
        self.from_ = str.lower(from_)
        self.to_ = str.lower(to_)
        
    def xls_to_TABtxt_converter(self):
        workbook = xlrd.open_workbook(self.file_path)
        sheet = workbook.sheet_by_index(0)    # retrive the very first sheet in excel file
        nrows = sheet.nrows
        ncols = sheet.ncols

        lines = list()        
        for row in range(nrows):
            line = ""
            for col in range(ncols):
                line = line + str(sheet.cell_value(row, col)) + "\t"
            line = line[:-1]   # remove the a special character: \t
            line = line + '\n' # add the a special character: \n
            lines.append(line)
        str_lines = "".join(lines)
        return str_lines        
        
            
    def __call__(self):
        if (self.from_ == converter.EXCEL) and (self.to_ == converter.TXT):
            txt_str = self.xls_to_TABtxt_converter()
            
            filted_basename = retrive_basename(self.file_path).replace('xlsx', 'txt')
            filted_dirname = retrive_dirname(self.file_path)
            path = filted_dirname + '\\' + filted_basename
            
            with open(path, 'w') as f:
                f.write(txt_str)
                
            print('cc')
        
        else:
            print('Error')
        
