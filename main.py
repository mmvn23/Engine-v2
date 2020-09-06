import pandas as pd
import functions as fc

# List of inputs (excel files):
#   1) Budget - OK
#   2) Actuals - OK
#   3) Forecast - Stopped here
#         as budget price
#         as avg actuals
#         as a constant
#         as an inflation rate
#         as a curve
#   4) Baseline
#   5) Predecessor - OK
#   6) UoM and FX equalization - OK
#   7) UoM and FX conversions - OK
#   8) Project mapping

#############################                Input Variables                      ######################################
report_month = 4
Fiscal_Year = '2020'
file_name_error_msg = './outputs/error msg {0}-{1}.txt'.format(Fiscal_Year, report_month)

########################    Data cleaning    ########################
### Budget ###
filename_bgt = './inputs/PAF.xlsx'
filename_bgt_csv = './outputs/budget {}.csv'.format(Fiscal_Year)

code_clmn = 'code'
description_clmn = 'description'
category_report_clmn = 'report_category'
category_clmn = 'category'
location_report_clmn = 'report_location'
location_clmn = 'location'
bgt_price_clmn = 'bgt_price'
bgt_currency_report_clmn = 'report_bgt_currency'
bgt_currency_clmn = 'bgt_currency'
bgt_uom_report_clmn = 'report_bgt_uom'
bgt_uom_clmn = 'bgt_uom'
bgt_per_clmn = 'bgt_per'
savings_type_report_clmn = 'report_savings_type'
savings_type_clmn = 'savings_type'
month_clmn = 'month'
bgt_volume_clmn = 'bgt_volume'
pred_code_clmn = 'bgt_predecessor'

df_wide_bgt_raw_clmn_expect_lt = ['Part Number', 'Description', 'Category', 'Plant', 'PAF price', 'FX', 'Unity',
                                        '1 or 1,000? ', 'PL or BS?', 'vol 01', 'vol 02', 'vol 03', 'vol 04', 'vol 05',
                                        'vol 06', 'vol 07', 'vol 08', 'vol 09', 'vol 10', 'vol 11', 'vol 12']

df_long_bgt_clmn_list = [description_clmn, category_clmn, location_clmn, savings_type_clmn, bgt_volume_clmn,
                         bgt_price_clmn, bgt_per_clmn, bgt_uom_clmn, bgt_currency_clmn, pred_code_clmn]

bgt_clmn_conversion = {df_wide_bgt_raw_clmn_expect_lt[0]: code_clmn,
                         df_wide_bgt_raw_clmn_expect_lt[1]: description_clmn,
                         df_wide_bgt_raw_clmn_expect_lt[2]: category_report_clmn,
                         df_wide_bgt_raw_clmn_expect_lt[3]: location_report_clmn,
                         df_wide_bgt_raw_clmn_expect_lt[4]: bgt_price_clmn,
                         df_wide_bgt_raw_clmn_expect_lt[5]: bgt_currency_report_clmn,
                         df_wide_bgt_raw_clmn_expect_lt[6]: bgt_uom_report_clmn,
                         df_wide_bgt_raw_clmn_expect_lt[7]: bgt_per_clmn,
                         df_wide_bgt_raw_clmn_expect_lt[8]: savings_type_report_clmn,
                         df_wide_bgt_raw_clmn_expect_lt[9]: '1',
                         df_wide_bgt_raw_clmn_expect_lt[10]: '2',
                         df_wide_bgt_raw_clmn_expect_lt[11]: '3',
                         df_wide_bgt_raw_clmn_expect_lt[12]: '4',
                         df_wide_bgt_raw_clmn_expect_lt[13]: '5',
                         df_wide_bgt_raw_clmn_expect_lt[14]: '6',
                         df_wide_bgt_raw_clmn_expect_lt[15]: '7',
                         df_wide_bgt_raw_clmn_expect_lt[16]: '8',
                         df_wide_bgt_raw_clmn_expect_lt[17]: '9',
                         df_wide_bgt_raw_clmn_expect_lt[18]: '10',
                         df_wide_bgt_raw_clmn_expect_lt[19]: '11',
                         df_wide_bgt_raw_clmn_expect_lt[20]: '12'}

bgt_error_str = "\nBgt file:\n"

### actuals ###
filename_act = './inputs/YTD.xlsx'
filename_act_csv = './outputs/actuals {0}-{1}.csv'.format(Fiscal_Year, report_month)

act_price_clmn = 'act_price'
act_currency_report_clmn = 'report_act_currency'
act_currency_clmn = 'act_currency'
act_price_uom_report_clmn = 'report_act_price_uom'
act_price_uom_clmn = 'act_price_uom'
act_volume_uom_report_clmn = 'report_act_volume_uom'
act_volume_uom_clmn = 'act_volume_uom'
act_price_per_clmn = 'act_price_per'
act_volume_per_clmn = 'act_volume_per'
act_volume_clmn = 'act_volume'
act_code_and_month_clmn = 'act_code_and_month'

