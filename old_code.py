
# # import seaborn as sns
# # import matplotlib.pyplot as plt
# # import matplotlib.colors as clr
# # from matplotlib.ticker import AutoLocator
# # import plotly.graph_objects as go
# # import chart_studio.plotly as py
# # import plotly
# # import plotly.express as px
#
# # List of inputs (excel files):
# #   1) Budget - OK
# #   2) Actuals - OK
# #   3) Forecast - OK
# #         as budget price
# #         as avg actuals
# #         as a constant
# #         as an inflation rate
# #         as a curve
# #   4) Baseline - OK
# #   5) Predecessor - OK
# #   6) UoM and FX equalization - OK
# #   7) UoM and FX conversions - OK
# #   8) Project mapping -OK
#
# #############################                Input Variables                      ######################################
# report_month = 5
# Fiscal_Year = '2020'
# filename_error_msg = './outputs/CSV files/error msg {0}-{1}.txt'.format(Fiscal_Year, report_month)
#
# ########################    Data cleaning    ########################
# ### Budget ###
# filename_bgt = './inputs/PAF.xlsx'
# filename_bgt_csv = './outputs/CSV files/budget {}.csv'.format(Fiscal_Year)
#
# code_clmn = 'code'
# description_clmn = 'description'
# category_report_clmn = 'report_category'
# category_clmn = 'category'
# location_report_clmn = 'report_location'
# location_clmn = 'location'
# bgt_price_clmn = 'bgt_price'
# bgt_currency_report_clmn = 'report_bgt_currency'
# bgt_currency_clmn = 'bgt_currency'
# bgt_uom_report_clmn = 'report_bgt_uom'
# bgt_uom_clmn = 'bgt_uom'
# bgt_per_clmn = 'bgt_per'
# savings_type_report_clmn = 'report_savings_type'
# savings_type_clmn = 'savings_type'
# month_clmn = 'month'
# bgt_volume_clmn = 'bgt_volume'
# pred_code_clmn = 'bgt_predecessor'
#
# df_wide_bgt_raw_clmn_expect_lt = ['Part Number', 'Description', 'Category', 'Plant', 'PAF price', 'FX', 'Unity',
#                                   '1 or 1,000? ', 'PL or BS?', 'vol 01', 'vol 02', 'vol 03', 'vol 04', 'vol 05',
#                                   'vol 06', 'vol 07', 'vol 08', 'vol 09', 'vol 10', 'vol 11', 'vol 12']
#
# df_long_bgt_clmn_list = [description_clmn, category_clmn, location_clmn, savings_type_clmn, bgt_volume_clmn,
#                          bgt_price_clmn, bgt_per_clmn, bgt_uom_clmn, bgt_currency_clmn, pred_code_clmn]
#
# bgt_clmn_conversion = {df_wide_bgt_raw_clmn_expect_lt[0]: code_clmn,
#                        df_wide_bgt_raw_clmn_expect_lt[1]: description_clmn,
#                        df_wide_bgt_raw_clmn_expect_lt[2]: category_report_clmn,
#                        df_wide_bgt_raw_clmn_expect_lt[3]: location_report_clmn,
#                        df_wide_bgt_raw_clmn_expect_lt[4]: bgt_price_clmn,
#                        df_wide_bgt_raw_clmn_expect_lt[5]: bgt_currency_report_clmn,
#                        df_wide_bgt_raw_clmn_expect_lt[6]: bgt_uom_report_clmn,
#                        df_wide_bgt_raw_clmn_expect_lt[7]: bgt_per_clmn,
#                        df_wide_bgt_raw_clmn_expect_lt[8]: savings_type_report_clmn,
#                        df_wide_bgt_raw_clmn_expect_lt[9]: '1',
#                        df_wide_bgt_raw_clmn_expect_lt[10]: '2',
#                        df_wide_bgt_raw_clmn_expect_lt[11]: '3',
#                        df_wide_bgt_raw_clmn_expect_lt[12]: '4',
#                        df_wide_bgt_raw_clmn_expect_lt[13]: '5',
#                        df_wide_bgt_raw_clmn_expect_lt[14]: '6',
#                        df_wide_bgt_raw_clmn_expect_lt[15]: '7',
#                        df_wide_bgt_raw_clmn_expect_lt[16]: '8',
#                        df_wide_bgt_raw_clmn_expect_lt[17]: '9',
#                        df_wide_bgt_raw_clmn_expect_lt[18]: '10',
#                        df_wide_bgt_raw_clmn_expect_lt[19]: '11',
#                        df_wide_bgt_raw_clmn_expect_lt[20]: '12'}
#
# bgt_error_str = "\nBgt file:\n"
#
# ### actuals ###
# filename_act = './inputs/YTD.xlsx'
# filename_act_csv = './outputs/CSV files/actuals {0}-{1}.csv'.format(Fiscal_Year, report_month)
#
# act_price_clmn = 'act_price'
# act_currency_report_clmn = 'report_act_currency'
# act_currency_clmn = 'act_currency'
# act_price_uom_report_clmn = 'report_act_price_uom'
# act_price_uom_clmn = 'act_price_uom'
# act_volume_uom_report_clmn = 'report_act_volume_uom'
# act_volume_uom_clmn = 'act_volume_uom'
# act_price_per_clmn = 'act_price_per'
# act_volume_per_clmn = 'act_volume_per'
# act_volume_clmn = 'act_volume'
# act_code_and_month_clmn = 'act_code_and_month'
#
# df_wide_act_raw_clmn_expect_lt_base = ['Part Number', 'Description', 'Category', 'Plant', 'FX', 'Unity', '1 or 1,000? ']
# df_wide_act_raw_clmn_expect_lt = ['Part Number', 'Description', 'Category', 'Plant', 'FX', 'Unity', '1 or 1,000? ']
# # input has only 1 UoM, therefore we will have to adjust
#
# volume_act_base_string = "v"
# df_wide_act_raw_clmn_expect_lt = fc.generate_wide_clmn_expected_list(df_wide_act_raw_clmn_expect_lt,
#                                                                      1, report_month, volume_act_base_string)
# price_act_base_string = "P"
# df_wide_act_raw_clmn_expect_lt = fc.generate_wide_clmn_expected_list(df_wide_act_raw_clmn_expect_lt, 1, report_month,
#                                                                      price_act_base_string)
#
# df_long_act_clmn_list = [description_clmn, category_clmn, location_clmn, act_volume_clmn, act_volume_per_clmn,
#                          act_volume_uom_clmn,  act_price_clmn, act_price_per_clmn, act_price_uom_clmn,
#                          act_currency_clmn]
#
# act_volume_clmns_conversion_base = {df_wide_act_raw_clmn_expect_lt[0]: code_clmn,
#                                     df_wide_act_raw_clmn_expect_lt[1]: description_clmn,
#                                     df_wide_act_raw_clmn_expect_lt[2]: category_report_clmn,
#                                     df_wide_act_raw_clmn_expect_lt[3]: location_report_clmn,
#                                     df_wide_act_raw_clmn_expect_lt[4]: act_currency_report_clmn,
#                                     df_wide_act_raw_clmn_expect_lt[5]: act_volume_uom_report_clmn,
#                                     df_wide_act_raw_clmn_expect_lt[6]: act_volume_per_clmn}
#
# act_volume_clmn_conversion = fc.generate_wide_clmn_conversion(act_volume_clmns_conversion_base, 1, report_month,
#                                                               volume_act_base_string)
# act_price_clmns_conversion_base = {df_wide_act_raw_clmn_expect_lt[0]: code_clmn,
#                                    df_wide_act_raw_clmn_expect_lt[5]: act_price_uom_report_clmn,
#                                    df_wide_act_raw_clmn_expect_lt[6]: act_price_per_clmn}
#
# act_price_clmn_conversion = fc.generate_wide_clmn_conversion(act_price_clmns_conversion_base, 1, report_month,
#                                                              price_act_base_string)
#
# act_error_str = "\nAct file:\n"
#
# ### forecast ###
# filename_frc = './inputs/YTG.xlsx'
# filename_frc_csv = './outputs/CSV files/forecast {0}-{1}.csv'.format(Fiscal_Year, report_month)
#
# sheet_frc_vol = 'Volume'
# sheet_frc_as_bgt = 'Budget'
# sheet_frc_as_act = 'YTD'
# sheet_frc_as_cnst = 'Constant'
# sheet_frc_as_inf = 'Inflation rate'
# sheet_frc_as_crv = 'Price curve'
#
# frc_vol_uom_report_clmn = 'report_frc_volume_uom'
# frc_vol_uom_clmn = 'frc_volume_uom'
# frc_vol_per_clmn = 'frc_volume_per_uom'
# frc_vol_clmn = 'frc_volume'
# frc_price_clmn = 'frc_price'
# frc_price_uom_report_clmn = 'report_frc_price_uom'
# frc_price_uom_clmn = 'frc_price_uom'
# frc_price_per_clmn = 'frc_price_per'
# frc_currency_clmn = 'frc_currency'
# frc_currency_report_clmn = 'report_frc_currency'
#
# frc_price_as_inf_base_price_clmn = 'frc_as_inf_base_price'
# frc_price_as_inf_inflation_clmn = 'frc_as_inf_inflation'
# frc_price_as_inf_month_clmn = 'frc_as_inf_month'
#
# frc_strategy_column = 'frc_strategy'
# frc_strategy_as_bgt = 'Budget'
# frc_strategy_as_act = 'Avg actuals'
# frc_strategy_as_cnst = 'Constant'
# frc_strategy_as_inf = 'Inflation rate'
# frc_strategy_as_crv = 'Price curve'
#
# df_wide_frc_vol_raw_clmn_expect_lt_base = ['Part Number',	'Plant', 'Description',	'Unity', '1 or 1,000? ']
# volume_frc_vol_base_string = "v"
# df_wide_frc_vol_raw_clmn_expect_lt = fc.generate_wide_clmn_expected_list(df_wide_frc_vol_raw_clmn_expect_lt_base,
#                                                                          report_month+1, 12,
#                                                                          volume_frc_vol_base_string)
# df_wide_frc_as_bgt_raw_clmn_expect_lt = ['Part Number',	'Plant', 'Description']
# df_wide_frc_as_act_raw_clmn_expect_lt = ['Part Number',	'Plant', 'Description']
# df_wide_frc_as_cnst_raw_clmn_expect_lt = ['Part Number',	'Plant', 'Description', 'Price', 'Unity', '1 or 1,000? ',
#                                           'FX']
# df_wide_frc_as_inf_raw_clmn_expect_lt = ['Part Number',	'Plant', 'Description', 'Unity', '1 or 1,000? ', 'FX',
#                                          'Base price', 'Inflation', 'Inflation month']
# df_wide_frc_as_crv_raw_clmn_expect_lt_base = ['Part Number', 'Plant', 'Description', 'Unity', '1 or 1,000? ', 'FX']
# price_frc_base_string = "P"
# df_wide_frc_as_crv_raw_clmn_expect_lt = fc.generate_wide_clmn_expected_list(df_wide_frc_as_crv_raw_clmn_expect_lt_base,
#                                                                             report_month+1, 12,
#                                                                             price_frc_base_string)
#
# df_long_frc_clmn_list = [description_clmn, category_clmn, location_clmn, frc_vol_clmn, frc_vol_per_clmn,
#                          frc_vol_uom_clmn,  frc_price_clmn, frc_price_per_clmn, frc_price_uom_clmn, frc_currency_clmn,
#                          frc_strategy_column]
#
# frc_vol_clmn_conversion_base = {df_wide_frc_vol_raw_clmn_expect_lt[0]: code_clmn,
#                                 df_wide_frc_vol_raw_clmn_expect_lt[1]: location_report_clmn,
#                                 df_wide_frc_vol_raw_clmn_expect_lt[2]: description_clmn,
#                                 df_wide_frc_vol_raw_clmn_expect_lt[3]: frc_vol_uom_report_clmn,
#                                 df_wide_frc_vol_raw_clmn_expect_lt[4]: frc_vol_per_clmn}
#
# frc_vol_clmn_conversion = fc.generate_wide_clmn_conversion(frc_vol_clmn_conversion_base, report_month+1, 12,
#                                                            volume_frc_vol_base_string)
#
# frc_as_bgt_clmn_conversion = {df_wide_frc_as_bgt_raw_clmn_expect_lt[0]: code_clmn,
#                               df_wide_frc_as_bgt_raw_clmn_expect_lt[1]: location_report_clmn,
#                               df_wide_frc_as_bgt_raw_clmn_expect_lt[2]: description_clmn}
#
# frc_as_act_clmn_conversion = {df_wide_frc_as_act_raw_clmn_expect_lt[0]: code_clmn,
#                               df_wide_frc_as_act_raw_clmn_expect_lt[1]: location_report_clmn,
#                               df_wide_frc_as_act_raw_clmn_expect_lt[2]: description_clmn}
#
# frc_as_cnst_clmn_conversion = {df_wide_frc_as_cnst_raw_clmn_expect_lt[0]: code_clmn,
#                                df_wide_frc_as_cnst_raw_clmn_expect_lt[1]: location_report_clmn,
#                                df_wide_frc_as_cnst_raw_clmn_expect_lt[2]: description_clmn,
#                                df_wide_frc_as_cnst_raw_clmn_expect_lt[3]: frc_price_clmn,
#                                df_wide_frc_as_cnst_raw_clmn_expect_lt[4]: frc_price_uom_report_clmn,
#                                df_wide_frc_as_cnst_raw_clmn_expect_lt[5]: frc_price_per_clmn,
#                                df_wide_frc_as_cnst_raw_clmn_expect_lt[6]: frc_currency_report_clmn}
#
# frc_as_inf_clmn_conversion = {df_wide_frc_as_inf_raw_clmn_expect_lt[0]: code_clmn,
#                               df_wide_frc_as_inf_raw_clmn_expect_lt[1]: location_report_clmn,
#                               df_wide_frc_as_inf_raw_clmn_expect_lt[2]: description_clmn,
#                               df_wide_frc_as_inf_raw_clmn_expect_lt[3]: frc_price_uom_report_clmn,
#                               df_wide_frc_as_inf_raw_clmn_expect_lt[4]: frc_price_per_clmn,
#                               df_wide_frc_as_inf_raw_clmn_expect_lt[5]: frc_currency_report_clmn,
#                               df_wide_frc_as_inf_raw_clmn_expect_lt[6]: frc_price_as_inf_base_price_clmn,
#                               df_wide_frc_as_inf_raw_clmn_expect_lt[7]: frc_price_as_inf_inflation_clmn,
#                               df_wide_frc_as_inf_raw_clmn_expect_lt[8]: frc_price_as_inf_month_clmn}
#
# frc_as_crv_clmn_conversion_base = {df_wide_frc_as_crv_raw_clmn_expect_lt_base[0]: code_clmn,
#                                    df_wide_frc_as_crv_raw_clmn_expect_lt_base[1]: location_report_clmn,
#                                    df_wide_frc_as_crv_raw_clmn_expect_lt_base[2]: description_clmn,
#                                    df_wide_frc_as_crv_raw_clmn_expect_lt_base[3]: frc_price_uom_report_clmn,
#                                    df_wide_frc_as_crv_raw_clmn_expect_lt_base[4]: frc_price_per_clmn,
#                                    df_wide_frc_as_crv_raw_clmn_expect_lt_base[5]: frc_currency_report_clmn}
#
# frc_as_crv_clmn_conversion = fc.generate_wide_clmn_conversion(frc_as_crv_clmn_conversion_base, report_month+1, 12,
#                                                               price_frc_base_string)
#
# frc_error_str = "\nForecast file:\n"
#
# ### baseline ###
# filename_bsl = './inputs/Baseline.xlsx'
# filename_bsl_csv = './outputs/CSV files/baseline {0}.csv'.format(Fiscal_Year)
# df_bsl_raw_clmn_expect_lt = ['Part Number', 'Plant', 'Description', 'Baseline', 'Unity', '1 or 1,000? ', 'FX',
#                              'Last FY']
# bsl_error_str = "\nBaseline file:\n"
# bsl_price_clmn = 'bsl_price'
# bsl_price_ly = 'bsl_average_price_last_year'
# bsl_price_uom_report_clmn = 'report_bsl_price_uom'
# bsl_price_uom_clmn = 'bsl_price_uom'
# bsl_price_per_clmn = 'bsl_price_per'
# bsl_currency_report_clmn = 'report_bsl_currency'
# bsl_currency_clmn = 'bsl_currency'
# bsl_pred_code_clmn = 'bsl_predecessor'
#
# bsl_clmns_conversion = {df_bsl_raw_clmn_expect_lt[0]: code_clmn,
#                         df_bsl_raw_clmn_expect_lt[1]: location_report_clmn,
#                         df_bsl_raw_clmn_expect_lt[2]: description_clmn,
#                         df_bsl_raw_clmn_expect_lt[3]: bsl_price_clmn,
#                         df_bsl_raw_clmn_expect_lt[4]: bsl_price_uom_report_clmn,
#                         df_bsl_raw_clmn_expect_lt[5]: bsl_price_per_clmn,
#                         df_bsl_raw_clmn_expect_lt[6]: bsl_currency_report_clmn,
#                         df_bsl_raw_clmn_expect_lt[7]: bsl_price_ly}
#
# ### predecessor ###
# filename_pred = './inputs/yhold.xlsx'
# filename_pred_csv = './outputs/CSV files/predecessors {0}-{1}.csv'.format(Fiscal_Year, report_month)
# df_pred_raw_clmn_expect_lt = ['From', 'To']
# pred_error_str = "\nPredecessor file:\n"
# pred_clmns_conversion = {df_pred_raw_clmn_expect_lt[0]: pred_code_clmn,
#                          df_pred_raw_clmn_expect_lt[1]: code_clmn}
#
# ### project mapping ###
# filename_pjmp = './inputs/project mapping.xlsx'
# filename_pjmp_csv = './outputs/CSV files/project mapping {0}-{1}.csv'.format(Fiscal_Year, report_month)
#
# sheet_pjmp_pcent = '% based'
# sheet_pjmp_cnst = 'Value'
# sheet_pjmp_pj_list = 'project list'
#
# pjmp_code_clmn = 'project_code'
# pjmp_description_clmn = 'project_description'
# pjmp_pcent_clmn = 'project_percent_savings'
# pjmp_cnst_clmn = 'project_constant_savings'
# pjmp_report_uom_clmn = 'report_project_uom'
# pjmp_uom_clmn = 'project_uom'
# pjmp_per_clmn = 'project_per'
# pjmp_currency_report_clmn = 'report_project_currency'
# pjmp_currency_clmn = 'project_currency'
# pjmp_type_report_clmn = 'report_project_type'
# pjmp_type_clmn = 'project_type'
# pjmp_sav_assignment_type = 'savings_assignment_type'
# pjmp_pcent_str = 'percent'
# pjmp_cnst_str = 'constant'
# pjmp_start_month_clmn = 'project_start_month'
#
# df_pjmp_pcent_raw_clmn_expect_lt = ['Part Number', 'Plant',	'Description',	'project code',	'project name',	'%']
# df_pjmp_cnst_raw_clmn_expect_lt = ['Part Number', 'Plant',	'Description',	'Pj code',	'Pj Name',	'Value',	'Unity',
#                                    '1 or 1,000? ',	'FX']
# df_pjmp_pj_list_raw_clmn_expect_lt = ['Code',	'Name',	'Type', 'kick-off mth']
#
# df_pjmp_clmn_list = [code_clmn, description_clmn, location_clmn, pjmp_code_clmn, pjmp_description_clmn,
#                      pjmp_sav_assignment_type, pjmp_pcent_clmn, pjmp_cnst_clmn, pjmp_uom_clmn, pjmp_per_clmn,
#                      pjmp_currency_clmn]
#
# pjmp_pcent_clmns_conversion_base = {df_pjmp_pcent_raw_clmn_expect_lt[0]: code_clmn,
#                                     df_pjmp_pcent_raw_clmn_expect_lt[1]: location_report_clmn,
#                                     df_pjmp_pcent_raw_clmn_expect_lt[2]: description_clmn,
#                                     df_pjmp_pcent_raw_clmn_expect_lt[3]: pjmp_code_clmn,
#                                     df_pjmp_pcent_raw_clmn_expect_lt[4]: pjmp_description_clmn,
#                                     df_pjmp_pcent_raw_clmn_expect_lt[5]: pjmp_pcent_clmn}
#
# pjmp_cnst_clmns_conversion_base = {df_pjmp_cnst_raw_clmn_expect_lt[0]: code_clmn,
#                                    df_pjmp_cnst_raw_clmn_expect_lt[1]: location_report_clmn,
#                                    df_pjmp_cnst_raw_clmn_expect_lt[2]: description_clmn,
#                                    df_pjmp_cnst_raw_clmn_expect_lt[3]: pjmp_code_clmn,
#                                    df_pjmp_cnst_raw_clmn_expect_lt[4]: pjmp_description_clmn,
#                                    df_pjmp_cnst_raw_clmn_expect_lt[5]: pjmp_cnst_clmn,
#                                    df_pjmp_cnst_raw_clmn_expect_lt[6]: pjmp_report_uom_clmn,
#                                    df_pjmp_cnst_raw_clmn_expect_lt[7]: pjmp_per_clmn,
#                                    df_pjmp_cnst_raw_clmn_expect_lt[8]: pjmp_currency_report_clmn}
#
# pjmp_pj_list_clmns_conversion_base = {df_pjmp_pj_list_raw_clmn_expect_lt[0]: pjmp_code_clmn,
#                                       df_pjmp_pj_list_raw_clmn_expect_lt[1]: pjmp_description_clmn,
#                                       df_pjmp_pj_list_raw_clmn_expect_lt[2]: pjmp_type_report_clmn,
#                                       df_pjmp_pj_list_raw_clmn_expect_lt[3]: pjmp_start_month_clmn}
#
# pjmp_pcent_error_str = "\n Pj Mapping file (percent):\n"
# pjmp_cnst_error_str = "\n Pj Mapping file (constant):\n"
# pjmp_pj_list_error_str = "\n Pj Mapping file (project list):\n"
#
# ### Uom and currency equalization ###
# filename_category_eq = './inputs/category equalization.xlsx'
# filename_location_eq = './inputs/plant equalization.xlsx'
# filename_currency_eq = './inputs/FX equalization.xlsx'
# filename_uom_eq = './inputs/unity equalization.xlsx'
# filename_savings_type_eq = './inputs/sav type equalization.xlsx'
# filename_project_type_eq = './inputs/proj type equalization.xlsx'
#
# filename_category_eq_csv = './outputs/CSV files/category equalization.csv'
# filename_location_eq_csv = './outputs/CSV files/location equalization.csv'
# filename_currency_eq_csv = './outputs/CSV files/currency equalization.csv'
# filename_uom_eq_csv = './outputs/CSV files/uom equalization.csv'
# filename_savings_type_eq_csv = './outputs/CSV files/savings type equalization.csv'
# filename_project_type_eq_csv = './outputs/CSV files/project type equalization.csv'
#
# df_category_eq_raw_clmn_expect_lt = ['Report category', 'Standard category']
# df_location_eq_raw_clmn_expect_lt = ['Report plant', 'Standard plant']
# df_uom_eq_raw_clmn_expect_lt = ['Report UoM',	'Standard UoM']
# df_currency_eq_raw_clmn_expect_lt = ['Report FX', 'Standard FX']
# df_savings_type_eq_raw_clmn_expect_lt = ['Report type', 'Standard type']
# df_project_type_eq_raw_clmn_expect_lt = ['Report pj type',	'Standard pj type']
#
# category_equalizer_clmns_conversion = {df_category_eq_raw_clmn_expect_lt[0]: category_report_clmn,
#                                        df_category_eq_raw_clmn_expect_lt[1]: category_clmn}
# location_equalizer_clmns_conversion = {df_location_eq_raw_clmn_expect_lt[0]: location_report_clmn,
#                                        df_location_eq_raw_clmn_expect_lt[1]: location_clmn}
# uom_equalizer_clmns_conversion = {df_uom_eq_raw_clmn_expect_lt[0]: bgt_uom_report_clmn,
#                                   df_uom_eq_raw_clmn_expect_lt[1]: bgt_uom_clmn}
# currency_equalizer_clmns_conversion = {df_currency_eq_raw_clmn_expect_lt[0]: bgt_currency_report_clmn,
#                                        df_currency_eq_raw_clmn_expect_lt[1]: bgt_currency_clmn}
# savings_type_equalizer_clmns_conversion = {df_savings_type_eq_raw_clmn_expect_lt[0]: savings_type_report_clmn,
#                                            df_savings_type_eq_raw_clmn_expect_lt[1]: savings_type_clmn}
# project_type_equalizer_clmns_conversion = {df_project_type_eq_raw_clmn_expect_lt[0]: pjmp_type_report_clmn,
#                                            df_project_type_eq_raw_clmn_expect_lt[1]: pjmp_type_clmn}
#
# category_eq_error_str = "\nCat eq file:\n"
# location_eq_error_str = "\nLoc eq file:\n"
# currency_eq_error_str = "\nCur eq file:\n"
# uom_eq_error_str = "\nUom eq file:\n"
# savings_type_eq_error_str = "\nSv tp eq file:\n"
# project_type_eq_error_str = "\nPj tp eq file:\n"
#
# ### uom and currency conversion ###
# filename_conv = './inputs/Conversion table.xlsx'
# filename_conv_csv = './outputs/CSV files/conversion_table.csv'
# filename_ref_uom_csv = './outputs/CSV files/reference_uom_currency.csv'
#
# reference_currency = 'USD'
# conv_old_uom_clmn = "Old UoM"
# conv_new_uom_clmn = "New UoM"
# conv_multiplier_clmn = "Multiplier"
#
# df_conv_raw_clmn_expect_lt = ['PN', 'From',	'To', 'Multiplier']
#
# conv_clmns_conversion_base = {df_conv_raw_clmn_expect_lt[0]: code_clmn,
#                               df_conv_raw_clmn_expect_lt[1]: conv_old_uom_clmn,
#                               df_conv_raw_clmn_expect_lt[2]: conv_new_uom_clmn,
#                               df_conv_raw_clmn_expect_lt[3]: conv_multiplier_clmn}
#
# ref_uom_clmn = 'Reference UoM'
# ref_currency_clmn = 'Reference Currency'
#
# conv_error_str = "\nConv file:\n"
#
# ### uom and currency reference ###
# uom_ref_per_price_clmn = 'Ref_per_price'
# uom_ref_uom_price_clmn = 'Ref_uom_price'
# uom_ref_currency_clmn = 'Ref_currency'
# uom_ref_per_volume_clmn = 'Ref_per_volume'
# uom_ref_uom_volume_clmn = 'Ref_uom_volume'
#
# filename_uom_ref_csv = './outputs/CSV files/uom reference.csv'
#
# ########################    Calculation Engine    ########################
# cy_volume_clmn = 'current_year_volume'
# cy_volume_per_clmn = 'current_year_volume_per'
# cy_volume_uom_clmn = 'current_year_volume_uom'
# cy_price_clmn = 'current_year_price'
# cy_price_per_clmn = 'current_year_price_per'
# cy_price_uom_clmn = 'current_year_price_uom'
# cy_currency_clmn = 'current_year_currency'
# cy_type_report_clmn = 'type_report'
# cy_act_report = 'Actuals'
# cy_frc_report = 'Forecast'
#
# cy_price_at_ref_clmn = 'current_price_at_ref'
# cy_volume_at_ref_clmn = 'current_volume_at_ref'
#
# cy_to_ref_mult_price_uom_clmn = 'cy_to_ref_multiplier_uom_price'
# cy_to_ref_mult_price_per_clmn = 'cy_to_ref_multiplier_per_price'
# cy_to_ref_mult_currency_clmn = 'cy_to_ref_multiplier_currency'
# cy_to_ref_mult_volume_uom_clmn = 'cy_to_ref_multiplier_uom_volume'
# cy_to_ref_mult_volume_per_clmn = 'cy_to_ref_multiplier_per_volume'
#
# bgt_price_at_ref_clmn = 'budget_price_at_ref'
# bgt_volume_at_ref_clmn = 'budget_volume_at_ref'
#
# bgt_to_ref_mult_price_uom_clmn = 'bgt_to_ref_multiplier_uom_price'
# bgt_to_ref_mult_price_per_clmn = 'bgt_to_ref_multiplier_per_price'
# bgt_to_ref_mult_currency_clmn = 'bgt_to_ref_multiplier_currency'
# bgt_to_ref_mult_volume_uom_clmn = 'bgt_to_ref_multiplier_uom_volume'
# bgt_to_ref_mult_volume_per_clmn = 'bgt_to_ref_multiplier_per_volume'
#
# bsl_price_at_ref_clmn = 'baseline_price_at_ref'
#
# bsl_to_ref_mult_price_uom_clmn = 'bsl_to_ref_multiplier_uom_price'
# bsl_to_ref_mult_price_per_clmn = 'bsl_to_ref_multiplier_per_price'
# bsl_to_ref_mult_currency_clmn = 'bsl_to_ref_multiplier_currency'
#
# ly_price_at_ref_clmn = 'ly_avg_price_at_ref'
#
# ly_spend_avg_pr_bgt_vl_clmn = 'ly_spd_at_ly_avg_price_bgt_volume'
# bsl_spend_bsl_pr_bgt_vl_clmn = 'bsl_spd_at_bsl_price_bgt_volume'
# bsl_inflation_clmn = 'baseline_inflation'
# bgt_spend_bgt_pr_bgt_vl_clmn = 'bgt_spd_at_bgt_price_bgt_volume'
# bgt_savings_clmn = 'budget_savings'
# bgt_spend_bgt_pr_cy_vl_clmn = 'bgt_spd_at_bgt_price_cy_volume'
# volume_adjustment_clmn = 'bgt_spend_adjustment_due_to_volume'
# cy_spend_cy_pr_cy_vl_clmn = 'cy_spd_at_cy_price_cy_volume'
# cy_bgt_savings_clmn = 'savings_vs_budget'
# bsl_spend_bsl_pr_cy_vl_clmn = 'bsl_spd_at_bsl_price_cy_volume'
# cy_bsl_savings_clmn = 'savings_vs_baseline'
# volume_influence_vs_bsl_clmn = 'volume_influence_vs_baseline'
# volume_influence_vs_bgt_clmn = 'volume_influence_vs_budget'
#
# engine_error_str = 'ENGINE ERROR: '
#
# filename_cy_csv = './outputs/CSV files/Savings Report – FY{0} P{1} per PN.csv'.format(Fiscal_Year, report_month)
# filename_pj_csv = './outputs/CSV files/Projects Report – FY{0} P{1} per PN.csv'.format(Fiscal_Year, report_month)
# filename_error_msg_engine = './outputs/CSV files/error msg Sv Rpt – FY{0} P{1} per PN.txt'.format(Fiscal_Year, report_month)
#
# filename_cy_pj_xlsx = './outputs/Savings Report – FY{0} P{1} per PN.xlsx'.format(Fiscal_Year, report_month)
# sheetname_cy = 'Part-number Report'
# sheetname_pj = 'Project Report'
#
# pjmp_cnst_at_ref_clmn = 'constant_at_ref'
# pjmp_to_ref_mult_uom_clmn = 'pjmp_to_ref_multiplier_uom'
# pjmp_to_ref_mult_per_clmn = 'pjmp_to_ref_multiplier_per'
# pjmp_to_ref_mult_currency_clmn = 'pjmp_to_ref_multiplier_currency'
#
# proj_str_description = 'project_name_'
# proj_str_value = 'project_value_vs_bsl_'
# proj_str_code = 'project_code_'
#
# proj_str_description_gen = 'project_description_0'
# proj_str_value_gen = 'project_value_vs_bsl_0'
# proj_str_code_gen = 'project_code_0'
#
# gen_pj_code_str = 'GP-'
# gen_pj_description_str = '-Negotiations'
#
# color_list = ['fef5a8', 'c5f19a', 'b9d0e8', 'd6bfd4', 'f79494']
# cy_color_index_for_clmns = [9, 16, 22, 28, 33, 36, 37, 39, 40, 43, 44, 46, 47, 50, 51, 52, 58, 65, 68, 71, 74, 77, 80,
#                             83]
# cy_color_order = [0, 1, 2, 0, 1, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 4, 1, 2, 0, 1, 2, 0, 1, 2]
# pj_color_index_for_clmns = [1, 2, 3, 4]
# pj_color_order = [0, 1, 2, 3, 4]
#
# #############################                1) DATA CLEANING                     ######################################
# ########################    Load excel files    ########################
# ### budget ###
# df_wide_bgt = pd.read_excel(filename_bgt)
#
# ### actuals ###
# df_wide_act = pd.read_excel(filename_act)
#
# ### forecast ###
# df_wide_frc_vol = pd.read_excel(filename_frc, sheet_name=sheet_frc_vol)
# df_wide_frc_as_bgt = pd.read_excel(filename_frc, sheet_name=sheet_frc_as_bgt)
# df_wide_frc_as_act = pd.read_excel(filename_frc, sheet_name=sheet_frc_as_act)
# df_wide_frc_as_cnst = pd.read_excel(filename_frc, sheet_name=sheet_frc_as_cnst)
# df_wide_frc_as_inf = pd.read_excel(filename_frc, sheet_name=sheet_frc_as_inf)
# df_wide_frc_as_crv = pd.read_excel(filename_frc, sheet_name=sheet_frc_as_crv)
#
# ## baseline ##
# df_bsl = pd.read_excel(filename_bsl)
#
# ## predecessor ##
# df_pred = pd.read_excel(filename_pred)
#
# ### equalization files ###
# df_category_equalizer = pd.read_excel(filename_category_eq)
# df_location_equalizer = pd.read_excel(filename_location_eq)
# df_currency_equalizer = pd.read_excel(filename_currency_eq)
# df_uom_equalizer = pd.read_excel(filename_uom_eq)
# df_savings_type_equalizer = pd.read_excel(filename_savings_type_eq)
# df_project_type_equalizer = pd.read_excel(filename_project_type_eq)
#
# ### conversion ###
# df_conv = pd.read_excel(filename_conv)
#
# ### project mapping ###
# df_pjmp_pcent = pd.read_excel(filename_pjmp, sheet_name=sheet_pjmp_pcent)
# df_pjmp_cnst = pd.read_excel(filename_pjmp, sheet_name=sheet_pjmp_cnst)
# df_pjmp_pj_list = pd.read_excel(filename_pjmp, sheet_name=sheet_pjmp_pj_list)
#
# ######################## Check column integrity ########################
# ### budget ###
# [clmns_to_delete_bgt, error_msg] = fc.file_clmn_integrity(df_wide_bgt, df_wide_bgt_raw_clmn_expect_lt, bgt_error_str)
#
# ### actuals ###
# [clmns_to_delete_act, error_msg] = fc.file_clmn_integrity(df_wide_act, df_wide_act_raw_clmn_expect_lt, act_error_str,
#                                                           error_msg)
#
# ### forecast ###
# [clmns_to_delete_frc_vol, error_msg] = fc.file_clmn_integrity(df_wide_frc_vol, df_wide_frc_vol_raw_clmn_expect_lt,
#                                                               frc_error_str, error_msg)
# [clmns_to_delete_frc_as_bgt, error_msg] = fc.file_clmn_integrity(df_wide_frc_as_bgt,
#                                                                  df_wide_frc_as_bgt_raw_clmn_expect_lt, frc_error_str,
#                                                                  error_msg)
# [clmns_to_delete_frc_as_act, error_msg] = fc.file_clmn_integrity(df_wide_frc_as_act,
#                                                                  df_wide_frc_as_act_raw_clmn_expect_lt, frc_error_str,
#                                                                  error_msg)
# [clmns_to_delete_frc_as_cnst, error_msg] = fc.file_clmn_integrity(df_wide_frc_as_cnst,
#                                                                   df_wide_frc_as_cnst_raw_clmn_expect_lt, frc_error_str,
#                                                                   error_msg)
# [clmns_to_delete_frc_as_inf, error_msg] = fc.file_clmn_integrity(df_wide_frc_as_inf,
#                                                                  df_wide_frc_as_inf_raw_clmn_expect_lt, frc_error_str,
#                                                                  error_msg)
# [clmns_to_delete_frc_as_crv, error_msg] = fc.file_clmn_integrity(df_wide_frc_as_crv,
#                                                                  df_wide_frc_as_crv_raw_clmn_expect_lt, frc_error_str,
#                                                                  error_msg)
#
# ######################## Drop extra columns ########################
# ### budget ###
# df_wide_bgt = df_wide_bgt.filter(items=df_wide_bgt_raw_clmn_expect_lt, axis=1)
#
# ### actuals ###
# df_wide_act = df_wide_act.filter(items=df_wide_act_raw_clmn_expect_lt, axis=1)
#
# ### forecast ###
# df_wide_frc_vol = df_wide_frc_vol.filter(items=df_wide_frc_vol_raw_clmn_expect_lt, axis=1)
# df_wide_frc_as_bgt = df_wide_frc_as_bgt.filter(items=df_wide_frc_as_bgt_raw_clmn_expect_lt, axis=1)
# df_wide_frc_as_act = df_wide_frc_as_act.filter(items=df_wide_frc_as_act_raw_clmn_expect_lt, axis=1)
# df_wide_frc_as_cnst = df_wide_frc_as_cnst.filter(items=df_wide_frc_as_cnst_raw_clmn_expect_lt, axis=1)
# df_wide_frc_as_inf = df_wide_frc_as_inf.filter(items=df_wide_frc_as_inf_raw_clmn_expect_lt, axis=1)
# df_wide_frc_as_crv = df_wide_frc_as_crv.filter(items=df_wide_frc_as_crv_raw_clmn_expect_lt, axis=1)
#
# ## baseline ##
# df_bsl = df_bsl.filter(items=df_bsl_raw_clmn_expect_lt, axis=1)
#
# ## predecessor ##
# df_pred = df_pred.filter(items=df_pred_raw_clmn_expect_lt, axis=1)
#
# ### equalization ###
# df_category_equalizer = df_category_equalizer.filter(items=df_category_eq_raw_clmn_expect_lt, axis=1)
# df_location_equalizer = df_location_equalizer.filter(items=df_location_eq_raw_clmn_expect_lt, axis=1)
# df_currency_equalizer = df_currency_equalizer.filter(items=df_currency_eq_raw_clmn_expect_lt, axis=1)
# df_uom_equalizer = df_uom_equalizer.filter(items=df_uom_eq_raw_clmn_expect_lt, axis=1)
# df_savings_type_equalizer = df_savings_type_equalizer.filter(items=df_savings_type_eq_raw_clmn_expect_lt, axis=1)
# df_project_type_equalizer = df_project_type_equalizer.filter(items=df_project_type_eq_raw_clmn_expect_lt, axis=1)
#
# ### conversion ###
# df_conv = df_conv.filter(items=df_conv_raw_clmn_expect_lt, axis=1)
#
# ### project mapping ###
# df_pjmp_pcent = df_pjmp_pcent.filter(items=df_pjmp_pcent_raw_clmn_expect_lt, axis=1)
# df_pjmp_cnst = df_pjmp_cnst.filter(items=df_pjmp_cnst_raw_clmn_expect_lt, axis=1)
# df_pjmp_pj_list = df_pjmp_pj_list.filter(items=df_pjmp_pj_list_raw_clmn_expect_lt, axis=1)
#
# ######################## Drop extra rows ########################
# ### budget ###
# [df_wide_bgt, error_msg] = fc.clear_extra_rows(df_wide_bgt, df_wide_bgt_raw_clmn_expect_lt[0], bgt_error_str,
#                                                error_msg)
# ### actuals ###
#
# [df_wide_act, error_msg] = fc.clear_extra_rows(df_wide_act, df_wide_act_raw_clmn_expect_lt[0], act_error_str,
#                                                error_msg, df_wide_act_raw_clmn_expect_lt_base)
# ### forecast ###
# # forecast files will be fully generated from scratch, therefore, there is not need to clean extra rows.
#
# ## baseline ##
# [df_bsl, error_msg] = fc.clear_extra_rows(df_bsl, df_bsl_raw_clmn_expect_lt[0], bsl_error_str, error_msg)
#
# ## predecessor ##
# [df_pred, error_msg] = fc.clear_extra_rows(df_pred, df_pred_raw_clmn_expect_lt[0], pred_error_str, error_msg)
#
# ### equalization ###
# [df_category_equalizer, error_msg] = fc.clear_extra_rows(df_category_equalizer,
#                                                          df_category_eq_raw_clmn_expect_lt[0],
#                                                          category_eq_error_str, error_msg)
# [df_location_equalizer, error_msg] = fc.clear_extra_rows(df_location_equalizer,
#                                                          df_location_eq_raw_clmn_expect_lt[0],
#                                                          location_eq_error_str, error_msg)
# [df_currency_equalizer, error_msg] = fc.clear_extra_rows(df_currency_equalizer,
#                                                          df_currency_eq_raw_clmn_expect_lt[0],
#                                                          currency_eq_error_str, error_msg)
# [df_uom_equalizer, error_msg] = fc.clear_extra_rows(df_uom_equalizer,
#                                                     df_uom_eq_raw_clmn_expect_lt[0],
#                                                     uom_eq_error_str, error_msg)
# [df_savings_type_equalizer, error_msg] = fc.clear_extra_rows(df_savings_type_equalizer,
#                                                              df_savings_type_eq_raw_clmn_expect_lt[0],
#                                                              savings_type_eq_error_str, error_msg)
# [df_project_type_equalizer, error_msg] = fc.clear_extra_rows(df_project_type_equalizer,
#                                                              df_project_type_eq_raw_clmn_expect_lt[0],
#                                                              project_type_eq_error_str, error_msg)
#
# ### conversion ###
#
# [df_conv, error_msg] = fc.clear_extra_rows(df_conv, df_conv_raw_clmn_expect_lt[0], conv_error_str, error_msg,
#                                            df_conv_raw_clmn_expect_lt)
#
# ### project mapping ###
# [df_pjmp_pcent, error_msg] = fc.clear_extra_rows(df_pjmp_pcent, df_pjmp_pcent_raw_clmn_expect_lt[0],
#                                                  pjmp_pcent_error_str, error_msg)
# [df_pjmp_cnst, error_msg] = fc.clear_extra_rows(df_pjmp_cnst, df_pjmp_cnst_raw_clmn_expect_lt[0],
#                                                 pjmp_cnst_error_str, error_msg)
# [df_pjmp_pj_list, error_msg] = fc.clear_extra_rows(df_pjmp_pj_list, df_pjmp_pj_list_raw_clmn_expect_lt[0],
#                                                    pjmp_pj_list_error_str, error_msg)
#
# ######################## Change column names ########################
# ### budget ###
# df_wide_bgt.rename(columns=bgt_clmn_conversion, inplace=True)
#
# ### actuals ###
# # Breaking dataframe in two before changing names before changing format
# df_act_clmn_list = df_wide_act_raw_clmn_expect_lt
# desired_clmn_vol_act = len(df_act_clmn_list)-report_month
# df_wide_volume_act = df_wide_act.filter(items=df_act_clmn_list[0:desired_clmn_vol_act], axis=1)
#
# desired_clmn_pr_act_list = df_wide_act_raw_clmn_expect_lt[desired_clmn_vol_act:len(df_act_clmn_list)]
# desired_clmn_pr_act_list.append(df_act_clmn_list[0])
# desired_clmn_pr_act_list.append(df_act_clmn_list[5])
# desired_clmn_pr_act_list.append(df_act_clmn_list[6])
# df_wide_price_act = df_wide_act.filter(items=desired_clmn_pr_act_list, axis=1)
#
# df_wide_volume_act.rename(columns=act_volume_clmn_conversion, inplace=True)
# df_wide_price_act.rename(columns=act_price_clmn_conversion, inplace=True)
#
# ### forecast ###
# df_wide_frc_vol.rename(columns=frc_vol_clmn_conversion, inplace=True)
# df_wide_frc_as_bgt.rename(columns=frc_as_bgt_clmn_conversion, inplace=True)
# df_wide_frc_as_act.rename(columns=frc_as_act_clmn_conversion, inplace=True)
# df_wide_frc_as_cnst.rename(columns=frc_as_cnst_clmn_conversion, inplace=True)
# df_wide_frc_as_inf.rename(columns=frc_as_inf_clmn_conversion, inplace=True)
# df_wide_frc_as_crv.rename(columns=frc_as_crv_clmn_conversion, inplace=True)
#
# ## baseline ##
# df_bsl.rename(columns=bsl_clmns_conversion, inplace=True) # filter non-desired columns
# # df_bsl.set_index(keys=code_clmn, drop=False, inplace=True)
#
# ## predecessor ##
# df_pred.rename(columns=pred_clmns_conversion, inplace=True) # filter non-desired columns
# # df_pred.set_index(keys=code_clmn, drop=False, inplace=True)
#
# ### equalization ###
# df_category_equalizer.rename(columns=category_equalizer_clmns_conversion, inplace=True) # filter non-desired columns
# df_category_equalizer = df_category_equalizer.filter(items=[category_report_clmn, category_clmn], axis=1)
#
# df_location_equalizer.rename(columns=location_equalizer_clmns_conversion, inplace=True)
# df_location_equalizer = df_location_equalizer.filter(items=[location_report_clmn, location_clmn], axis=1)
#
# df_currency_equalizer.rename(columns=currency_equalizer_clmns_conversion, inplace=True)
# df_currency_equalizer = df_currency_equalizer.filter(items=[bgt_currency_report_clmn, bgt_currency_clmn], axis=1)
#
# df_uom_equalizer.rename(columns=uom_equalizer_clmns_conversion, inplace=True)
# df_uom_equalizer = df_uom_equalizer.filter(items=[bgt_uom_report_clmn, bgt_uom_clmn], axis=1)
#
# df_savings_type_equalizer.rename(columns=savings_type_equalizer_clmns_conversion, inplace=True)
# df_savings_type_equalizer = df_savings_type_equalizer.filter(items=[savings_type_report_clmn,
#                                                                     savings_type_clmn], axis=1)
#
# df_project_type_equalizer.rename(columns=project_type_equalizer_clmns_conversion, inplace=True)
# df_project_type_equalizer = df_project_type_equalizer.filter(items=[pjmp_type_report_clmn, pjmp_type_clmn], axis=1)
#
# ### conversion ###
# df_conv.rename(columns=conv_clmns_conversion_base, inplace=True)
#
# ### project mapping ###
# df_pjmp_pcent.rename(columns=pjmp_pcent_clmns_conversion_base, inplace=True)
# df_pjmp_cnst.rename(columns=pjmp_cnst_clmns_conversion_base, inplace=True)
# df_pjmp_pj_list.rename(columns=pjmp_pj_list_clmns_conversion_base, inplace=True)
#
# ######################## Remove key duplicates ########################
# ### budget ###
# df_wide_bgt = fc.remove_key_duplicates(df_wide_bgt, code_clmn)
#
# ### actuals ###
# df_wide_volume_act = fc.remove_key_duplicates(df_wide_volume_act, code_clmn)
# df_wide_price_act = fc.remove_key_duplicates(df_wide_price_act, code_clmn)
#
# ### forecast ###
# df_wide_frc_vol = fc.remove_key_duplicates(df_wide_frc_vol, code_clmn)
# df_wide_frc_as_bgt = fc.remove_key_duplicates(df_wide_frc_as_bgt, code_clmn)
# df_wide_frc_as_act = fc.remove_key_duplicates(df_wide_frc_as_act, code_clmn)
# df_wide_frc_as_cnst = fc.remove_key_duplicates(df_wide_frc_as_cnst, code_clmn)
# df_wide_frc_as_inf = fc.remove_key_duplicates(df_wide_frc_as_inf, code_clmn)
# df_wide_frc_as_crv = fc.remove_key_duplicates(df_wide_frc_as_crv, code_clmn)
#
# ## baseline ##
# df_bsl = fc.remove_key_duplicates(df_bsl, code_clmn) #indexed
#
# ## predecessor ##
# df_pred = fc.remove_key_duplicates(df_pred, pred_code_clmn) #indexed
#
# ### equalization ###
# df_category_equalizer = fc.remove_key_duplicates(df_category_equalizer, category_report_clmn)
# df_location_equalizer = fc.remove_key_duplicates(df_location_equalizer, location_report_clmn)
# df_currency_equalizer = fc.remove_key_duplicates(df_currency_equalizer, bgt_currency_report_clmn)
# df_uom_equalizer = fc.remove_key_duplicates(df_uom_equalizer, bgt_uom_report_clmn)
# df_savings_type_equalizer = fc.remove_key_duplicates(df_savings_type_equalizer, savings_type_report_clmn)
# df_project_type_equalizer = fc.remove_key_duplicates(df_project_type_equalizer, pjmp_type_report_clmn)
#
# ### conversion ###
#
# ### project mapping ###
# df_pjmp_pj_list = fc.remove_key_duplicates(df_pjmp_pj_list, pjmp_code_clmn)
#
# ######################## Terminology equalization ########################
# ### budget ###
# # filter NaN inside of merge and drop
#
# [df_wide_bgt, error_msg] = fc.merge_and_drop(df_wide_bgt, df_category_equalizer, category_report_clmn,
#                                               category_report_clmn, category_clmn, code_clmn, bgt_error_str,
#                                               error_msg)
# [df_wide_bgt, error_msg] = fc.merge_and_drop(df_wide_bgt, df_location_equalizer, location_report_clmn,
#                                               location_report_clmn, location_clmn, code_clmn, bgt_error_str,
#                                               error_msg)
# [df_wide_bgt, error_msg] = fc.merge_and_drop(df_wide_bgt, df_currency_equalizer, bgt_currency_report_clmn,
#                                               bgt_currency_report_clmn, bgt_currency_clmn, code_clmn,
#                                               bgt_error_str, error_msg)
# [df_wide_bgt, error_msg] = fc.merge_and_drop(df_wide_bgt, df_uom_equalizer, bgt_uom_report_clmn,
#                                               bgt_uom_report_clmn, bgt_uom_clmn, code_clmn, bgt_error_str,
#                                               error_msg)
# [df_wide_bgt, error_msg] = fc.merge_and_drop(df_wide_bgt, df_savings_type_equalizer, savings_type_report_clmn,
#                                               savings_type_report_clmn, savings_type_clmn, code_clmn,
#                                               bgt_error_str, error_msg)
#
# ### actuals ###
#
# df_wide_act_volume_clmn_expect_lt_base = [code_clmn, description_clmn, category_clmn, location_report_clmn,
#                                           act_currency_report_clmn, act_volume_uom_report_clmn, act_volume_per_clmn]
# [df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_category_equalizer, category_report_clmn,
#                                                     category_report_clmn, category_clmn, code_clmn,
#                                                     act_error_str, error_msg, df_wide_act_volume_clmn_expect_lt_base)
#
# df_wide_act_volume_clmn_expect_lt_base = [code_clmn, description_clmn, category_clmn, location_clmn,
#                                           act_currency_report_clmn, act_volume_uom_report_clmn, act_volume_per_clmn]
# [df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_location_equalizer, location_report_clmn,
#                                                     location_report_clmn, location_clmn, code_clmn,
#                                                     act_error_str, error_msg, df_wide_act_volume_clmn_expect_lt_base)
#
# df_wide_act_volume_clmn_expect_lt_base = [code_clmn, description_clmn, category_clmn, location_clmn,
#                                           act_currency_clmn, act_volume_uom_report_clmn, act_volume_per_clmn]
# [df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_currency_equalizer,
#                                                     act_currency_report_clmn, bgt_currency_report_clmn,
#                                                     act_currency_clmn, code_clmn, act_error_str, error_msg,
#                                                     df_wide_act_volume_clmn_expect_lt_base)
#
# df_wide_act_volume_clmn_expect_lt_base = [code_clmn, description_clmn, category_clmn, location_clmn,
#                                           act_currency_clmn, act_volume_uom_clmn, act_volume_per_clmn]
# [df_wide_volume_act, error_msg] = fc.merge_and_drop(df_wide_volume_act, df_uom_equalizer, act_volume_uom_report_clmn,
#                                                     bgt_uom_report_clmn, act_volume_uom_clmn, code_clmn,
#                                                     act_error_str, error_msg, df_wide_act_volume_clmn_expect_lt_base)
#
# df_wide_act_price_clmn_expect_lt_base = [code_clmn, act_price_per_clmn]
# [df_wide_price_act, error_msg] = fc.merge_and_drop(df_wide_price_act, df_uom_equalizer, act_price_uom_report_clmn,
#                                                    bgt_uom_report_clmn, act_price_uom_clmn, code_clmn,
#                                                    act_error_str, error_msg, df_wide_act_price_clmn_expect_lt_base)
#
# ### forecast ###
# # volume
# df_wide_frc_volume_clmn_expect_lt_base = [code_clmn, description_clmn, location_clmn, frc_vol_uom_report_clmn,
#                                           frc_vol_per_clmn]
# [df_wide_frc_vol, error_msg] = fc.merge_and_drop(df_wide_frc_vol, df_location_equalizer, location_report_clmn,
#                                                  location_report_clmn, location_clmn, code_clmn, frc_error_str,
#                                                  error_msg, df_wide_frc_volume_clmn_expect_lt_base)
#
# df_wide_frc_volume_clmn_expect_lt_base = [code_clmn, description_clmn, location_clmn, frc_vol_uom_clmn,
#                                           frc_vol_per_clmn]
# [df_wide_frc_vol, error_msg] = fc.merge_and_drop(df_wide_frc_vol, df_uom_equalizer, frc_vol_uom_report_clmn,
#                                                  bgt_uom_report_clmn, frc_vol_uom_clmn, code_clmn, frc_error_str,
#                                                  error_msg, df_wide_frc_volume_clmn_expect_lt_base)
#
# # as budget
# [df_wide_frc_as_bgt, error_msg] = fc.merge_and_drop(df_wide_frc_as_bgt, df_location_equalizer, location_report_clmn,
#                                                     location_report_clmn, location_clmn, code_clmn, frc_error_str,
#                                                     error_msg)
#
# # as actuals
# [df_wide_frc_as_act, error_msg] = fc.merge_and_drop(df_wide_frc_as_act, df_location_equalizer, location_report_clmn,
#                                                     location_report_clmn, location_clmn, code_clmn, frc_error_str,
#                                                     error_msg)
#
# # as a constant
# [df_wide_frc_as_cnst, error_msg] = fc.merge_and_drop(df_wide_frc_as_cnst, df_location_equalizer, location_report_clmn,
#                                                      location_report_clmn, location_clmn, code_clmn, frc_error_str,
#                                                      error_msg)
# [df_wide_frc_as_cnst, error_msg] = fc.merge_and_drop(df_wide_frc_as_cnst, df_currency_equalizer,
#                                                      frc_currency_report_clmn, bgt_currency_report_clmn,
#                                                      frc_currency_clmn, code_clmn, act_error_str, error_msg)
# [df_wide_frc_as_cnst, error_msg] = fc.merge_and_drop(df_wide_frc_as_cnst, df_uom_equalizer, frc_price_uom_report_clmn,
#                                                      bgt_uom_report_clmn, frc_price_uom_clmn, code_clmn, act_error_str,
#                                                      error_msg)
#
# # as inflation
# [df_wide_frc_as_inf, error_msg] = fc.merge_and_drop(df_wide_frc_as_inf, df_location_equalizer, location_report_clmn,
#                                                     location_report_clmn, location_clmn, code_clmn, frc_error_str,
#                                                     error_msg)
# [df_wide_frc_as_inf, error_msg] = fc.merge_and_drop(df_wide_frc_as_inf, df_currency_equalizer,
#                                                     frc_currency_report_clmn, bgt_currency_report_clmn,
#                                                     frc_currency_clmn, code_clmn, act_error_str, error_msg)
# [df_wide_frc_as_inf, error_msg] = fc.merge_and_drop(df_wide_frc_as_inf, df_uom_equalizer, frc_price_uom_report_clmn,
#                                                     bgt_uom_report_clmn, frc_price_uom_clmn, code_clmn, act_error_str,
#                                                     error_msg)
#
# # as price curve
# [df_wide_frc_as_crv, error_msg] = fc.merge_and_drop(df_wide_frc_as_crv, df_location_equalizer, location_report_clmn,
#                                                     location_report_clmn, location_clmn, code_clmn, frc_error_str,
#                                                     error_msg)
# [df_wide_frc_as_crv, error_msg] = fc.merge_and_drop(df_wide_frc_as_crv, df_currency_equalizer,
#                                                     frc_currency_report_clmn, bgt_currency_report_clmn,
#                                                     frc_currency_clmn, code_clmn, act_error_str, error_msg)
# [df_wide_frc_as_crv, error_msg] = fc.merge_and_drop(df_wide_frc_as_crv, df_uom_equalizer, frc_price_uom_report_clmn,
#                                                     bgt_uom_report_clmn, frc_price_uom_clmn, code_clmn, act_error_str,
#                                                     error_msg)
# ### baseline ###
# [df_bsl, error_msg] = fc.merge_and_drop(df_bsl, df_location_equalizer, location_report_clmn, location_report_clmn,
#                                         location_clmn, code_clmn, bsl_error_str, error_msg)
# [df_bsl, error_msg] = fc.merge_and_drop(df_bsl, df_currency_equalizer, bsl_currency_report_clmn,
#                                         bgt_currency_report_clmn, bsl_currency_clmn, code_clmn, bsl_error_str,
#                                         error_msg)
#
# [df_bsl, error_msg] = fc.merge_and_drop(df_bsl, df_uom_equalizer, bsl_price_uom_report_clmn, bgt_uom_report_clmn,
#                                         bsl_price_uom_clmn, code_clmn, bsl_error_str, error_msg)
#
# ### project mapping ###
# [df_pjmp_pcent, error_msg] = fc.merge_and_drop(df_pjmp_pcent, df_location_equalizer, location_report_clmn,
#                                                location_report_clmn, location_clmn, code_clmn, pjmp_pcent_error_str,
#                                                error_msg)
#
# [df_pjmp_cnst, error_msg] = fc.merge_and_drop(df_pjmp_cnst, df_location_equalizer, location_report_clmn,
#                                               location_report_clmn, location_clmn, code_clmn, pjmp_cnst_error_str,
#                                               error_msg)
# [df_pjmp_cnst, error_msg] = fc.merge_and_drop(df_pjmp_cnst, df_uom_equalizer, pjmp_report_uom_clmn, bgt_uom_report_clmn,
#                                               pjmp_uom_clmn, code_clmn, act_error_str, error_msg)
# [df_pjmp_cnst, error_msg] = fc.merge_and_drop(df_pjmp_cnst, df_currency_equalizer, pjmp_currency_report_clmn,
#                                               bgt_currency_report_clmn, pjmp_currency_clmn, code_clmn,
#                                               pjmp_cnst_error_str, error_msg)
#
# [df_pjmp_pj_list, error_msg] = fc.merge_and_drop(df_pjmp_pj_list, df_project_type_equalizer, pjmp_type_report_clmn,
#                                                  pjmp_type_report_clmn, pjmp_type_clmn, pjmp_code_clmn,
#                                                  pjmp_pj_list_error_str, error_msg)
#
# ######################## From wide to long format ########################
# ### budget ###
# bgt_id_vars = [code_clmn, description_clmn, category_clmn, location_clmn, bgt_price_clmn, bgt_currency_clmn,
#                bgt_uom_clmn, bgt_per_clmn, savings_type_clmn]
#
# df_long_bgt = fc.melt_and_index(df_wide_bgt, bgt_id_vars, month_clmn, bgt_volume_clmn, code_clmn)
#
#
# ### actuals ###
# act_volume_id_vars = [code_clmn, description_clmn, category_clmn, location_clmn, act_currency_clmn,
#                       act_volume_uom_clmn, act_volume_per_clmn]
#
# df_long_volume_act = fc.melt_and_index(df_wide_volume_act, act_volume_id_vars, month_clmn, act_volume_clmn,
#                                        code_clmn)
#
# act_price_id_vars = [code_clmn, act_price_per_clmn, act_price_uom_clmn]
# df_long_price_act = fc.melt_and_index(df_wide_price_act, act_price_id_vars, month_clmn, act_price_clmn,
#                                       code_clmn)
#
# df_long_act = df_long_volume_act.merge(right=df_long_price_act, left_index=True, right_index=True)
#
# ### forecast volume ###
#
# frc_volume_id_vars = [code_clmn, description_clmn, location_clmn, frc_vol_uom_clmn, frc_vol_per_clmn]
# df_long_frc_vol = fc.melt_and_index(df_wide_frc_vol, frc_volume_id_vars, month_clmn, frc_vol_clmn, code_clmn)
#
# frc_vol_converting_clmns = [frc_vol_clmn]
# df_long_frc_vol = fc.convert_nan_to_zero(df_long_frc_vol, frc_vol_converting_clmns)
#
# ######################## Convert data types ########################
#
# ### budget ###
# bgt_clmn_list = [bgt_volume_clmn, bgt_per_clmn]
# bgt_conversion_error_string = bgt_error_str + " volume and per"
#
# [df_long_bgt, error_msg] = fc.clean_types(df_long_bgt, bgt_clmn_list, bgt_conversion_error_string, error_msg)
#
# ### actuals ###
# act_clmn_list = [act_volume_per_clmn, act_price_per_clmn]
# act_conversion_error_string = act_error_str + " volume, price and per"
# [df_long_act, error_msg] = fc.clean_types(df_long_act, act_clmn_list, act_conversion_error_string, error_msg)
#
# act_converting_clmns = [act_volume_clmn, act_price_clmn]
# df_long_act = fc.convert_nan_to_zero(df_long_act, act_converting_clmns)
#
# ## baseline ##
# bsl_clmn_list = [bsl_price_clmn, bsl_price_per_clmn]
# bsl_conversion_error_string = bsl_error_str + " conversion"
# [df_bsl, error_msg] = fc.clean_types(df_bsl, bsl_clmn_list, bsl_conversion_error_string, error_msg)
#
# ### conversion ###
# conv_clmn_list = [conv_multiplier_clmn]
# conv_error_string = conv_error_str + " conversion"
#
# [df_conv, error_msg] = fc.clean_types(df_conv, conv_clmn_list, conv_error_string, error_msg)
#
#
# ### project mapping ###
# pjmp_pcent_clmn_list = [pjmp_pcent_clmn]
# pjmp_pcent_error_string = pjmp_pcent_error_str + " conversion"
# [df_pjmp_pcent, error_msg] = fc.clean_types(df_pjmp_pcent, pjmp_pcent_clmn_list, pjmp_pcent_error_string, error_msg)
#
# pjmp_cnst_clmn_list = [pjmp_cnst_clmn]
# pjmp_cnst_error_string = pjmp_pcent_error_str + " conversion"
# [df_pjmp_cnst, error_msg] = fc.clean_types(df_pjmp_cnst, pjmp_cnst_clmn_list, pjmp_cnst_error_string, error_msg)
#
# pjmp_pj_list_clmn_list = [pjmp_cnst_clmn]
# pjmp_pj_list_error_string = pjmp_pj_list_error_str + " conversion"
# # pj_list dataframe does not have any numerical columns.
#
# ######################## Prepare conversion files ########################
# ### Generate reference file
# df_ref_uom = fc.generate_uom_ref_file(df_wide_bgt, code_clmn, bgt_uom_clmn, bgt_currency_clmn, ref_uom_clmn,
#                                       ref_currency_clmn)
#
# ######################## Indexing ########################
# ### baseline ###
# df_bsl.set_index(keys=[code_clmn], drop=True, inplace=True)
#
# ## predecessor ##
# df_pred.set_index(keys=[code_clmn], drop=True, inplace=True)
#
# ### equalization ###
# df_category_equalizer.set_index(keys=[category_report_clmn], drop=True, inplace=True)
# df_location_equalizer.set_index(keys=[location_clmn], drop=True, inplace=True)
# df_currency_equalizer.set_index(keys=[bgt_currency_clmn], drop=True, inplace=True)
# df_uom_equalizer.set_index(keys=[bgt_uom_report_clmn], drop=True, inplace=True)
# df_savings_type_equalizer.set_index(keys=[savings_type_report_clmn], drop=True, inplace=True)
#
#
# ######################## Include predecessor's data into budget ########################
# df_long_bgt = fc.include_predecessors(df_long_bgt, df_pred, pred_code_clmn, pred_code_clmn, code_clmn, month_clmn,
#                                       bgt_volume_clmn)
# df_bsl = fc.include_predecessors(df_bsl, df_pred, pred_code_clmn, bsl_pred_code_clmn, code_clmn)
#
# ######################## Calculate monthly price forecast ########################
# frc_id_vars = [code_clmn, description_clmn, location_clmn, frc_currency_clmn, frc_price_uom_clmn, frc_price_per_clmn]
# frc_desired_clmn_list = [description_clmn, location_clmn, frc_currency_clmn, frc_price_uom_clmn, frc_price_per_clmn,
#                          frc_price_clmn, frc_strategy_column]
#
# ### as budget price
# desired_bgt_clmn_lt = [bgt_currency_clmn, bgt_uom_clmn, bgt_per_clmn, bgt_price_clmn]
# bgt_matching_tuple = {bgt_currency_clmn: frc_currency_clmn,
#                       bgt_uom_clmn: frc_price_uom_clmn,
#                       bgt_per_clmn: frc_price_per_clmn,
#                       bgt_price_clmn: frc_price_clmn}
#
# df_long_frc_as_bgt = fc.generate_price_curve_based_on_budget(df_wide_frc_as_bgt, report_month + 1, 12,
#                                                              month_clmn, frc_price_clmn, code_clmn,
#                                                              frc_strategy_column, frc_strategy_as_bgt,
#                                                              df_long_bgt, desired_bgt_clmn_lt, bgt_matching_tuple,
#                                                              frc_desired_clmn_list)
#
# ### as avg actuals
# desired_act_clmn_lt = [act_currency_clmn, act_price_uom_clmn, act_price_per_clmn, act_price_clmn, act_volume_clmn]
# act_matching_tuple = {act_currency_clmn: frc_currency_clmn,
#                       act_price_uom_clmn: frc_price_uom_clmn,
#                       act_price_per_clmn: frc_price_per_clmn,
#                       act_price_clmn: frc_price_clmn}
#
#
# df_long_frc_as_act = fc.generate_price_curve_based_on_actuals(df_wide_frc_as_act, report_month + 1, 12,
#                                                               month_clmn, frc_price_clmn, code_clmn,
#                                                               frc_strategy_column, frc_strategy_as_act,
#                                                               df_long_act, desired_act_clmn_lt, act_matching_tuple,
#                                                               act_price_clmn, act_volume_clmn, frc_desired_clmn_list)
#
# ### as a constant
# df_long_frc_as_cnst = fc.generate_price_curve_based_on_constant(df_wide_frc_as_cnst, df_wide_frc_as_cnst[frc_price_clmn],
#                                                                 report_month+1, 12, frc_id_vars, month_clmn,
#                                                                 frc_price_clmn, code_clmn, frc_strategy_column,
#                                                                 frc_strategy_as_cnst, frc_desired_clmn_list)
#
# ### as an inflation rate
# df_long_frc_as_inf = fc.generate_price_curve_based_on_inflation(df_wide_frc_as_inf, report_month+1, 12, month_clmn,
#                                                                 frc_price_clmn, code_clmn,
#                                                                 frc_price_as_inf_base_price_clmn,
#                                                                 frc_price_as_inf_inflation_clmn,
#                                                                 frc_price_as_inf_month_clmn, frc_strategy_column,
#                                                                 frc_strategy_as_inf, frc_desired_clmn_list)
#
# ### as a curve
# df_long_frc_as_crv = fc.generate_price_curve_based_on_curve(df_wide_frc_as_crv, frc_id_vars, month_clmn,
#                                                             frc_price_clmn, code_clmn, frc_strategy_column,
#                                                             frc_strategy_as_crv, frc_desired_clmn_list)
#
# # unify all of them
#
# df_long_frc = df_long_frc_as_bgt
# df_long_frc = df_long_frc.append(df_long_frc_as_act)
# df_long_frc = df_long_frc.append(df_long_frc_as_cnst)
# df_long_frc = df_long_frc.append(df_long_frc_as_inf)
# df_long_frc = df_long_frc.append(df_long_frc_as_crv)
#
# df_long_frc_vol.drop(columns=[description_clmn, location_clmn], inplace=True)
# df_long_frc = df_long_frc.merge(df_long_frc_vol, how='outer', left_index=True, right_index=True)
#
# df_long_frc = fc.add_category_to_frc(df_long_frc, df_long_bgt, code_clmn, month_clmn, category_clmn)
#
# ######################## Calculate project list ########################
# # add column with savings assignement type
#
# df_pjmp_pcent[pjmp_sav_assignment_type] = pjmp_pcent_str
# df_pjmp_pcent[pjmp_per_clmn] = 1
# df_pjmp_pcent[pjmp_cnst_clmn] = 0
# df_pjmp_pcent[pjmp_uom_clmn] = 'N/A'
# df_pjmp_pcent[pjmp_currency_clmn] = 'N/A'
#
# df_pjmp_cnst[pjmp_sav_assignment_type] = pjmp_cnst_str
# df_pjmp_cnst[pjmp_pcent_clmn] = 0
#
# df_pjmp_pcent = df_pjmp_pcent[df_pjmp_clmn_list]
# df_pjmp_cnst = df_pjmp_cnst[df_pjmp_clmn_list]
#
# # merge pcent and const
# df_pjmp = df_pjmp_pcent
# df_pjmp = df_pjmp.append(df_pjmp_cnst)
#
# # add column with project savings type
# df_pjmp_pj_list.drop(columns=pjmp_description_clmn, inplace=True)
# df_pjmp = df_pjmp.merge(df_pjmp_pj_list, how='left', on=pjmp_code_clmn)
# df_pjmp.set_index(keys=code_clmn, drop=True, inplace=True)
#
# ######################## Add forecast strategy ########################
# ### budget ###
# df_long_act[frc_strategy_column] = 'NA'
# df_long_act_clmn_list.append(frc_strategy_column)
#
# ################## Load and structure conversion file ##################
# conv_to_all_str = 'All'
#
# code_clmn_list = df_long_bgt.reset_index()
# code_clmn_list = code_clmn_list[code_clmn]
# code_clmn_list = np.unique(code_clmn_list).tolist()
#
# df_conv = fc.prepare_long_uom_ref_file(df_conv, code_clmn_list, code_clmn, conv_old_uom_clmn, conv_new_uom_clmn,
#                                        conv_to_all_str)
#
# ######################## Reorder columns ########################
# ### budget ###
# df_long_bgt = df_long_bgt[df_long_bgt_clmn_list]
# ### actuals ###
# df_long_act = df_long_act[df_long_act_clmn_list]
# ### forecast ###
# df_long_frc = df_long_frc[df_long_frc_clmn_list]
#
# ### uom and currency reference file ###
# df_uom_ref = df_long_bgt.reset_index(inplace=False)
#
# df_uom_ref_clmn_expect_lt = [code_clmn, bgt_uom_clmn, bgt_currency_clmn, bgt_per_clmn]
# df_uom_ref = df_uom_ref.filter(items=df_uom_ref_clmn_expect_lt, axis=1)
#
# uom_ref_clmn_conversion = {bgt_per_clmn: uom_ref_per_price_clmn,
#                            bgt_uom_clmn: uom_ref_uom_price_clmn,
#                            bgt_currency_clmn: uom_ref_currency_clmn}
# df_uom_ref.rename(columns=uom_ref_clmn_conversion, inplace=True)
#
# df_uom_ref[uom_ref_per_volume_clmn] = df_uom_ref[uom_ref_per_price_clmn]
# df_uom_ref[uom_ref_uom_volume_clmn] = df_uom_ref[uom_ref_uom_price_clmn]
#
# df_uom_ref = fc.remove_key_duplicates(df_uom_ref, code_clmn)
#
# df_uom_ref.set_index(keys=[code_clmn], drop=True, inplace=True)
#
# df_uom_ref[uom_ref_currency_clmn] = reference_currency
#
# df_uom_ref_clmn_list = [uom_ref_uom_volume_clmn, uom_ref_per_volume_clmn, uom_ref_uom_price_clmn,
#                         uom_ref_per_price_clmn, uom_ref_currency_clmn]
# df_uom_ref = df_uom_ref[df_uom_ref_clmn_list]
#
# ######################## Save data-frame on CSV ########################
# ### budget ###
# df_long_bgt.to_csv(filename_bgt_csv)
#
# ### actuals ###
# df_long_act.to_csv(filename_act_csv)
#
# ### forecast ###
# df_long_frc.to_csv(filename_frc_csv)
#
# ### baseline ###
# df_bsl.to_csv(filename_bsl_csv)
#
# ## predecessor ##
# df_pred.to_csv(filename_pred_csv)
#
# ### equalization ###
# df_category_equalizer.to_csv(filename_category_eq_csv)
# df_location_equalizer.to_csv(filename_location_eq_csv)
# df_currency_equalizer.to_csv(filename_currency_eq_csv)
# df_uom_equalizer.to_csv(filename_uom_eq_csv)
# df_savings_type_equalizer.to_csv(filename_savings_type_eq_csv)
#
# ### conversion ###
# df_conv.to_csv(filename_conv_csv)
#
# ### project mapping ###
# df_pjmp.to_csv(filename_pjmp_csv)
#
# ### uom and currency reference file ###
# df_uom_ref.to_csv(filename_uom_ref_csv)
#
# ## error msg ##
# error_file = open(filename_error_msg, "w")
# error_file.write(error_msg)
# error_file.close()
#
# # print(error_msg)
# #############################                   2) CALCULATION ENGINE (var. 380)           #############################
# # temp location for inputs
#
# # df_long_act
# # Index: ['code', 'month']
# # Columns: ['description', 'category', 'location', 'act_volume', 'act_volume_per',
# #        'act_volume_uom', 'act_price', 'act_price_per', 'act_price_uom',
# #        'act_currency', 'frc_strategy']
#
# act_to_cy_clmn_conversion = {act_volume_clmn: cy_volume_clmn,
#                              act_volume_per_clmn: cy_volume_per_clmn,
#                              act_volume_uom_clmn: cy_volume_uom_clmn,
#                              act_price_clmn: cy_price_clmn,
#                              act_price_per_clmn: cy_price_per_clmn,
#                              act_price_uom_clmn: cy_price_uom_clmn,
#                              act_currency_clmn: cy_currency_clmn}
#
# # df_long_frc
# # Index: ['code', 'month']
# # Columns: ['description', 'category', 'location', 'frc_volume',
# #        'frc_volume_per_uom', 'frc_volume_uom', 'frc_price', 'frc_price_per',
# #        'frc_price_uom', 'frc_currency', 'frc_strategy']
# frc_to_cy_clmn_conversion = {frc_vol_clmn: cy_volume_clmn,
#                              frc_vol_per_clmn: cy_volume_per_clmn,
#                              frc_vol_uom_clmn: cy_volume_uom_clmn,
#                              frc_price_clmn: cy_price_clmn,
#                              frc_price_per_clmn: cy_price_per_clmn,
#                              frc_price_uom_clmn: cy_price_uom_clmn,
#                              frc_currency_clmn: cy_currency_clmn}
#
# # df_long_bgt
# # Index: ['code', 'month']
# # Columns: ['description', 'category', 'location', 'savings_type', 'bgt_volume',
# #        'bgt_price', 'bgt_per', 'bgt_uom', 'bgt_currency', 'bgt_predecessor']
# bgt_to_cy_to_drop = [description_clmn, category_clmn, location_clmn]
#
# # df_long_bsl
# # Index: ['code']
# # Columns: ['description', 'bsl_price', 'bsl_price_per',
# #        'bsl_average_price_last_year', 'location', 'bsl_currency',
# #        'bsl_price_uom']
# bsl_to_cy_to_drop = [description_clmn, location_clmn]
#
# # df_uom_ref
# # Index: ['code']
# # Columns:['Ref_uom_volume', 'Ref_per_volume', 'Ref_uom_price', 'Ref_per_price',
# #        'Ref_currency']
#
# # df_conv
# # Index: ['code', 'Old UoM', 'New UoM']
# # Columns: ['Multiplier']
#
# ######################### Calculating Savings per PN file #########################
# # 1) merge actuals and forecast information
# # 2) add budget information
# # 3) add baseline information
# # 4) convert UOMs and currency
# # 5) calculate:
# #       LY avg spend ly_spd => avg_price * bgt_vol
# #       baseline inflation (USD) bsl_inf => bsl_spd - ly_spd
# #       baseline spend bsl_spd => bsl_price * bgt_vol
# #       budget savings bsl_sav => bgt_spd - bsl_spd
# #       budget spend bgt_spd => bgt_price * bgt_vol
# #       impact due to delta volume vol_imp => cy_bgt_spd - bgt_spd
# #       budget spend at current year volume cy_bgt_spd => bgt_price * cy_vol
# #       current year savings cy_sav => cy_spd - cy_bgt_spd
# #       current year spend cy_spd => cy_price * cy_vol
# #       total savings total_sav => bsl_sav + vol_imp + cy_sav
#
# ### Change columns names ###
#
# df_long_act.rename(columns=act_to_cy_clmn_conversion, inplace=True)
# df_long_act[cy_type_report_clmn] = cy_act_report
#
# df_long_frc.rename(columns=frc_to_cy_clmn_conversion, inplace=True)
# df_long_frc[cy_type_report_clmn] = cy_frc_report
#
# ### Merge actuals and forecast information ###
# df_cy = df_long_act
# df_cy = df_cy.append(df_long_frc)
#
# ### Add budget information ###
# df_long_bgt = df_long_bgt.drop(bgt_to_cy_to_drop, axis=1, inplace=False)
# df_cy = df_cy.merge(df_long_bgt, how='left', left_index=True, right_index=True)
#
# ### Add baseline information ###
# df_bsl = df_bsl.drop(bsl_to_cy_to_drop, axis=1, inplace=False)
# df_cy.reset_index(inplace=True)
# df_cy = df_cy.merge(df_bsl, how='left', on=code_clmn)
# df_cy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=True)
#
# ### Add ref uom and currency ###
# df_cy.reset_index(inplace=True)
# df_cy = df_cy.merge(df_uom_ref, how='left', on=code_clmn)
# df_cy[month_clmn] = df_cy[month_clmn].astype('int64', copy=False)
# df_cy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=True)
#
# ### convert uom and currency to reference ###
#
# # cy to ref (price, per, currency, volume, per)
# cy_clmn_list_to_conv = [cy_price_clmn, cy_price_uom_clmn, cy_price_per_clmn, cy_currency_clmn, cy_volume_clmn,
#                         cy_volume_uom_clmn, cy_volume_per_clmn]
# cy_to_ref_mult_list = [cy_to_ref_mult_price_uom_clmn, cy_to_ref_mult_price_per_clmn, cy_to_ref_mult_currency_clmn,
#                        cy_to_ref_mult_volume_uom_clmn, cy_to_ref_mult_volume_per_clmn]
# cy_ref_clmn_list = [cy_price_at_ref_clmn, uom_ref_uom_price_clmn, uom_ref_per_price_clmn,
#                     uom_ref_currency_clmn, cy_volume_at_ref_clmn, uom_ref_uom_volume_clmn, uom_ref_per_volume_clmn]
#
# df_cy = fc.convert_uom(df_cy, df_conv, cy_clmn_list_to_conv, cy_ref_clmn_list, cy_to_ref_mult_list,
#                        conv_multiplier_clmn, code_clmn, month_clmn,)
#
# # bgt to ref
# bgt_clmn_list_to_conv = [bgt_price_clmn, bgt_uom_clmn, bgt_per_clmn, bgt_currency_clmn, bgt_volume_clmn, bgt_uom_clmn,
#                          bgt_per_clmn]
# bgt_to_ref_mult_list = [bgt_to_ref_mult_price_uom_clmn, bgt_to_ref_mult_price_per_clmn, bgt_to_ref_mult_currency_clmn,
#                         bgt_to_ref_mult_volume_uom_clmn, bgt_to_ref_mult_volume_per_clmn]
# bgt_ref_clmn_list = [bgt_price_at_ref_clmn, uom_ref_uom_price_clmn, uom_ref_per_price_clmn,
#                      uom_ref_currency_clmn, bgt_volume_at_ref_clmn, uom_ref_uom_volume_clmn, uom_ref_per_volume_clmn]
#
# df_cy = fc.convert_uom(df_cy, df_conv, bgt_clmn_list_to_conv, bgt_ref_clmn_list, bgt_to_ref_mult_list,
#                        conv_multiplier_clmn, code_clmn, month_clmn,)
#
# # bsl to ref
# bsl_clmn_list_to_conv = [bsl_price_clmn, bsl_price_uom_clmn, bsl_price_per_clmn, bsl_currency_clmn, 'empty', 'empty',
#                          'empty']
# bsl_to_ref_mult_list = [bsl_to_ref_mult_price_uom_clmn, bsl_to_ref_mult_price_per_clmn, bsl_to_ref_mult_currency_clmn,
#                         'empty', 'empty']
# bsl_ref_clmn_list = [bsl_price_at_ref_clmn, uom_ref_uom_price_clmn, uom_ref_per_price_clmn,
#                      uom_ref_currency_clmn, 'empty', 'empty', 'empty']
#
# df_cy = fc.convert_uom(df_cy, df_conv, bsl_clmn_list_to_conv, bsl_ref_clmn_list, bsl_to_ref_mult_list,
#                        conv_multiplier_clmn, code_clmn, month_clmn)
#
# # avg ly to ref
# df_cy[ly_price_at_ref_clmn] = df_cy[bsl_price_ly] * df_cy[bsl_to_ref_mult_price_uom_clmn] * \
#                               df_cy[bsl_to_ref_mult_price_per_clmn] * df_cy[bsl_to_ref_mult_currency_clmn]
#
# ### Spend and inflation calculations ###
# # LY avg spend ly_spd => avg_price * bgt_vol
#
# df_cy[ly_spend_avg_pr_bgt_vl_clmn] = df_cy[ly_price_at_ref_clmn] * df_cy[bgt_volume_at_ref_clmn]
#
# # BSL spend bsl_spd => bsl_price * bgt_vol
# df_cy[bsl_spend_bsl_pr_bgt_vl_clmn] = df_cy[bsl_price_at_ref_clmn] * df_cy[bgt_volume_at_ref_clmn]
#
# # baseline inflation (USD) bsl_inf => bsl_spd - ly_spd
# df_cy[bsl_inflation_clmn] = df_cy[bsl_spend_bsl_pr_bgt_vl_clmn] - df_cy[ly_spend_avg_pr_bgt_vl_clmn]
#
# # budget spend bgt_spd => bgt_price * bgt_vol
# df_cy[bgt_spend_bgt_pr_bgt_vl_clmn] = df_cy[bgt_price_at_ref_clmn] * df_cy[bgt_volume_at_ref_clmn]
#
# # budget savings bsl_sav => bgt_spd - bsl_spd
# df_cy[bgt_savings_clmn] = df_cy[bgt_spend_bgt_pr_bgt_vl_clmn] - df_cy[bsl_spend_bsl_pr_bgt_vl_clmn]
#
# # current year spend at budget volume cy_bgt_spd => cy_price * bgt_vol
# df_cy[bgt_spend_bgt_pr_cy_vl_clmn] = df_cy[bgt_price_at_ref_clmn] * df_cy[cy_volume_at_ref_clmn]
#
# # volume adjustment vol_adj => adj_bgt_spd - bgt_spd
# df_cy[volume_adjustment_clmn] = df_cy[bgt_spend_bgt_pr_cy_vl_clmn] - df_cy[bgt_spend_bgt_pr_bgt_vl_clmn]
#
# # current year spend cy_spd => cy_price * cy_vol
# df_cy[cy_spend_cy_pr_cy_vl_clmn] = df_cy[cy_price_at_ref_clmn] * df_cy[cy_volume_at_ref_clmn]
#
# # current year savings vs bgt cy_sav => cy_spd - adj_bgt_spd
# df_cy[cy_bgt_savings_clmn] = df_cy[bgt_spend_bgt_pr_cy_vl_clmn] - df_cy[cy_spend_cy_pr_cy_vl_clmn]
#
# # total savings total_sav => bsl_sav + cy_sav
# df_cy[bsl_spend_bsl_pr_cy_vl_clmn] = df_cy[bsl_price_at_ref_clmn] * df_cy[cy_volume_at_ref_clmn]
# df_cy[cy_bsl_savings_clmn] = df_cy[bsl_spend_bsl_pr_cy_vl_clmn] - df_cy[cy_spend_cy_pr_cy_vl_clmn]
#
# # volume influence bsl vol_inf_bsl => (bsl_price - cy_price) * (cy_volume - bsl_volume)
# df_cy[volume_influence_vs_bsl_clmn] = (df_cy[bsl_price_clmn] - df_cy[cy_volume_clmn]) * \
#                                       (df_cy[cy_volume_clmn] - df_cy[bgt_volume_clmn])
#
# # volume influence bgt vol_inf_bgt => (bgt_price - cy_price) * (cy_volume - bgt_volume)
# df_cy[volume_influence_vs_bgt_clmn] = (df_cy[bgt_price_clmn] - df_cy[cy_volume_clmn]) * \
#                                       (df_cy[cy_volume_clmn] - df_cy[bgt_volume_clmn])
#
# ### Filter NAN ###
# [df_cy, error_msg_engine] = fc.clean_nan_engine(df_cy, code_clmn,  month_clmn, engine_error_str)
#
# ######################### Calculating Savings per PJ file #########################
# ### filter desired columns from df_cy ###
# df_pj_clmn_list = [description_clmn, category_clmn, location_clmn, savings_type_clmn, cy_type_report_clmn,
#                    savings_type_clmn, frc_strategy_column]
#
# ### convert uoms ###
# df_pjmp.reset_index(inplace=True)
# df_pjmp = df_pjmp.merge(df_uom_ref, how='left', on=code_clmn)
# df_pjmp.set_index(keys=[code_clmn], drop=True, inplace=True)
#
# pjmp_clmn_list_to_conv = [pjmp_cnst_clmn, pjmp_uom_clmn, pjmp_per_clmn, pjmp_currency_clmn, 'empty', 'empty', 'empty']
# pjmp_ref_clmn_list = [pjmp_cnst_at_ref_clmn,  uom_ref_uom_price_clmn, uom_ref_per_price_clmn, uom_ref_currency_clmn,
#                       'empty', 'empty', 'empty']
# pjmp_to_ref_mult_list = [pjmp_to_ref_mult_uom_clmn, pjmp_to_ref_mult_per_clmn, pjmp_to_ref_mult_currency_clmn,
#                          'empty', 'empty']
# df_pjmp = fc.convert_uom(df_pjmp, df_conv, pjmp_clmn_list_to_conv, pjmp_ref_clmn_list, pjmp_to_ref_mult_list,
#                          conv_multiplier_clmn, code_clmn)
#
# ### include projects as columns ###
# pj_layer = fc.get_max_amount_of_code_repetitions(df_pjmp)
#
# proj_str_description_lt = fc.generate_prj_clm_list(proj_str_description, pj_layer)
# proj_str_value_lt = fc.generate_prj_clm_list(proj_str_value, pj_layer)
# proj_str_code_lt = fc.generate_prj_clm_list(proj_str_code, pj_layer)
#
# # create generate generic projects
# df_cy = fc.generate_generic_project_info(df_cy, category_clmn, proj_str_code_gen, proj_str_description_gen,
#                                          proj_str_value_gen, gen_pj_code_str, gen_pj_description_str, code_clmn, month_clmn)
#
# # calculate project values
# desired_calc_clmn_list = [pjmp_code_clmn, pjmp_description_clmn, pjmp_pcent_clmn, pjmp_cnst_at_ref_clmn,
#                           pjmp_start_month_clmn]
# desired_calc_clmn_list = [pjmp_code_clmn, pjmp_description_clmn, pjmp_pcent_clmn, pjmp_cnst_at_ref_clmn,
#                           pjmp_start_month_clmn]
# df_pjmp_short = df_pjmp[desired_calc_clmn_list]
# pj_delete_clmn_list = [pjmp_pcent_clmn, pjmp_cnst_at_ref_clmn, pjmp_start_month_clmn]
#
# df_cy = fc.add_projects(df_cy, df_pjmp_short, proj_str_description_lt, proj_str_value_lt, proj_str_code_lt,
#                         code_clmn, month_clmn, pjmp_code_clmn, pjmp_description_clmn, pjmp_pcent_clmn,
#                         pjmp_cnst_at_ref_clmn, pjmp_start_month_clmn, cy_bsl_savings_clmn, cy_volume_at_ref_clmn,
#                         uom_ref_per_price_clmn, uom_ref_per_price_clmn, proj_str_value_gen, pj_layer,
#                         pj_delete_clmn_list)
#
# ### calculate savings per project and include on df_pj ###
# # pj_desired_list
# pj_desired_clmn_list = [pjmp_code_clmn, pjmp_sav_assignment_type]
# proj_str_description_lt = [proj_str_description_gen] + proj_str_description_lt
# proj_str_value_lt = [proj_str_value_gen] + proj_str_value_lt
# proj_str_code_lt = [proj_str_code_gen] + proj_str_code_lt
#
# new_str_clmn_list = [proj_str_code, proj_str_description, proj_str_value]
# df_pj = fc.create_project_dataframe(df_pjmp, df_cy, pj_desired_clmn_list, proj_str_description_lt, proj_str_value_lt,
#                                     proj_str_code_lt, pjmp_code_clmn, proj_str_value, new_str_clmn_list,
#                                     uom_ref_currency_clmn)
#
# #sum savings versus baseline
#
# ### clean nan ###
#
# ### Reorder columns ###
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
#
# df_cy_clmn_list = fc.add_project_to_clmn_list(df_cy_clmn_list, proj_str_code_lt, proj_str_description_lt,
#                                               proj_str_value_lt, pj_layer)
#
# df_cy = df_cy[df_cy_clmn_list]
# df_cy.sort_values(by=[code_clmn, month_clmn], axis=0, inplace=True, ascending=[True, True])
#
# df_pj_clmn_list = [proj_str_description, proj_str_value, pjmp_sav_assignment_type]
# df_pj = df_pj[df_pj_clmn_list]
# df_pj.sort_values(by=[proj_str_code], axis=0, inplace=True, ascending=[True])
#
# ### save on CSV “Savings Report – FY YYYY period XX per PN”) ###
# df_cy.to_csv(filename_cy_csv)
# df_pj.to_csv(filename_pj_csv)
#
# ### save on Excel “Savings Report – FY YYYY period XX ###
# fc.save_excel(filename_cy_pj_xlsx, df_cy, df_pj, sheetname_cy, sheetname_pj, color_list, cy_color_index_for_clmns,
#               cy_color_order, pj_color_index_for_clmns, pj_color_order)
#
#
# ## error msg ##
# error_file_engine = open(filename_error_msg_engine, "w")
# error_file_engine.write(error_msg_engine)
# error_file_engine.close()
#
# #############################                    3) REPORT GENERATOR                       #############################
#
#
# #############################                  4) WEB INTERFACE (input)                    #############################
#
# #############################               5) INTERACTIVE INTERFACE (output)              #############################


