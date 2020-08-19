# TARGETS:
# import data from excel: OK
# cross data using a key OK
# load YTD using objects OK
# load YTD using arrays LATER
# Implement predecessor OK
# calculate ytg based on different scenarios OK
# load and save data using CSV
# break ytg calculations into many different functions
# avoid args with [i,:]
# use different files for functions and classes
# group repetitive codes into functions
# save date on a excel file
# calculate savings
# plot data
# unity conversion


import pandas as pd
import numpy as np
import csv


class PartNumberClass:

    def __init__(self, code, category="", price_budget=0):
        months_per_year = 12
        array_of_zeros = np.full((1, months_per_year), 0)
        self.code = code                     # string
        self.category = category             # string
        self.price_budget = price_budget     # float
        self.price = array_of_zeros          # np array of floats
        self.volume_budget = array_of_zeros  # np array of floats
        self.volume = array_of_zeros         # np array of floats
        self.part_number_ref = code          # string

    def __str__(self):
        part_number_string = "Part number code: {0}\n" \
                             "Category: {1}\n" \
                             "Price:\n" \
                             "  Budget: {2}\n" \
                             "  {3}\n" \
                             "Volume:\n" \
                             "  Budget: {4}\n" \
                             "  {5}\n" \
            .format(self.code, self.category, self.price_budget, self.price,
                    self.volume_budget, self.volume)
        return part_number_string

    def update_ytd_price(self, price_ytd_lc):
        for ii_lc in range(0, len(price_ytd_lc)):
            self.price[0, ii_lc] = price_ytd_lc[ii_lc]

    def update_ytd_volume(self, volume_ytd_lc):
        for ii_lc in range(0, len(volume_ytd_lc)):
            self.volume[0, ii_lc] = volume_ytd_lc[ii_lc]

    def update_ytd(self, price_ytd_lc, volume_ytd_lc):
        print(self.code)
        print(price_ytd_lc)
        print(volume_ytd_lc)
        print(self.price)
        print(self.volume)
      
        self.update_ytd_price(price_ytd_lc)
        print("update ytd price")
        print(self.code)
        print(price_ytd_lc)
        print(volume_ytd_lc)
        print(self.price)
        print(self.volume)

        self.update_ytd_volume(volume_ytd_lc)

        print("update ytd volume")
        print(self.code)
        print(price_ytd_lc)
        print(volume_ytd_lc)
        print(self.price)
        print(self.volume)



    def update_ytg(self, price_info, volume_ytg_lc, strategy, report_month_lc):
        len_ytg = 12 - report_month_lc
        price_ytg = np.full((1, len_ytg), 0)
        if strategy == 1:
            price_ytg[0:len_ytg:1] = self.price_budget
        elif strategy == 2:
            price_ytd = self.price[0, 0:report_month_lc+1:1]
            ytd_avg = sum(price_ytd) / len(price_ytd)
            price_ytg[0:len_ytg:1] = ytd_avg
        elif strategy == 3:
            base_price = float(price_info[0])
            inflation_value = float(price_info[1])
            price_ytg[0:len_ytg:1] = base_price
            inflation_month = int(price_info[2])
            if inflation_month > report_month_lc:
                new_value = base_price * (1 + inflation_value)
                price_ytg[inflation_month:12:1] = new_value
        elif strategy == 4:
            price_ytg = price_info

        for ii_lc in range(report_month_lc, 11):
            ytg_position = ii_lc - report_month_lc
            # print(self.code)
            # print(strategy)
            # print(self.price)
            # print(price_ytg)
            self.price[0, ii_lc] = price_ytg[0, ytg_position]
            self.volume[0, ii_lc] = volume_ytg_lc[ytg_position]


    def update_volume_budget(self, volume_budget_lc):
        self.volume_budget = volume_budget_lc


def update_volume_budget_part_number_list(part_number_list_lc, volume_budget_array_lc):
    for item_lc in part_number_list_lc:
        ii = 0
        volume_item_lc = volume_budget_array_lc[ii, :]
        item_lc.update_volume_budget(volume_item_lc)
        ii = ii + 1