df_wide_act_raw_clmn_expect_lt = ['Part Number', 'Description', 'Category', 'Plant', 'FX', 'Unity', '1 or 1,000? ']
# input has only 1 UoM, therefore we will have to adjust

volume_act_base_string = "v"
df_wide_act_raw_clmn_expect_lt = fc.generate_wide_clmn_expected_list(df_wide_act_raw_clmn_expect_lt,
                                                                                     1, report_month, volume_act_base_string)
price_act_base_string = "P"
df_wide_act_raw_clmn_expect_lt = fc.generate_wide_clmn_expected_list(df_wide_act_raw_clmn_expect_lt,
                                                                                     1, report_month, price_act_base_string)

df_long_act_clmn_list = [description_clmn, category_clmn, location_clmn, act_volume_clmn,
                           act_volume_per_clmn, act_volume_uom_clmn,  act_price_clmn, act_price_per_clmn,
                           act_price_uom_clmn, act_currency_clmn]

act_volume_clmns_conversion_base = {df_wide_act_raw_clmn_expect_lt[0]: code_clmn,
                                    df_wide_act_raw_clmn_expect_lt[1]: description_clmn,
                                    df_wide_act_raw_clmn_expect_lt[2]: category_report_clmn,
                                    df_wide_act_raw_clmn_expect_lt[3]: location_report_clmn,
                                    df_wide_act_raw_clmn_expect_lt[4]: act_currency_report_clmn,
                                    df_wide_act_raw_clmn_expect_lt[5]: act_volume_uom_report_clmn,
                                    df_wide_act_raw_clmn_expect_lt[6]: act_volume_per_clmn}

act_volume_clmn_conversion = fc.generate_wide_clmn_conversion(act_volume_clmns_conversion_base, 1, report_month,
                                                              volume_act_base_string)
act_price_clmns_conversion_base = {df_wide_act_raw_clmn_expect_lt[0]: code_clmn,
                                     df_wide_act_raw_clmn_expect_lt[5]: act_price_uom_report_clmn,
                                     df_wide_act_raw_clmn_expect_lt[6]: act_price_per_clmn}

act_price_clmn_conversion = fc.generate_wide_clmn_conversion(act_price_clmns_conversion_base, 1, report_month,
                                                             price_act_base_string)

act_error_str = "\nAct file:\n"

### forecast ###
filename_frc = './inputs/YTG.xlsx'
sheet_frc_vol = 'Volume'
sheet_frc_as_bgt = 'Budget'
sheet_frc_as_act = 'YTD'
sheet_frc_as_cnst = 'Constant'
sheet_frc_as_inf = 'Inflation rate'
sheet_frc_as_crv = 'Price curve'

frc_vol_uom_report_clmn = 'report_frc_volume_uom'
frc_vol_per_clmn = 'frc_volume_per_uom'
frc_price_clmn = 'frc_price'
frc_price_uom_report_clmn = 'report_frc_price_uom'
frc_price_uom_clmn = 'frc_price_uom'
frc_price_per_clmn = 'frc_price_per'
frc_currency_clmn = 'frc_currency'
frc_currency_report_clmn = 'report_frc_currency'

frc_price_as_inf_base_price_clmn = 'frc_as_inf_base_price'
frc_price_as_inf_inflation_clmn = 'frc_as_inf_inflation'
frc_price_as_inf_month_clmn = 'frc_as_inf_month'

frc_strategy_column = 'frc_strategy'
frc_strategy_as_bgt = 'Budget'
frc_strategy_as_act = 'YTD'
frc_strategy_as_cnst = 'Constant'
frc_strategy_as_inf = 'Inflation rate'
frc_strategy_as_crv = 'Price curve'

df_wide_frc_vol_raw_clmn_expect_lt_base = ['Part Number',	'Plant', 'Description',	'Unity', '1 or 1,000? ']
volume_frc_vol_base_string = "v"
df_wide_frc_vol_raw_clmn_expect_lt = fc.generate_wide_clmn_expected_list(df_wide_frc_vol_raw_clmn_expect_lt_base,
                                                                         report_month+1, 12,
                                                                         volume_frc_vol_base_string)
df_wide_frc_as_bgt_raw_clmn_expect_lt = ['Part Number',	'Plant', 'Description']
df_wide_frc_as_act_raw_clmn_expect_lt = ['Part Number',	'Plant', 'Description']
df_wide_frc_as_cnst_raw_clmn_expect_lt = ['Part Number',	'Plant', 'Description', 'Price', 'Unity', '1 or 1,000? ',
                                                'FX']
df_wide_frc_as_inf_raw_clmn_expect_lt = ['Part Number',	'Plant', 'Description', 'Unity', '1 or 1,000? ', 'FX',
                                               'Base price', 'Inflation', 'Inflation month']
df_wide_frc_as_crv_raw_clmn_expect_lt_base = ['Part Number', 'Plant', 'Description', 'Unity', '1 or 1,000? ', 'FX']
price_frc_base_string = "P"
df_wide_frc_as_crv_raw_clmn_expect_lt = fc.generate_wide_clmn_expected_list(df_wide_frc_as_crv_raw_clmn_expect_lt_base,
                                                                            report_month+1, 12,
                                                                            price_frc_base_string)

