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
import csv


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
        part_number_string = "Part number code: {0}\n" \
                             "Category: {1}\n" \
                             "Price:\n" \
                             "  Budget: {2}\n" \
                             "  YTD:{3}\n" \
                             "  YTG: {4}\n" \
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
            ytd_avg = sum(self.price_ytd) / len(self.price_ytd)
            self.price_ytg = [ytd_avg] * (12 - report_month)
        elif strategy == 3:
            base_price = price_info[0]
            inflation_value = price_info[1]
            inflation_month = int(price_info[2])
            price_ytg = np.array([base_price] * 12)
            list_position = inflation_month - 1
            new_value = base_price * (1 + inflation_value)
            price_ytg[range(list_position, 11)] = new_value
            self.price_ytg = price_ytg[range(int(report_month - 1), 11)]
        elif strategy == 4:
            self.price_ytg = price_info[range(int(report_month - 1), 11)]


def update_ytd_from_list_search(code, pn_list, price_ytd, volume_ytd):
    part_of_list = False
    for item in pn_list:
        if item.code == code:
            item.update_ytd(price_ytd, volume_ytd)
            part_of_list = True
    return part_of_list


def update_ytg_from_list_search(code, pn_list, price_ytg, volume_ytg, strategy, report_month_lc):
    part_of_list = False
    for item in pn_list:
        if item.code == code:
            item.update_ytg(price_ytg, volume_ytg, strategy, report_month_lc)
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


def array_to_attribute_ytd(code_list_ytd_lc, part_number_list_lc, price_ytd_list_lc, volume_ytd_list_lc):
    # sweep code list from YTD data in order to update Part Number objects
    for i in range(len(code_list_ytd_lc)):
        # if code is found on part-number list, we update price and volume information
        x = update_ytd_from_list_search(code_list_ytd_lc[i], part_number_list_lc, price_ytd_list_lc[i, :],
                                        volume_ytd_list_lc[i, :])

        # If code is not found, we will find predecessor and use its budget information to create a new object, assign
        # attributes and add to part-number list.
        if not x:
            code_from_predecessor = predecessor_search(code_list_ytd_lc[i], predecessor_match)
            part_number_from_predecessor = part_number_list_search(code_from_predecessor, part_number_list_lc)
            category_from_predecessor = part_number_from_predecessor.category
            price_budget_from_predecessor = part_number_from_predecessor.price_budget
            volume_budget_from_predecessor = part_number_from_predecessor.volume_budget
            part_number_add = PartNumberClass(code_list_ytd_lc[i], category_from_predecessor,
                                              price_budget_from_predecessor, volume_budget_from_predecessor)
            part_number_list_lc.append(part_number_add)
            update_ytd_from_list_search(part_number_add.code, part_number_list_lc, price_ytd_list_lc[i, :],
                                        volume_ytd_list_lc[i, :])


def array_to_attribute_ytg(code_list_ytg_lc, part_number_list_lc, price_ytg_list_lc, volume_ytg_list_lc):
    # sweep code list from YTG data in order to update Part Number objects
    for i in range(len(code_list_ytg_lc)):
        # if code is found on part-number list, we update price and volume information
        x = update_ytg_from_list_search(code_list_ytg_lc[i], part_number_list_lc, price_ytg_list_lc[i, :],
                                        volume_ytg_list_lc[i, :], ytg_strategy[i], report_month)

        # If code is not found, we will find predecessor and use its budget information to create a new object, assign
        # attributes and add to part-number list.
        if not x:
            code_from_predecessor = predecessor_search(code_list_ytg_lc[i], predecessor_match)
            part_number_from_predecessor = part_number_list_search(code_from_predecessor, part_number_list_lc)
            category_from_predecessor = part_number_from_predecessor.category
            price_budget_from_predecessor = part_number_from_predecessor.price_budget
            part_number_add = PartNumberClass(code_list_ytg_lc[i], category_from_predecessor,
                                              price_budget_from_predecessor)
            part_number_list_lc.append(part_number_add)
            y = update_ytg_from_list_search(code_list_ytg_lc[i], part_number_list_lc, price_ytg_list_lc[i, :],
                                            volume_ytg_list_lc[i, :], ytg_strategy[i], report_month)


# def save_part_number_csv(columns, part_number, writer):
#     my_data = {columns[0]: part_number.code}
#     writer.writerow(dict_data)
#
#
# def save_part_number_list_csv(file, columns, part_number_list):
#     with open(file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=columns)
#         writer.writeheader()
#     for item_lc in part_number_list:
#         save_part_number_csv(columns, item_lc, writer)

# inputs
report_month = 4
savingsFile = pd.ExcelFile(r'.\inputs\Test.xlsx')

########################################## BUDGET SECTION ############################################################
# getting raw data from Excel file
budget_raw_array = np.array(pd.read_excel(savingsFile, sheet_name="PAF"))

# processing raw data
code_list = budget_raw_array[:, 0]
category_list = budget_raw_array[:, 1]
price_budget_list = budget_raw_array[:, 2]
volume_budget_list = budget_raw_array[:, [range(3, 15)]]

# converting arrays into attributes
part_number_amount = len(code_list)
part_number_list = [PartNumberClass(code_list[i], category_list[i], price_budget_list[i], volume_budget_list[i, :])
                    for i in range(part_number_amount)]

########################################## YTD SECTION ############################################################
# getting raw data from Excel file
ytd_raw_array = np.array(pd.read_excel(savingsFile, sheet_name="YTD"))
predecessor_match = np.array(pd.read_excel(savingsFile, sheet_name="Yhold"))

# processing raw data
code_list_ytd = ytd_raw_array[:, 0]
price_ytd_list = ytd_raw_array[:, range(1, 1 + report_month)]
volume_ytd_list = ytd_raw_array[:, range(13, 13 + report_month)]

# converting arrays into attributes
array_to_attribute_ytd(code_list_ytd, part_number_list, price_ytd_list, volume_ytd_list)

########################################## YTG SECTION ############################################################
# getting raw data from Excel file
ytg_raw_array = np.array(pd.read_excel(savingsFile, sheet_name="YTG"))

# processing raw data
code_list_ytg = ytg_raw_array[:, 0]
ytg_strategy = ytg_raw_array[:, 1]
volume_ytg_list = ytg_raw_array[:, range(report_month + 1, 13)]
price_ytg_list = ytg_raw_array[:, range(14, 25)]

# converting arrays into attributes
array_to_attribute_ytg(code_list_ytg, part_number_list, price_ytg_list, volume_ytg_list)


########################################## OUTPUTS ############################################################
# simple printing
# for i in range(len(part_number_list)):
#     print(part_number_list[i])

csv_file = r'.\outputs\Part Number Report.csv'

a = 'Code'
b = 'Category'
c = 'Price Budget'

csv_columns = [a, b, c]

data_array = np.array(csv_columns)
for item in part_number_list:
    new_row = [item.code, item.category, item.price_budget]
    data_array = np.vstack([data_array, new_row])

print(data_array)
myFile = open(csv_file, 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(data_array)


# save_part_number_list_csv(csv_file, csv_columns, part_number_list)