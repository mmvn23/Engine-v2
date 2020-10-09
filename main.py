import pandas as pd
import numpy as np
import functions as fc

# List of inputs (excel files):
#   1) Budget - OK
#   2) Actuals - OK
#   3) Forecast - OK
#         as budget price
#         as avg actuals
#         as a constant
#         as an inflation rate
#         as a curve
#   4) Baseline - OK
#   5) Predecessor - OK
#   6) UoM and FX equalization - OK
#   7) UoM and FX conversions - OK
#   8) Project mapping -OK

#############################                Input Variables                      ######################################
report_month = 5
Fiscal_Year = '2020'
filename_error_msg = './outputs/error msg {0}-{1}.txt'.format(Fiscal_Year, report_month)

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

df_wide_act_raw_clmn_expect_lt_base = ['Part Number', 'Description', 'Category', 'Plant', 'FX', 'Unity', '1 or 1,000? ']
df_wide_act_raw_clmn_expect_lt = ['Part Number', 'Description', 'Category', 'Plant', 'FX', 'Unity', '1 or 1,000? ']
# input has only 1 UoM, therefore we will have to adjust

volume_act_base_string = "v"
df_wide_act_raw_clmn_expect_lt = fc.generate_wide_clmn_expected_list(df_wide_act_raw_clmn_expect_lt,
                                                                     1, report_month, volume_act_base_string)
price_act_base_string = "P"
df_wide_act_raw_clmn_expect_lt = fc.generate_wide_clmn_expected_list(df_wide_act_raw_clmn_expect_lt, 1, report_month,
                                                                     price_act_base_string)

df_long_act_clmn_list = [description_clmn, category_clmn, location_clmn, act_volume_clmn, act_volume_per_clmn,
                         act_volume_uom_clmn,  act_price_clmn, act_price_per_clmn, act_price_uom_clmn,
                         act_currency_clmn]

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
filename_frc_csv = './outputs/forecast {0}-{1}.csv'.format(Fiscal_Year, report_month)

sheet_frc_vol = 'Volume'
sheet_frc_as_bgt = 'Budget'
sheet_frc_as_act = 'YTD'
sheet_frc_as_cnst = 'Constant'
sheet_frc_as_inf = 'Inflation rate'
sheet_frc_as_crv = 'Price curve'

frc_vol_uom_report_clmn = 'report_frc_volume_uom'
frc_vol_uom_clmn = 'frc_volume_uom'
frc_vol_per_clmn = 'frc_volume_per_uom'
frc_vol_clmn = 'frc_volume'
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
frc_strategy_as_act = 'Avg actuals'
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

df_long_frc_clmn_list = [description_clmn, category_clmn, location_clmn, frc_vol_clmn, frc_vol_per_clmn,
                         frc_vol_uom_clmn,  frc_price_clmn, frc_price_per_clmn, frc_price_uom_clmn, frc_currency_clmn,
                         frc_strategy_column]

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

### baseline ###
filename_bsl = './inputs/Baseline.xlsx'
filename_bsl_csv = './outputs/baseline {0}.csv'.format(Fiscal_Year)
df_bsl_raw_clmn_expect_lt = ['Part Number', 'Plant', 'Description', 'Baseline', 'Unity', '1 or 1,000? ', 'FX',
                             'Last FY']
bsl_error_str = "\nBaseline file:\n"
bsl_price_clmn = 'bsl_price'
bsl_price_ly = 'bsl_average_price_last_year'
bsl_price_uom_report_clmn = 'report_bsl_price_uom'
bsl_price_uom_clmn = 'bsl_price_uom'
bsl_price_per_clmn = 'bsl_price_per'
bsl_currency_report_clmn = 'report_bsl_currency'
bsl_currency_clmn = 'bsl_currency'
bsl_pred_code_clmn = 'bsl_predecessor'

bsl_clmns_conversion = {df_bsl_raw_clmn_expect_lt[0]: code_clmn,
                        df_bsl_raw_clmn_expect_lt[1]: location_report_clmn,
                        df_bsl_raw_clmn_expect_lt[2]: description_clmn,
                        df_bsl_raw_clmn_expect_lt[3]: bsl_price_clmn,
                        df_bsl_raw_clmn_expect_lt[4]: bsl_price_uom_report_clmn,
                        df_bsl_raw_clmn_expect_lt[5]: bsl_price_per_clmn,
                        df_bsl_raw_clmn_expect_lt[6]: bsl_currency_report_clmn,
                        df_bsl_raw_clmn_expect_lt[7]: bsl_price_ly}

### predecessor ###
filename_pred = './inputs/yhold.xlsx'
filename_pred_csv = './outputs/predecessors {0}-{1}.csv'.format(Fiscal_Year, report_month)
df_pred_raw_clmn_expect_lt = ['From', 'To']
pred_error_str = "\nPredecessor file:\n"
pred_clmns_conversion = {df_pred_raw_clmn_expect_lt[0]: pred_code_clmn,
                         df_pred_raw_clmn_expect_lt[1]: code_clmn}

### project mapping ###
filename_pjmp = './inputs/project mapping.xlsx'
filename_pjmp_csv = './outputs/project mapping {0}-{1}.csv'.format(Fiscal_Year, report_month)

sheet_pjmp_pcent = '% based'
sheet_pjmp_cnst = 'Value'
sheet_pjmp_pj_list = 'project list'

pjmp_code_clmn = 'project_code'
pjmp_description_clmn = 'project_description'
pjmp_pcent_clmn = 'project_percent_savings'
pjmp_cnst_clmn = 'project_constant_savings'
pjmp_report_uom_clmn = 'report_project_uom'
pjmp_uom_clmn = 'project_uom'
pjmp_per_clmn = 'project_per'
pjmp_currency_report_clmn = 'report_project_currency'
pjmp_currency_clmn = 'project_currency'
pjmp_type_report_clmn = 'report_project_type'
pjmp_type_clmn = 'project_type'
pjmp_sav_assignment_type = 'savings_assignment_type'
pjmp_pcent_str = 'percent'
pjmp_cnst_str = 'constant'
pjmp_start_month_clmn = 'project_start_month'

df_pjmp_pcent_raw_clmn_expect_lt = ['Part Number', 'Plant',	'Description',	'project code',	'project name',	'%']
df_pjmp_cnst_raw_clmn_expect_lt = ['Part Number', 'Plant',	'Description',	'Pj code',	'Pj Name',	'Value',	'Unity',
                                   '1 or 1,000? ',	'FX']
df_pjmp_pj_list_raw_clmn_expect_lt = ['Code',	'Name',	'Type', 'kick-off mth']

df_pjmp_clmn_list = [code_clmn, description_clmn, location_clmn, pjmp_code_clmn, pjmp_description_clmn,
                     pjmp_sav_assignment_type, pjmp_pcent_clmn, pjmp_cnst_clmn, pjmp_uom_clmn, pjmp_per_clmn,
                     pjmp_currency_clmn]

pjmp_pcent_clmns_conversion_base = {df_pjmp_pcent_raw_clmn_expect_lt[0]: code_clmn,
                                    df_pjmp_pcent_raw_clmn_expect_lt[1]: location_report_clmn,
                                    df_pjmp_pcent_raw_clmn_expect_lt[2]: description_clmn,
                                    df_pjmp_pcent_raw_clmn_expect_lt[3]: pjmp_code_clmn,
                                    df_pjmp_pcent_raw_clmn_expect_lt[4]: pjmp_description_clmn,
                                    df_pjmp_pcent_raw_clmn_expect_lt[5]: pjmp_pcent_clmn}