frc_vol_clmn_conversion_base = {df_wide_frc_vol_raw_clmn_expect_lt[0]: code_clmn,
                                df_wide_frc_vol_raw_clmn_expect_lt[1]: location_report_clmn,
                                df_wide_frc_vol_raw_clmn_expect_lt[2]: description_clmn,
                                df_wide_frc_vol_raw_clmn_expect_lt[3]: frc_vol_uom_report_clmn,
                                df_wide_frc_vol_raw_clmn_expect_lt[4]: frc_vol_per_clmn}

frc_vol_clmn_conversion = fc.generate_wide_clmn_conversion(frc_vol_clmn_conversion_base, report_month+1, 12,
                                                           volume_frc_vol_base_string)

frc_as_bgt_clmn_conversion = {df_wide_frc_as_bgt_raw_clmn_expect_lt[0]: code_clmn,
                              df_wide_frc_as_bgt_raw_clmn_expect_lt[1]: location_report_clmn,
                              df_wide_frc_as_bgt_raw_clmn_expect_lt[2]: description_clmn}

frc_as_act_clmn_conversion = {df_wide_frc_as_act_raw_clmn_expect_lt[0]: code_clmn,
                              df_wide_frc_as_act_raw_clmn_expect_lt[1]: location_report_clmn,
                              df_wide_frc_as_act_raw_clmn_expect_lt[2]: description_clmn}

frc_as_cnst_clmn_conversion = {df_wide_frc_as_cnst_raw_clmn_expect_lt[0]: code_clmn,
                               df_wide_frc_as_cnst_raw_clmn_expect_lt[1]: location_report_clmn,
                               df_wide_frc_as_cnst_raw_clmn_expect_lt[2]: description_clmn,
                               df_wide_frc_as_cnst_raw_clmn_expect_lt[3]: frc_price_clmn,
                               df_wide_frc_as_cnst_raw_clmn_expect_lt[4]: frc_price_uom_report_clmn,
                               df_wide_frc_as_cnst_raw_clmn_expect_lt[5]: frc_price_per_clmn,
                               df_wide_frc_as_cnst_raw_clmn_expect_lt[6]: frc_currency_report_clmn}

frc_as_inf_clmn_conversion = {df_wide_frc_as_inf_raw_clmn_expect_lt[0]: code_clmn,
                              df_wide_frc_as_inf_raw_clmn_expect_lt[1]: location_report_clmn,
                              df_wide_frc_as_inf_raw_clmn_expect_lt[2]: description_clmn,
                              df_wide_frc_as_inf_raw_clmn_expect_lt[3]: frc_price_uom_report_clmn,
                              df_wide_frc_as_inf_raw_clmn_expect_lt[4]: frc_price_per_clmn,
                              df_wide_frc_as_inf_raw_clmn_expect_lt[5]: frc_currency_report_clmn,
                              df_wide_frc_as_inf_raw_clmn_expect_lt[6]: frc_price_as_inf_base_price_clmn,
                              df_wide_frc_as_inf_raw_clmn_expect_lt[7]: frc_price_as_inf_inflation_clmn,
                              df_wide_frc_as_inf_raw_clmn_expect_lt[8]: frc_price_as_inf_month_clmn}

frc_as_crv_clmn_conversion_base = {df_wide_frc_as_crv_raw_clmn_expect_lt_base[0]: code_clmn,
                                   df_wide_frc_as_crv_raw_clmn_expect_lt_base[1]: location_report_clmn,
                                   df_wide_frc_as_crv_raw_clmn_expect_lt_base[2]: description_clmn,
                                   df_wide_frc_as_crv_raw_clmn_expect_lt_base[3]: frc_price_uom_report_clmn,
                                   df_wide_frc_as_crv_raw_clmn_expect_lt_base[4]: frc_price_per_clmn,
                                   df_wide_frc_as_crv_raw_clmn_expect_lt_base[5]: frc_currency_report_clmn}

frc_as_crv_clmn_conversion = fc.generate_wide_clmn_conversion(frc_as_crv_clmn_conversion_base, report_month+1, 12,
                                                              price_frc_base_string)

frc_error_str = "\nForecast file:\n"

### predecessor ###
filename_pred = './inputs/yhold.xlsx'
filename_pred_csv = './outputs/predecessors {0}-{1}.csv'.format(Fiscal_Year, report_month)
df_pred_raw_clmn_expect_lt = ['From', 'To']
pred_error_str = "\nPredecessor file:\n"
pred_clmns_conversion = {df_pred_raw_clmn_expect_lt[0]: pred_code_clmn,
                         df_pred_raw_clmn_expect_lt[1]: code_clmn}

### uom and currency equalization ###
filename_category_eq = './inputs/category equalization.xlsx'
filename_location_eq = './inputs/plant equalization.xlsx'
filename_currency_eq = './inputs/FX equalization.xlsx'
filename_uom_eq = './inputs/unity equalization.xlsx'
filename_savings_type_eq = './inputs/sav type equalization.xlsx'

