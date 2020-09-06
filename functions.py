import pandas as pd
import numpy as np

#############################                1) DATA CLEANING                     ######################################
def verify_integrity_from_code(code, clmn_list, new_error_list, function_error_str, error_str):
    is_part_of_clmn_list = code in clmn_list
    if not is_part_of_clmn_list:
        new_error_list = new_error_list + function_error_str + error_str.format(code)
    return new_error_list

def verify_integrity_from_code_lt(clmn_expected_list, clmn_list, error_list, function_error_str, error_str):
    for item in clmn_expected_list:
        error_list = verify_integrity_from_code(item, clmn_list, error_list, function_error_str, error_str)
    return error_list


def gen_delete_list(raw_clmn_list, clmn_expected_list):
    clmns_to_delete = []
    for item in raw_clmn_list:
        is_part_of_expected_list = item in clmn_expected_list
        if not is_part_of_expected_list:
            clmns_to_delete.append(item)
    return clmns_to_delete

def file_clmn_integrity(dataframe, clmn_expected_list, error_str, old_error_list="",
                        function_error_str = "Failed column integrity "):
    raw_clmn_list = dataframe.columns.tolist()
    new_error_list = verify_integrity_from_code_lt(clmn_expected_list, clmn_expected_list, old_error_list,
                                            function_error_str, error_str)
    clmns_to_delete = gen_delete_list(raw_clmn_list, clmn_expected_list)

    return [clmns_to_delete, new_error_list]


def list_differential(old_list, new_list):
    item_diff = []
    are_list_equal = True

    for old_item in old_list:

        if old_item not in new_list:
            item_diff.append(old_item)
            are_list_equal = False

    return [item_diff, are_list_equal]


def generate_wide_clmn_expected_list(old_list, start, end, base_string):
    new_list = old_list
    for ii in range(start, end+1):
        new_list.append(base_string + str(ii))

    return new_list


def generate_wide_clmn_conversion(base_dict, start_month, end_month, base_string):
    final_dict = base_dict
    for jj in range(start_month, end_month+1):
         final_dict[base_string + str(jj)] = str(jj)

    return final_dict


def merge_and_drop(dataframe, df_equalizer, df_merge_clmn, equalizer_merge_clmn, new_clmn_name, code_clmn,
                   error_str, old_error_list=""):
    function_error_str = "Failed merge and drop "
    dataframe = dataframe.merge(df_equalizer, left_on=df_merge_clmn, right_on=equalizer_merge_clmn, how='left')
    new_error_list = old_error_list
    if df_merge_clmn in dataframe.columns:
        dataframe.drop(df_merge_clmn, axis=1, inplace=True)
    if equalizer_merge_clmn in dataframe.columns:
        dataframe.drop(equalizer_merge_clmn, axis=1, inplace=True)
    equalizer_clmn_names = df_equalizer.columns
    dataframe.rename(columns={equalizer_clmn_names[1]: new_clmn_name}, inplace=True)

    [dataframe, mid_error_list, are_list_equal] = clean_nan(dataframe, code_clmn)
    if not are_list_equal:
        error_str_nan = "PNs with problems: "
        aux = "--"
        new_error_list = new_error_list + aux + error_str + aux + function_error_str + aux + error_str_nan + aux + \
                         str(mid_error_list)

    return [dataframe, new_error_list]


def clean_nan(dataframe, code_clmn):
    old_part_number_bgt_list = dataframe[code_clmn]
    old_part_number_bgt_list = [str(item) for item in old_part_number_bgt_list]

    dataframe.dropna(inplace=True)

    new_part_number_bgt_list = dataframe[code_clmn]
    new_part_number_bgt_list = [str(item) for item in new_part_number_bgt_list]

    [missing_codes, are_lists_equal] = list_differential(old_part_number_bgt_list, new_part_number_bgt_list)

    return [dataframe, missing_codes, are_lists_equal]


def melt_and_index(wide_dataframe, wide_vars, long_clmn, value_clmn, code_clmn):
    long_dataframe = pd.melt(frame=wide_dataframe, id_vars=wide_vars, value_vars=None, var_name=long_clmn,
                             value_name=value_clmn)
    long_dataframe.set_index(keys=[code_clmn, long_clmn], drop=False, inplace=True)

    return long_dataframe


def clean_types(dataframe, cleaning_clmns, clmn_types, error_str, old_error_list=""):
    old_index_list = dataframe.index

    for item in cleaning_clmns:
        dataframe = dataframe[dataframe[item].apply(lambda x: not isinstance(x, str))]
        dataframe[item].astype(clmn_types)

    new_index_list = dataframe.index
    new_error_list = old_error_list
    [missing_codes, are_lists_equal] = list_differential(old_index_list, new_index_list)

    if not are_lists_equal:
        error_str_nan = "PNs/month with problems: "
        aux = " -- "
        new_error_list = new_error_list + aux + error_str + aux + error_str_nan + str(missing_codes)

    return [dataframe, new_error_list]