pjmp_cnst_clmns_conversion_base = {df_pjmp_cnst_raw_clmn_expect_lt[0]: code_clmn,
                                   df_pjmp_cnst_raw_clmn_expect_lt[1]: location_report_clmn,
                                   df_pjmp_cnst_raw_clmn_expect_lt[2]: description_clmn,
                                   df_pjmp_cnst_raw_clmn_expect_lt[3]: pjmp_code_clmn,
                                   df_pjmp_cnst_raw_clmn_expect_lt[4]: pjmp_description_clmn,
                                   df_pjmp_cnst_raw_clmn_expect_lt[5]: pjmp_cnst_clmn,
                                   df_pjmp_cnst_raw_clmn_expect_lt[6]: pjmp_report_uom_clmn,
                                   df_pjmp_cnst_raw_clmn_expect_lt[7]: pjmp_per_clmn,
                                   df_pjmp_cnst_raw_clmn_expect_lt[8]: pjmp_currency_report_clmn}

pjmp_pj_list_clmns_conversion_base = {df_pjmp_pj_list_raw_clmn_expect_lt[0]: pjmp_code_clmn,
                                      df_pjmp_pj_list_raw_clmn_expect_lt[1]: pjmp_description_clmn,
                                      df_pjmp_pj_list_raw_clmn_expect_lt[2]: pjmp_type_report_clmn,
                                      df_pjmp_pj_list_raw_clmn_expect_lt[3]: pjmp_start_month_clmn}

pjmp_pcent_error_str = "\n Pj Mapping file (percent):\n"
pjmp_cnst_error_str = "\n Pj Mapping file (constant):\n"
pjmp_pj_list_error_str = "\n Pj Mapping file (project list):\n"

### Uom and currency equalization ###
filename_category_eq = './inputs/category equalization.xlsx'
filename_location_eq = './inputs/plant equalization.xlsx'
filename_currency_eq = './inputs/FX equalization.xlsx'
filename_uom_eq = './inputs/unity equalization.xlsx'
filename_savings_type_eq = './inputs/sav type equalization.xlsx'
filename_project_type_eq = './inputs/proj type equalization.xlsx'

filename_category_eq_csv = './outputs/category equalization.csv'
filename_location_eq_csv = './outputs/location equalization.csv'
filename_currency_eq_csv = './outputs/currency equalization.csv'
filename_uom_eq_csv = './outputs/uom equalization.csv'
filename_savings_type_eq_csv = './outputs/savings type equalization.csv'
filename_project_type_eq_csv = './outputs/project type equalization.csv'

df_category_eq_raw_clmn_expect_lt = ['Report category', 'Standard category']
df_location_eq_raw_clmn_expect_lt = ['Report plant', 'Standard plant']
df_uom_eq_raw_clmn_expect_lt = ['Report UoM',	'Standard UoM']
df_currency_eq_raw_clmn_expect_lt = ['Report FX', 'Standard FX']
df_savings_type_eq_raw_clmn_expect_lt = ['Report type', 'Standard type']
df_project_type_eq_raw_clmn_expect_lt = ['Report pj type',	'Standard pj type']

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
project_type_equalizer_clmns_conversion = {df_project_type_eq_raw_clmn_expect_lt[0]: pjmp_type_report_clmn,
                                           df_project_type_eq_raw_clmn_expect_lt[1]: pjmp_type_clmn}

category_eq_error_str = "\nCat eq file:\n"
location_eq_error_str = "\nLoc eq file:\n"
currency_eq_error_str = "\nCur eq file:\n"
uom_eq_error_str = "\nUom eq file:\n"
savings_type_eq_error_str = "\nSv tp eq file:\n"
project_type_eq_error_str = "\nPj tp eq file:\n"

### uom and currency conversion ###
filename_conv = './inputs/Conversion table.xlsx'
filename_conv_csv = './outputs/conversion_table.csv'
filename_ref_uom_csv = './outputs/reference_uom_currency.csv'

reference_currency = 'USD'
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

### uom and currency reference ###
uom_ref_per_price_clmn = 'Ref_per_price'
uom_ref_uom_price_clmn = 'Ref_uom_price'
uom_ref_currency_clmn = 'Ref_currency'
uom_ref_per_volume_clmn = 'Ref_per_volume'
uom_ref_uom_volume_clmn = 'Ref_uom_volume'

filename_uom_ref_csv = './outputs/uom reference.csv'

########################    Calculation Engine    ########################
cy_volume_clmn = 'current_year_volume'
cy_volume_per_clmn = 'current_year_volume_per'
cy_volume_uom_clmn = 'current_year_volume_uom'
cy_price_clmn = 'current_year_price'
cy_price_per_clmn = 'current_year_price_per'
cy_price_uom_clmn = 'current_year_price_uom'
cy_currency_clmn = 'current_year_currency'
cy_type_report_clmn = 'type_report'
cy_act_report = 'Actuals'
cy_frc_report = 'Forecast'

cy_price_at_ref_clmn = 'current_price_at_ref'
cy_volume_at_ref_clmn = 'current_volume_at_ref'

cy_to_ref_mult_price_uom_clmn = 'cy_to_ref_multiplier_uom_price'
cy_to_ref_mult_price_per_clmn = 'cy_to_ref_multiplier_per_price'
cy_to_ref_mult_currency_clmn = 'cy_to_ref_multiplier_currency'
cy_to_ref_mult_volume_uom_clmn = 'cy_to_ref_multiplier_uom_volume'
cy_to_ref_mult_volume_per_clmn = 'cy_to_ref_multiplier_per_volume'

bgt_price_at_ref_clmn = 'budget_price_at_ref'
bgt_volume_at_ref_clmn = 'budget_volume_at_ref'

bgt_to_ref_mult_price_uom_clmn = 'bgt_to_ref_multiplier_uom_price'
bgt_to_ref_mult_price_per_clmn = 'bgt_to_ref_multiplier_per_price'
bgt_to_ref_mult_currency_clmn = 'bgt_to_ref_multiplier_currency'
bgt_to_ref_mult_volume_uom_clmn = 'bgt_to_ref_multiplier_uom_volume'
bgt_to_ref_mult_volume_per_clmn = 'bgt_to_ref_multiplier_per_volume'

bsl_price_at_ref_clmn = 'baseline_price_at_ref'

bsl_to_ref_mult_price_uom_clmn = 'bsl_to_ref_multiplier_uom_price'
bsl_to_ref_mult_price_per_clmn = 'bsl_to_ref_multiplier_per_price'
bsl_to_ref_mult_currency_clmn = 'bsl_to_ref_multiplier_currency'

ly_price_at_ref_clmn = 'ly_avg_price_at_ref'

ly_spend_avg_pr_bgt_vl_clmn = 'ly_spd_at_ly_avg_price_bgt_volume'
bsl_spend_bsl_pr_bgt_vl_clmn = 'bsl_spd_at_bsl_price_bgt_volume'
bsl_inflation_clmn = 'baseline_inflation'
bgt_spend_bgt_pr_bgt_vl_clmn = 'bgt_spd_at_bgt_price_bgt_volume'
bgt_savings_clmn = 'budget_savings'
bgt_spend_bgt_pr_cy_vl_clmn = 'bgt_spd_at_bgt_price_cy_volume'
volume_adjustment_clmn = 'bgt_spend_adjustment_due_to_volume'
cy_spend_cy_pr_cy_vl_clmn = 'cy_spd_at_cy_price_cy_volume'
cy_bgt_savings_clmn = 'savings_vs_budget'
bsl_spend_bsl_pr_cy_vl_clmn = 'bsl_spd_at_bsl_price_cy_volume'
cy_bsl_savings_clmn = 'savings_vs_baseline'
volume_influence_vs_bsl_clmn = 'volume_influence_vs_baseline'
volume_influence_vs_bgt_clmn = 'volume_influence_vs_budget'

