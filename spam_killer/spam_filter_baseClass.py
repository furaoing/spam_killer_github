# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:15:49 2015

@author: Taikor
"""


from .lib import kw_spam_detect, read_from_json, len_spam_detect, generate_newpath


class spam_filter:
    """ spam_filter base class """
    def __init__(self, file_path, rule_path):   
        self.kwargs_rules = read_from_json(rule_path)
        self.file_path = file_path
        self.kwargs_field_position = None
        self.fields = None
        self.field_position = 2
        self.min_len = 40
        
        
    def kw_spam_recognize(self, line):
        """ filting and remove spams via spam kewword search """
        return kw_spam_detect(line, self.kwargs_rules, self.kwargs_field_position)
        
    def len_spam_recognize(self, line):
        return len_spam_detect(line, self.field_position, self.min_len)
              
    def open_file(self, file_path):
        """ import data source from plain text file (routine) """ 
        with open(file_path, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            fields = lines.pop(0)    #remove the first element, which is the tag row in excel 
            self.fields = fields
            
            field_list = fields.split('\t')
            field_list[0] = field_list[0].strip('\ufeff')
            field_list[-1] = field_list[-1].strip('\n')
            self.kwargs_field_position = {key: field_list.index(key) for key in self.kwargs_rules.keys()}
            
            return lines
            
    def kw_batch_spam_rm(self):
        lines = self.open_file(self.file_path)
        offset = 0
        for i in range(len(lines)):
            if self.kw_spam_recognize(lines[i-offset]):
                del lines[i-offset]
                offset = offset + 1
        return lines
        
    def len_batch_spam_rm(self):
        lines = self.open_file(self.file_path)
        offset = 0
        for i in range(len(lines)):
            if self.len_spam_recognize(self, lines[i-offset]):
                del lines[i-offset]
                offset = offset + 1
        return lines
        
    def kw_spam_rm(self):
        lines = self.kw_batch_spam_rm()
        txt_string = self.fields+"".join(lines)
        
        prefix = '(kw_spamfilted) '
        f_path = generate_newpath(prefix, self.file_path)
        with open(f_path, 'w', encoding="utf-8") as f:
            f.write(txt_string)
        return f_path
            
    def len_spam_rm(self):
        lines = self.len_batch_spam_rm()
        txt_string = self.fields+"".join(lines)
        
        prefix = '(len_spamfilted) '
        f_path = generate_newpath(prefix, self.file_path)
        with open(f_path, 'w', encoding="utf-8") as f:
            f.write(txt_string)
        return f_path