# def find_multiplier(df_conversion, pn_code_clmn, old_uom, new_uom,
#                           gen_pn):
#     mtx_xy = df_base.filter(items=[code_clmn, ref_uom, ref_currency], axis=1)
#     mtx_xy = mtx_xy.rename(columns={ref_uom: ref_uom_str, ref_currency: ref_currency_str}, inplace=False)
#
#     return mtx_xy

# def remove_key_duplicates(old_mtx_xy, key_column):
#     new_mtx_xy = old_mtx_xy.drop_duplicates(key_column)
#
#     return new_mtx_xy
#
#
# def verify_integrity_from_code(code, clmn_list, new_error_list, function_error_str, error_str):
#     is_part_of_clmn_list = code in clmn_list
#     if not is_part_of_clmn_list:
#         new_error_list = new_error_list + function_error_str + error_str.format(code)
#     return new_error_list
#
#
# def verify_integrity_from_code_lt(clmn_expected_list, clmn_list, error_list, function_error_str, error_str):
#     for item in clmn_expected_list:
#         error_list = verify_integrity_from_code(item, clmn_list, error_list, function_error_str, error_str)
#     return error_list
#
#
# def gen_delete_list(raw_clmn_list, clmn_expected_list):
#     clmns_to_delete = []
#     for item in raw_clmn_list:
#         is_part_of_expected_list = item in clmn_expected_list
#         if not is_part_of_expected_list:
#             clmns_to_delete.append(item)
#     return clmns_to_delete
#
# def file_clmn_integrity(mtx_xy, clmn_expected_list, error_str, old_error_list="",
#                         function_error_str = "Failed column integrity "):
#     raw_clmn_list = mtx_xy.columns.tolist()
#     new_error_list = verify_integrity_from_code_lt(clmn_expected_list, clmn_expected_list, old_error_list,
#                                             function_error_str, error_str)
#     clmns_to_delete = gen_delete_list(raw_clmn_list, clmn_expected_list)
#
#     return [clmns_to_delete, new_error_list]
#
#