engine_error_str = 'ENGINE ERROR: '

filename_cy_csv = './outputs/Savings Report – FY{0} P{1} per PN.csv'.format(Fiscal_Year, report_month)
filename_pj_csv = './outputs/Projects Report – FY{0} P{1} per PN.csv'.format(Fiscal_Year, report_month)
filename_error_msg_engine = './outputs/error msg Sv Rpt – FY{0} P{1} per PN.txt'.format(Fiscal_Year, report_month)

pjmp_cnst_at_ref_clmn = 'constant_at_ref'
pjmp_to_ref_mult_uom_clmn = 'pjmp_to_ref_multiplier_uom'
pjmp_to_ref_mult_per_clmn = 'pjmp_to_ref_multiplier_per'
pjmp_to_ref_mult_currency_clmn = 'pjmp_to_ref_multiplier_currency'

proj_str_description = 'project_name_'
proj_str_value = 'project_value_vs_bsl_'
proj_str_code = 'project_code_'

proj_str_description_gen = 'project_description_0'
proj_str_value_gen = 'project_value_vs_bsl_0'
proj_str_code_gen = 'project_code_0'

gen_pj_code_str = 'GP-'
gen_pj_description_str = '-Negotiations'

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

## baseline ##
df_bsl = pd.read_excel(filename_bsl)

## predecessor ##
df_pred = pd.read_excel(filename_pred)

### equalization files ###
df_category_equalizer = pd.read_excel(filename_category_eq)
df_location_equalizer = pd.read_excel(filename_location_eq)
df_currency_equalizer = pd.read_excel(filename_currency_eq)
df_uom_equalizer = pd.read_excel(filename_uom_eq)
df_savings_type_equalizer = pd.read_excel(filename_savings_type_eq)
df_project_type_equalizer = pd.read_excel(filename_project_type_eq)

### conversion ###
df_conv = pd.read_excel(filename_conv)

### project mapping ###
df_pjmp_pcent = pd.read_excel(filename_pjmp, sheet_name=sheet_pjmp_pcent)
df_pjmp_cnst = pd.read_excel(filename_pjmp, sheet_name=sheet_pjmp_cnst)
df_pjmp_pj_list = pd.read_excel(filename_pjmp, sheet_name=sheet_pjmp_pj_list)

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

## baseline ##
df_bsl = df_bsl.filter(items=df_bsl_raw_clmn_expect_lt, axis=1)

## predecessor ##
df_pred = df_pred.filter(items=df_pred_raw_clmn_expect_lt, axis=1)

### equalization ###
df_category_equalizer = df_category_equalizer.filter(items=df_category_eq_raw_clmn_expect_lt, axis=1)
df_location_equalizer = df_location_equalizer.filter(items=df_location_eq_raw_clmn_expect_lt, axis=1)
df_currency_equalizer = df_currency_equalizer.filter(items=df_currency_eq_raw_clmn_expect_lt, axis=1)
df_uom_equalizer = df_uom_equalizer.filter(items=df_uom_eq_raw_clmn_expect_lt, axis=1)
df_savings_type_equalizer = df_savings_type_equalizer.filter(items=df_savings_type_eq_raw_clmn_expect_lt, axis=1)
df_project_type_equalizer = df_project_type_equalizer.filter(items=df_project_type_eq_raw_clmn_expect_lt, axis=1)

### conversion ###
df_conv = df_conv.filter(items=df_conv_raw_clmn_expect_lt, axis=1)

### project mapping ###
df_pjmp_pcent = df_pjmp_pcent.filter(items=df_pjmp_pcent_raw_clmn_expect_lt, axis=1)
df_pjmp_cnst = df_pjmp_cnst.filter(items=df_pjmp_cnst_raw_clmn_expect_lt, axis=1)
df_pjmp_pj_list = df_pjmp_pj_list.filter(items=df_pjmp_pj_list_raw_clmn_expect_lt, axis=1)

######################## Drop extra rows ########################
### budget ###
[df_wide_bgt, error_msg] = fc.clear_extra_rows(df_wide_bgt, df_wide_bgt_raw_clmn_expect_lt[0], bgt_error_str,
                                               error_msg)
### actuals ###
[df_wide_act, error_msg] = fc.clear_extra_rows(df_wide_act, df_wide_act_raw_clmn_expect_lt[0], act_error_str,
                                               error_msg, df_wide_act_raw_clmn_expect_lt_base)

### forecast ###
# forecast files will be fully generated from scratch, therefore, there is not need to clean extra rows.

## baseline ##
[df_bsl, error_msg] = fc.clear_extra_rows(df_bsl, df_bsl_raw_clmn_expect_lt[0], bsl_error_str, error_msg)

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
[df_project_type_equalizer, error_msg] = fc.clear_extra_rows(df_project_type_equalizer,
                                                             df_project_type_eq_raw_clmn_expect_lt[0],
                                                             project_type_eq_error_str, error_msg)

### conversion ###

[df_conv, error_msg] = fc.clear_extra_rows(df_conv, df_conv_raw_clmn_expect_lt[0], conv_error_str, error_msg,
                                           df_conv_raw_clmn_expect_lt)

### project mapping ###
[df_pjmp_pcent, error_msg] = fc.clear_extra_rows(df_pjmp_pcent, df_pjmp_pcent_raw_clmn_expect_lt[0],
                                                 pjmp_pcent_error_str, error_msg)
[df_pjmp_cnst, error_msg] = fc.clear_extra_rows(df_pjmp_cnst, df_pjmp_cnst_raw_clmn_expect_lt[0],
                                                pjmp_cnst_error_str, error_msg)
[df_pjmp_pj_list, error_msg] = fc.clear_extra_rows(df_pjmp_pj_list, df_pjmp_pj_list_raw_clmn_expect_lt[0],
                                                   pjmp_pj_list_error_str, error_msg)

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

## baseline ##
df_bsl.rename(columns=bsl_clmns_conversion, inplace=True) # filter non-desired columns
# df_bsl.set_index(keys=code_clmn, drop=False, inplace=True)

## predecessor ##
df_pred.rename(columns=pred_clmns_conversion, inplace=True) # filter non-desired columns
# df_pred.set_index(keys=code_clmn, drop=False, inplace=True)

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

df_project_type_equalizer.rename(columns=project_type_equalizer_clmns_conversion, inplace=True)
df_project_type_equalizer = df_project_type_equalizer.filter(items=[pjmp_type_report_clmn, pjmp_type_clmn], axis=1)

### conversion ###
df_conv.rename(columns=conv_clmns_conversion_base, inplace=True)

### project mapping ###
df_pjmp_pcent.rename(columns=pjmp_pcent_clmns_conversion_base, inplace=True)
df_pjmp_cnst.rename(columns=pjmp_cnst_clmns_conversion_base, inplace=True)
df_pjmp_pj_list.rename(columns=pjmp_pj_list_clmns_conversion_base, inplace=True)

######################## Remove key duplicates ########################
### budget ###
df_wide_bgt = fc.remove_key_duplicates(df_wide_bgt, code_clmn)

### actuals ###
df_wide_volume_act = fc.remove_key_duplicates(df_wide_volume_act, code_clmn)
df_wide_price_act = fc.remove_key_duplicates(df_wide_price_act, code_clmn)

