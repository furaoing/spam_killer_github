# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:05:55 2015

@author: Taikor
"""

from spam_filter_baseClass import *

text_file_path = r'C:\workspace\Gagget\Python\Weibo_Spam_Filter\Sample_Data\UserID_WIP.txt'

blackList_file_path = r'C:\workspace\Gagget\Python\Weibo_Spam_Filter\Sample_Data\black_list.txt'


filter = spam_filter(text_file_path, blackList_file_path)

filter.kw_spam_rm()