def clear_extra_rows(dataframe, code_clmn, error_str, old_error_list=""):
    old_index_list = dataframe[code_clmn]
    dataframe.dropna(axis=0, inplace=True)
    new_index_list = dataframe[code_clmn]
    old_index_list = [str(item) for item in old_index_list]
    new_index_list = [str(item) for item in new_index_list]

    [missing_codes, are_lists_equal] = list_differential(old_index_list, new_index_list)
    new_error_list = old_error_list

    if not are_lists_equal:
        error_str_nan = "Rows w/Nan: "
        aux = " -- "
        new_error_list = new_error_list + aux + error_str + aux + error_str_nan + str(missing_codes)

    return [dataframe, new_error_list]


def generate_uom_ref_file(df_base, code_clmn, ref_uom, ref_currency, ref_uom_str, ref_currency_str):
    dataframe = df_base.filter(items=[code_clmn, ref_uom, ref_currency], axis=1)
    dataframe.rename(columns={ref_uom: ref_uom_str, ref_currency: ref_currency_str}, inplace=True)

    return dataframe


def prepare_long_uom_ref_file(df_conv_short, code_list, code_clmn, conv_old_uom_clmn, conv_new_uom_clmn,
                                conv_to_all_str):

    query_str1 = code_clmn + '!="' + conv_to_all_str + '"'
    df_conv_long = df_conv_short.query(query_str1, inplace=False)

    query_str2 = code_clmn + '=="' + conv_to_all_str + '"'
    df_conv_short.query(query_str2, inplace=True)

    for kk in range(0, len(code_list)):
        df_conv_long = add_all_uom_fx_to_code(df_conv_long, df_conv_short, code_list[kk], code_clmn, conv_to_all_str)

    df_conv_long = df_conv_long.set_index(keys=[code_clmn, conv_old_uom_clmn, conv_new_uom_clmn], drop=False,
                                          inplace=False)

    return df_conv_long


def add_all_uom_fx_to_code(dataframe, base_dataframe, code, code_clmn, conv_to_all_str):
    base_dataframe[code_clmn] = base_dataframe[code_clmn].replace([conv_to_all_str], code)
    dataframe = dataframe.append(base_dataframe)

    return dataframe


def include_predecessors(old_df_bgt, df_pred, pred_code_clmn, code_clmn, month_clmn):
    new_df_bgt = old_df_bgt
    new_df_bgt[pred_code_clmn] = new_df_bgt[code_clmn]

    code_list = df_pred[code_clmn]
    for kk in range(0, len(code_list)):
        new_df_bgt = include_single_predecessor(new_df_bgt, df_pred, pred_code_clmn, code_clmn, month_clmn,
                                                code_list[kk])

    return new_df_bgt


def include_single_predecessor(old_df_bgt, df_pred, pred_code_clmn, code_clmn, month_clmn, new_code):
    new_df_bgt = old_df_bgt

    bgt_pred = df_pred.at[new_code, pred_code_clmn]
    #filter based on predecessor
    #append this filterd item into dataframe
    #change index and predecessor column
    bgt_pred_array = [12 * [bgt_pred],
                      ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']]
    bgt_pred_tuple = list(zip(*bgt_pred_array))

    add_row = old_df_bgt.filter(bgt_pred_tuple, axis=0)
    add_row[code_clmn] = new_code
    add_row.set_index(keys=[code_clmn, month_clmn], drop=False, inplace=True)
    new_df_bgt = new_df_bgt.append(add_row)

    return new_df_bgt


def generate_price_curve_based_on_constant(old_dataframe, value_list, start_month, end_month, df_id_vars, month_clmn,
                                           price_clmn, code_clmn, strategy_clmn, strategy_str):
    month_list = range(start_month, end_month+1)
    new_dataframe = old_dataframe
    new_dataframe.rename(columns={price_clmn: str(month_list[0])}, inplace=True)

    for item in month_list:
        new_dataframe[str(item)] = value_list

    new_dataframe = generate_price_curve_based_on_curve(old_dataframe, df_id_vars, month_clmn, price_clmn, code_clmn,
                                                        strategy_clmn, strategy_str)

    return new_dataframe


def generate_price_curve_based_on_curve(old_dataframe, df_id_vars, month_clmn, price_clmn, code_clmn, strategy_clmn,
                                        strategy_str):
    # wide to long
    new_dataframe = melt_and_index(old_dataframe, df_id_vars, month_clmn, price_clmn, code_clmn)
    # add column with forecast strategy
    new_dataframe[strategy_clmn] = strategy_str

    return new_dataframe


def generate_price_curve_based_on_another_file(old_dataframe, start_month, end_month, month_clmn, price_clmn, code_clmn,
                                               strategy_clmn, strategy_str, ref_file, ref_clmn_lt, matching_tuple):
    # forecast as a budget file
    old_df_clmn_lt = old_dataframe.columns
    month_list = range(start_month, end_month + 1)
    wide_dataframe = old_dataframe
    value = 0

    for item in month_list:
        wide_dataframe[str(item)] = value

    long_dataframe = melt_and_index(wide_dataframe, old_df_clmn_lt, month_clmn, price_clmn, code_clmn)
    long_dataframe.drop(columns=price_clmn, inplace=True)

    # budget file
    ref_data = ref_file.filter(items=ref_clmn_lt, axis=1)
    ref_data.rename(columns=matching_tuple, inplace=True)

    new_dataframe = long_dataframe.merge(ref_data, how='left', left_index=True, right_index=True)
    new_dataframe[strategy_clmn] = strategy_str

    return new_dataframe
