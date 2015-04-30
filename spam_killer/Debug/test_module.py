__author__ = 'Taikor'

from spam_killer import converter
from spam_killer import spam_filter
from spam_killer import easy

""" Test Converter functionality (xlsx to txt)

file_path = "C:\workspace\Github_MasterRepository\spam_killer_github\spam_killer\Debug\汽车3.xlsx"
excel_to_txt_con = converter(file_path, "Excel", "Txt")

new_path = excel_to_txt_con()

print(new_path)

"""

""" Test spam_filter functionality

text_file_path = 'C:\workspace\Github_MasterRepository\spam_killer_github\spam_killer\Debug\汽车3.txt'
blackList_file_path = 'C:\workspace\Github_MasterRepository\spam_killer_github\spam_killer\Debug\kw.txt'
our_filter = spam_filter(text_file_path, blackList_file_path)
filted_file_path = our_filter.kw_spam_rm()
print(filted_file_path)

"""

"""
 Test Converter functionality (txt to xlsx)

filted_file_path = 'C:\workspace\Github_MasterRepository\spam_killer_github\spam_killer\Debug\(kw_spamfilted) 汽车3.txt'
txt_to_excel_con = converter(filted_file_path, "Txt", "Excel")
result_path = txt_to_excel_con()
"""

file_path = "C:\workspace\Github_MasterRepository\spam_killer_github\spam_killer\Debug\汽车3.xlsx"
blackList_file_path = 'C:\workspace\Github_MasterRepository\spam_killer_github\spam_killer\Debug\kw.txt'
easy(file_path, blackList_file_path)