filename_category_eq_csv = './outputs/category equalization.csv'
filename_location_eq_csv = './outputs/location equalization.csv'
filename_currency_eq_csv = './outputs/currency equalization.csv'
filename_uom_eq_csv = './outputs/uom equalization.csv'
filename_savings_type_eq_csv = './outputs/savings type equalization.csv'

df_category_eq_raw_clmn_expect_lt = ['Report category', 'Standard category']
df_location_eq_raw_clmn_expect_lt = ['Report plant', 'Standard plant']
df_uom_eq_raw_clmn_expect_lt = ['Report UoM',	'Standard UoM']
df_currency_eq_raw_clmn_expect_lt = ['Report FX', 'Standard FX']
df_savings_type_eq_raw_clmn_expect_lt = ['Report type', 'Standard type']

category_equalizer_clmns_conversion = {df_category_eq_raw_clmn_expect_lt[0]: category_report_clmn,
                                         df_category_eq_raw_clmn_expect_lt[1]: category_clmn}
location_equalizer_clmns_conversion = {df_location_eq_raw_clmn_expect_lt[0]: location_report_clmn,
                                         df_location_eq_raw_clmn_expect_lt[1]: location_clmn}
uom_equalizer_clmns_conversion = {df_uom_eq_raw_clmn_expect_lt[0]: bgt_uom_report_clmn,
                                    df_uom_eq_raw_clmn_expect_lt[1]: bgt_uom_clmn}
currency_equalizer_clmns_conversion = {df_currency_eq_raw_clmn_expect_lt[0]: bgt_currency_report_clmn,
                                         df_currency_eq_raw_clmn_expect_lt[1]: bgt_currency_clmn}
savings_type_equalizer_clmns_conversion = {df_savings_type_eq_raw_clmn_expect_lt[0]: savings_type_report_clmn,
                                             df_savings_type_eq_raw_clmn_expect_lt[1]: savings_type_clmn}

category_eq_error_str = "\nCat eq file:\n"
location_eq_error_str = "\nLoc eq file:\n"
currency_eq_error_str = "\nCur eq file:\n"
uom_eq_error_str = "\nUom eq file:\n"
savings_type_eq_error_str = "\nSv tp eq file:\n"


### uom and currency conversion ###
filename_conv = './inputs/Conversion table.xlsx'
filename_conv_csv = './outputs/conversion_table.csv'
filename_ref_uom_csv = './outputs/reference_uom_currency.csv'

conv_old_uom_clmn = "Old UoM"
conv_new_uom_clmn = "New UoM"
conv_multiplier_clmn = "Multiplier"

df_conv_raw_clmn_expect_lt = ['PN', 'From',	'To', 'Multiplier']

conv_clmns_conversion_base = {df_conv_raw_clmn_expect_lt[0]: code_clmn,
                                df_conv_raw_clmn_expect_lt[1]: conv_old_uom_clmn,
                                df_conv_raw_clmn_expect_lt[2]: conv_new_uom_clmn,
                                df_conv_raw_clmn_expect_lt[3]: conv_multiplier_clmn}

ref_uom_clmn = 'Reference UoM'
ref_currency_clmn = 'Reference Currency'

conv_error_str = "\nConv file:\n"

#############################                1) DATA CLEANING                     ######################################
########################    Load excel files    ########################
### budget ###
df_wide_bgt = pd.read_excel(filename_bgt)

### actuals ###
df_wide_act = pd.read_excel(filename_act)

### forecast ###
df_wide_frc_vol = pd.read_excel(filename_frc, sheet_name=sheet_frc_vol)
df_wide_frc_as_bgt = pd.read_excel(filename_frc, sheet_name=sheet_frc_as_bgt)
df_wide_frc_as_act = pd.read_excel(filename_frc, sheet_name=sheet_frc_as_act)
df_wide_frc_as_cnst = pd.read_excel(filename_frc, sheet_name=sheet_frc_as_cnst)
df_wide_frc_as_inf = pd.read_excel(filename_frc, sheet_name=sheet_frc_as_inf)
df_wide_frc_as_crv = pd.read_excel(filename_frc, sheet_name=sheet_frc_as_crv)

## predecessor ##
df_pred = pd.read_excel(filename_pred)

### equalization files ###
df_category_equalizer = pd.read_excel(filename_category_eq)
df_location_equalizer = pd.read_excel(filename_location_eq)
df_currency_equalizer = pd.read_excel(filename_currency_eq)
df_uom_equalizer = pd.read_excel(filename_uom_eq)
df_savings_type_equalizer = pd.read_excel(filename_savings_type_eq)

### conversion ###
df_conv = pd.read_excel(filename_conv)

#  forecast, baseline, and project mapping

######################## Check column integrity ########################
### budget ###
[clmns_to_delete_bgt, error_msg] = fc.file_clmn_integrity(df_wide_bgt, df_wide_bgt_raw_clmn_expect_lt, bgt_error_str)

