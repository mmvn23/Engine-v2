import pandas as pd
import functions as fc

# List of inputs (excel files):
#   1) Budget - OK
#   2) Actuals
#   3) Predecessor
#   4) Forecast
#   5) Baseline
#   6) UoM and FX conversions
#   7) Project mapping

#############################                Input Variables                      ######################################
report_month = 4
Fiscal_Year = '2020'

########################    Data cleaning    ########################
### Budget ###
filename_bgt = './inputs/PAF.xlsx'
filename_bgt_csv = './outputs/budget {}.csv'.format(Fiscal_Year)

code_column = 'code'
description_column = 'description'
category_report_column = 'report_category'
category_column = 'category'
location_report_column = 'report_location'
location_column = 'location'
bgt_price_column = 'bgt_price'
bgt_currency_report_column = 'report_bgt_currency'
bgt_currency_column = 'bgt_currency'
bgt_uom_report_column = 'report_bgt_uom'
bgt_uom_column = 'bgt_uom'
bgt_per_column = 'bgt_per'
savings_type_report_column = 'report_savings_type'
savings_type_column = 'savings_type'
bgt_month_column = 'month'
bgt_volume_column = 'bgt_volume'

df_wide_bgt_raw_column_expected_list = ['Part Number', 'Description', 'Category', 'Plant', 'PAF price', 'FX', 'Unity',
                                        '1 or 1,000? ', 'PL or BS?', 'vol 01', 'vol 02', 'vol 03', 'vol 04', 'vol 05',
                                        'vol 06', 'vol 07', 'vol 08', 'vol 09', 'vol 10', 'vol 11', 'vol 12']

df_long_bgt_column_list_equalization = [code_column, description_column, category_column, location_column,
                                           bgt_price_column, bgt_currency_column, bgt_uom_column, bgt_per_column,
                                           savings_type_column, bgt_volume_column, bgt_month_column]

bgt_column_conversion = {df_wide_bgt_raw_column_expected_list[0]: code_column,
                          df_wide_bgt_raw_column_expected_list[1]: description_column,
                          df_wide_bgt_raw_column_expected_list[2]: category_report_column,
                          df_wide_bgt_raw_column_expected_list[3]: location_report_column,
                          df_wide_bgt_raw_column_expected_list[4]: bgt_price_column,
                          df_wide_bgt_raw_column_expected_list[5]: bgt_currency_report_column,
                          df_wide_bgt_raw_column_expected_list[6]: bgt_uom_report_column,
                          df_wide_bgt_raw_column_expected_list[7]: bgt_per_column,
                          df_wide_bgt_raw_column_expected_list[8]: savings_type_report_column,
                          df_wide_bgt_raw_column_expected_list[9]: '1',
                          df_wide_bgt_raw_column_expected_list[10]: '2',
                          df_wide_bgt_raw_column_expected_list[11]: '3',
                          df_wide_bgt_raw_column_expected_list[12]: '4',
                          df_wide_bgt_raw_column_expected_list[13]: '5',
                          df_wide_bgt_raw_column_expected_list[14]: '6',
                          df_wide_bgt_raw_column_expected_list[15]: '7',
                          df_wide_bgt_raw_column_expected_list[16]: '8',
                          df_wide_bgt_raw_column_expected_list[17]: '9',
                          df_wide_bgt_raw_column_expected_list[18]: '10',
                          df_wide_bgt_raw_column_expected_list[19]: '11',
                          df_wide_bgt_raw_column_expected_list[20]: '12'}

### Equalization ###
filename_category_equalization = './inputs/category equalization.xlsx'
filename_location_equalization = './inputs/plant equalization.xlsx'
filename_currency_equalization = './inputs/FX equalization.xlsx'
filename_uom_equalization = './inputs/unity equalization.xlsx'
filename_savings_type_equalization = './inputs/sav type equalization.xlsx'

category_equalizer_columns_conversion = {'Report category': category_report_column,
                                         'Standard category': category_column}
location_equalizer_columns_conversion = {'Report plant': location_report_column, 'Standard plant': location_column}
uom_equalizer_columns_conversion = {'Report UoM': bgt_uom_report_column, 'Standard UoM': bgt_uom_column}
currency_equalizer_columns_conversion = {'Report FX': bgt_currency_report_column, 'Standard FX': bgt_currency_column}
savings_type_equalizer_columns_conversion = {'Report type': savings_type_report_column,
                                             'Standard type': savings_type_column}

### Actuals ###
filename_act = './inputs/YTD.xlsx'
filename_act_csv = './outputs/actuals {0}-{1}.csv'.format(Fiscal_Year, report_month)

