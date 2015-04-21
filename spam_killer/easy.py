# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:51:51 2015

@author: Taikor
"""

from .file_converter_baseClass import converter
from .spam_filter_baseClass import spam_filter


def easy(file_path, rule_path):
    excel_to_txt_con = converter(file_path, "Excel", "Txt")
    new_path = excel_to_txt_con()
    
    text_file_path = new_path
    blackList_file_path = rule_path
    our_filter = spam_filter(text_file_path, blackList_file_path)
    filted_file_path = our_filter.kw_spam_rm()
    
    txt_to_excel_con = converter(filted_file_path, "Txt", "Excel")
    result_path = txt_to_excel_con()
    
    return result_path
    
    