### actuals ###
[clmns_to_delete_act, error_msg] = fc.file_clmn_integrity(df_wide_act, df_wide_act_raw_clmn_expect_lt, act_error_str,
                                                          error_msg)

### forecast ###
[clmns_to_delete_frc_vol, error_msg] = fc.file_clmn_integrity(df_wide_frc_vol, df_wide_frc_vol_raw_clmn_expect_lt,
                                                              frc_error_str, error_msg)
[clmns_to_delete_frc_as_bgt, error_msg] = fc.file_clmn_integrity(df_wide_frc_as_bgt,
                                                                 df_wide_frc_as_bgt_raw_clmn_expect_lt, frc_error_str,
                                                                 error_msg)
[clmns_to_delete_frc_as_act, error_msg] = fc.file_clmn_integrity(df_wide_frc_as_act,
                                                                 df_wide_frc_as_act_raw_clmn_expect_lt, frc_error_str,
                                                                 error_msg)
[clmns_to_delete_frc_as_cnst, error_msg] = fc.file_clmn_integrity(df_wide_frc_as_cnst,
                                                                  df_wide_frc_as_cnst_raw_clmn_expect_lt, frc_error_str,
                                                                  error_msg)
[clmns_to_delete_frc_as_inf, error_msg] = fc.file_clmn_integrity(df_wide_frc_as_inf,
                                                                 df_wide_frc_as_inf_raw_clmn_expect_lt, frc_error_str,
                                                                 error_msg)
[clmns_to_delete_frc_as_crv, error_msg] = fc.file_clmn_integrity(df_wide_frc_as_crv,
                                                                 df_wide_frc_as_crv_raw_clmn_expect_lt, frc_error_str,
                                                                 error_msg)

######################## Drop extra columns ########################
### budget ###
df_wide_bgt = df_wide_bgt.filter(items=df_wide_bgt_raw_clmn_expect_lt, axis=1)

### actuals ###
df_wide_act = df_wide_act.filter(items=df_wide_act_raw_clmn_expect_lt, axis=1)

### forecast ###
df_wide_frc_vol = df_wide_frc_vol.filter(items=df_wide_frc_vol_raw_clmn_expect_lt, axis=1)
df_wide_frc_as_bgt = df_wide_frc_as_bgt.filter(items=df_wide_frc_as_bgt_raw_clmn_expect_lt, axis=1)
df_wide_frc_as_act = df_wide_frc_as_act.filter(items=df_wide_frc_as_act_raw_clmn_expect_lt, axis=1)
df_wide_frc_as_cnst = df_wide_frc_as_cnst.filter(items=df_wide_frc_as_cnst_raw_clmn_expect_lt, axis=1)
df_wide_frc_as_inf = df_wide_frc_as_inf.filter(items=df_wide_frc_as_inf_raw_clmn_expect_lt, axis=1)
df_wide_frc_as_crv = df_wide_frc_as_crv.filter(items=df_wide_frc_as_crv_raw_clmn_expect_lt, axis=1)


## predecessor ##
df_pred = df_pred.filter(items=df_pred_raw_clmn_expect_lt, axis=1)

### Equalization ###
df_category_equalizer = df_category_equalizer.filter(items=df_category_eq_raw_clmn_expect_lt, axis=1)
df_location_equalizer = df_location_equalizer.filter(items=df_location_eq_raw_clmn_expect_lt, axis=1)
df_currency_equalizer = df_currency_equalizer.filter(items=df_currency_eq_raw_clmn_expect_lt, axis=1)
df_uom_equalizer = df_uom_equalizer.filter(items=df_uom_eq_raw_clmn_expect_lt, axis=1)
df_savings_type_equalizer = df_savings_type_equalizer.filter(items=df_savings_type_eq_raw_clmn_expect_lt, axis=1)

### conversion ###
df_conv = df_conv.filter(items=df_conv_raw_clmn_expect_lt, axis=1)

######################## Drop extra rows ########################
### budget ###
[df_wide_bgt, error_msg] = fc.clear_extra_rows(df_wide_bgt, df_wide_bgt_raw_clmn_expect_lt[0], bgt_error_str,
                                               error_msg)
### actuals ###
[df_wide_act, error_msg] = fc.clear_extra_rows(df_wide_act, df_wide_act_raw_clmn_expect_lt[0], act_error_str,
                                               error_msg)
### forecast ###
# forecast files will be fully generated from scratch, therefore, there is not need to clean extra rows.

## predecessor ##
[df_pred, error_msg] = fc.clear_extra_rows(df_pred, df_pred_raw_clmn_expect_lt[0], pred_error_str, error_msg)

### equalization ###
[df_category_equalizer, error_msg] = fc.clear_extra_rows(df_category_equalizer,
                                                         df_category_eq_raw_clmn_expect_lt[0],
                                                         category_eq_error_str, error_msg)
[df_location_equalizer, error_msg] = fc.clear_extra_rows(df_location_equalizer,
                                                         df_location_eq_raw_clmn_expect_lt[0],
                                                         location_eq_error_str, error_msg)