### forecast ###
df_wide_frc_vol = fc.remove_key_duplicates(df_wide_frc_vol, code_clmn)
df_wide_frc_as_bgt = fc.remove_key_duplicates(df_wide_frc_as_bgt, code_clmn)
df_wide_frc_as_act = fc.remove_key_duplicates(df_wide_frc_as_act, code_clmn)
df_wide_frc_as_cnst = fc.remove_key_duplicates(df_wide_frc_as_cnst, code_clmn)
df_wide_frc_as_inf = fc.remove_key_duplicates(df_wide_frc_as_inf, code_clmn)
df_wide_frc_as_crv = fc.remove_key_duplicates(df_wide_frc_as_crv, code_clmn)

## baseline ##
df_bsl = fc.remove_key_duplicates(df_bsl, code_clmn) #indexed

## predecessor ##
df_pred = fc.remove_key_duplicates(df_pred, pred_code_clmn) #indexed

### equalization ###
df_category_equalizer = fc.remove_key_duplicates(df_category_equalizer, category_report_clmn)
df_location_equalizer = fc.remove_key_duplicates(df_location_equalizer, location_report_clmn)
df_currency_equalizer = fc.remove_key_duplicates(df_currency_equalizer, bgt_currency_report_clmn)
df_uom_equalizer = fc.remove_key_duplicates(df_uom_equalizer, bgt_uom_report_clmn)
df_savings_type_equalizer = fc.remove_key_duplicates(df_savings_type_equalizer, savings_type_report_clmn)
df_project_type_equalizer = fc.remove_key_duplicates(df_project_type_equalizer, pjmp_type_report_clmn)

### conversion ###

### project mapping ###
df_pjmp_pj_list = fc.remove_key_duplicates(df_pjmp_pj_list, pjmp_code_clmn)

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

df_wide_act_volume_clmn_expect_lt_base = [code_clmn, description_clmn, category_clmn, location_report_clmn,
                                          act_currency_report_clmn, act_volume_uom_report_clmn, act_volume_per_clmn]
[df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_category_equalizer, category_report_clmn,
                                                    category_report_clmn, category_clmn, code_clmn,
                                                    act_error_str, error_msg, df_wide_act_volume_clmn_expect_lt_base)

df_wide_act_volume_clmn_expect_lt_base = [code_clmn, description_clmn, category_clmn, location_clmn,
                                          act_currency_report_clmn, act_volume_uom_report_clmn, act_volume_per_clmn]
[df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_location_equalizer, location_report_clmn,
                                                    location_report_clmn, location_clmn, code_clmn,
                                                    act_error_str, error_msg, df_wide_act_volume_clmn_expect_lt_base)

df_wide_act_volume_clmn_expect_lt_base = [code_clmn, description_clmn, category_clmn, location_clmn,
                                          act_currency_clmn, act_volume_uom_report_clmn, act_volume_per_clmn]
[df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_currency_equalizer,
                                                    act_currency_report_clmn, bgt_currency_report_clmn,
                                                    act_currency_clmn, code_clmn, act_error_str, error_msg,
                                                    df_wide_act_volume_clmn_expect_lt_base)

df_wide_act_volume_clmn_expect_lt_base = [code_clmn, description_clmn, category_clmn, location_clmn,
                                          act_currency_clmn, act_volume_uom_clmn, act_volume_per_clmn]
[df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_uom_equalizer, act_volume_uom_report_clmn,
                                                    bgt_uom_report_clmn, act_volume_uom_clmn, code_clmn,
                                                    act_error_str, error_msg, df_wide_act_volume_clmn_expect_lt_base)

df_wide_act_price_clmn_expect_lt_base = [code_clmn, act_price_per_clmn]
[df_wide_price_act, error_msg] = fc.merge_and_drop(df_wide_price_act, df_uom_equalizer, act_price_uom_report_clmn,
                                                   bgt_uom_report_clmn, act_price_uom_clmn, code_clmn,
                                                   act_error_str, error_msg, df_wide_act_price_clmn_expect_lt_base)

### forecast ###
# volume
df_wide_frc_volume_clmn_expect_lt_base = [code_clmn, description_clmn, location_clmn, frc_vol_uom_report_clmn,
                                          frc_vol_per_clmn]
[df_wide_frc_vol, error_msg] = fc.merge_and_drop(df_wide_frc_vol, df_location_equalizer, location_report_clmn,
                                                 location_report_clmn, location_clmn, code_clmn, frc_error_str,
                                                 error_msg, df_wide_frc_volume_clmn_expect_lt_base)

df_wide_frc_volume_clmn_expect_lt_base = [code_clmn, description_clmn, location_clmn, frc_vol_uom_clmn,
                                          frc_vol_per_clmn]
[df_wide_frc_vol, error_msg] = fc.merge_and_drop(df_wide_frc_vol, df_uom_equalizer, frc_vol_uom_report_clmn,
                                                 bgt_uom_report_clmn, frc_vol_uom_clmn, code_clmn, frc_error_str,
                                                 error_msg, df_wide_frc_volume_clmn_expect_lt_base)

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
### baseline ###
[df_bsl, error_msg] = fc.merge_and_drop(df_bsl, df_location_equalizer, location_report_clmn, location_report_clmn,
                                        location_clmn, code_clmn, bsl_error_str, error_msg)
[df_bsl, error_msg] = fc.merge_and_drop(df_bsl, df_currency_equalizer, bsl_currency_report_clmn,
                                        bgt_currency_report_clmn, bsl_currency_clmn, code_clmn, bsl_error_str,
                                        error_msg)

[df_bsl, error_msg] = fc.merge_and_drop(df_bsl, df_uom_equalizer, bsl_price_uom_report_clmn, bgt_uom_report_clmn,
                                        bsl_price_uom_clmn, code_clmn, bsl_error_str, error_msg)

### project mapping ###
[df_pjmp_pcent, error_msg] = fc.merge_and_drop(df_pjmp_pcent, df_location_equalizer, location_report_clmn,
                                               location_report_clmn, location_clmn, code_clmn, pjmp_pcent_error_str,
                                               error_msg)

[df_pjmp_cnst, error_msg] = fc.merge_and_drop(df_pjmp_cnst, df_location_equalizer, location_report_clmn,
                                              location_report_clmn, location_clmn, code_clmn, pjmp_cnst_error_str,
                                              error_msg)
[df_pjmp_cnst, error_msg] = fc.merge_and_drop(df_pjmp_cnst, df_uom_equalizer, pjmp_report_uom_clmn, bgt_uom_report_clmn,
                                              pjmp_uom_clmn, code_clmn, act_error_str, error_msg)
[df_pjmp_cnst, error_msg] = fc.merge_and_drop(df_pjmp_cnst, df_currency_equalizer, pjmp_currency_report_clmn,
                                              bgt_currency_report_clmn, pjmp_currency_clmn, code_clmn,
                                              pjmp_cnst_error_str, error_msg)

[df_pjmp_pj_list, error_msg] = fc.merge_and_drop(df_pjmp_pj_list, df_project_type_equalizer, pjmp_type_report_clmn,
                                                 pjmp_type_report_clmn, pjmp_type_clmn, pjmp_code_clmn,
                                                 pjmp_pj_list_error_str, error_msg)

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

df_long_act = df_long_volume_act.merge(right=df_long_price_act, left_index=True, right_index=True)

### forecast volume ###

frc_volume_id_vars = [code_clmn, description_clmn, location_clmn, frc_vol_uom_clmn, frc_vol_per_clmn]
df_long_frc_vol = fc.melt_and_index(df_wide_frc_vol, frc_volume_id_vars, month_clmn, frc_vol_clmn, code_clmn)

frc_vol_converting_clmns = [frc_vol_clmn]
df_long_frc_vol = fc.convert_nan_to_zero(df_long_frc_vol, frc_vol_converting_clmns)

######################## Convert data types ########################

