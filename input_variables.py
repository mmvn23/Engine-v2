from clmn_names import *

output_folder_name_mtx = 'outputs'
input_folder_name = 'inputs'
main_input_file = 'System inputs'
main_input_format = '.xlsx'
main_output_format = '.csv'

enabled_to_all_pn = 'All'
beam_dist_uom = 'Proof-gallon'
beam_grain_usage_uom = 'Dist. Bushel'

makers_location = "Maker's Mark"
makers_code = 'MM'
makers_msh_description = 'MM'
makers_dist_uom = beam_dist_uom
makers_grain_usage_uom = beam_grain_usage_uom

mtx_error_name = 'MTX error'

mtx_nomenclature_setup_dict = {any_raw_dataset_name_dict_element: 'Raw nomenclature',
                               any_datamatrix_name_dict_element: 'MTX nomenclature',
                               input_file_name_dict_element: main_input_file,
                               input_sheet_name_dict_element: 'Nomenclature',
                               desired_input_clmns_dict_element: ['From', 'To'],
                               desired_clmns_at_std_dict_element: [original_term_clmn, standard_term_clmn],
                               key_codes_dict_element: [original_term_clmn],
                               clmn_types_dict_element: {original_term_clmn: str,
                                                         standard_term_clmn: str},
                               nomenclature_clmns_dict_element: []}
mtx_conversion_setup_dict = {any_raw_dataset_name_dict_element: 'Raw conversion',
                             any_datamatrix_name_dict_element: 'MTX conversion',
                             input_file_name_dict_element: main_input_file,
                             input_sheet_name_dict_element: 'Conversion',
                             desired_input_clmns_dict_element: ['PN', 'From', 'To', 'Multiplier'],
                             desired_clmns_at_std_dict_element: [pn_code_clmn, old_uom_clmn, new_uom_clmn,
                                                                 multiplier_clmn],
                             key_codes_dict_element: [pn_code_clmn],
                             clmn_types_dict_element: {pn_code_clmn: str,
                                                       old_uom_clmn: str,
                                                       new_uom_clmn: str,
                                                       multiplier_clmn: float},
                             nomenclature_clmns_dict_element: [old_uom_clmn, new_uom_clmn]}
mtx_part_number_setup_dict = {any_raw_dataset_name_dict_element: 'Raw part_number',
                              any_datamatrix_name_dict_element: 'MTX part_number',
                              input_file_name_dict_element: main_input_file,
                              input_sheet_name_dict_element: 'Part-Number List',
                              desired_input_clmns_dict_element: ['Part Number Code', 'Part Number Description', 
                                                                 'Category', 'Preferred UoM', 'SI UoM'],
                              desired_clmns_at_std_dict_element: [pn_code_clmn, pn_description_clmn, category_l0_clmn,
                                                                  uom_output_clmn, uom_si_clmn],
                              key_codes_dict_element: [pn_code_clmn],
                              clmn_types_dict_element: {pn_code_clmn: str,
                                                        pn_description_clmn: str,
                                                        category_l0_clmn: str,
                                                        uom_output_clmn: str,
                                                        uom_si_clmn: str},
                              nomenclature_clmns_dict_element: [category_l0_clmn, uom_output_clmn, uom_si_clmn]}
mtx_vendor_setup_dict = {any_raw_dataset_name_dict_element: 'Raw vendor',
                         any_datamatrix_name_dict_element: 'MTX vendor',
                         input_file_name_dict_element: main_input_file,
                         input_sheet_name_dict_element: 'Vendor List',
                         desired_input_clmns_dict_element: ['Vendor Code', 'Vendor Description'],
                         desired_clmns_at_std_dict_element: [vendor_code_clmn, vendor_description_clmn],
                         key_codes_dict_element: [vendor_code_clmn],
                         clmn_types_dict_element: {vendor_code_clmn: str,
                                                   vendor_description_clmn: str},
                         nomenclature_clmns_dict_element: []}