def update_ytd_from_list_search(code, pn_list, price_ytd_lc, volume_ytd_lc):
    part_of_list = False
    for item_lc in pn_list:
        if item_lc.code == code:
            item_lc.update_ytd(price_ytd_lc, volume_ytd_lc)
            part_of_list = True
    return part_of_list


def update_ytg_from_list_search(code, pn_list, price_ytg, volume_ytg, strategy, report_month_lc):  #
    part_of_list = False
    for item_lc in pn_list:
        if item_lc.code == code:
            item_lc.update_ytg(price_ytg, volume_ytg, strategy, report_month_lc)
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


def array_to_attribute_budget(self, volume_budget_lc):
    for ii_lc in range(0, 11):
        self.volume_budget[ii_lc] = volume_budget_lc[ii_lc]


# Opportunity: create a list of object following code list from YTD file
def array_to_attribute_ytd(code_list_ytd_lc, part_number_list_lc, price_ytd_list_lc, volume_ytd_list_lc):
    # sweep code list from YTD data in order to update Part Number objects
    for i in range(len(code_list_ytd_lc)):
        # if code is found on part-number list, we update price and volume information
        item_code = code_list_ytd_lc[i]
        item_price_ytd_list = price_ytd_list_lc[i, :]
        item_volume_ytd_list = volume_ytd_list_lc[i, :]

        is_part_of_list = update_ytd_from_list_search(item_code, part_number_list_lc, item_price_ytd_list,
                                                      item_volume_ytd_list)

        # If code is not found, we will find predecessor and use its budget information to create a new object, assign
        # attributes and add to part-number list.
        if not is_part_of_list:
            code_from_predecessor = predecessor_search(code_list_ytd_lc[i], predecessor_match)
            part_number_from_predecessor = part_number_list_search(code_from_predecessor, part_number_list_lc)
            category_from_predecessor = part_number_from_predecessor.category
            price_budget_from_predecessor = part_number_from_predecessor.price_budget
            volume_budget_from_predecessor = part_number_from_predecessor.volume_budget
            part_number_add = PartNumberClass(code_list_ytd_lc[i], category_from_predecessor,
                                              price_budget_from_predecessor)
            part_number_add.update_volume_budget = volume_budget_from_predecessor
            part_number_list_lc.append(part_number_add)
            update_ytd_from_list_search(part_number_add.code, part_number_list_lc, item_price_ytd_list,
                                        item_volume_ytd_list)


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
            volume_budget_from_predecessor = part_number_from_predecessor.volume_budget
            part_number_add = PartNumberClass(code_list_ytg_lc[i], category_from_predecessor,
                                              price_budget_from_predecessor)
            part_number_add.update_volume_budget = volume_budget_from_predecessor
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

########################################## BUDGET SECTION ############################################################
# getting raw data from Excel file
budget_file = pd.ExcelFile(r'.\inputs\Test.xlsx')
budget_sheet_name = "PAF"
code_position_at_budget = 0
category_position_at_budget = 1
price_budget_position_at_budget = 2
volume_budget_position_at_budget = [3, 15]

budget_raw_array = np.array(pd.read_excel(budget_file, sheet_name=budget_sheet_name))

# processing raw data
code_array = budget_raw_array[:, code_position_at_budget]
category_array = budget_raw_array[:, category_position_at_budget]
price_budget_array = budget_raw_array[:, price_budget_position_at_budget]
volume_budget_array = budget_raw_array[:, [range(volume_budget_position_at_budget[0],
                                                 volume_budget_position_at_budget[1])]]

# converting arrays into attributes
part_number_amount = code_array.shape[0]

part_number_list = [PartNumberClass(code_array[i], category_array[i], price_budget_array[i])
                    for i in range(part_number_amount)]

update_volume_budget_part_number_list(part_number_list, volume_budget_array)

########################################## YTD SECTION ############################################################
# getting raw data from Excel file
ytd_file = pd.ExcelFile(r'.\inputs\Test.xlsx')
ytd_sheet_name = "YTD"
code_position_at_ytd = 0
price_position_at_ytd = 1
volume_position_at_ytd = 13

