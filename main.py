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
df_long_bgt_column_list = [code_column, description_column, category_column, location_column, bgt_price_column,
                           bgt_currency_column, bgt_uom_column, bgt_per_column, savings_type_column,bgt_volume_column,
                           bgt_month_column]

bgt_columns_conversion = {df_wide_bgt_raw_column_expected_list[0]: df_long_bgt_column_list[0],
                          df_wide_bgt_raw_column_expected_list[1]: df_long_bgt_column_list[1],
                          df_wide_bgt_raw_column_expected_list[2]: df_long_bgt_column_list[2],
                          df_wide_bgt_raw_column_expected_list[3]: df_long_bgt_column_list[3],
                          df_wide_bgt_raw_column_expected_list[4]: df_long_bgt_column_list[4],
                          df_wide_bgt_raw_column_expected_list[5]: df_long_bgt_column_list[5],
                          df_wide_bgt_raw_column_expected_list[6]: df_long_bgt_column_list[6],
                          df_wide_bgt_raw_column_expected_list[7]: df_long_bgt_column_list[7],
                          df_wide_bgt_raw_column_expected_list[8]: df_long_bgt_column_list[8],
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

df_wide_act_raw_column_expected_list = ['Part Number', 'Description', 'Category', 'Plant', 'FX',
                                        'PL or BS?']
volume_act_base_string = "v"
df_wide_act_raw_column_expected_list = fc.generate_wide_act_raw_column_expected_list(df_wide_act_raw_column_expected_list,
                                                                                  report_month, volume_act_base_string)
price_act_base_string = "P"
df_wide_act_raw_column_expected_list = fc.generate_wide_act_raw_column_expected_list(df_wide_act_raw_column_expected_list,
                                                                                  report_month, price_act_base_string)
df_long_act_column_list = [code_column, description_column, category_column, location_column, act_price_column,
                           act_currency_column, act_price_uom_column, act_price_per_column, act_volume_column, 
                           act_volume_uom_column, act_volume_per_column, act_month_column]
# act_columns_conversion

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

######################## Check if all expected columns are on file ########################
### budget ###
[columns_to_delete_bgt, is_bgt_raw_column_integrous, bgt_error_list] = fc.file_column_integrity(df_wide_bgt,
                                                                                   df_wide_bgt_raw_column_expected_list)
error_list = '''MISSING COLUMNS: \non Bgt file: {}\n'''.format(bgt_error_list)
if not is_bgt_raw_column_integrous:
    print(error_list)
    exit()

### actuals ###
[columns_to_delete_act, is_act_raw_column_integrous, act_error_list] = fc.file_column_integrity(df_wide_act,
                                                                                   df_wide_act_raw_column_expected_list)
act_error_list = '''on Act file: {}\n'''.format(act_error_list)
error_list = error_list + act_error_list
if not is_act_raw_column_integrous:
    print(error_list)
    exit()

######################## Drop extra columns ########################
### budget ###
df_wide_bgt.drop(columns=columns_to_delete_bgt, inplace=True)
### actuals ###
df_wide_act.drop(columns=columns_to_delete_act, inplace=True)

######################## Change column names ########################
### budget ###
df_wide_bgt.rename(columns=bgt_columns_conversion, inplace=True)
### actuals ###
# Breaking dataframe in two before changing names before changing format
df_act_column_list = df_wide_act_raw_column_expected_list
desired_column_vol_act = len(df_act_column_list)-report_month
df_wide_volume_act = df_wide_act.filter(items=df_act_column_list[0:desired_column_vol_act], axis=1)

desired_column_pr_act_list = df_wide_act_raw_column_expected_list[desired_column_vol_act:len(df_act_column_list)]
desired_column_pr_act_list.append(df_act_column_list[0])
df_wide_price_act = df_wide_act.filter(items=desired_column_pr_act_list, axis=1)
print(df_wide_price_act.columns)

# df_wide_act.rename(columns=act_columns_conversion, inplace=True)

### terminology equalization
# category
df_category_equalizer.rename(columns=category_equalizer_columns_conversion, inplace=True)

df_wide_bgt = pd.merge(df_wide_bgt, df_category_equalizer, on=category_report_column, how='left')
df_wide_bgt.drop(category_report_column, axis=1, inplace=True)

# location
df_location_equalizer.rename(columns=location_equalizer_columns_conversion, inplace=True)

df_wide_bgt = pd.merge(df_wide_bgt, df_location_equalizer, on=location_report_column, how='left')
df_wide_bgt.drop(location_report_column, axis=1, inplace=True)

# currency
df_currency_equalizer.rename(columns=currency_equalizer_columns_conversion, inplace=True)

df_wide_bgt = pd.merge(df_wide_bgt, df_currency_equalizer, on=bgt_currency_report_column, how='left')
df_wide_bgt.drop(bgt_currency_report_column, axis=1, inplace=True)

# UoM
df_uom_equalizer.rename(columns=uom_equalizer_columns_conversion, inplace=True)

df_wide_bgt = pd.merge(df_wide_bgt, df_uom_equalizer, on=bgt_uom_report_column, how='left')
df_wide_bgt.drop(bgt_uom_report_column, axis=1, inplace=True)

# savings type
df_savings_type_equalizer.rename(columns=savings_type_equalizer_columns_conversion, inplace=True)

df_wide_bgt = pd.merge(df_wide_bgt, df_savings_type_equalizer, on=savings_type_report_column, how='left')
df_wide_bgt.drop(savings_type_report_column, axis=1, inplace=True)

### verify NaN and prepare a PN with errors

old_part_number_bgt_list = df_wide_bgt[code_column]
old_part_number_bgt_list = [str(item) for item in old_part_number_bgt_list]

df_wide_bgt.dropna(inplace=True)

new_part_number_bgt_list = df_wide_bgt[code_column]
new_part_number_bgt_list = [str(item) for item in new_part_number_bgt_list]

missing_codes_bgt = fc.list_differential(old_part_number_bgt_list, new_part_number_bgt_list)
error_list_bgt = '''PART-NUMBERS W/ PROBLEMS: \non Bgt file: {}'''.format(missing_codes_bgt)

error_list = error_list + error_list_bgt


### from wide to long format
bgt_id_vars = [code_column, description_column, category_column, location_column, bgt_price_column, bgt_currency_column,
               bgt_uom_column, bgt_per_column, savings_type_column]
df_long_bgt = pd.melt(frame=df_wide_bgt, id_vars=bgt_id_vars, value_vars=None, var_name=bgt_month_column,
                      value_name=bgt_volume_column)

### convert data types
df_long_bgt.astype({bgt_price_column: float, bgt_volume_column: float, bgt_per_column: float, bgt_month_column: int})

### convert price and volume into budget price UoM
# not applied for budget file




### Reorder columns
df_long_bgt = df_long_bgt[df_long_bgt_column_list]

### save data-frame on CSV
df_long_bgt.to_csv(filename_bgt_csv)




#############################                   2) CALCULATION ENGINE                      #############################

#############################                    3) REPORT GENERATOR                       #############################

#############################                  4) WEB INTERFACE (input)                    #############################

#############################               5) INTERACTIVE INTERFACE (output)              #############################