act_price_column = 'act_price'
act_currency_report_column = 'report_act_currency'
act_currency_column = 'act_currency'
act_price_uom_report_column = 'report_act_price_uom'
act_price_uom_column = 'act_price_uom'
act_volume_uom_report_column = 'report_act_volume_uom'
act_volume_uom_column = 'act_volume_uom'
act_price_per_column = 'act_price_per'
act_volume_per_column = 'act_volume_per'
act_month_column = 'month'
act_volume_column = 'act_volume'

df_wide_act_raw_column_expected_list = ['Part Number', 'Description', 'Category', 'Plant', 'FX', 'Unity',
                                        'PL or BS?'] # input has only 1 UoM, therefore we will have to adjust

volume_act_base_string = "v"
df_wide_act_raw_column_expected_list = fc.generate_wide_act_raw_column_expected_list(df_wide_act_raw_column_expected_list,
                                                                                  report_month, volume_act_base_string)
price_act_base_string = "P"
df_wide_act_raw_column_expected_list = fc.generate_wide_act_raw_column_expected_list(df_wide_act_raw_column_expected_list,
                                                                                  report_month, price_act_base_string)
df_long_act_column_list = [code_column, description_column, category_column, location_column, act_price_column,
                           act_currency_column, act_price_uom_column, act_price_per_column, act_volume_column,
                           act_volume_uom_column, act_volume_per_column, act_month_column]
act_volume_columns_conversion_base = {df_wide_act_raw_column_expected_list[0]: code_column,
                                      df_wide_act_raw_column_expected_list[1]: description_column,
                                      df_wide_act_raw_column_expected_list[2]: category_report_column,
                                      df_wide_act_raw_column_expected_list[3]: location_report_column,
                                      df_wide_act_raw_column_expected_list[4]: act_currency_report_column,
                                      df_wide_act_raw_column_expected_list[5]: act_volume_uom_report_column,
                                      df_wide_act_raw_column_expected_list[6]: savings_type_report_column}

act_volume_column_conversion = fc.generate_wide_act_column_conversion(act_volume_columns_conversion_base,
                                                                      report_month, volume_act_base_string)

act_price_columns_conversion_base = {df_wide_act_raw_column_expected_list[0]: code_column,
                                     df_wide_bgt_raw_column_expected_list[6]: act_price_uom_report_column}

act_price_column_conversion = fc.generate_wide_act_column_conversion(act_price_columns_conversion_base, report_month,
                                                                     price_act_base_string)

#############################                1) DATA CLEANING                     ######################################
########################    Load excel files    ########################
### budget ###
df_wide_bgt = pd.read_excel(filename_bgt)

### equalization files ###
df_category_equalizer = pd.read_excel(filename_category_equalization)
df_location_equalizer = pd.read_excel(filename_location_equalization)
df_currency_equalizer = pd.read_excel(filename_currency_equalization)
df_uom_equalizer = pd.read_excel(filename_uom_equalization)
df_savings_type_equalizer = pd.read_excel(filename_savings_type_equalization)

### actuals ###
df_wide_act = pd.read_excel(filename_act)
# budget, actuals, forecast, baseline, UoM and FX and project mapping

######################## Check column integrity ########################
### budget ###
bgt_error_str = '''MISSING COLUMNS: \non Bgt file: {}\n'''
[columns_to_delete_bgt, error_list] = fc.file_column_integrity(df_wide_bgt, df_wide_bgt_raw_column_expected_list,
                                                               bgt_error_str)

### actuals ###
act_error_str = act_error_list = '''on Act file: {}\n'''
[columns_to_delete_act, error_list] = fc.file_column_integrity(df_wide_act, df_wide_act_raw_column_expected_list,
                                                               act_error_str, error_list)
print(error_list)
######################## Drop extra columns ########################
### budget ###
df_wide_bgt.drop(columns=columns_to_delete_bgt, inplace=True)
### actuals ###
df_wide_act.drop(columns=columns_to_delete_act, inplace=True)

######################## Change column names ########################
### budget ###
df_wide_bgt.rename(columns=bgt_column_conversion, inplace=True)

### actuals ###
# Breaking dataframe in two before changing names before changing format
df_act_column_list = df_wide_act_raw_column_expected_list
desired_column_vol_act = len(df_act_column_list)-report_month
df_wide_volume_act = df_wide_act.filter(items=df_act_column_list[0:desired_column_vol_act], axis=1)

desired_column_pr_act_list = df_wide_act_raw_column_expected_list[desired_column_vol_act:len(df_act_column_list)]
desired_column_pr_act_list.append(df_act_column_list[0])
desired_column_pr_act_list.append(df_act_column_list[5])
df_wide_price_act = df_wide_act.filter(items=desired_column_pr_act_list, axis=1)