### budget ###
bgt_clmn_list = [bgt_volume_clmn, bgt_per_clmn]
bgt_conversion_error_string = bgt_error_str + " volume and per"

[df_long_bgt, error_msg] = fc.clean_types(df_long_bgt, bgt_clmn_list, bgt_conversion_error_string, error_msg)

### actuals ###
act_clmn_list = [act_volume_per_clmn, act_price_per_clmn]
act_conversion_error_string = act_error_str + " volume, price and per"
[df_long_act, error_msg] = fc.clean_types(df_long_act, act_clmn_list, act_conversion_error_string, error_msg)

act_converting_clmns = [act_volume_clmn, act_price_clmn]
df_long_act = fc.convert_nan_to_zero(df_long_act, act_converting_clmns)

## baseline ##
bsl_clmn_list = [bsl_price_clmn, bsl_price_per_clmn]
bsl_conversion_error_string = bsl_error_str + " conversion"
[df_bsl, error_msg] = fc.clean_types(df_bsl, bsl_clmn_list, bsl_conversion_error_string, error_msg)

### conversion ###
conv_clmn_list = [conv_multiplier_clmn]
conv_error_string = conv_error_str + " conversion"

[df_conv, error_msg] = fc.clean_types(df_conv, conv_clmn_list, conv_error_string, error_msg)


### project mapping ###
pjmp_pcent_clmn_list = [pjmp_pcent_clmn]
pjmp_pcent_error_string = pjmp_pcent_error_str + " conversion"
[df_pjmp_pcent, error_msg] = fc.clean_types(df_pjmp_pcent, pjmp_pcent_clmn_list, pjmp_pcent_error_string, error_msg)

pjmp_cnst_clmn_list = [pjmp_cnst_clmn]
pjmp_cnst_error_string = pjmp_pcent_error_str + " conversion"
[df_pjmp_cnst, error_msg] = fc.clean_types(df_pjmp_cnst, pjmp_cnst_clmn_list, pjmp_cnst_error_string, error_msg)

pjmp_pj_list_clmn_list = [pjmp_cnst_clmn]
pjmp_pj_list_error_string = pjmp_pj_list_error_str + " conversion"
# pj_list dataframe does not have any numerical columns.

######################## Prepare conversion files ########################
### Generate reference file
df_ref_uom = fc.generate_uom_ref_file(df_wide_bgt, code_clmn, bgt_uom_clmn, bgt_currency_clmn, ref_uom_clmn,
                                      ref_currency_clmn)

######################## Indexing ########################
### baseline ###
df_bsl.set_index(keys=[code_clmn], drop=True, inplace=True)

## predecessor ##
df_pred.set_index(keys=[code_clmn], drop=True, inplace=True)

### equalization ###
df_category_equalizer.set_index(keys=[category_report_clmn], drop=True, inplace=True)
df_location_equalizer.set_index(keys=[location_clmn], drop=True, inplace=True)
df_currency_equalizer.set_index(keys=[bgt_currency_clmn], drop=True, inplace=True)
df_uom_equalizer.set_index(keys=[bgt_uom_report_clmn], drop=True, inplace=True)
df_savings_type_equalizer.set_index(keys=[savings_type_report_clmn], drop=True, inplace=True)


######################## Include predecessor's data into budget ########################
df_long_bgt = fc.include_predecessors(df_long_bgt, df_pred, pred_code_clmn, pred_code_clmn, code_clmn, month_clmn)
df_bsl = fc.include_predecessors(df_bsl, df_pred, pred_code_clmn, bsl_pred_code_clmn, code_clmn)

######################## Calculate monthly price forecast ########################
frc_id_vars = [code_clmn, description_clmn, location_clmn, frc_currency_clmn, frc_price_uom_clmn, frc_price_per_clmn]
frc_desired_clmn_list = [description_clmn, location_clmn, frc_currency_clmn, frc_price_uom_clmn, frc_price_per_clmn,
                         frc_price_clmn, frc_strategy_column]

### as budget price
desired_bgt_clmn_lt = [bgt_currency_clmn, bgt_uom_clmn, bgt_per_clmn, bgt_price_clmn]
bgt_matching_tuple = {bgt_currency_clmn: frc_currency_clmn,
                      bgt_uom_clmn: frc_price_uom_clmn,
                      bgt_per_clmn: frc_price_per_clmn,
                      bgt_price_clmn: frc_price_clmn}

df_long_frc_as_bgt = fc.generate_price_curve_based_on_budget(df_wide_frc_as_bgt, report_month + 1, 12,
                                                             month_clmn, frc_price_clmn, code_clmn,
                                                             frc_strategy_column, frc_strategy_as_bgt,
                                                             df_long_bgt, desired_bgt_clmn_lt, bgt_matching_tuple,
                                                             frc_desired_clmn_list)

### as avg actuals
desired_act_clmn_lt = [act_currency_clmn, act_price_uom_clmn, act_price_per_clmn, act_price_clmn, act_volume_clmn]
act_matching_tuple = {act_currency_clmn: frc_currency_clmn,
                      act_price_uom_clmn: frc_price_uom_clmn,
                      act_price_per_clmn: frc_price_per_clmn,
                      act_price_clmn: frc_price_clmn}


df_long_frc_as_act = fc.generate_price_curve_based_on_actuals(df_wide_frc_as_act, report_month + 1, 12,
                                                              month_clmn, frc_price_clmn, code_clmn,
                                                              frc_strategy_column, frc_strategy_as_act,
                                                              df_long_act, desired_act_clmn_lt, act_matching_tuple,
                                                              act_price_clmn, act_volume_clmn, frc_desired_clmn_list)

### as a constant
df_long_frc_as_cnst = fc.generate_price_curve_based_on_constant(df_wide_frc_as_cnst, df_wide_frc_as_cnst[frc_price_clmn],
                                                                report_month+1, 12, frc_id_vars, month_clmn,
                                                                frc_price_clmn, code_clmn, frc_strategy_column,
                                                                frc_strategy_as_cnst, frc_desired_clmn_list)

### as an inflation rate
df_long_frc_as_inf = fc.generate_price_curve_based_on_inflation(df_wide_frc_as_inf, report_month+1, 12, month_clmn,
                                                                frc_price_clmn, code_clmn,
                                                                frc_price_as_inf_base_price_clmn,
                                                                frc_price_as_inf_inflation_clmn,
                                                                frc_price_as_inf_month_clmn, frc_strategy_column,
                                                                frc_strategy_as_inf, frc_desired_clmn_list)

### as a curve
df_long_frc_as_crv = fc.generate_price_curve_based_on_curve(df_wide_frc_as_crv, frc_id_vars, month_clmn,
                                                            frc_price_clmn, code_clmn, frc_strategy_column,
                                                            frc_strategy_as_crv, frc_desired_clmn_list)

# unify all of them

df_long_frc = df_long_frc_as_bgt
df_long_frc = df_long_frc.append(df_long_frc_as_act)
df_long_frc = df_long_frc.append(df_long_frc_as_cnst)
df_long_frc = df_long_frc.append(df_long_frc_as_inf)
df_long_frc = df_long_frc.append(df_long_frc_as_crv)

df_long_frc_vol.drop(columns=[description_clmn, location_clmn], inplace=True)
df_long_frc = df_long_frc.merge(df_long_frc_vol, how='outer', left_index=True, right_index=True)

df_long_frc = fc.add_category_to_frc(df_long_frc, df_long_bgt, code_clmn, month_clmn, category_clmn)

######################## Calculate project list ########################
# add column with savings assignement type