mtx_mash_setup_dict = {any_raw_dataset_name_dict_element: 'Raw mash',
                       any_datamatrix_name_dict_element: 'MTX mash',
                       input_file_name_dict_element: main_input_file,
                       input_sheet_name_dict_element: 'Mash List',
                       desired_input_clmns_dict_element: ['Mash code', 'Mash Description',
                                                          'Output liquid preferred UoM', 'Output liquid SI UoM'],
                       desired_clmns_at_std_dict_element: [msh_code_clmn, msh_description_clmn, uom_output_clmn,
                                                           uom_si_clmn],
                       key_codes_dict_element: [msh_code_clmn],
                       clmn_types_dict_element: {msh_code_clmn: str,
                                                 msh_description_clmn: str,
                                                 uom_output_clmn: str,
                                                 uom_si_clmn: str},
                       nomenclature_clmns_dict_element: [uom_output_clmn, uom_si_clmn]}
mtx_mash_grain_setup_dict = {any_raw_dataset_name_dict_element: 'Raw mash grain',
                       any_datamatrix_name_dict_element: 'MTX mash grain',
                       input_file_name_dict_element: main_input_file,
                       input_sheet_name_dict_element: 'Mash List',
                       desired_input_clmns_dict_element: ['Mash code', 'Mash Description',
                                                          'Grain preferred UoM', 'Grain SI UoM'],
                       desired_clmns_at_std_dict_element: [msh_code_clmn, msh_description_clmn, uom_output_clmn,
                                                           uom_si_clmn],
                       key_codes_dict_element: [msh_code_clmn],
                       clmn_types_dict_element: {msh_code_clmn: str,
                                                 msh_description_clmn: str,
                                                 uom_output_clmn: str,
                                                 uom_si_clmn: str},
                       nomenclature_clmns_dict_element: [uom_output_clmn, uom_si_clmn]}
mtx_ppv_historical_volume_setup_dict = {any_raw_dataset_name_dict_element: 'Raw PPV historical volume',
                                        any_datamatrix_name_dict_element: 'MTX PPV historical volume',
                                        input_file_name_dict_element: 'zfi302',
                                        input_sheet_name_dict_element: '(3) YTD',
                                        desired_input_clmns_dict_element: ['Document number', 'Purchasing doc.', 
                                                                           'Material number', 'Plant', 'Period', 
                                                                           'Material Group descr', 'Vendor number', 
                                                                           '(FI) Quantity', '(FI) Base unit'],
                                        desired_clmns_at_std_dict_element: [invoice_code_clmn, po_code_clmn,
                                                                            pn_code_clmn,
                                                                            location_l0_clmn, month_clmn,
                                                                            material_group_code_clmn, vendor_code_clmn,
                                                                            volume_uom_input_clmn, uom_input_clmn],
                                        key_codes_dict_element: [invoice_code_clmn, po_code_clmn, pn_code_clmn],
                                        input_skiprows_dict_element: 2,
                                        clmn_types_dict_element: {invoice_code_clmn: str,
                                                                  po_code_clmn: str,
                                                                  pn_code_clmn: str,
                                                                  location_l0_clmn: str,
                                                                  month_clmn: int,
                                                                  material_group_code_clmn: str,
                                                                  vendor_code_clmn: str,
                                                                  volume_uom_input_clmn: float,
                                                                  uom_input_clmn: str},
                                        nomenclature_clmns_dict_element: [location_l0_clmn, uom_input_clmn],
                                        clmn_uom_conversion_dict_element: {volume_uom_input_clmn:
                                                                           [volume_uom_si_clmn, uom_input_clmn,
                                                                            uom_si_clmn]}}
raw_beam_distillation_schedule_setup_dict = {any_raw_dataset_name_dict_element:
                                                 'Raw Beam distillation schedule',
                                             input_file_name_dict_element: 'Beam 2021 Budget Distillation_2020-7-17',
                                             input_sheet_name_dict_element: 'Raw Materials',
                                             desired_input_clmns_dict_element: ['Location', 'Month', 'Description',
                                                                                'DMmash', 'OPGs'],
                                             desired_clmns_at_std_dict_element: [location_l0_clmn, month_clmn,
                                                                                 msh_description_clmn, msh_code_clmn,
                                                                                 volume_uom_input_clmn],
                                             key_codes_dict_element: [msh_code_clmn],
                                             input_skiprows_dict_element: 2,
                                             clmn_types_dict_element: {location_l0_clmn: str,
                                                                       month_clmn: str, # it will be converted to int later
                                                                       msh_description_clmn: str,
                                                                       msh_code_clmn: str,
                                                                       volume_uom_input_clmn: float}}
