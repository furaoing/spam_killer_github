# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:30:01 2015

@author: Taikor
"""

kwargs_rules = {"SearchEngine": {'维权'}}
print(kwargs_rules.keys())

with open('UserID_WIP.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    fields = lines.pop(0)    #remove the first element, which is the tag row in excel 
            
    field_list = fields.split('\t')
    
    field_list[0] = field_list[0].strip('\ufeff')
    field_list[-1] = field_list[0].strip('\n')
    
    kwargs_field_position = {key: field_list.index(key) for key in kwargs_rules.keys()}