df_pjmp_pcent[pjmp_sav_assignment_type] = pjmp_pcent_str
df_pjmp_pcent[pjmp_per_clmn] = 1
df_pjmp_pcent[pjmp_cnst_clmn] = 0
df_pjmp_pcent[pjmp_uom_clmn] = 'N/A'
df_pjmp_pcent[pjmp_currency_clmn] = 'N/A'

df_pjmp_cnst[pjmp_sav_assignment_type] = pjmp_cnst_str
df_pjmp_cnst[pjmp_pcent_clmn] = 0

df_pjmp_pcent = df_pjmp_pcent[df_pjmp_clmn_list]
df_pjmp_cnst = df_pjmp_cnst[df_pjmp_clmn_list]

# merge pcent and const
df_pjmp = df_pjmp_pcent
df_pjmp = df_pjmp.append(df_pjmp_cnst)

# add column with project savings type
df_pjmp_pj_list.drop(columns=pjmp_description_clmn, inplace=True)
df_pjmp = df_pjmp.merge(df_pjmp_pj_list, how='left', on=pjmp_code_clmn)
df_pjmp.set_index(keys=code_clmn, drop=True, inplace=True)

######################## Add forecast strategy ########################
### budget ###
df_long_act[frc_strategy_column] = 'NA'
df_long_act_clmn_list.append(frc_strategy_column)

################## Load and structure conversion file ##################
conv_to_all_str = 'All'

code_clmn_list = df_long_bgt.reset_index()
code_clmn_list = code_clmn_list[code_clmn]
code_clmn_list = np.unique(code_clmn_list).tolist()

df_conv = fc.prepare_long_uom_ref_file(df_conv, code_clmn_list, code_clmn, conv_old_uom_clmn, conv_new_uom_clmn,
                                       conv_to_all_str)

######################## Reorder columns ########################
### budget ###
df_long_bgt = df_long_bgt[df_long_bgt_clmn_list]
### actuals ###
df_long_act = df_long_act[df_long_act_clmn_list]
### forecast ###
df_long_frc = df_long_frc[df_long_frc_clmn_list]

### uom and currency reference file ###
df_uom_ref = df_long_bgt.reset_index(inplace=False)

df_uom_ref_clmn_expect_lt = [code_clmn, bgt_uom_clmn, bgt_currency_clmn, bgt_per_clmn]
df_uom_ref = df_uom_ref.filter(items=df_uom_ref_clmn_expect_lt, axis=1)

uom_ref_clmn_conversion = {bgt_per_clmn: uom_ref_per_price_clmn,
                           bgt_uom_clmn: uom_ref_uom_price_clmn,
                           bgt_currency_clmn: uom_ref_currency_clmn}
df_uom_ref.rename(columns=uom_ref_clmn_conversion, inplace=True)

df_uom_ref[uom_ref_per_volume_clmn] = df_uom_ref[uom_ref_per_price_clmn]
df_uom_ref[uom_ref_uom_volume_clmn] = df_uom_ref[uom_ref_uom_price_clmn]

df_uom_ref = fc.remove_key_duplicates(df_uom_ref, code_clmn)

df_uom_ref.set_index(keys=[code_clmn], drop=True, inplace=True)

df_uom_ref[uom_ref_currency_clmn] = reference_currency

df_uom_ref_clmn_list = [uom_ref_uom_volume_clmn, uom_ref_per_volume_clmn, uom_ref_uom_price_clmn,
                        uom_ref_per_price_clmn, uom_ref_currency_clmn]
df_uom_ref = df_uom_ref[df_uom_ref_clmn_list]

######################## Save data-frame on CSV ########################
### budget ###
df_long_bgt.to_csv(filename_bgt_csv)

### actuals ###
df_long_act.to_csv(filename_act_csv)

### forecast ###
df_long_frc.to_csv(filename_frc_csv)

### baseline ###
df_bsl.to_csv(filename_bsl_csv)

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

### project mapping ###
df_pjmp.to_csv(filename_pjmp_csv)

### uom and currency reference file ###
df_uom_ref.to_csv(filename_uom_ref_csv)

## error msg ##
error_file = open(filename_error_msg, "w")
error_file.write(error_msg)
error_file.close()

# print(error_msg)
#############################                   2) CALCULATION ENGINE (var. 380)           #############################
# temp location for inputs

# df_long_act
# Index: ['code', 'month']
# Columns: ['description', 'category', 'location', 'act_volume', 'act_volume_per',
#        'act_volume_uom', 'act_price', 'act_price_per', 'act_price_uom',
#        'act_currency', 'frc_strategy']

act_to_cy_clmn_conversion = {act_volume_clmn: cy_volume_clmn,
                             act_volume_per_clmn: cy_volume_per_clmn,
                             act_volume_uom_clmn: cy_volume_uom_clmn,
                             act_price_clmn: cy_price_clmn,
                             act_price_per_clmn: cy_price_per_clmn,
                             act_price_uom_clmn: cy_price_uom_clmn,
                             act_currency_clmn: cy_currency_clmn}

# df_long_frc
# Index: ['code', 'month']
# Columns: ['description', 'category', 'location', 'frc_volume',
#        'frc_volume_per_uom', 'frc_volume_uom', 'frc_price', 'frc_price_per',
#        'frc_price_uom', 'frc_currency', 'frc_strategy']
frc_to_cy_clmn_conversion = {frc_vol_clmn: cy_volume_clmn,
                             frc_vol_per_clmn: cy_volume_per_clmn,
                             frc_vol_uom_clmn: cy_volume_uom_clmn,
                             frc_price_clmn: cy_price_clmn,
                             frc_price_per_clmn: cy_price_per_clmn,
                             frc_price_uom_clmn: cy_price_uom_clmn,
                             frc_currency_clmn: cy_currency_clmn}

# df_long_bgt
# Index: ['code', 'month']
# Columns: ['description', 'category', 'location', 'savings_type', 'bgt_volume',
#        'bgt_price', 'bgt_per', 'bgt_uom', 'bgt_currency', 'bgt_predecessor']
bgt_to_cy_to_drop = [description_clmn, category_clmn, location_clmn]

# df_long_bsl
# Index: ['code']
# Columns: ['description', 'bsl_price', 'bsl_price_per',
#        'bsl_average_price_last_year', 'location', 'bsl_currency',
#        'bsl_price_uom']
bsl_to_cy_to_drop = [description_clmn, location_clmn]

# df_uom_ref
# Index: ['code']
# Columns:['Ref_uom_volume', 'Ref_per_volume', 'Ref_uom_price', 'Ref_per_price',
#        'Ref_currency']

# df_conv
# Index: ['code', 'Old UoM', 'New UoM']
# Columns: ['Multiplier']

######################### Calculating Savings per PN file #########################
# 1) merge actuals and forecast information
# 2) add budget information
# 3) add baseline information
# 4) convert UOMs and currency
# 5) calculate:
#       LY avg spend ly_spd => avg_price * bgt_vol
#       baseline inflation (USD) bsl_inf => bsl_spd - ly_spd
#       baseline spend bsl_spd => bsl_price * bgt_vol
#       budget savings bsl_sav => bgt_spd - bsl_spd
#       budget spend bgt_spd => bgt_price * bgt_vol
#       impact due to delta volume vol_imp => cy_bgt_spd - bgt_spd
#       budget spend at current year volume cy_bgt_spd => bgt_price * cy_vol
#       current year savings cy_sav => cy_spd - cy_bgt_spd
#       current year spend cy_spd => cy_price * cy_vol
#       total savings total_sav => bsl_sav + vol_imp + cy_sav

### Change columns names ###

df_long_act.rename(columns=act_to_cy_clmn_conversion, inplace=True)
df_long_act[cy_type_report_clmn] = cy_act_report