[df_currency_equalizer, error_msg] = fc.clear_extra_rows(df_currency_equalizer,
                                                         df_currency_eq_raw_clmn_expect_lt[0],
                                                         currency_eq_error_str, error_msg)
[df_uom_equalizer, error_msg] = fc.clear_extra_rows(df_uom_equalizer,
                                                    df_uom_eq_raw_clmn_expect_lt[0],
                                                    uom_eq_error_str, error_msg)
[df_savings_type_equalizer, error_msg] = fc.clear_extra_rows(df_savings_type_equalizer,
                                                             df_savings_type_eq_raw_clmn_expect_lt[0],
                                                             savings_type_eq_error_str, error_msg)


### conversion ###
[df_conv, error_msg] = fc.clear_extra_rows(df_conv, df_conv_raw_clmn_expect_lt[0], conv_error_str, error_msg)

######################## Change column names ########################
### budget ###
df_wide_bgt.rename(columns=bgt_clmn_conversion, inplace=True)

### actuals ###
# Breaking dataframe in two before changing names before changing format
df_act_clmn_list = df_wide_act_raw_clmn_expect_lt
desired_clmn_vol_act = len(df_act_clmn_list)-report_month
df_wide_volume_act = df_wide_act.filter(items=df_act_clmn_list[0:desired_clmn_vol_act], axis=1)

desired_clmn_pr_act_list = df_wide_act_raw_clmn_expect_lt[desired_clmn_vol_act:len(df_act_clmn_list)]
desired_clmn_pr_act_list.append(df_act_clmn_list[0])
desired_clmn_pr_act_list.append(df_act_clmn_list[5])
desired_clmn_pr_act_list.append(df_act_clmn_list[6])
df_wide_price_act = df_wide_act.filter(items=desired_clmn_pr_act_list, axis=1)

df_wide_volume_act.rename(columns=act_volume_clmn_conversion, inplace=True)
df_wide_price_act.rename(columns=act_price_clmn_conversion, inplace=True)

### forecast ###
df_wide_frc_vol.rename(columns=frc_vol_clmn_conversion, inplace=True)
df_wide_frc_as_bgt.rename(columns=frc_as_bgt_clmn_conversion, inplace=True)
df_wide_frc_as_act.rename(columns=frc_as_act_clmn_conversion, inplace=True)
df_wide_frc_as_cnst.rename(columns=frc_as_cnst_clmn_conversion, inplace=True)
df_wide_frc_as_inf.rename(columns=frc_as_inf_clmn_conversion, inplace=True)
df_wide_frc_as_crv.rename(columns=frc_as_crv_clmn_conversion, inplace=True)

## predecessor ##
df_pred.rename(columns=pred_clmns_conversion, inplace=True) # filter non-desired columns
df_pred.set_index(keys=code_clmn, drop=False, inplace=True)

### equalization ###
df_category_equalizer.rename(columns=category_equalizer_clmns_conversion, inplace=True) # filter non-desired columns
df_category_equalizer = df_category_equalizer.filter(items=[category_report_clmn, category_clmn], axis=1)

df_location_equalizer.rename(columns=location_equalizer_clmns_conversion, inplace=True)
df_location_equalizer = df_location_equalizer.filter(items=[location_report_clmn, location_clmn], axis=1)

df_currency_equalizer.rename(columns=currency_equalizer_clmns_conversion, inplace=True)
df_currency_equalizer = df_currency_equalizer.filter(items=[bgt_currency_report_clmn, bgt_currency_clmn], axis=1)

df_uom_equalizer.rename(columns=uom_equalizer_clmns_conversion, inplace=True)
df_uom_equalizer = df_uom_equalizer.filter(items=[bgt_uom_report_clmn, bgt_uom_clmn], axis=1)

df_savings_type_equalizer.rename(columns=savings_type_equalizer_clmns_conversion, inplace=True)
df_savings_type_equalizer = df_savings_type_equalizer.filter(items=[savings_type_report_clmn,
                                                                    savings_type_clmn], axis=1)

### conversion ###
df_conv.rename(columns=conv_clmns_conversion_base, inplace=True)

######################## Terminology equalization ########################
### budget ###
# filter NaN inside of merge and drop
[df_wide_bgt, error_msg] = fc.merge_and_drop(df_wide_bgt, df_category_equalizer, category_report_clmn,
                                              category_report_clmn, category_clmn, code_clmn, bgt_error_str,
                                              error_msg)
[df_wide_bgt, error_msg] = fc.merge_and_drop(df_wide_bgt, df_location_equalizer, location_report_clmn,
                                              location_report_clmn, location_clmn, code_clmn, bgt_error_str,
                                              error_msg)
[df_wide_bgt, error_msg] = fc.merge_and_drop(df_wide_bgt, df_currency_equalizer, bgt_currency_report_clmn,
                                              bgt_currency_report_clmn, bgt_currency_clmn, code_clmn,
                                              bgt_error_str, error_msg)