#
#
# def generate_wide_clmn_expected_list(old_list, start, end, base_string):
#     new_list = old_list
#     for ii in range(start, end+1):
#         new_list.append(base_string + str(ii))
#
#     return new_list
#
#
# def generate_wide_clmn_conversion(base_dict, start_month, end_month, base_string):
#     final_dict = base_dict
#     for jj in range(start_month, end_month+1):
#          final_dict[base_string + str(jj)] = str(jj)
#
#     return final_dict
#
#
#
#
#
#
# def melt_and_index(wide_mtx_xy, wide_vars, long_clmn, value_clmn, code_clmn):
#     long_mtx_xy = pd.melt(frame=wide_mtx_xy, id_vars=wide_vars, value_vars=None, var_name=long_clmn,
#                              value_name=value_clmn)
#     long_mtx_xy = long_mtx_xy.set_index(keys=[code_clmn, long_clmn], drop=True, inplace=False)
#
#     return long_mtx_xy
#
#
# def convert_strings_to_nan(item):
#     if isinstance(item, str):
#         return np.nan
#     else:
#         return item
#
#
# def convert_to_numeric(item):
#     item = pd.to_numeric(item)
#
#     return item
#
#
# def convert_to_zero(item):
#     if pd.isnull(item):
#         item = 0
#
#     return item
#
# def clean_types(mtx_xy, cleaning_clmns, error_str, old_error_list=""):
#     new_mtx_xy = mtx_xy
#     old_index_list = mtx_xy.index
#     # Use applymap to find str and substitute
#     mtx_xy = mtx_xy.filter(items=cleaning_clmns, axis=1).applymap(convert_strings_to_nan)
#     # delete these rows
#     mtx_xy = mtx_xy.dropna(axis=0, subset=cleaning_clmns, inplace=False)
#     # check which rows where deleted
#
#     new_index_list = mtx_xy.index
#     new_error_list = old_error_list
#     [missing_codes, are_lists_equal] = list_differential(old_index_list, new_index_list)
#
#     # save list of deleted of rows into error msg
#     if not are_lists_equal:
#         error_str_nan = "PNs/month with problems: "
#         aux = " -- "
#         new_error_list = new_error_list + aux + error_str + aux + error_str_nan + str(missing_codes)
#
#     level_qty = mtx_xy.index.nlevels
#
#     if level_qty > 1:
#         df_missing_codes = pd.mtx_xy(missing_codes, columns=['code', 'month'])
#         df_missing_codes_list = df_missing_codes['code'].to_list()
#
#         if len(df_missing_codes_list) != 0:
#            new_mtx_xy = new_mtx_xy.drop(df_missing_codes_list, level=0, axis=0)
#     else:
#         new_mtx_xy = new_mtx_xy.drop(missing_codes, axis=0)
#
#     for item in cleaning_clmns:
#         new_mtx_xy[item] = new_mtx_xy[item].apply(convert_to_numeric)
#
#     return [new_mtx_xy, new_error_list]
#
#
# def convert_nan_to_zero(mtx_xy, converting_clmns):
#     new_mtx_xy = mtx_xy
#
#     for item in converting_clmns:
#         new_mtx_xy[item] = new_mtx_xy[item].apply(convert_to_zero)
#
#     return new_mtx_xy
#
#
# def remove_from_list(list, item):
#     if item in list:
#         list.remove(item)
#     return list
#
#
# def drop_na_crossed(mtx_xy, ref_clmn, clm_list):
#     new_mtx_xy = mtx_xy
#     mtx_xy = mtx_xy.filter(items=clm_list, axis=1)
#
#     old_index_list = mtx_xy[ref_clmn]
#
#     mtx_xy = mtx_xy.dropna(axis=0, inplace=False)
#
#     # is_there_nan = any(pd.isnull(old_index_list))
#
#     old_index_list = mtx_xy[ref_clmn]
#     old_index_list = [str(item) for item in old_index_list]
#     old_index_list = remove_from_list(old_index_list, 'nan')
#
#     new_index_list = mtx_xy[ref_clmn]
#
#     new_index_list = [str(item) for item in new_index_list]
#
#     [missing_codes, are_lists_equal] = list_differential(old_index_list, new_index_list)
#
#     new_mtx_xy = new_mtx_xy.drop(missing_codes, axis=0)
#
#     # if is_there_nan:
#     #     new_mtx_xy = new_mtx_xy.dropna(axis=0, inplace=False)
#
#     return new_mtx_xy
#
#
# def clear_extra_rows(mtx_xy, ref_clmn, error_str, old_error_list="", clm_list='empty'):
#     if clm_list == 'empty':
#         clm_list = mtx_xy.columns
#
#     old_index_list = mtx_xy[ref_clmn]
#
#     mtx_xy = drop_na_crossed(mtx_xy, ref_clmn, clm_list)
#
#     new_index_list = mtx_xy[ref_clmn]
#
#     old_index_list = [str(item) for item in old_index_list]
#     new_index_list = [str(item) for item in new_index_list]
#
#     old_index_list = remove_from_list(old_index_list, 'nan')
#     [missing_codes, are_lists_equal] = list_differential(old_index_list, new_index_list)
#
#     new_error_list = old_error_list
#
#     if not are_lists_equal:
#         error_str_nan = "Rows w/Nan: "
#         aux = " -- "
#         new_error_list = new_error_list + aux + error_str + aux + error_str_nan + str(missing_codes)
#
#     return [mtx_xy, new_error_list]
#
#
#
#
# def prepare_long_uom_ref_file(df_conv_short, code_list, code_clmn, conv_old_uom_clmn, conv_new_uom_clmn,
#                                 conv_to_all_str):
#
#     query_str1 = code_clmn + '!="' + conv_to_all_str + '"'
#     df_conv_long = df_conv_short.query(query_str1, inplace=False)
#
#     query_str2 = code_clmn + '=="' + conv_to_all_str + '"'
#     df_conv_short = df_conv_short.query(query_str2, inplace=False)
#
#     for item in code_list:
#         df_conv_long = add_all_uom_fx_to_code(df_conv_long, df_conv_short, item, conv_to_all_str)
#
#     df_conv_long = df_conv_long.set_index(keys=[code_clmn, conv_old_uom_clmn, conv_new_uom_clmn], drop=True,
#                                           inplace=False)
#
#     return df_conv_long
#
#
# def add_all_uom_fx_to_code(mtx_xy, base_mtx_xy, code, conv_to_all_str):
#     base_mtx_xy = base_mtx_xy.replace(conv_to_all_str, code, inplace=False)
#     mtx_xy = mtx_xy.append(base_mtx_xy)
#
#     return mtx_xy
#
#
# def include_predecessors(mtx_xy, df_pred, pred_code_clmn, extra_clmn_name, code_clmn, month_clmn="empty",
#                          bgt_volume_clmn='empty'):
#     new_mtx_xy = mtx_xy
#     new_mtx_xy[extra_clmn_name] = new_mtx_xy.index.get_level_values(code_clmn)
#
#     code_list = df_pred.index
#
#     if month_clmn == "empty":
#         for item in code_list:
#             new_mtx_xy = include_single_predecessor_single_index(new_mtx_xy, df_pred, pred_code_clmn, code_clmn,
#                                                                     item)
#     else:
#         for item in code_list:
#             new_mtx_xy = include_single_predecessor_double_index(new_mtx_xy, df_pred, pred_code_clmn, code_clmn,
#                                                                     month_clmn, item, bgt_volume_clmn)
#
#     return new_mtx_xy
#
#
# def include_single_predecessor_single_index(mtx_xy, df_pred, pred_code_clmn, code_clmn, new_code):
#
#     bgt_pred = df_pred.loc[new_code, pred_code_clmn]
#
#     add_row = mtx_xy.reset_index(inplace=False)
#     add_row = add_row[add_row.apply(lambda x: x[code_clmn] == bgt_pred, axis=1)]
#     add_row[code_clmn] = new_code
#     add_row = add_row.set_index(keys=[code_clmn], drop=True, inplace=False)
#
#     new_mtx_xy = mtx_xy.append(add_row)
#
#     return new_mtx_xy
#
#
# def include_single_predecessor_double_index(mtx_xy, df_pred, pred_code_clmn, code_clmn, month_clmn, new_code,
#                                             bgt_volume_clmn):
#     new_mtx_xy = mtx_xy
#
#     bgt_pred = df_pred.loc[new_code, pred_code_clmn]
#
#     bgt_pred_array = [12 * [bgt_pred],
#                       ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']]
#
#     bgt_pred_tuple = list(zip(*bgt_pred_array))
#
#     add_row = new_mtx_xy.filter(bgt_pred_tuple, axis=0)
#     add_row = add_row.reset_index(inplace=False)
#     add_row[code_clmn] = new_code
#     if bgt_volume_clmn != 'empty':
#         add_row[bgt_volume_clmn] = 0
#     add_row = add_row.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=False)
#
#     new_mtx_xy = new_mtx_xy.append(add_row)
#
#     return new_mtx_xy
#
#
# def generate_price_curve_based_on_constant(old_mtx_xy, value_list, start_month, end_month, df_id_vars, month_clmn,
#                                            price_clmn, code_clmn, strategy_clmn, strategy_str, desired_clmn_list):
#     month_list = range(start_month, end_month+1)
#     new_mtx_xy = old_mtx_xy
#     new_mtx_xy = new_mtx_xy.rename(columns={price_clmn: str(month_list[0])}, inplace=False)
#
#     for item in month_list:
#         new_mtx_xy[str(item)] = value_list
#
#     new_mtx_xy = generate_price_curve_based_on_curve(new_mtx_xy, df_id_vars, month_clmn, price_clmn, code_clmn,
#                                                         strategy_clmn, strategy_str, desired_clmn_list)
#
#     return new_mtx_xy
#
#
# def generate_price_curve_based_on_curve(old_mtx_xy, df_id_vars, month_clmn, price_clmn, code_clmn, strategy_clmn,
#                                         strategy_str, desired_clmn_list):
#     # wide to long
#     new_mtx_xy = melt_and_index(old_mtx_xy, df_id_vars, month_clmn, price_clmn, code_clmn)
#     # add column with forecast strategy
#     new_mtx_xy[strategy_clmn] = strategy_str
#     new_mtx_xy = new_mtx_xy.filter(items=desired_clmn_list, axis=1)
#
#     return new_mtx_xy
#
#
# def generate_price_curve_based_on_budget(old_mtx_xy, start_month, end_month, month_clmn, price_clmn, code_clmn,
#                                          strategy_clmn, strategy_str, ref_file, ref_clmn_lt, matching_tuple,
#                                          desired_clmn_list):
#     # forecast as a budget file
#     old_df_clmn_lt = old_mtx_xy.columns
#     month_list = range(start_month, end_month + 1)
#     wide_mtx_xy = old_mtx_xy
#     value = 0
#
#     for item in month_list:
#         wide_mtx_xy[str(item)] = value
#
#     long_mtx_xy = melt_and_index(wide_mtx_xy, old_df_clmn_lt, month_clmn, price_clmn, code_clmn)
#     long_mtx_xy = long_mtx_xy.drop(columns=price_clmn, inplace=False)
#
#     # budget file
#     ref_data = ref_file.filter(items=ref_clmn_lt, axis=1)
#     ref_data = ref_data.rename(columns=matching_tuple, inplace=False)
#
#     new_mtx_xy = long_mtx_xy.merge(ref_data, how='left', left_index=True, right_index=True)
#     new_mtx_xy[strategy_clmn] = strategy_str
#     new_mtx_xy = new_mtx_xy.filter(items=desired_clmn_list, axis=1)
#
#     return new_mtx_xy
#
#
# def generate_price_curve_based_on_actuals(old_mtx_xy, start_month, end_month, month_clmn, price_clmn, code_clmn,
#                                           strategy_clmn, strategy_str, ref_file, ref_clmn_lt, matching_tuple,
#                                           act_price_clmn, act_volume_clmn, desired_clmn_list):
#
#     old_df_clmn_lt = old_mtx_xy.columns
#     month_list = range(start_month, end_month + 1)
#     wide_mtx_xy = old_mtx_xy
#     value = 0
#
#     for item in month_list:
#         wide_mtx_xy[str(item)] = value
#
#     long_mtx_xy = melt_and_index(wide_mtx_xy, old_df_clmn_lt, month_clmn, price_clmn, code_clmn)
#     long_mtx_xy = long_mtx_xy.drop(columns=price_clmn, inplace=False)
#
#     # budget file
#     ref_data = ref_file.filter(items=ref_clmn_lt, axis=1)
#
#     df_avg = ref_data
#
#     ref_data = ref_data.drop(columns=act_price_clmn)
#     spend_clmn = 'act_spend'
#     df_avg[spend_clmn] = df_avg[act_volume_clmn] * df_avg[act_price_clmn]
#     # filter data (only code and PN)
#
#     df_avg = df_avg.groupby(level=code_clmn).sum()
#     df_avg[act_price_clmn] = df_avg[spend_clmn] / df_avg[act_volume_clmn]
#     df_avg = df_avg.filter(items=[act_price_clmn], axis=1)
#
#     df_avg = df_avg.reset_index(inplace=False)
#     ref_data = ref_data.reset_index(inplace=False)
#     ref_data = ref_data.drop(columns=month_clmn)
#
#     ref_data = ref_data.merge(df_avg, how='left', on=code_clmn)
#     ref_data = remove_key_duplicates(ref_data, code_clmn)
#
#     long_mtx_xy = long_mtx_xy.reset_index(inplace=False)
#
#     new_mtx_xy = long_mtx_xy.merge(ref_data, how='left', on=code_clmn)
#
#     new_mtx_xy = new_mtx_xy.rename(columns=matching_tuple, inplace=False)
#     new_mtx_xy = new_mtx_xy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=False)
#
#     new_mtx_xy[strategy_clmn] = strategy_str
#     new_mtx_xy = new_mtx_xy.filter(items=desired_clmn_list, axis=1)
#
#
#     return new_mtx_xy
#
#
# def generate_price_curve_based_on_inflation(old_mtx_xy, start_month, end_month, month_clmn, price_clmn, code_clmn,
#                                             base_price_clmn, inflation_clmn, inf_month_clmn, strategy_clmn,
#                                             strategy_str, desired_clmn_list):
#
#     # add column with inflated price
#     wide_mtx_xy = old_mtx_xy
#     inf_price_clmn = 'inf_price'
#     wide_mtx_xy[inf_price_clmn] = wide_mtx_xy[base_price_clmn] * (1 + wide_mtx_xy[inflation_clmn])
#
#     # create month columns from report month+1 until 12
#     old_df_clmn_lt = old_mtx_xy.columns
#     month_list = range(start_month, end_month + 1)
#     wide_mtx_xy = old_mtx_xy
#     value = 0
#
#     for item in month_list:
#         wide_mtx_xy[str(item)] = value
#
#     # wide to long
#     new_mtx_xy = melt_and_index(wide_mtx_xy, old_df_clmn_lt, month_clmn, price_clmn, code_clmn)
#     new_mtx_xy = new_mtx_xy.drop(columns=price_clmn, inplace=False)
#
#     new_mtx_xy = new_mtx_xy.reset_index(inplace=False)
#     new_mtx_xy[month_clmn] = new_mtx_xy[month_clmn].astype(int)
#
#     new_mtx_xy.loc[new_mtx_xy[month_clmn] < new_mtx_xy[inf_month_clmn], price_clmn] = new_mtx_xy[base_price_clmn]
#     new_mtx_xy.loc[new_mtx_xy[month_clmn] >= new_mtx_xy[inf_month_clmn], price_clmn] = new_mtx_xy[inf_price_clmn]
#
#     new_mtx_xy[strategy_clmn] = strategy_str
#     new_mtx_xy[month_clmn] = new_mtx_xy[month_clmn].astype(str)
#     new_mtx_xy = new_mtx_xy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=False)
#     new_mtx_xy = new_mtx_xy.filter(items=desired_clmn_list, axis=1)
#     # drop base price and inflation column
#
#     return new_mtx_xy
#
#
# def add_category_to_frc(old_mtx_xy, category_mtx_xy, code_clmn, month_clmn, category_clmn):
#
#     category_mtx_xy = category_mtx_xy.reset_index(inplace=False)
#     category_mtx_xy = category_mtx_xy.filter(items=[code_clmn, month_clmn, category_clmn], axis=1)
#     category_mtx_xy = category_mtx_xy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=False)
#     new_mtx_xy = old_mtx_xy.merge(category_mtx_xy, how='inner', left_index=True, right_index=True)
#
#     return new_mtx_xy
#
#
# def fix_index(old_mtx_xy, code_clmn, month_clmn):
#     new_mtx_xy = old_mtx_xy
#
#     new_mtx_xy = new_mtx_xy.reset_index(inplace=False)
#     new_mtx_xy[month_clmn] = new_mtx_xy[month_clmn].apply(convert_to_numeric)
#
#     new_mtx_xy = new_mtx_xy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=False)
#
#     return new_mtx_xy
#
#
# #############################              2) CALCULATION ENGINE                  ######################################
#
# def convert_uom(mtx_xy, df_conv, old_uom_list, new_uom_list, mult_list, conv_multiplier_clmn, code_clmn,
#                 month_clmn='empty'):
#
#     old_price_value_clmn = old_uom_list[0]
#     old_price_uom_clmn = old_uom_list[1]
#     old_price_per_clmn = old_uom_list[2]
#     old_price_currency_clmn = old_uom_list[3]
#     old_volume_value_clmn = old_uom_list[4]
#     old_volume_uom_clmn = old_uom_list[5]
#     old_volume_per_clmn = old_uom_list[6]
#
#     new_price_value_clmn = new_uom_list[0]
#     new_price_uom_clmn = new_uom_list[1]
#     new_price_per_clmn = new_uom_list[2]
#     new_price_currency_clmn = new_uom_list[3]
#     new_volume_value_clmn = new_uom_list[4]
#     new_volume_uom_clmn = new_uom_list[5]
#     new_volume_per_clmn = new_uom_list[6]
#
#     mult_price_uom_clmn = mult_list[0]
#     mult_price_per_clmn = mult_list[1]
#     mult_price_currency_clmn = mult_list[2]
#     mult_volume_uom_clmn = mult_list[3]
#     mult_volume_per_clmn = mult_list[4]
#
#     mtx_xy.reset_index(inplace=True)
#
#     mtx_xy = find_multiplier(mtx_xy, df_conv, code_clmn, old_price_uom_clmn, new_price_uom_clmn,
#                                 conv_multiplier_clmn, mult_price_uom_clmn)
#     mtx_xy[mult_price_uom_clmn] = 1/mtx_xy[mult_price_uom_clmn]
#
#     mtx_xy[mult_price_per_clmn] = mtx_xy[new_price_per_clmn]/mtx_xy[old_price_per_clmn]
#
#     mtx_xy = find_multiplier(mtx_xy, df_conv, code_clmn, old_price_currency_clmn, new_price_currency_clmn,
#                                 conv_multiplier_clmn, mult_price_currency_clmn)
#
#     mtx_xy[new_price_value_clmn] = mtx_xy[old_price_value_clmn] * mtx_xy[mult_price_uom_clmn] * \
#                                       mtx_xy[mult_price_per_clmn] * mtx_xy[mult_price_currency_clmn]
#
#     if mult_volume_per_clmn != 'empty':
#         mtx_xy = find_multiplier(mtx_xy, df_conv, code_clmn, old_volume_uom_clmn, new_volume_uom_clmn,
#                                     conv_multiplier_clmn, mult_volume_uom_clmn)
#         mtx_xy[mult_volume_per_clmn] = mtx_xy[old_volume_per_clmn]/mtx_xy[new_volume_per_clmn]
#         mtx_xy[new_volume_value_clmn] = mtx_xy[old_volume_value_clmn] * mtx_xy[mult_volume_uom_clmn] * \
#                                            mtx_xy[mult_volume_per_clmn]
#
#     if month_clmn != 'empty':
#         mtx_xy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=True)
#     else:
#         mtx_xy.set_index(keys=code_clmn, drop=True, inplace=True)
#
#     return mtx_xy
#
#
# def find_multiplier(mtx_xy, df_conv, code_clmn, old_clmn, new_clmn, old_name_clmn, new_name_clmn):
#
#     mtx_xy = mtx_xy.merge(df_conv, how='left', left_on=[code_clmn, old_clmn, new_clmn], right_index=True)
#     mtx_xy.rename(columns={old_name_clmn: new_name_clmn}, inplace=True)
#
#     return mtx_xy
#
#
# def clean_nan_engine(mtx_xy, code_clmn, month_clmn, error_str, old_error_list='empty', clm_list='empty'):
#     if clm_list == 'empty':
#         clm_list = mtx_xy.columns
#
#     mtx_xy.reset_index(inplace=True)
#
#     old_part_number_bgt_list = mtx_xy[code_clmn]
#     old_part_number_bgt_list = set(old_part_number_bgt_list)
#
#     old_part_number_bgt_list = [str(item) for item in old_part_number_bgt_list]
#
#     mtx_xy = mtx_xy.dropna(inplace=False, subset=clm_list)
#
#     new_part_number_bgt_list = mtx_xy[code_clmn]
#     new_part_number_bgt_list = set(new_part_number_bgt_list)
#
#     new_part_number_bgt_list = [str(item) for item in new_part_number_bgt_list]
#
#     [missing_codes, are_lists_equal] = list_differential(old_part_number_bgt_list, new_part_number_bgt_list)
#
#     new_error_list = old_error_list
#
#     if not are_lists_equal:
#         error_str_nan = "Rows w/Nan: "
#         aux = " -- "
#         new_error_list = new_error_list + aux + error_str + aux + error_str_nan + str(missing_codes)
#
#     mtx_xy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=True)
#
#     return [mtx_xy, new_error_list]
#
#
# def get_max_amount_of_code_repetitions(mtx_xy):
#     code_list = mtx_xy.index.tolist()
#
#     code_qty = []
#     for item in code_list:
#         code_qty.append(code_list.count(item))
#
#     max_qty = max(code_qty)
#
#     return max_qty
#
#
# def generate_prj_clm_list(proj_str, layer_qty):
#     proj_str_lt = []
#
#     for i in range(1, layer_qty+1):
#         proj_str_lt.append(proj_str+str(i))
#
#     return proj_str_lt
#
#
# def generate_generic_project_info(mtx_xy, category_clmn, pj_code_clmn, pj_name_clmn, pj_value_clmn, gen_code_str,
#                                   gen_name_str, code_clmn, month_clmn):
#
#     category_list = set(mtx_xy[category_clmn])
#
#     pj_code_list = generate_code_list(len(category_list), gen_code_str)
#     pj_name_list = generate_name_list(category_list, gen_name_str)
#
#     df_gen = pd.mtx_xy(category_list, columns=[category_clmn])
#     df_gen[pj_code_clmn] = pj_code_list
#     df_gen[pj_name_clmn] = pj_name_list
#     df_gen[pj_value_clmn] = 0
#
#     mtx_xy.reset_index(inplace=True)
#     mtx_xy = mtx_xy.merge(df_gen, how='left', left_on=category_clmn, right_on=category_clmn)
#     mtx_xy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=True)
#
#     return mtx_xy
#
#
# def generate_name_list(category_list, gen_name_str):
#     name_list = []
#
#     for item in category_list:
#         name_list.append(item+gen_name_str)
#
#     return name_list
#
#
# def generate_code_list(category_list_size, gen_code_str):
#     code_list = []
#
#     for ii in range(1, category_list_size+1):
#         if ii < 10:
#             code_list.append(gen_code_str + '00' + str(ii))
#         elif ii < 100:
#             code_list.append(gen_code_str + '0' + str(ii))
#         else:
#             code_list.append(gen_code_str + str(ii))
#
#     return code_list
#
#
# def add_projects(mtx_xy, df_project,  pj_description_list, pj_value_list, pj_code_list, code_clmn, month_clmn,
#                  pjmp_code_clmn, pjmp_description_clmn, pcent_clmn, cnst_clmn_at_ref, start_mth_clmn, bsl_sav_clmn,
#                  volume_at_ref_clmn, cnst_per_clmn, volume_per_clmn_at_ref, pj_gen_value_clmn, layers, delete_list):
#
#     df_project.reset_index(inplace=True)
#     df_remainder_pj = df_project
#     mtx_xy[pj_gen_value_clmn] = mtx_xy[bsl_sav_clmn]
#
#     for kk in range(0, layers):
#
#         [df_clean_pj, df_remainder_pj] = remove_project_duplicates(df_remainder_pj, code_clmn)
#
#         mtx_xy.reset_index(inplace=True)
#         mtx_xy = mtx_xy.merge(df_clean_pj, how='left', left_on=code_clmn, right_on=code_clmn)
#         mtx_xy[pj_value_list[kk]] = mtx_xy.apply(lambda x: calculate_project(x[bsl_sav_clmn],
#                                                                                    x[volume_at_ref_clmn],
#                                                                                    x[pcent_clmn], x[cnst_clmn_at_ref],
#                                                                                    x[start_mth_clmn], x[month_clmn],
#                                                                                    x[cnst_per_clmn],
#                                                                                    x[volume_per_clmn_at_ref]),
#                                                                                   axis=1)
#         mtx_xy.set_index(keys=[code_clmn, month_clmn], drop=True, inplace=True)
#         rename_base = {pjmp_code_clmn: pj_code_list[kk],
#                        pjmp_description_clmn: pj_description_list[kk]}
#         mtx_xy = mtx_xy.rename(columns=rename_base, inplace=False)
#         mtx_xy.drop(delete_list, axis=1, inplace=True)
#         mtx_xy[pj_gen_value_clmn] = mtx_xy[pj_gen_value_clmn] - mtx_xy[pj_value_list[kk]]
#
#     return mtx_xy
#
#
# def calculate_project(savings, volume, pcent, cnst, start_mth, month, cnst_per, vol_per):
#
#     if convert_to_numeric(start_mth) > convert_to_numeric(month):
#         value = 0
#     else:
#         value_cnst = volume/vol_per * cnst/cnst_per
#         value_pcent = pcent * savings
#
#         value_cnst = 0 if np.isnan(value_cnst) else value_cnst
#         value_pcent = 0 if np.isnan(value_pcent) else value_pcent
#
#         value = value_cnst + value_pcent
#
#     return value
#
#
# def remove_project_duplicates(df_pj, code_column):
#     df_clean_pj = remove_key_duplicates(df_pj, code_column)
#
#     [missing_codes, are_lists_equal] = list_differential(df_pj.index, df_clean_pj.index)
#     df_remainder_pj =df_pj.filter(items=missing_codes, axis=0)
#
#     return [df_clean_pj, df_remainder_pj]
#
#
# def create_project_mtx_xy(df_pj, df_cy, pj_desired_clmn_list, proj_str_description_lt, proj_str_value_lt,
#                              proj_str_code_lt, pj_code_clmn, pj_value_clmn, new_str_clmn_list, uom_ref_currency_clmn):
#     pj_code = new_str_clmn_list[0]
#     pj_description = new_str_clmn_list[1]
#     pj_value = new_str_clmn_list[2]
#
#     df_pj.reset_index(inplace=True)
#     df_pj = df_pj[pj_desired_clmn_list]
#
#     df_cy = df_cy.reset_index(inplace=False)
#     df_cy = df_cy[proj_str_description_lt + proj_str_value_lt + proj_str_code_lt + [uom_ref_currency_clmn]]
#
#     cy_len = int(df_cy.shape[1]/3)
#     short_clmn_list = [proj_str_code_lt[0], proj_str_description_lt[0], proj_str_value_lt[0], uom_ref_currency_clmn]
#     new_cy = df_cy[short_clmn_list]
#     new_cy = new_cy.rename(columns={proj_str_code_lt[0]: pj_code,
#                                     proj_str_description_lt[0]: pj_description,
#                                     proj_str_value_lt[0]:  pj_value}, inplace=False)
#
#     for kk in range(1, cy_len):
#         short_clmn_list = [proj_str_code_lt[kk], proj_str_description_lt[kk], proj_str_value_lt[kk],
#                            uom_ref_currency_clmn]
#         add_cy = df_cy[short_clmn_list]
#         add_cy = add_cy.rename(columns={proj_str_code_lt[kk]: pj_code,
#                                         proj_str_description_lt[kk]: pj_description,
#                                         proj_str_value_lt[kk]:  pj_value}, inplace=False)
#         new_cy = new_cy.append(add_cy)
#
#     new_cy = pd.pivot_table(new_cy, values=pj_value, index=[pj_code, pj_description], aggfunc=np.sum)
#     new_cy.reset_index(inplace=True)
#
#     df_pj = df_pj.drop_duplicates(pj_code_clmn)
#
#     df_pj = new_cy.merge(df_pj, how='left', left_on=pj_code, right_on=pj_code_clmn)
#     df_pj.set_index(keys=pj_code, drop=True, inplace=True)
#
#     return df_pj
#
#
# def add_project_to_clmn_list(clmn_list, pj_str_code_lt, pj_str_description_lt, pj_str_value_lt, pj_layer):
#
#     for kk in range(0, pj_layer+1):
#         clmn_list.append(pj_str_code_lt[kk])
#         clmn_list.append(pj_str_description_lt[kk])
#         clmn_list.append(pj_str_value_lt[kk])
#
#     return clmn_list
#
#
# def save_excel(filename, df_cy, df_pj, sheetname_cy, sheetname_pj, color_list, cy_color_index_for_clmns, cy_color_order,
#                pj_color_index_for_clmns, pj_color_order):
#
#     # Create a Pandas Excel writer using XlsxWriter as the engine.
#     index_qty_cy = len(df_cy.index.names)
#     index_qty_pj = len(df_pj.index.names)
#
#     cy_color_index_for_clmns.append(index_qty_cy)
#     cy_color_index_for_clmns.sort()
#
#     pj_color_index_for_clmns.append(index_qty_pj)
#     pj_color_index_for_clmns.sort()
#
#     writer = pd.ExcelWriter(filename, engine='xlsxwriter')
#
#     # Convert the mtx_xy to an XlsxWriter Excel object.
#     df_cy.to_excel(writer, sheet_name=sheetname_cy, float_format="%.4f", startrow=1, startcol=0, merge_cells=False,
#                    freeze_panes={1, 2}, header=False)
#     df_pj.to_excel(writer, sheet_name=sheetname_pj, float_format="%.4f", startrow=1, startcol=0, merge_cells=False,
#                    header=False)
#
#     # Get the xlsxwriter workbook and worksheet objects.
#     workbook = writer.book
#     worksheet_cy = writer.sheets[sheetname_cy]
#     worksheet_pj = writer.sheets[sheetname_pj]
#
#     # first line in bold
#     header_format = workbook.add_format({'align': 'center',
#                                          'border': 1,
#                                          'valign': 'vcenter',
#                                          'bold': True,
#                                          'text_wrap': True})
#
#     # Write the column headers with the defined format.
#
#     for col_num, value in enumerate(df_cy.columns.values):
#         worksheet_cy.write(0, col_num + index_qty_cy, value, header_format)
#
#     for col_num, value in enumerate(df_pj.columns.values):
#         worksheet_pj.write(0, col_num + index_qty_pj, value, header_format)
#
#
#     index_format = workbook.add_format({'align': 'center',
#                                         'text_wrap': True,
#                                         'border': 1,
#                                         'valign': 'middle',
#                                         'num_format': '#,##0.00'})
#     worksheet_cy.set_column(0, index_qty_cy-1, 10, index_format)
#     worksheet_pj.set_column(0, index_qty_pj - 1, 10, index_format)
#
#     color0_format = workbook.add_format({'align': 'center',
#                                          'text_wrap': True,
#                                          'border': 1,
#                                          'valign': 'middle',
#                                          'bg_color': color_list[0],
#                                          'num_format': '#,##0.00000'})
#
#     color1_format = workbook.add_format({'align': 'center',
#                                          'text_wrap': True,
#                                          'border': 1,
#                                          'valign': 'middle',
#                                          'bg_color': color_list[1],
#                                          'num_format': '#,##0.00000'})
#
#     color2_format = workbook.add_format({'align': 'center',
#                                          'text_wrap': True,
#                                          'border': 1,
#                                          'valign': 'middle',
#                                          'bg_color': color_list[2],
#                                          'num_format': '#,##0.00000'})
#
#     color3_format = workbook.add_format({'align': 'center',
#                                          'text_wrap': True,
#                                          'border': 1,
#                                          'valign': 'middle',
#                                          'bg_color': color_list[3],
#                                          'num_format': '#,##0.00000'})
#
#     color4_format = workbook.add_format({'align': 'center',
#                                          'text_wrap': True,
#                                          'border': 1,
#                                          'valign': 'middle',
#                                          'bg_color': color_list[4],
#                                          'num_format': '#,##0.00000'})
#
#     format_list = [color0_format, color1_format, color2_format, color3_format, color4_format]
#
#     cy_index_clmn = len(cy_color_index_for_clmns)
#     for kk in range(1, cy_index_clmn):
#         worksheet_cy.set_column(cy_color_index_for_clmns[kk-1], cy_color_index_for_clmns[kk]-1, 25,
#                                 format_list[cy_color_order[kk-1]])
#
#     pj_index_clmn = len(pj_color_index_for_clmns)
#     for kk in range(1, pj_index_clmn):
#         worksheet_pj.set_column(pj_color_index_for_clmns[kk - 1], pj_color_index_for_clmns[kk] - 1, 25,
#                                 format_list[pj_color_order[kk - 1]])
#
#     writer.save()
#
#     ret