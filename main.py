import pandas as pd
import numpy as np

class Part_Number_Class:

    def __init__(self,part_number_code,category= "", price_budget = 0):
        months_per_year = 12
        start_var = [0] * months_per_year
        self.part_number_code = part_number_code
        self.category = category
        self.price_budget = price_budget
        self.price_YTD = start_var
        self.price_YTG = start_var
        self.volume_budget = start_var
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

    def printPN(self):
        print("PN: {}".format(self.part_number_code))
        print("Category: {}".format(self.category))
        print("pricePAF: {}".format(self.price_budget))
        print("priceYTD: {}".format(self.price_YTD))
        print("priceYTG: {}".format(self.price_YTG))
        print("volumePAF: {}".format(self.volume_budget))
        print("volumeYTD: {}".format(self.volume_YTD))
        print("volumeYTG: {}".format(self.volume_YTG))

savingsFile = pd.ExcelFile(r'.\inputs\Test.xlsx')
budget_raw_array = np.array(pd.read_excel(savingsFile,sheet_name="PAF"))
ytd_raw_array = np.array(pd.read_excel(savingsFile,sheet_name="YTD"))
ytg_raw_array = np.array(pd.read_excel(savingsFile,sheet_name="YTG"))

part_number_code_list = budget_raw_array[:,0]
category_list = budget_raw_array[:,1]
price_budget_list = budget_raw_array[:,2]

part_number_amount = len(part_number_code_list)
part_number_list = [Part_Number_Class(part_number_code_list[i],category_list[i],price_budget_list[i]) for i in range (part_number_amount)]

for item in part_number_list:
    print(item)