df_long_frc.rename(columns=frc_to_cy_clmn_conversion, inplace=True)
df_long_frc[cy_type_report_clmn] = cy_frc_report

### Merge actuals and forecast information ###
df_cy = df_long_act
df_cy = df_cy.append(df_long_frc)

### Add budget information ###
df_long_bgt = df_long_bgt.drop(bgt_to_cy_to_drop, axis=1, inplace=False)
df_cy = df_cy.merge(df_long_bgt, how='left', left_index=True, right_index=True)

### Add baseline information ###
df_bsl = df_bsl.drop(bsl_to_cy_to_drop, axis=1, inplace=False)
df_cy.reset_index(inplace=True)
df_cy = df_cy.merge(df_bsl, how='left', on=code_clmn)
df_cy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=True)

### Add ref uom and currency ###
df_cy.reset_index(inplace=True)
df_cy = df_cy.merge(df_uom_ref, how='left', on=code_clmn)
df_cy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=True)

### convert uom and currency to reference ###

# cy to ref (price, per, currency, volume, per)
cy_clmn_list_to_conv = [cy_price_clmn, cy_price_uom_clmn, cy_price_per_clmn, cy_currency_clmn, cy_volume_clmn,
                        cy_volume_uom_clmn, cy_volume_per_clmn]
cy_to_ref_mult_list = [cy_to_ref_mult_price_uom_clmn, cy_to_ref_mult_price_per_clmn, cy_to_ref_mult_currency_clmn,
                       cy_to_ref_mult_volume_uom_clmn, cy_to_ref_mult_volume_per_clmn]
cy_ref_clmn_list = [cy_price_at_ref_clmn, uom_ref_uom_price_clmn, uom_ref_per_price_clmn,
                    uom_ref_currency_clmn, cy_volume_at_ref_clmn, uom_ref_uom_volume_clmn, uom_ref_per_volume_clmn]

df_cy = fc.convert_uom(df_cy, df_conv, cy_clmn_list_to_conv, cy_ref_clmn_list, cy_to_ref_mult_list,
                       conv_multiplier_clmn, code_clmn, month_clmn,)

# bgt to ref
bgt_clmn_list_to_conv = [bgt_price_clmn, bgt_uom_clmn, bgt_per_clmn, bgt_currency_clmn, bgt_volume_clmn, bgt_uom_clmn,
                         bgt_per_clmn]
bgt_to_ref_mult_list = [bgt_to_ref_mult_price_uom_clmn, bgt_to_ref_mult_price_per_clmn, bgt_to_ref_mult_currency_clmn,
                        bgt_to_ref_mult_volume_uom_clmn, bgt_to_ref_mult_volume_per_clmn]
bgt_ref_clmn_list = [bgt_price_at_ref_clmn, uom_ref_uom_price_clmn, uom_ref_per_price_clmn,
                     uom_ref_currency_clmn, bgt_volume_at_ref_clmn, uom_ref_uom_volume_clmn, uom_ref_per_volume_clmn]

df_cy = fc.convert_uom(df_cy, df_conv, bgt_clmn_list_to_conv, bgt_ref_clmn_list, bgt_to_ref_mult_list,
                       conv_multiplier_clmn, code_clmn, month_clmn,)

# bsl to ref
bsl_clmn_list_to_conv = [bsl_price_clmn, bsl_price_uom_clmn, bsl_price_per_clmn, bsl_currency_clmn, 'empty', 'empty',
                         'empty']
bsl_to_ref_mult_list = [bsl_to_ref_mult_price_uom_clmn, bsl_to_ref_mult_price_per_clmn, bsl_to_ref_mult_currency_clmn,
                        'empty', 'empty']
bsl_ref_clmn_list = [bsl_price_at_ref_clmn, uom_ref_uom_price_clmn, uom_ref_per_price_clmn,
                     uom_ref_currency_clmn, 'empty', 'empty', 'empty']

df_cy = fc.convert_uom(df_cy, df_conv, bsl_clmn_list_to_conv, bsl_ref_clmn_list, bsl_to_ref_mult_list,
                       conv_multiplier_clmn, code_clmn, month_clmn)

# avg ly to ref
df_cy[ly_price_at_ref_clmn] = df_cy[bsl_price_ly] * df_cy[bsl_to_ref_mult_price_uom_clmn] * \
                              df_cy[bsl_to_ref_mult_price_per_clmn] * df_cy[bsl_to_ref_mult_currency_clmn]

### Spend and inflation calculations ###
# LY avg spend ly_spd => avg_price * bgt_vol

df_cy[ly_spend_avg_pr_bgt_vl_clmn] = df_cy[ly_price_at_ref_clmn] * df_cy[bgt_volume_at_ref_clmn]

# BSL spend bsl_spd => bsl_price * bgt_vol
df_cy[bsl_spend_bsl_pr_bgt_vl_clmn] = df_cy[bsl_price_at_ref_clmn] * df_cy[bgt_volume_at_ref_clmn]

# baseline inflation (USD) bsl_inf => bsl_spd - ly_spd
df_cy[bsl_inflation_clmn] = df_cy[bsl_spend_bsl_pr_bgt_vl_clmn] - df_cy[ly_spend_avg_pr_bgt_vl_clmn]

# budget spend bgt_spd => bgt_price * bgt_vol
df_cy[bgt_spend_bgt_pr_bgt_vl_clmn] = df_cy[bgt_price_at_ref_clmn] * df_cy[bgt_volume_at_ref_clmn]

# budget savings bsl_sav => bgt_spd - bsl_spd
df_cy[bgt_savings_clmn] = df_cy[bgt_spend_bgt_pr_bgt_vl_clmn] - df_cy[bsl_spend_bsl_pr_bgt_vl_clmn]

# current year spend at budget volume cy_bgt_spd => cy_price * bgt_vol
df_cy[bgt_spend_bgt_pr_cy_vl_clmn] = df_cy[bgt_price_at_ref_clmn] * df_cy[cy_volume_at_ref_clmn]

# volume adjustment vol_adj => adj_bgt_spd - bgt_spd
df_cy[volume_adjustment_clmn] = df_cy[bgt_spend_bgt_pr_cy_vl_clmn] - df_cy[bgt_spend_bgt_pr_bgt_vl_clmn]

# current year spend cy_spd => cy_price * cy_vol
df_cy[cy_spend_cy_pr_cy_vl_clmn] = df_cy[cy_price_at_ref_clmn] * df_cy[cy_volume_at_ref_clmn]

# current year savings vs bgt cy_sav => cy_spd - adj_bgt_spd
df_cy[cy_bgt_savings_clmn] = df_cy[bgt_spend_bgt_pr_cy_vl_clmn] - df_cy[cy_spend_cy_pr_cy_vl_clmn]

# total savings total_sav => bsl_sav + cy_sav
df_cy[bsl_spend_bsl_pr_cy_vl_clmn] = df_cy[bsl_price_at_ref_clmn] * df_cy[cy_volume_at_ref_clmn]
df_cy[cy_bsl_savings_clmn] = df_cy[bsl_spend_bsl_pr_cy_vl_clmn] - df_cy[cy_spend_cy_pr_cy_vl_clmn]

# volume influence bsl vol_inf_bsl => (bsl_price - cy_price) * (cy_volume - bsl_volume) 
df_cy[volume_influence_vs_bsl_clmn] = (df_cy[bsl_price_clmn] - df_cy[cy_volume_clmn]) * \
                                      (df_cy[cy_volume_clmn] - df_cy[bgt_volume_clmn])