[df_wide_bgt, error_msg] = fc.merge_and_drop(df_wide_bgt, df_uom_equalizer, bgt_uom_report_clmn,
                                              bgt_uom_report_clmn, bgt_uom_clmn, code_clmn, bgt_error_str,
                                              error_msg)
[df_wide_bgt, error_msg] = fc.merge_and_drop(df_wide_bgt, df_savings_type_equalizer, savings_type_report_clmn,
                                              savings_type_report_clmn, savings_type_clmn, code_clmn,
                                              bgt_error_str, error_msg)

### actuals ###
[df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_category_equalizer, category_report_clmn,
                                                    category_report_clmn, category_clmn, code_clmn,
                                                    act_error_str, error_msg)
[df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_location_equalizer, location_report_clmn,
                                                    location_report_clmn, location_clmn, code_clmn,
                                                    act_error_str, error_msg)
[df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_currency_equalizer,
                                                    act_currency_report_clmn, bgt_currency_report_clmn,
                                                    act_currency_clmn, code_clmn, act_error_str, error_msg)
[df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_uom_equalizer, act_volume_uom_report_clmn,
                                                    bgt_uom_report_clmn, act_volume_uom_clmn, code_clmn,
                                                    act_error_str, error_msg)
[df_wide_price_act, error_msg] = fc.merge_and_drop(df_wide_price_act, df_uom_equalizer, act_price_uom_report_clmn,
                                                   bgt_uom_report_clmn, act_price_uom_clmn, code_clmn,
                                                   act_error_str, error_msg)

### forecast ###
# volume
[df_wide_frc_vol, error_msg] = fc.merge_and_drop(df_wide_frc_vol, df_location_equalizer, location_report_clmn,
                                                 location_report_clmn, location_clmn, code_clmn, frc_error_str,
                                                 error_msg)

[df_wide_frc_vol, error_msg] = fc.merge_and_drop(df_wide_frc_vol, df_uom_equalizer, frc_vol_uom_report_clmn,
                                                 bgt_uom_report_clmn, act_volume_uom_clmn, code_clmn, frc_error_str,
                                                 error_msg)

# as budget
[df_wide_frc_as_bgt, error_msg] = fc.merge_and_drop(df_wide_frc_as_bgt, df_location_equalizer, location_report_clmn,
                                                    location_report_clmn, location_clmn, code_clmn, frc_error_str,
                                                    error_msg)

# as actuals
[df_wide_frc_as_act, error_msg] = fc.merge_and_drop(df_wide_frc_as_act, df_location_equalizer, location_report_clmn,
                                                    location_report_clmn, location_clmn, code_clmn, frc_error_str,
                                                    error_msg)

# as a constant
[df_wide_frc_as_cnst, error_msg] = fc.merge_and_drop(df_wide_frc_as_cnst, df_location_equalizer, location_report_clmn,
                                                     location_report_clmn, location_clmn, code_clmn, frc_error_str,
                                                     error_msg)
[df_wide_frc_as_cnst, error_msg] = fc.merge_and_drop(df_wide_frc_as_cnst, df_currency_equalizer,
                                                     frc_currency_report_clmn, bgt_currency_report_clmn,
                                                     frc_currency_clmn, code_clmn, act_error_str, error_msg)
[df_wide_frc_as_cnst, error_msg] = fc.merge_and_drop(df_wide_frc_as_cnst, df_uom_equalizer, frc_price_uom_report_clmn,
                                                     bgt_uom_report_clmn, frc_price_uom_clmn, code_clmn, act_error_str,
                                                     error_msg)

# as inflation
[df_wide_frc_as_inf, error_msg] = fc.merge_and_drop(df_wide_frc_as_inf, df_location_equalizer, location_report_clmn,
                                                    location_report_clmn, location_clmn, code_clmn, frc_error_str,
                                                    error_msg)
[df_wide_frc_as_inf, error_msg] = fc.merge_and_drop(df_wide_frc_as_inf, df_currency_equalizer,
                                                    frc_currency_report_clmn, bgt_currency_report_clmn,
                                                    frc_currency_clmn, code_clmn, act_error_str, error_msg)
[df_wide_frc_as_inf, error_msg] = fc.merge_and_drop(df_wide_frc_as_inf, df_uom_equalizer, frc_price_uom_report_clmn,
                                                    bgt_uom_report_clmn, frc_price_uom_clmn, code_clmn, act_error_str,
                                                    error_msg)

# as price curve
[df_wide_frc_as_crv, error_msg] = fc.merge_and_drop(df_wide_frc_as_crv, df_location_equalizer, location_report_clmn,
                                                    location_report_clmn, location_clmn, code_clmn, frc_error_str,
                                                    error_msg)
[df_wide_frc_as_crv, error_msg] = fc.merge_and_drop(df_wide_frc_as_crv, df_currency_equalizer,
                                                    frc_currency_report_clmn, bgt_currency_report_clmn,
                                                    frc_currency_clmn, code_clmn, act_error_str, error_msg)
