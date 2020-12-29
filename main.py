import pandas as pd
import numpy as np
from functions import *
import time
from clmn_names import *
from input_variables import *
from control_panel import *

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

start_time = time.time()


mtx_error = ErrorDataset(name=mtx_error_name,
                         output_directory=Directory(folder=output_folder_name_mtx, format='.csv',
                         file=mtx_error_name),
                         desired_clmns_at_std=[index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
                                               error_msg_clmn])
# print(mtx_error)

mtx_nomenclature = load_mtx_from_raw(mtx_error=mtx_error, error_msg_clmn=error_msg_clmn,
                                     raw_nomenclature_name=raw_nomenclature_name,
                                     mtx_nomenclature_name=mtx_nomenclature_name,
                                     input_file_name=main_input_file,
                                     input_sheet_name='Nomenclature',
                                     input_format='.xlsx',
                                     input_folder_name=input_folder_name,
                                     desired_clmns_at_std=[original_term_clmn, standard_term_clmn],
                                     key_codes=[original_term_clmn],
                                     clmn_types={original_term_clmn: str,
                                                 standard_term_clmn: str},
                                     output_folder_name=output_folder_name_mtx,
                                     index_clmn=index_clmn,
                                     input_file_clmn=input_file_clmn,
                                     input_sheet_clmn=input_sheet_clmn,
                                     output_report_clmn=output_report_clmn)


# mtx_conversion_desired_input_clmns = ['PN', 'From', 'To', 'Multiplier']
# mtx_conversion = fc.MyDataframe(name='MTX conversion',
#                                 input_folder=input_folder_name,
#                                 input_file=main_input_file,
#                                 input_sheet='Conversion',
#                                 output_folder=output_folder_name_mtx,
#                                 key_code_clmns=[pn_code_clmn],
#                                 desired_input_clmns=mtx_conversion_desired_input_clmns,
#                                 clmn_rename={mtx_conversion_desired_input_clmns[0]: pn_code_clmn,
#                                              mtx_conversion_desired_input_clmns[1]: old_uom_clmn,
#                                              mtx_conversion_desired_input_clmns[2]: new_uom_clmn,
#                                              mtx_conversion_desired_input_clmns[3]: multiplier_clmn},
#                                 clmn_types={pn_code_clmn: str,
#                                             old_uom_clmn: str,
#                                             new_uom_clmn: str,
#                                             multiplier_clmn: float},
#                                 desired_clmns_at_std=[pn_code_clmn, old_uom_clmn, new_uom_clmn, multiplier_clmn])
# mtx_xy_list.append(mtx_conversion)




# name='MTX error',
#                            output_folder=,


# # nomenclature
# input_directory = fc.Directory(folder=input_folder_name, file=main_input_file, format='.xlsx',
#                                sheet='Nomenclature')

