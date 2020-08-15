# TARGETS:
# import data from excel: OK
# cross data using a key OK
# load YTD using objects OK
# load YTD using arrays LATER
# Implement inheritance (predecessor) OK
# calculate ytg based on different scenarios OK
# load and save data using CSV
# save date on a excel file
# calculate savings
# plot data
# unity conversion

import pandas as pd
import numpy as np


class PartNumberClass:

    def __init__(self, code, category="", price_budget=0, volume_budget=[0] * 12):
        months_per_year = 12
        start_var = [0] * months_per_year
        self.code = code
        self.category = category
        self.price_budget = price_budget
        self.price_ytd = start_var
        self.price_ytg = start_var
        self.volume_budget = volume_budget
        self.volume_ytd = start_var
        self.volume_ytg = start_var
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
                             .format(self.code, self.category, self.price_budget, self.price_ytd,
                                     self.price_ytg, self.volume_budget, self.volume_ytd, self.volume_ytg)
        return part_number_string

    def update_ytd(self, price_ytd, volume_ytd):
        self.price_ytd = price_ytd
        self.volume_ytd = volume_ytd


    def update_ytg(self, price_info, volume_ytg, strategy, report_month):
        self.volume_ytg = volume_ytg
        if strategy == 1:
            self.price_ytg = [self.price_budget] * (12 - report_month)
        elif strategy == 2:
            ytd_avg = sum(self.price_ytd)/len(self.price_ytd)
            self.price_ytg = [ytd_avg] * (12 - report_month)
        elif strategy == 3:
            base_price = price_info[0]
            inflation_value = price_info[1]
            inflation_month = int(price_info[2])
            price_ytg = np.array([base_price] * 12)
            list_position = inflation_month - 1
            new_value = base_price * (1 + inflation_value)
            price_ytg[range(list_position, 11)] = new_value
            self.price_ytg = price_ytg[range(int(report_month-1), 11)]
        elif strategy == 4:
            self.price_ytg = price_info[range(int(report_month-1), 11)]


def update_ytd_from_list_search(code, pn_list, price_ytd, volume_ytd):
    part_of_list = False
    for item in pn_list:
        if item.code == code:
            item.update_ytd(price_ytd, volume_ytd)
            part_of_list = True
    return part_of_list


def update_ytg_from_list_search(code, pn_list, price_ytg, volume_ytg, strategy, report_month):
    part_of_list = False
    for item in pn_list:
        if item.code == code:
            item.update_ytg(price_ytg, volume_ytg, strategy, report_month)
            part_of_list = True
    return part_of_list


def part_number_list_search(code, pn_list):
    right_part_number = False
    for item in pn_list:
        if item.code == code:
            right_part_number = item
    return right_part_number


def predecessor_search(code, predecessor_list):
    predecessor = False
    for i in range(len(predecessor_list)):
        if predecessor_list[i, 1] == code:
            predecessor = predecessor_list[i, 0]
    return predecessor


savingsFile = pd.ExcelFile(r'.\inputs\Test.xlsx')
budget_raw_array = np.array(pd.read_excel(savingsFile, sheet_name="PAF"))

code_list = budget_raw_array[:, 0]
category_list = budget_raw_array[:, 1]
# budget information
price_budget_list = budget_raw_array[:, 2]
volume_budget_list = budget_raw_array[:, [3, 14]]
# YTD information

# creating objects and assigning budgets
part_number_amount = len(code_list)
part_number_list = [PartNumberClass(code_list[i], category_list[i], price_budget_list[i])
                    for i in range(part_number_amount)]

# for item in part_number_list:
#     print(item)

# assigning YTD
report_month = 4

ytd_raw_array = np.array(pd.read_excel(savingsFile, sheet_name="YTD"))
# print(ytd_raw_array.shape)
code_list_ytd = ytd_raw_array[:, 0]
price_ytd_list = ytd_raw_array[:, range(1, 1+report_month)]
volume_ytd_list = ytd_raw_array[:, range(13, 13+report_month)]
predecessor_match = np.array(pd.read_excel(savingsFile, sheet_name="Yhold"))

for i in range(len(code_list_ytd)):
    x = update_ytd_from_list_search(code_list_ytd[i], part_number_list, price_ytd_list[i, :],
                                    volume_ytd_list[i, :])
    if not x:
        code_from_predecessor = predecessor_search(code_list_ytd[i], predecessor_match)
        part_number_from_predecessor = part_number_list_search(code_from_predecessor, part_number_list)
        category_from_predecessor = part_number_from_predecessor.category
        price_budget_from_predecessor = part_number_from_predecessor.price_budget
        part_number_add = PartNumberClass(code_list_ytd[i], category_from_predecessor, price_budget_from_predecessor)
        part_number_list.append(part_number_add)
        y = update_ytd_from_list_search(part_number_add.code, part_number_list, price_ytd_list[i, :],
                                        volume_ytd_list[i, :])

ytg_raw_array = np.array(pd.read_excel(savingsFile, sheet_name="YTG"))
code_list_ytg = ytg_raw_array[:, 0]
ytg_strategy = ytg_raw_array[:, 1]
volume_ytg_list = ytg_raw_array[:, range(report_month+1, 13)]
price_ytg_list = ytg_raw_array[:, range(14, 25)]

for i in range(len(code_list_ytg)):
    x = update_ytg_from_list_search(code_list_ytg[i], part_number_list, price_ytg_list[i, :],
                                    volume_ytg_list[i, :], ytg_strategy[i], report_month)
    if not x:
        code_from_predecessor = predecessor_search(code_list_ytg[i], predecessor_match)
        part_number_from_predecessor = part_number_list_search(code_from_predecessor, part_number_list)
        category_from_predecessor = part_number_from_predecessor.category
        price_budget_from_predecessor = part_number_from_predecessor.price_budget
        part_number_add = PartNumberClass(code_list_ytg[i], category_from_predecessor, price_budget_from_predecessor)
        part_number_list.append(part_number_add)
        y = update_ytg_from_list_search(code_list_ytg[i], part_number_list, price_ytg_list[i, :],
                                        volume_ytg_list[i, :], ytg_strategy[i], report_month)



print(len(part_number_list))
for i in range(len(part_number_list)):
    print(i)
    print(part_number_list[i])

# print(part_number_list_ytd)