[df_wide_frc_as_crv, error_msg] = fc.merge_and_drop(df_wide_frc_as_crv, df_uom_equalizer, frc_price_uom_report_clmn,
                                                    bgt_uom_report_clmn, frc_price_uom_clmn, code_clmn, act_error_str,
                                                    error_msg)

######################## From wide to long format ########################
### budget ###
bgt_id_vars = [code_clmn, description_clmn, category_clmn, location_clmn, bgt_price_clmn, bgt_currency_clmn,
               bgt_uom_clmn, bgt_per_clmn, savings_type_clmn]
df_long_bgt = fc.melt_and_index(df_wide_bgt, bgt_id_vars, month_clmn, bgt_volume_clmn, code_clmn)

### actuals ###
act_volume_id_vars = [code_clmn, description_clmn, category_clmn, location_clmn, act_currency_clmn,
                      act_volume_uom_clmn, act_volume_per_clmn]
df_long_volume_act = fc.melt_and_index(df_wide_volume_act, act_volume_id_vars, month_clmn, act_volume_clmn,
                                       code_clmn)

act_price_id_vars = [code_clmn, act_price_per_clmn, act_price_uom_clmn]
df_long_price_act = fc.melt_and_index(df_wide_price_act, act_price_id_vars, month_clmn, act_price_clmn,
                                      code_clmn)

df_long_price_act.drop([code_clmn, month_clmn], axis=1, inplace=True)
df_long_act = df_long_volume_act.merge(right=df_long_price_act, left_index=True, right_index=True)

######################## Convert data types ########################
### budget ###
bgt_clmn_list = [bgt_volume_clmn, bgt_per_clmn]
num_types = float
bgt_conversion_error_string = bgt_error_str + " volume and per"

[df_long_bgt, error_msg] = fc.clean_types(df_long_bgt, bgt_clmn_list, num_types, bgt_conversion_error_string, error_msg)

### actuals ###
act_clmn_list = [act_volume_per_clmn, act_price_per_clmn, act_volume_clmn, act_price_clmn]
act_conversion_error_string = act_error_str + " volume, price and per"

[df_long_act, error_msg] = fc.clean_types(df_long_act, act_clmn_list, num_types, act_conversion_error_string, error_msg)

### conversion ###
conv_clmn_list = [conv_multiplier_clmn]
num_types = float
conv_error_string = conv_error_str + " conversion"
[df_conv, error_msg] = fc.clean_types(df_conv, conv_clmn_list, num_types, conv_error_string, error_msg)

######################## Prepare conversion files ########################
### Expand conversion table to have a PN-from-to structure
# Generate reference file
df_ref_uom = fc.generate_uom_ref_file(df_wide_bgt, code_clmn, bgt_uom_clmn, bgt_currency_clmn, ref_uom_clmn,
                                      ref_currency_clmn)
# Load and structure conversion file
conv_to_all_str = 'All'
df_conv = fc.prepare_long_uom_ref_file(df_conv, df_wide_bgt[code_clmn], code_clmn, conv_old_uom_clmn, conv_new_uom_clmn,
                                       conv_to_all_str)

######################## Include predecessor's data into budget ########################

df_long_bgt = fc.include_predecessors(df_long_bgt, df_pred, pred_code_clmn, code_clmn, month_clmn)

######################## Calculate monthly price forecast ########################
### as budget price
### as avg actuals
### as a constant
### as an inflation rate
### as a curve


# wide to long
frc_as_cvr_id_vars = [code_clmn, description_clmn, location_clmn, frc_currency_clmn, frc_price_uom_clmn,
                      frc_price_per_clmn]
df_long_frc_as_crv = fc.melt_and_index(df_wide_frc_as_crv, frc_as_cvr_id_vars, month_clmn, frc_price_clmn, code_clmn)
# add column with forecast strategy
df_long_frc_as_crv[frc_strategy_column] = frc_strategy_as_crv


######################## Reorder columns ########################
### budget ###
df_long_bgt = df_long_bgt[df_long_bgt_clmn_list]
### actuals ###
df_long_act = df_long_act[df_long_act_clmn_list]

######################## Save data-frame on CSV ########################
### budget ###
df_long_bgt.to_csv(filename_bgt_csv)

### actuals ###
df_long_act.to_csv(filename_act_csv)

## predecessor ##
df_pred.to_csv(filename_pred_csv)

### equalization ###
df_category_equalizer.to_csv(filename_category_eq_csv)
df_location_equalizer.to_csv(filename_location_eq_csv)
df_currency_equalizer.to_csv(filename_currency_eq_csv)
df_uom_equalizer.to_csv(filename_uom_eq_csv)
df_savings_type_equalizer.to_csv(filename_savings_type_eq_csv)

### conversion ###
df_conv.to_csv(filename_conv_csv)

## error msg ##
error_file = open(file_name_error_msg, "w")
error_file.write(error_msg)
error_file.close()

#############################                   2) CALCULATION ENGINE                      #############################

#############################                    3) REPORT GENERATOR                       #############################

#############################                  4) WEB INTERFACE (input)                    #############################

#############################               5) INTERACTIVE INTERFACE (output)              #############################