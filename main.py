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

setup_dict_list = [mtx_nomenclature_setup_dict, mtx_conversion_setup_dict, mtx_part_number_setup_dict,
                   mtx_vendor_setup_dict, mtx_mash_setup_dict, mtx_mash_grain_setup_dict]


[mtx_error, mtx_nomenclature, mtx_conversion, mtx_part_number, mtx_vendor, mtx_mash, mtx_mash_grain,
 mtx_ppv_historical_volume, mtx_distillation_schedule] = \
    process_datamatrices(setup_dict_list, mtx_ppv_historical_volume_setup_dict,
                         raw_beam_distillation_schedule_setup_dict, raw_beam_bill_of_materials_setup_dict,
                         raw_makers_distillation_schedule_setup_dict,
                         mtx_distillation_schedule_setup_dict, raw_makers_bill_of_materials_setup_dict,
                         mtx_bill_of_materials_setup_dict,
                         mtx_error,
                         beam_dist_uom, beam_grain_usage_uom,
                         makers_location, makers_code, makers_msh_description, makers_dist_uom, makers_grain_usage_uom,
                         enabled_to_all_pn,
                         any_raw_dataset_name_dict_element,
                         any_datamatrix_name_dict_element,
                         input_file_name_dict_element,
                         input_sheet_name_dict_element,
                         desired_input_clmns_dict_element,
                         desired_clmns_at_std_dict_element,
                         key_codes_dict_element, clmn_types_dict_element,
                         nomenclature_clmns_dict_element,
                         input_skiprows_dict_element,
                         clmn_uom_conversion_dict_element,
                         error_msg_clmn, main_input_format, input_folder_name,
                         output_folder_name_mtx, main_output_format,
                         location_l0_clmn, msh_code_clmn, msh_description_clmn, uom_input_clmn,
                         index_clmn, input_file_clmn, input_sheet_clmn,
                         output_report_clmn, original_term_clmn, pn_code_clmn, uom_si_clmn, old_uom_clmn,
                         new_uom_clmn, multiplier_clmn)




#
#

# mtx_xy_list.append(mtx_ppv_historical_volume)
#
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
