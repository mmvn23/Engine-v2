#############################                1) DATA CLEANING                     ######################################

def file_column_integrity(dataframe, column_expected_list, error_str, old_error_list=[]):
    new_error_list = old_error_list
    columns_to_delete = []
    raw_column_list = dataframe.columns.tolist()
    column_integrity = True

    for ii in range(1, len(column_expected_list)):
        is_part_of_raw_column_list = column_expected_list[ii] in raw_column_list
        if not is_part_of_raw_column_list:
            new_error_list.append(error_str.format(column_expected_list[ii]))
        column_integrity = column_integrity and is_part_of_raw_column_list

    for jj in range(1, len(raw_column_list)):
        is_part_of_expected_list = raw_column_list[jj] in column_expected_list
        if not is_part_of_expected_list:
            columns_to_delete.append(raw_column_list[jj])

    if not is_part_of_raw_column_list:
        print(new_error_list)

    return [columns_to_delete, new_error_list]


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


def generate_wide_act_column_conversion(base_dict, report_month, base_string):
    final_dict = base_dict
    for jj in range(1, report_month+1):
         final_dict[base_string + str(jj)] = str(jj)

    return final_dict


def merge_and_drop(dataframe, df_equalizer, df_merge_column, equalizer_merge_column, new_column_name):
    dataframe = dataframe.merge(df_equalizer, left_on=df_merge_column, right_on=equalizer_merge_column, how='left')
    if df_merge_column in dataframe.columns:
        dataframe.drop(df_merge_column, axis=1, inplace=True)
    if equalizer_merge_column in dataframe.columns:
        dataframe.drop(equalizer_merge_column, axis=1, inplace=True)
    equalizer_column_names = df_equalizer.columns
    dataframe.rename(columns={equalizer_column_names[1]: new_column_name}, inplace=True)

    return dataframe