df_wide_volume_act.rename(columns=act_volume_column_conversion, inplace=True)
df_wide_price_act.rename(columns=act_price_column_conversion, inplace=True)

######################## Terminology equalization ########################
df_category_equalizer.rename(columns=category_equalizer_columns_conversion, inplace=True)
df_location_equalizer.rename(columns=location_equalizer_columns_conversion, inplace=True)
df_currency_equalizer.rename(columns=currency_equalizer_columns_conversion, inplace=True)
df_uom_equalizer.rename(columns=uom_equalizer_columns_conversion, inplace=True)
df_savings_type_equalizer.rename(columns=savings_type_equalizer_columns_conversion, inplace=True)

### budget ###
df_wide_bgt = fc.merge_and_drop(df_wide_bgt, df_category_equalizer, category_report_column, category_report_column,
                                category_column)
df_wide_bgt = fc.merge_and_drop(df_wide_bgt, df_location_equalizer, location_report_column, location_report_column,
                                location_column)
df_wide_bgt = fc.merge_and_drop(df_wide_bgt, df_currency_equalizer, bgt_currency_report_column,
                                bgt_currency_report_column, bgt_currency_column)
df_wide_bgt = fc.merge_and_drop(df_wide_bgt, df_uom_equalizer, bgt_uom_report_column,
                                bgt_uom_report_column, bgt_uom_column)
df_wide_bgt = fc.merge_and_drop(df_wide_bgt, df_savings_type_equalizer, savings_type_report_column,
                                savings_type_report_column, savings_type_column)

### actuals ###
df_wide_volume_act = fc.merge_and_drop(df_wide_volume_act, df_category_equalizer, category_report_column,
                                       category_report_column, category_column)
df_wide_volume_act = fc.merge_and_drop(df_wide_volume_act, df_location_equalizer, location_report_column,
                                       location_report_column, location_column)
df_wide_volume_act = fc.merge_and_drop(df_wide_volume_act, df_currency_equalizer, act_currency_report_column,
                                       bgt_currency_report_column, act_currency_column)
df_wide_volume_act = fc.merge_and_drop(df_wide_volume_act, df_uom_equalizer, act_volume_uom_report_column,
                                       bgt_uom_report_column, act_volume_uom_column)
df_wide_price_act = fc.merge_and_drop(df_wide_price_act, df_uom_equalizer, act_price_uom_report_column,
                                      bgt_uom_report_column, act_price_uom_column)
df_wide_volume_act = fc.merge_and_drop(df_wide_volume_act, df_savings_type_equalizer, savings_type_report_column,
                                       savings_type_report_column, savings_type_column)

# ### verify NaN and prepare a PN with errors
#
# old_part_number_bgt_list = df_wide_bgt[code_column]
# old_part_number_bgt_list = [str(item) for item in old_part_number_bgt_list]
#
# df_wide_bgt.dropna(inplace=True)
#
# new_part_number_bgt_list = df_wide_bgt[code_column]
# new_part_number_bgt_list = [str(item) for item in new_part_number_bgt_list]
#
# missing_codes_bgt = fc.list_differential(old_part_number_bgt_list, new_part_number_bgt_list)
# error_list_bgt = '''PART-NUMBERS W/ PROBLEMS: \non Bgt file: {}'''.format(missing_codes_bgt)
#
# error_list = error_list + error_list_bgt
#
#
# ### from wide to long format
# bgt_id_vars = [code_column, description_column, category_column, location_column, bgt_price_column, bgt_currency_column,
#                bgt_uom_column, bgt_per_column, savings_type_column]
# df_long_bgt = pd.melt(frame=df_wide_bgt, id_vars=bgt_id_vars, value_vars=None, var_name=bgt_month_column,
#                       value_name=bgt_volume_column)
#
# ### convert data types
# df_long_bgt.astype({bgt_price_column: float, bgt_volume_column: float, bgt_per_column: float, bgt_month_column: int})
#
# ### convert price and volume into budget price UoM
# # not applied for budget file
#
#
#
#
# ### Reorder columns
# df_long_bgt = df_long_bgt[df_long_bgt_column_list_equalization]
#
# ### save data-frame on CSV
# df_long_bgt.to_csv(filename_bgt_csv)
#



#############################                   2) CALCULATION ENGINE                      #############################

#############################                    3) REPORT GENERATOR                       #############################

#############################                  4) WEB INTERFACE (input)                    #############################

#############################               5) INTERACTIVE INTERFACE (output)              #############################