predecessor_sheet_name = "Yhold"
predecessor_file = pd.ExcelFile(r'.\inputs\Test.xlsx')

ytd_raw_array = np.array(pd.read_excel(ytd_file, sheet_name=ytd_sheet_name))
predecessor_match = np.array(pd.read_excel(predecessor_file, sheet_name=predecessor_sheet_name))

# processing raw data
code_array_ytd = ytd_raw_array[:, code_position_at_ytd]
price_ytd_array = ytd_raw_array[:, range(price_position_at_ytd, price_position_at_ytd + report_month)]
volume_ytd_array = ytd_raw_array[:, range(volume_position_at_ytd, volume_position_at_ytd + report_month)]

# converting arrays into attributes
array_to_attribute_ytd(code_array_ytd, part_number_list, price_ytd_array, volume_ytd_array)

########################################## YTG SECTION ############################################################
# getting raw data from Excel file
ytg_file = pd.ExcelFile(r'.\inputs\Test.xlsx')
ytg_sheet_name = "YTG"
ytg_raw_array = np.array(pd.read_excel(ytg_file, sheet_name=ytg_sheet_name))
code_position_at_ytg = 0
strategy_position_at_ytg = 1
volume_position_at_ytg = 13
price_position_at_ytg = [14, 25]

# processing raw data
code_array_ytg = ytg_raw_array[:, code_position_at_ytg]
ytg_strategy = ytg_raw_array[:, strategy_position_at_ytg]
volume_ytg_array = ytg_raw_array[:, range(report_month + 1, volume_position_at_ytg)]
price_ytg_array = ytg_raw_array[:, range(price_position_at_ytg[0], price_position_at_ytg[1])]

# converting arrays into attributes
# array_to_attribute_ytg(code_array_ytg, part_number_list, price_ytg_array, volume_ytg_array)

for item in part_number_list:
    print(item)
########################################## OUTPUTS ############################################################
# simple printing
# for i in range(len(part_number_list)):
#     print(part_number_list[i])
#
# csv_file = r'.\outputs\Part Number Report.csv'
#
# csv_columns = ['Code', 'Category', 'Price Budget', "Bgt V01", "Bgt V02", "Bgt V03", "Bgt V04", "Bgt V05", "Bgt V06",
#                "Bgt V07", "Bgt V08", "Bgt V09", "Bgt V10", "Bgt V11", "Bgt V12", "P01", "P02", "P03", "P04", "P05",
#                "P06", "P07", "P08", "P09", "P10", "P11", "P12", "V01", "V02", "V03", "V04", "V05", "V06", "V07",
#                "V08", "V09", "V10", "V11", "V12"]
#
# data_array = np.array(csv_columns)
# item = part_number_list[1]
# # for item in part_number_list:
#
# price = item.price
# volume = item.volume
#
# new_row = np.array(item.code)
# print("+code: {}".format(new_row))
# new_row = np.append(new_row, item.category)
# print("+category: {}".format(len(new_row)))
# new_row = np.append(new_row, item.price_budget)
# print("+price bgt: {}".format(len(new_row)))
# print(len(item.volume_budget))
# for ii in range(0, len(item.volume_budget) - 1):
#     new_row = np.append(new_row, item.volume_budget[ii])
# print("+volume bgt: {}".format(len(new_row)))
#
# for ii in range(0, len(price) - 1):
#     new_row = np.append(new_row, price[ii])
# print("+price: {}".format(len(new_row)))
# for ii in range(0, len(volume) - 1):
#     new_row = np.append(new_row, volume[ii])
# print("+volume: {}".format(len(new_row)))
#
# print(len(csv_columns))
# print(len(new_row))
# # myFile = open(csv_file, 'w')
# # with myFile:
# #     writer = csv.writer(myFile)
# #     writer.writerows(data_array)
#
#
# # save_part_number_list_csv(csv_file, csv_columns, part_number_list)