# mtx_xy_list = []
#
# mtx_error_desired_input_clmns=[index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn]
# mtx_error = fc.MyDataframe(name='MTX error',
#                            output_folder=output_folder_name_mtx,
#                            desired_input_clmns=mtx_error_desired_input_clmns,
#                            desired_clmns_at_std=mtx_error_desired_input_clmns)
# mtx_xy_list.append(mtx_error)
#
# mtx_nomenclature_desired_input_clmns=['From', 'To']
# mtx_nomenclature = fc.MyDataframe(name='MTX nomenclature',
#                                   input_folder=input_folder_name,
#                                   input_file=main_input_file,
#                                   input_sheet='Nomenclature',
#                                   output_folder=output_folder_name_mtx,
#                                   key_code_clmns=[original_term_clmn],
#                                   desired_input_clmns=mtx_nomenclature_desired_input_clmns,
#                                   clmn_rename={mtx_nomenclature_desired_input_clmns[0]: original_term_clmn,
#                                                mtx_nomenclature_desired_input_clmns[1]: standard_term_clmn},
#                                   clmn_types={original_term_clmn: str,
#                                               standard_term_clmn: str},
#                                   desired_clmns_at_std=[original_term_clmn, standard_term_clmn])
# mtx_xy_list.append(mtx_nomenclature)
#
# mtx_conversion_desired_input_clmns = ['PN', 'From', 'To', 'Multiplier']
# mtx_conversion = fc.MyDataframe(name='MTX conversion',
#                                 input_folder=input_folder_name,
#                                 input_file=main_input_file,
#                                 input_sheet='Conversion',
#                                 output_folder=output_folder_name_mtx,
#                                 key_code_clmns=[pn_code_clmn],
#                                 desired_input_clmns=mtx_conversion_desired_input_clmns,
#                                 clmn_rename={mtx_conversion_desired_input_clmns[0]: pn_code_clmn,
#                                              mtx_conversion_desired_input_clmns[1]: old_uom_clmn,
#                                              mtx_conversion_desired_input_clmns[2]: new_uom_clmn,
#                                              mtx_conversion_desired_input_clmns[3]: multiplier_clmn},
#                                 clmn_types={pn_code_clmn: str,
#                                             old_uom_clmn: str,
#                                             new_uom_clmn: str,
#                                             multiplier_clmn: float},
#                                 desired_clmns_at_std=[pn_code_clmn, old_uom_clmn, new_uom_clmn, multiplier_clmn])
# mtx_xy_list.append(mtx_conversion)
#
# mtx_part_number_desired_input_clmns = ['Part Number Code', 'Part Number Description', 'Category', 'Preferred UoM',
#                                        'SI UoM']
# mtx_part_number = fc.MyDataframe(name='MTX part number',
#                                  input_folder=input_folder_name,
#                                  input_file=main_input_file,
#                                  input_sheet='Part-Number List',
#                                  output_folder=output_folder_name_mtx,
#                                  key_code_clmns=[pn_code_clmn],
#                                  desired_input_clmns=mtx_part_number_desired_input_clmns,
#                                  clmn_rename={mtx_part_number_desired_input_clmns[0]: pn_code_clmn,
#                                               mtx_part_number_desired_input_clmns[1]: pn_description_clmn,
#                                               mtx_part_number_desired_input_clmns[2]: category_l0_clmn,
#                                               mtx_part_number_desired_input_clmns[3]: uom_output_clmn,
#                                               mtx_part_number_desired_input_clmns[4]: uom_si_clmn},
#                                  desired_clmns_at_std=[pn_code_clmn, pn_description_clmn, category_l0_clmn, uom_si_clmn,
#                                                        uom_output_clmn],
#                                  clmn_types={pn_code_clmn: str,
#                                              pn_description_clmn: str,
#                                              category_l0_clmn: str,
#                                              uom_output_clmn: str,
#                                              uom_si_clmn: str},
#                                  nomenclature_clmns=[category_l0_clmn, uom_si_clmn, uom_output_clmn])
# mtx_xy_list.append(mtx_part_number)
#
# mtx_vendor_desired_input_clmns = ['Vendor Code', 'Vendor Description']
# mtx_vendor = fc.MyDataframe(name='MTX vendor',
#                             input_folder=input_folder_name,
#                             input_file=main_input_file,
#                             input_sheet='Vendor List',
#                             output_folder=output_folder_name_mtx,
#                             key_code_clmns=[vendor_code_clmn],
#                             desired_input_clmns=mtx_vendor_desired_input_clmns,
#                             clmn_rename={mtx_vendor_desired_input_clmns[0]: vendor_code_clmn,
#                                          mtx_vendor_desired_input_clmns[1]: vendor_description_clmn},
#                             desired_clmns_at_std=[vendor_code_clmn, vendor_description_clmn],
#                             clmn_types={vendor_code_clmn: str,
#                                         vendor_description_clmn: str})
# mtx_xy_list.append(mtx_vendor)
#
#
# mtx_ppv_historical_volume_desired_input_clmns = ['Document number', 'Purchasing doc.', 'Material number', 'Plant',
#                                               'Period', 'Material Group descr', 'Vendor number', '(FI) Quantity',
#                                               '(FI) Base unit']
# mtx_ppv_historical_volume = fc.MyDataframe(name='MTX PPV historical volumes',
#                                            input_folder=input_folder_name,
#                                            input_file='zfi302.xlsx',
#                                            input_sheet='(3) YTD',
#                                            input_skiprows=2,
#                                            output_folder=output_folder_name_mtx,
#                                            key_code_clmns=[invoice_code_clmn, po_code_clmn, pn_code_clmn],
#                                            desired_input_clmns=mtx_ppv_historical_volume_desired_input_clmns,
#                                            clmn_rename={mtx_ppv_historical_volume_desired_input_clmns[0]:
#                                                         invoice_code_clmn,
#                                                         mtx_ppv_historical_volume_desired_input_clmns[1]:
#                                                         po_code_clmn,
#                                                         mtx_ppv_historical_volume_desired_input_clmns[2]:
#                                                         pn_code_clmn,
#                                                         mtx_ppv_historical_volume_desired_input_clmns[3]:
#                                                         location_l0_clmn,
#                                                         mtx_ppv_historical_volume_desired_input_clmns[4]:
#                                                         month_clmn,
#                                                         mtx_ppv_historical_volume_desired_input_clmns[5]:
#                                                         material_group_code_clmn,
#                                                         mtx_ppv_historical_volume_desired_input_clmns[6]:
#                                                         vendor_code_clmn,
#                                                         mtx_ppv_historical_volume_desired_input_clmns[7]:
#                                                         volume_uom_input_clmn,
#                                                         mtx_ppv_historical_volume_desired_input_clmns[8]:
#                                                             uom_input_clmn},
#                                            desired_clmns_at_std=[invoice_code_clmn, po_code_clmn, pn_code_clmn,
#                                                                  location_l0_clmn, month_clmn,
#                                                                  material_group_code_clmn, vendor_code_clmn,
#                                                                  volume_uom_input_clmn, uom_input_clmn],
#                                            nomenclature_clmns=[location_l0_clmn, uom_input_clmn],
#                                            clmn_types={invoice_code_clmn: str,
#                                                        po_code_clmn: str,
#                                                        pn_code_clmn: str,
#                                                        location_l0_clmn: str,
#                                                        month_clmn: int,
#                                                        material_group_code_clmn: str,
#                                                        vendor_code_clmn: str,
#                                                        volume_uom_input_clmn: float,
#                                                        uom_input_clmn: str},
#                                            clmn_uom_conversion={volume_uom_input_clmn:
#                                                                 [volume_uom_si_clmn, uom_input_clmn, uom_si_clmn]})
# mtx_xy_list.append(mtx_ppv_historical_volume)
#
# raw_beam_distillation_schedule_desired_input_clmns = ['Location', 'Month', 'Description', 'DMmash', 'OPGs', 'Yield']
# raw_beam_distillation_schedule = fc.MyDataframe(name='Raw dataframe: Beam distillation schedule',
#                                                 input_folder=input_folder_name,
#                                                 input_file='Beam 2021 Budget Distillation_2020-7-17.xlsx',
#                                                 input_sheet='Raw Materials',
#                                                 input_skiprows=2,
#                                                 desired_input_clmns=raw_beam_distillation_schedule_desired_input_clmns,
#                                                 key_code_clmns=[msh_code_clmn],
#                                                 clmn_rename={raw_beam_distillation_schedule_desired_input_clmns[0]:
#                                                              location_l0_clmn,
#                                                              raw_beam_distillation_schedule_desired_input_clmns[1]:
#                                                              month_clmn,
#                                                              raw_beam_distillation_schedule_desired_input_clmns[2]:
#                                                              msh_description_clmn,
#                                                              raw_beam_distillation_schedule_desired_input_clmns[3]:
#                                                              msh_code_clmn,
#                                                              raw_beam_distillation_schedule_desired_input_clmns[4]:
#                                                              volume_uom_input_clmn,
#                                                              raw_beam_distillation_schedule_desired_input_clmns[5]:
#                                                              grain_usage_at_input_clmn},
#                                                 desired_clmns_at_std=[location_l0_clmn, month_clmn,
#                                                                       msh_description_clmn, msh_code_clmn,
#                                                                       volume_uom_input_clmn, grain_usage_at_input_clmn],
#                                                 nomenclature_clmns=[location_l0_clmn, month_clmn],
#                                                 clmn_types={location_l0_clmn: str,
#                                                             month_clmn: str, # it will be converted to int later
#                                                             msh_description_clmn: str,
#                                                             msh_code_clmn: str,
#                                                             volume_uom_input_clmn: float,
#                                                             grain_usage_at_input_clmn: float})
#
#
# trash = mtx_error.dataframe_init()
#
# mtx_error = mtx_nomenclature.dataframe_init(mtx_error=mtx_error,
#                                             index_clmn=index_clmn, input_file_clmn=input_file_clmn,
#                                             input_sheet_clmn=input_sheet_clmn,
#                                             output_report_clmn=output_report_clmn,
#                                             error_msg_clmn=error_msg_clmn)
#
# mtx_error = mtx_conversion.dataframe_init(mtx_error=mtx_error,
#                                           index_clmn=index_clmn, input_file_clmn=input_file_clmn,
#                                           input_sheet_clmn=input_sheet_clmn,
#                                           output_report_clmn=output_report_clmn,
#                                           error_msg_clmn=error_msg_clmn)
# mtx_conversion.dataframe.set_index([pn_code_clmn, old_uom_clmn, new_uom_clmn], inplace=True)
#
# mtx_error = mtx_part_number.dataframe_init(mtx_error=mtx_error,
#                                            mtx_nomenclature=mtx_nomenclature,
#                                            index_clmn=index_clmn, input_file_clmn=input_file_clmn,
#                                            input_sheet_clmn=input_sheet_clmn,
#                                            output_report_clmn=output_report_clmn,
#                                            error_msg_clmn=error_msg_clmn,
#                                            original_term_clmn=original_term_clmn)
# mtx_part_number.dataframe.set_index(pn_code_clmn, inplace=True)
#
# mtx_error = mtx_vendor.dataframe_init(mtx_error=mtx_error,
#                                       mtx_nomenclature=mtx_nomenclature,
#                                       index_clmn=index_clmn, input_file_clmn=input_file_clmn,
#                                       input_sheet_clmn=input_sheet_clmn,
#                                       output_report_clmn=output_report_clmn,
#                                       error_msg_clmn=error_msg_clmn,
#                                       original_term_clmn=original_term_clmn)
# mtx_vendor.dataframe.set_index(vendor_code_clmn, inplace=True)
#
# if loading_mtx_ppv_historical_volume_is_enabled:
#     mtx_error = mtx_ppv_historical_volume.dataframe_init(mtx_error=mtx_error,
#                                                          mtx_nomenclature=mtx_nomenclature,
#                                                          mtx_part_number=mtx_part_number,
#                                                          mtx_conversion=mtx_conversion,
#                                                          enabled_to_all_pn=enabled_to_all_pn,
#                                                          pn_code_clmn=pn_code_clmn, uom_si_clmn=uom_si_clmn,
#                                                          old_uom_clmn=old_uom_clmn, new_uom_clmn=new_uom_clmn,
#                                                          multiplier_clmn=multiplier_clmn,
#                                                          index_clmn=index_clmn, input_file_clmn=input_file_clmn,
#                                                          input_sheet_clmn=input_sheet_clmn,
#                                                          output_report_clmn=output_report_clmn,
#                                                          error_msg_clmn=error_msg_clmn,
#                                                          original_term_clmn=original_term_clmn)
#     # mtx_ppv_historical_volume.dataframe.set_index(ppv_historical_volume_code_clmn, inplace=True)
#
# else:
#     mtx_ppv_historical_volume.load_dataframe()
#
# mtx_error = raw_beam_distillation_schedule.dataframe_init(mtx_error=mtx_error,
#                                                           mtx_nomenclature=mtx_nomenclature,
#                                                           pn_code_clmn=pn_code_clmn, uom_si_clmn=uom_si_clmn,
#                                                           index_clmn=index_clmn, input_file_clmn=input_file_clmn,
#                                                           input_sheet_clmn=input_sheet_clmn,
#                                                           output_report_clmn=output_report_clmn,
#                                                           error_msg_clmn=error_msg_clmn,
#                                                           original_term_clmn=original_term_clmn)
#
# raw_beam_distillation_schedule.dataframe[uom_input_clmn] = beam_dist_uom
# print(raw_beam_distillation_schedule.dataframe)
# # load raw_beam to mtx_bom
#
#
# fc.save_mtx_xy_dataframe_list(mtx_xy_list)

print("--- %s seconds ---" % (time.time() - start_time))
