# TARGETS:
# import data from excel: OK
# cross data using a key OK
# load YTD using objects
# load YTD using arrays
# calculate YTG based on yearly readjustments
# load and save data using CSV
# save date on a excel file
# calculate savings
# plot data

import pandas as pd
import numpy as np

class Part_Number_Class:

    def __init__(self,part_number_code,category= "", price_budget = 0,volume_budget = [0] * 12):
        months_per_year = 12
        start_var = [0] * months_per_year
        self.part_number_code = part_number_code
        self.category = category
        self.price_budget = price_budget
        self.price_YTD = start_var
        self.price_YTG = start_var
        self.volume_budget = volume_budget
        self.volume_YTD = start_var
        self.volume_YTG = start_var
        self.part_number_ref = ""

    def __str__(self):
        part_number_string = "Part number code: {0}\n"\
                             "Category: {1}\n"\
                             "Price:\n"\
                             "  Budget: {2}\n"\
                             "  YTD:{3}\n"\
                             "  YTG: {4}\n"\
                             "Volume:\n" \
                             "  Budget: {5}\n" \
                             "  YTD:{6}\n" \
                             "  YTG: {7}\n" \
                             .format(self.part_number_code,self.category,self.price_budget,self.price_YTD,self.price_YTG,self.volume_budget,self.volume_YTD,self.volume_YTG)
        return part_number_string

    def update_YTD(self,price_YTD,volume_YTD):
        self.price_YTD = price_YTD
        self.volume_YTD = volume_YTD

def update_YTD_from_list_search(part_number_code,part_number_list,price_YTD,volume_YTD):
    part_of_list = False
    for item in part_number_list:
        if item.part_number_code == part_number_code:
            item.update_YTD(price_YTD, volume_YTD)
            part_of_list = True
    return part_of_list

def part_number_list_search(part_number_code,part_number_list):
    right_part_number = False
    for item in part_number_list:
        if item.part_number_code == part_number_code:
            right_part_number = item
    return right_part_number

def yhold_search(part_number_code,yhold_list):
    yhold = False
    for i in range(len(yhold_list)):
        if yhold_list[i,1] == part_number_code: yhold = yhold_list[i,0]
    return yhold

savingsFile = pd.ExcelFile(r'.\inputs\Test.xlsx')
budget_raw_array = np.array(pd.read_excel(savingsFile,sheet_name="PAF"))

part_number_code_list = budget_raw_array[:,0]
category_list = budget_raw_array[:,1]
# budget information
price_budget_list = budget_raw_array[:,2]
volume_budget_list = budget_raw_array[:,[3,14]]
# YTD information

# creating objects and assigning budgets
part_number_amount = len(part_number_code_list)
part_number_list = [Part_Number_Class(part_number_code_list[i],category_list[i],price_budget_list[i]) for i in range (part_number_amount)]

# for item in part_number_list:
#     print(item)

# assigning YTD
report_month = 4

ytd_raw_array = np.array(pd.read_excel(savingsFile,sheet_name="YTD"))
# print(ytd_raw_array.shape)
part_number_code_list_YTD = ytd_raw_array[:,0]
price_YTD_list = ytd_raw_array[:,range(1,1+report_month)]
volume_YTD_list = ytd_raw_array[:,range(13,13+report_month)]
yhold_match = np.array(pd.read_excel(savingsFile,sheet_name="Yhold"))

print(yhold_match)
x=yhold_search("PN-027",yhold_match)
print(x) # yholds is working, next step is to create new object with yhold reference

# for i in range(len(part_number_code_list_YTD)):
#     x = update_YTD_from_list_search(part_number_code_list_YTD[i],part_number_list,price_YTD_list[i,:],volume_YTD_list[i,:])
#     if not(x):
#         part_number_list[i] =  part_number_list_search(YHOLDREFERENCEHERE,part_number_list)
#     print(part_number_list[i])
# print(ytd_raw_array)
# print(part_number_list_YTD)

#ytg_raw_array = np.array(pd.read_excel(savingsFile,sheet_name="YTG"))












#
# # assigning YTD and YTG
# month_report = 3
# price_YTD #next step is assigning columns from master data array
# volume_YTD
# price_YTG
# volume_YTG
# master_data_array
#
# for item in part_number_list:
#     item.update_YTD_and_YTG()
#     print(item)


