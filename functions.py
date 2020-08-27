#############################                1) DATA CLEANING                     ######################################

def file_column_integrity(dataframe, column_expected_list):
    error_list = []
    columns_to_delete = []
    raw_column_list = dataframe.columns.tolist()
    column_integrity = True

    for ii in range(1, len(column_expected_list)):
        is_part_of_raw_column_list = column_expected_list[ii] in raw_column_list
        if not is_part_of_raw_column_list:
            error_list.append(column_expected_list[ii])
        column_integrity = column_integrity and is_part_of_raw_column_list

    for jj in range(1, len(raw_column_list)):
        is_part_of_expected_list = raw_column_list[jj] in column_expected_list
        if not is_part_of_expected_list:
            columns_to_delete.append(raw_column_list[jj])

    return [columns_to_delete, column_integrity, error_list]

def list_differential(old_list, new_list):
    item_diff = []

    for old_item in old_list:

        if old_item not in new_list:
            item_diff.append(old_item)

    return item_diff


def generate_wide_act_raw_column_expected_list(old_list, report_month, base_string):
    new_list = old_list
    for ii in range(1, report_month+1):
        new_list.append(base_string + str(ii))

    return new_list