# volume influence bgt vol_inf_bgt => (bgt_price - cy_price) * (cy_volume - bgt_volume)
df_cy[volume_influence_vs_bgt_clmn] = (df_cy[bgt_price_clmn] - df_cy[cy_volume_clmn]) * \
                                      (df_cy[cy_volume_clmn] - df_cy[bgt_volume_clmn])

### Filter NAN ###
[df_cy, error_msg_engine] = fc.clean_nan_engine(df_cy, code_clmn,  month_clmn, engine_error_str)

######################### Calculating Savings per PJ file #########################
### filter desired columns from df_cy ###
df_pj_clmn_list = [description_clmn, category_clmn, location_clmn, savings_type_clmn, cy_type_report_clmn,
                   savings_type_clmn, frc_strategy_column]

### convert uoms ###
df_pjmp.reset_index(inplace=True)
df_pjmp = df_pjmp.merge(df_uom_ref, how='left', on=code_clmn)
df_pjmp.set_index(keys=[code_clmn], drop=True, inplace=True)

pjmp_clmn_list_to_conv = [pjmp_cnst_clmn, pjmp_uom_clmn, pjmp_per_clmn, pjmp_currency_clmn, 'empty', 'empty', 'empty']
pjmp_ref_clmn_list = [pjmp_cnst_at_ref_clmn,  uom_ref_uom_price_clmn, uom_ref_per_price_clmn, uom_ref_currency_clmn,
                      'empty', 'empty', 'empty']
pjmp_to_ref_mult_list = [pjmp_to_ref_mult_uom_clmn, pjmp_to_ref_mult_per_clmn, pjmp_to_ref_mult_currency_clmn,
                         'empty', 'empty']
df_pjmp = fc.convert_uom(df_pjmp, df_conv, pjmp_clmn_list_to_conv, pjmp_ref_clmn_list, pjmp_to_ref_mult_list,
                         conv_multiplier_clmn, code_clmn)

### include projects as columns ###
pj_layer = fc.get_max_amount_of_code_repetitions(df_pjmp)

proj_str_description_lt = fc.generate_prj_clm_list(proj_str_description, pj_layer)
proj_str_value_lt = fc.generate_prj_clm_list(proj_str_value, pj_layer)
proj_str_code_lt = fc.generate_prj_clm_list(proj_str_code, pj_layer)

# create generate generic projects
df_cy = fc.generate_generic_project_info(df_cy, category_clmn, proj_str_code_gen, proj_str_description_gen,
                                         proj_str_value_gen, gen_pj_code_str, gen_pj_description_str, code_clmn, month_clmn)

# calculate project values
desired_calc_clmn_list = [pjmp_code_clmn, pjmp_description_clmn, pjmp_pcent_clmn, pjmp_cnst_at_ref_clmn,
                          pjmp_start_month_clmn]
desired_calc_clmn_list = [pjmp_code_clmn, pjmp_description_clmn, pjmp_pcent_clmn, pjmp_cnst_at_ref_clmn,
                          pjmp_start_month_clmn]
df_pjmp_short = df_pjmp[desired_calc_clmn_list]
pj_delete_clmn_list = [pjmp_pcent_clmn, pjmp_cnst_at_ref_clmn, pjmp_start_month_clmn]

df_cy = fc.add_projects(df_cy, df_pjmp_short, proj_str_description_lt, proj_str_value_lt, proj_str_code_lt,
                        code_clmn, month_clmn, pjmp_code_clmn, pjmp_description_clmn, pjmp_pcent_clmn,
                        pjmp_cnst_at_ref_clmn, pjmp_start_month_clmn, cy_bsl_savings_clmn, cy_volume_at_ref_clmn,
                        uom_ref_per_price_clmn, uom_ref_per_price_clmn, proj_str_value_gen, pj_layer,
                        pj_delete_clmn_list)

### calculate savings per project and include on df_pj ###
# pj_desired_list
pj_desired_clmn_list = [pjmp_code_clmn, pjmp_sav_assignment_type]
proj_str_description_lt = [proj_str_description_gen] + proj_str_description_lt
proj_str_value_lt = [proj_str_value_gen] + proj_str_value_lt
proj_str_code_lt = [proj_str_code_gen] + proj_str_code_lt

new_str_clmn_list = [proj_str_code, proj_str_description, proj_str_value]
df_pj = fc.create_project_dataframe(df_pjmp, df_cy, pj_desired_clmn_list, proj_str_description_lt, proj_str_value_lt,
                                    proj_str_code_lt, pjmp_code_clmn, proj_str_value, new_str_clmn_list,
                                    uom_ref_currency_clmn)

#sum savings versus baseline

### clean nan ###

### Reorder columns ###
# df_cy_clmn_list = [description_clmn, category_clmn, location_clmn, savings_type_clmn, cy_type_report_clmn,
#                    savings_type_clmn, frc_strategy_column,
#                    cy_price_clmn, cy_currency_clmn, cy_price_per_clmn, cy_price_uom_clmn, cy_volume_clmn,
#                    cy_volume_per_clmn, cy_volume_uom_clmn,
#                    bgt_price_clmn, bgt_currency_clmn, bgt_per_clmn, bgt_uom_clmn, bgt_volume_clmn, pred_code_clmn,
#                    bsl_price_ly, bsl_price_clmn, bsl_currency_clmn, bsl_price_per_clmn, bsl_price_uom_clmn,
#                    bsl_pred_code_clmn,
#                    uom_ref_per_price_clmn, uom_ref_uom_price_clmn, uom_ref_currency_clmn, uom_ref_per_volume_clmn,
#                    uom_ref_uom_volume_clmn,
#                    cy_to_ref_mult_price_uom_clmn, cy_to_ref_mult_price_per_clmn, cy_to_ref_mult_currency_clmn,
#                    cy_price_at_ref_clmn,
#                    cy_to_ref_mult_volume_uom_clmn, cy_to_ref_mult_volume_per_clmn, cy_volume_at_ref_clmn,
#                    bgt_to_ref_mult_price_uom_clmn, bgt_to_ref_mult_price_per_clmn, bgt_to_ref_mult_currency_clmn,
#                    bgt_price_at_ref_clmn,
#                    bgt_to_ref_mult_volume_uom_clmn, bgt_to_ref_mult_volume_per_clmn, bgt_volume_at_ref_clmn,
#                    bsl_to_ref_mult_price_uom_clmn, bsl_to_ref_mult_price_per_clmn, bsl_to_ref_mult_currency_clmn,
#                    bsl_price_at_ref_clmn, ly_price_at_ref_clmn,
#                    ly_spend_avg_pr_bgt_vl_clmn, bsl_spend_bsl_pr_bgt_vl_clmn, bsl_spend_bsl_pr_cy_vl_clmn,
#                    bgt_spend_bgt_pr_bgt_vl_clmn, bgt_spend_bgt_pr_cy_vl_clmn, cy_spend_cy_pr_cy_vl_clmn,
#                    volume_adjustment_clmn, bsl_inflation_clmn, bgt_savings_clmn, cy_bgt_savings_clmn,
#                    cy_bsl_savings_clmn, volume_influence_vs_bsl_clmn, volume_influence_vs_bgt_clmn]
# df_cy = df_cy[df_cy_clmn_list]

### save on CSV “Savings Report – FY YYYY period XX per PN”) ###
df_cy.to_csv(filename_cy_csv)
df_pj.to_csv(filename_pj_csv)

# format excel table

## error msg ##
error_file_engine = open(filename_error_msg_engine, "w")
error_file_engine.write(error_msg_engine)
error_file_engine.close()

# DOUBLE CHECK CALCULATIONS

#############################                    3) REPORT GENERATOR                       #############################

#############################                  4) WEB INTERFACE (input)                    #############################

#############################               5) INTERACTIVE INTERFACE (output)              #############################