raw_makers_distillation_schedule_setup_dict = {any_raw_dataset_name_dict_element: "Raw Maker' distillation schedule",
                                               input_file_name_dict_element:
                                                   "Maker's Estimated Distillation 2017_2020 5.10.19",
                                               input_sheet_name_dict_element: '2021 estimate',
                                               desired_input_clmns_dict_element: ['MONTH', 'OPGS'],
                                               desired_clmns_at_std_dict_element: [month_clmn, volume_uom_input_clmn],
                                               key_codes_dict_element: [month_clmn],
                                               input_skiprows_dict_element: 4,
                                               clmn_types_dict_element: {month_clmn: str, # it will be converted to int later
                                                                         volume_uom_input_clmn: float}}
raw_beam_bill_of_materials_setup_dict = {any_raw_dataset_name_dict_element: 'Beam Bill of Materials',
                                         input_file_name_dict_element: 'Beam 2021 Budget Distillation_2020-7-17',
                                         input_sheet_name_dict_element: 'Raw Materials',
                                         desired_input_clmns_dict_element: ['Location', 'Month', 'DMmash', 'Yield'],
                                         desired_clmns_at_std_dict_element: [location_l0_clmn, month_clmn,
                                                                             msh_code_clmn,
                                                                             volume_uom_input_clmn],
                                         key_codes_dict_element: [msh_code_clmn],
                                         input_skiprows_dict_element: 2,
                                         clmn_types_dict_element: {location_l0_clmn: str,
                                                                   month_clmn: str, # it will be converted to int later
                                                                   msh_code_clmn: str,
                                                                   volume_uom_input_clmn: float}}
raw_makers_bill_of_materials_setup_dict = {any_raw_dataset_name_dict_element: "Maker's Beam Bill of Materials",
                                           input_file_name_dict_element:
                                               "Maker's Estimated Distillation 2017_2020 5.10.19",
                                           input_sheet_name_dict_element: '2021 estimate',
                                           desired_input_clmns_dict_element: ['MONTH', 'Yield'],
                                           desired_clmns_at_std_dict_element: [month_clmn, volume_uom_input_clmn],
                                           key_codes_dict_element: [month_clmn],
                                           input_skiprows_dict_element: 4,
                                           clmn_types_dict_element: {month_clmn: str,
                                                                     # it will be converted to int later
                                                                     volume_uom_input_clmn: float}}
mtx_distillation_schedule_setup_dict = {any_datamatrix_name_dict_element: 'MTX Distilling schedule',
                                        desired_clmns_at_std_dict_element: [msh_code_clmn, location_l0_clmn, month_clmn,
                                                                            uom_input_clmn, volume_uom_input_clmn],
                                        key_codes_dict_element: [msh_code_clmn, location_l0_clmn, month_clmn],
                                        clmn_types_dict_element: {msh_code_clmn: str,
                                                                  location_l0_clmn: str,
                                                                  month_clmn: int,
                                                                  volume_uom_input_clmn: float,
                                                                  uom_input_clmn: str},
                                        nomenclature_clmns_dict_element: [location_l0_clmn, month_clmn],
                                        clmn_uom_conversion_dict_element: {volume_uom_input_clmn:
                                                                          [volume_uom_si_clmn, uom_input_clmn,
                                                                          uom_si_clmn]}}
mtx_bill_of_materials_setup_dict = {any_datamatrix_name_dict_element: 'Bill of materials',
                                    desired_clmns_at_std_dict_element: [location_l0_clmn, month_clmn,
                                                                        msh_code_clmn, volume_uom_input_clmn,
                                                                        uom_input_clmn],
                                    key_codes_dict_element: [msh_code_clmn, location_l0_clmn, month_clmn],
                                    clmn_types_dict_element: {msh_code_clmn: str,
                                                              location_l0_clmn: str,
                                                              month_clmn: int,
                                                              volume_uom_input_clmn: float,
                                                              uom_input_clmn: str},
                                    nomenclature_clmns_dict_element: [location_l0_clmn, month_clmn],
                                    clmn_uom_conversion_dict_element: {volume_uom_input_clmn:
                                                                       [volume_uom_si_clmn, uom_input_clmn,
                                                                        uom_si_clmn]}}
