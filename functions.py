import pandas as pd
import numpy as np


# sub_class: ErrorDataset
# sub_class: RegularDataset

# sub_class: RawDataset
# sub_class: DataMatrix
# sub_class: Report

class Directory:
    def __init__(self, folder, file, format, sheet=[], skiprows=0):
        self.folder = folder
        self.file = file
        self.format = format
        self.sheet = sheet
        self.skiprows = skiprows

    def __str__(self):
        out_str = "\n     Folder: {folder}\n"\
                  "     File: {file}\n"\
                  "     Format: {format}\n"\
                  "     Sheet: {sheet}\n"\
                  "     Skiprows: {skiprows}" \
                  .format(folder=self.folder,
                          file=self.file,
                          format=self.format,
                          sheet=self.sheet,
                          skiprows=self.skiprows)

        return out_str


class DatasetManager:
    def __init__(self, name,
                 output_directory, desired_clmns_at_std):
        self.name = name
        self.output_directory = output_directory
        self.desired_clmns_at_std = desired_clmns_at_std
        self.dataframe = pd.DataFrame()

    def __str__(self):
        out_str = "\n\n*******************************\n" \
                  "name: {name} \n" \
                  "Output directory: {output_directory}\n" \
                  "Desired colums at std: {desired_clmns_at_std}\n" \
                  "Dataframe: \n{dataframe}"\
                  .format(name=self.name,
                          output_directory=self.output_directory,
                          desired_clmns_at_std=self.desired_clmns_at_std,
                          dataframe=self.dataframe)

        return out_str

    def filter_columns(self):
        for item_clmn in self.dataframe.columns:
            if item_clmn not in self.desired_clmns_at_std:
                self.dataframe.drop(columns=[item_clmn], inplace=True)
        return


class ErrorDataset(DatasetManager):
    def __init__(self, name, output_directory, desired_clmns_at_std):
        super().__init__(name, output_directory, desired_clmns_at_std)
        self.dataframe = pd.DataFrame(columns=self.desired_clmns_at_std)

    def append_dataframe(self, any_dataset, missing_codes, error_msg,
                         index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn):
        mtx_error_to_append = pd.DataFrame(columns=[index_clmn])
        kk = 0

        for item in list(missing_codes):
            mtx_error_to_append.loc[kk, index_clmn] = item
            kk = kk + 1

        dataset_class = any_dataset.__class__

        if str(dataset_class) == "<class 'functions.RawDataset'>":
            mtx_error_to_append[input_file_clmn] = any_dataset.input_directory.file
            mtx_error_to_append[input_sheet_clmn] = any_dataset.input_directory.sheet
        else:
            mtx_error_to_append[input_file_clmn] = pd.NA
            mtx_error_to_append[input_sheet_clmn] = pd.NA

        mtx_error_to_append[output_report_clmn] = any_dataset.name
        mtx_error_to_append[error_msg_clmn] = error_msg

        self.dataframe = self.dataframe.append(mtx_error_to_append)

        return

    def save(self):
        address = './' + self.output_directory.folder + '/' + self.output_directory.file + self.output_directory.format
        self.dataframe.to_csv(address)
        return


class RegularDataset(DatasetManager):
    def __init__(self, name, output_directory, desired_clmns_at_std, key_codes):
        super().__init__(name, output_directory, desired_clmns_at_std)
        self.key_codes = key_codes

    def __str__(self):
        out_str = "\nKey codes: {key_codes}\n" \
                  .format(key_codes=self.key_codes)

        return super(RegularDataset, self).__str__() + out_str


class RawDataset(RegularDataset):
    def __init__(self, name,  output_directory, desired_clmns_at_std,
                 key_codes, desired_input_clmns, input_directory, clmn_types):
        super().__init__(name, output_directory, desired_clmns_at_std, key_codes)
        self.desired_input_clmns = desired_input_clmns
        self.input_directory = input_directory
        self.clmn_types = clmn_types
        
    def __str__(self):
        out_str = "\nDesired input columns: {desired_input_clmns}\n" \
                  "Input directory: {input_directory}\n" \
                  "Clmn types: {clmn_types}\n" \
                  .format(desired_input_clmns=self.desired_input_clmns,
                          input_directory=self.input_directory,
                          clmn_types=self.clmn_types)

        return super(RawDataset, self).__str__() + out_str

    def load(self):
        address = './' + self.input_directory.folder + '/' + self.input_directory.file + self.input_directory.format
        self.dataframe = pd.read_excel(address, sheet_name=self.input_directory.sheet,
                                       skiprows=self.input_directory.skiprows)
        self.dataframe = self.dataframe[self.desired_input_clmns]
        return

    def init_dataframe(self, mtx_error, index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
                       error_msg_clmn):
        self.load()
        self.cleanse(mtx_error, index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn)

        return mtx_error

    def cleanse(self, mtx_error, index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn):
        error_msg_nan = 'CLEANSE: NaN on original file'
        clmn_rename = dict(zip(self.desired_input_clmns, self.desired_clmns_at_std))
        self.dataframe.rename(columns=clmn_rename, inplace=True)
        self.dataframe = self.dataframe[self.desired_clmns_at_std]
        # include key code_clmns in class
        self.dataframe.dropna(inplace=True, axis=0, subset=self.key_codes)
        self.assure_type_input()
        missing_codes = []

        for item in self.key_codes:
            [self.dataframe, missing_codes_to_append, are_lists_equal] = clean_nan(self.dataframe, item)
            missing_codes.append(missing_codes_to_append)

        mtx_error.append_dataframe(self, missing_codes,
                                   error_msg_nan,
                                   index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn)
        return mtx_error

    def assure_type_input(self):

        for key, value in self.clmn_types.items():
            self.dataframe[key].astype(value)

        return


class DataMatrix(RegularDataset):
    def __init__(self, name, output_directory, desired_clmns_at_std, raw_dataset_list, key_codes,
                 clmn_uom_conversion=[], nomenclature_clmns=[]):
        super().__init__(name, output_directory, desired_clmns_at_std, key_codes)
        self.clmn_uom_conversion = clmn_uom_conversion
        self.raw_dataset_list = raw_dataset_list
        self.nomenclature_clmns = nomenclature_clmns
        
    def __str__(self):
        out_str = "\nClmns for UoM conversion: {clmn_uom_conversion}\n" \
                  "Nomenclature clmns: {nomenclature_clmns}\n" \
                  .format(clmn_uom_conversion=self.clmn_uom_conversion,
                          nomenclature_clmns=self.nomenclature_clmns)

        return super(DataMatrix, self).__str__() + out_str

    def load(self):
        address = './' + self.output_directory.folder + '/' + self.output_directory.file + self.output_directory.format
        self.dataframe = pd.read_csv(address)
        return

    def save(self):
        address = './' + self.output_directory.folder + '/' + self.output_directory.file + self.output_directory.format
        self.dataframe.to_csv(address)
        return

    def init_dataframe(self):
        self.dataframe = pd.DataFrame(columns=self.desired_clmns_at_std)

        for item in self.raw_dataset_list:
            self.dataframe = self.dataframe.append(item.dataframe)

        self.dataframe.set_index(self.key_codes, inplace=True)

        return
   
    def apply_nomenclature(self, mtx_error, mtx_nomenclature,
                           original_term_clmn,
                           index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn):
        
        error_msg_nomenclature = 'Nomenclature not found'
        item_key_code = self.key_codes[0]

        self.dataframe.reset_index(inplace=True)
        df_nomenclature = mtx_nomenclature.dataframe.reset_index(inplace=False)

        for item_nomenclature in self.nomenclature_clmns:
            self.dataframe = merge_and_drop(self.dataframe, df_nomenclature, item_nomenclature,
                                            original_term_clmn, item_nomenclature, item_key_code)

        [self.dataframe, missing_codes, are_lists_equal] = clean_nan(self.dataframe, item_key_code)
        self.dataframe.set_index(self.key_codes, inplace=True)

        any_datamatrix = self

        mtx_error.append_dataframe(any_datamatrix, missing_codes,
                                   error_msg_nomenclature,
                                   index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
                                   error_msg_clmn)
        
        return mtx_error

    def convert_volume_to_si_uom(self, mtx_error, mtx_conversion, mtx_key_code,
                                 enabled_to_all_pn, key_code_clmn,
                                 pn_code_clmn, uom_si_clmn, old_uom_clmn, new_uom_clmn, multiplier_clmn,
                                 index_clmn, input_sheet_clmn, input_file_clmn, output_report_clmn, error_msg_clmn):
        # clmn_uom_conversion = {pd.NA: [pd.NA, pd.NA, pd.NA]}):
        # # clmn_uom_conversion -> {dict_key: [L0, L1, L2]}
        # # dict_key -> clmn name with float at input UoM (to be converted)
        # # L0 -> clmn name with float at SI UoM
        # # L1 -> clmn name of input UoM
        # # L2  -> clmn name of standard UoM
        # add columns: standard UoM, value at standard UoM OK
        # access mtx_key_code to get standard UoM OK
        # add column: multiplier OK
        # find multiplier OK
        # apply multiplier to value at standard UoM OK
        # drop multiplier OK
        # clear NaN
        # update mtx_error
        error_msg_convert_volume = 'Volume UoM conversion'

        self.include_standard_clmn(mtx_key_code, key_code_clmn, pn_code_clmn, uom_si_clmn)

        self.calculate_volume_at_si(mtx_conversion, enabled_to_all_pn,
                                    key_code_clmn, pn_code_clmn, old_uom_clmn, new_uom_clmn, multiplier_clmn)

        self.dataframe.reset_index(inplace=True)
        [self.dataframe, missing_codes, are_lists_equal] = clean_nan(self.dataframe, key_code_clmn)
        self.dataframe.set_index(self.key_codes, inplace=True)
        any_datamatrix = self

        mtx_error.append_dataframe(any_datamatrix, missing_codes,
                                   error_msg_convert_volume,
                                   index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
                                   error_msg_clmn)

        return mtx_error

    def include_standard_clmn(self, mtx_key_code, key_code_clmn, pn_code_clmn, uom_si_clmn):

        mtx_uom_si = mtx_key_code.dataframe.reset_index()
        mtx_uom_si = mtx_uom_si[[key_code_clmn, uom_si_clmn]]
        self.dataframe.reset_index(inplace=True)

        self.dataframe = merge_and_rename(self.dataframe, mtx_uom_si, key_code_clmn, key_code_clmn, uom_si_clmn,
                                          key_code_clmn)
        self.dataframe.set_index(self.key_codes, inplace=True)

        return

    def calculate_volume_at_si(self, mtx_conversion, enabled_to_all_pn,
                               key_code_clmn, pn_code_clmn, old_uom_clmn, new_uom_clmn, multiplier_clmn):

        old_value_clmn = list(self.clmn_uom_conversion.keys())[0]
        value_list = list(self.clmn_uom_conversion.values())[0]
        new_value_clmn = value_list[0]
        input_uom_clmn = value_list[1]
        si_uom_clmn = value_list[2]

        df_conversion = mtx_conversion.dataframe.reset_index()
        self.dataframe.reset_index(inplace=True)

        self.dataframe[new_value_clmn] = self.dataframe.apply(lambda row: row[old_value_clmn] * get_multiplier(
                                                                               df_conversion=df_conversion,
                                                                               pn_code=row[key_code_clmn],
                                                                               old_uom=row[input_uom_clmn],
                                                                               new_uom=row[si_uom_clmn],
                                                                               pn_code_clmn=pn_code_clmn,
                                                                               enabled_to_all_pn=enabled_to_all_pn,
                                                                               old_uom_clmn=old_uom_clmn,
                                                                               new_uom_clmn=new_uom_clmn,
                                                                               multiplier_clmn=multiplier_clmn), axis=1)
        self.dataframe.set_index(self.key_codes, inplace=True)
        self.dataframe.drop(columns=[old_value_clmn, input_uom_clmn], axis=1, inplace=True)

        return


def clean_nan(dataframe, code_clmn, clm_list='empty'):

    if clm_list == 'empty':
        clm_list = dataframe.columns

    old_part_number_bgt_list = dataframe[code_clmn]
    old_part_number_bgt_list = [str(item) for item in old_part_number_bgt_list]

    dataframe = dataframe.dropna(inplace=False, subset=clm_list)

    new_part_number_bgt_list = dataframe[code_clmn]
    new_part_number_bgt_list = [str(item) for item in new_part_number_bgt_list]

    [missing_codes, are_lists_equal] = list_differential(old_part_number_bgt_list, new_part_number_bgt_list)

    return [dataframe, missing_codes, are_lists_equal]


def list_differential(old_list, new_list):
    item_diff = []
    are_list_equal = True

    for old_item in old_list:

        if old_item not in new_list:
            item_diff.append(old_item)
            are_list_equal = False

    return [item_diff, are_list_equal]


def load_mtx_from_raw_single(mtx_error, error_msg_clmn,
                             any_raw_dataset_name, any_datamatrix_name,
                             input_file_name, input_sheet_name, input_format,
                             input_folder_name,
                             desired_input_clmns, desired_clmns_at_std, key_codes, clmn_types,
                             nomenclature_clmns,
                             output_folder_name, main_output_format,
                             index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn):

    any_raw_dataset = RawDataset(name=any_raw_dataset_name,
                                 input_directory=Directory(folder=input_folder_name, file=input_file_name,
                                                           format=input_format,
                                                           sheet=input_sheet_name),
                                 output_directory=Directory(folder=output_folder_name, format=main_output_format,
                                                            file=any_raw_dataset_name),
                                 desired_input_clmns=desired_input_clmns,
                                 desired_clmns_at_std=desired_clmns_at_std,
                                 key_codes=key_codes,
                                 clmn_types=clmn_types)

    mtx_error = any_raw_dataset.init_dataframe(mtx_error, index_clmn, input_file_clmn, input_sheet_clmn,
                                               output_report_clmn,
                                               error_msg_clmn)

    any_datamatrix = DataMatrix(name=any_datamatrix_name,
                                output_directory=Directory(folder=output_folder_name, format=main_output_format,
                                                           file=any_datamatrix_name),
                                desired_clmns_at_std=desired_clmns_at_std,
                                key_codes=key_codes,
                                raw_dataset_list=[any_raw_dataset],
                                nomenclature_clmns=nomenclature_clmns)

    any_datamatrix.init_dataframe()

    return [any_datamatrix, mtx_error]


def load_mtx_from_raw_from_list(setup_dict_list,
                                mtx_error,
                                any_raw_dataset_name_dict_element,
                                any_datamatrix_name_dict_element,
                                input_file_name_dict_element, input_sheet_name_dict_element,
                                desired_input_clmns_dict_element,
                                desired_clmns_at_std_dict_element, key_codes_dict_element, clmn_types_dict_element,
                                nomenclature_clmns_dict_element,
                                error_msg_clmn, main_input_format, input_folder_name, output_folder_name_mtx,
                                main_output_format,
                                index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn):
    any_datamatrix_list = list()

    for item_setup_dict in setup_dict_list:

        [any_datamatrix, mtx_error] = load_mtx_from_raw_single(
            any_raw_dataset_name=item_setup_dict[any_raw_dataset_name_dict_element],
            any_datamatrix_name=item_setup_dict[any_datamatrix_name_dict_element],
            input_file_name=item_setup_dict[input_file_name_dict_element],
            input_sheet_name=item_setup_dict[input_sheet_name_dict_element],
            desired_input_clmns=item_setup_dict[desired_input_clmns_dict_element],
            desired_clmns_at_std=item_setup_dict[desired_clmns_at_std_dict_element],
            key_codes=item_setup_dict[key_codes_dict_element],
            clmn_types=item_setup_dict[clmn_types_dict_element],
            nomenclature_clmns=item_setup_dict[nomenclature_clmns_dict_element],
            mtx_error=mtx_error,
            error_msg_clmn=error_msg_clmn,
            input_format=main_input_format,
            input_folder_name=input_folder_name,
            output_folder_name=output_folder_name_mtx,
            main_output_format=main_output_format,
            index_clmn=index_clmn,
            input_file_clmn=input_file_clmn,
            input_sheet_clmn=input_sheet_clmn,
            output_report_clmn=output_report_clmn)
        any_datamatrix_list.append(any_datamatrix)

    return [any_datamatrix_list, mtx_error]


def save_datamatrices(datamatrix_list):
    for item in datamatrix_list:
        item.save()

    return


def apply_nomenclature_datamatrices(datamatrix_list, mtx_error, mtx_nomenclature,
                                original_term_clmn,
                                index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn):

    for item in datamatrix_list:
        if len(item.nomenclature_clmns) > 0:
            item.apply_nomenclature(mtx_error, mtx_nomenclature,
                                    original_term_clmn,
                                    index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn)

    return


def process_datamatrices(setup_dict_list, mtx_ppv_historical_volume_setup_dict, 
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
                         input_file_name_dict_element, input_sheet_name_dict_element,
                         desired_input_clmns_dict_element,
                         desired_clmns_at_std_dict_element, key_codes_dict_element, clmn_types_dict_element,
                         nomenclature_clmns_dict_element, input_skiprows_dict_element,
                         clmn_uom_conversion_dict_element,
                         error_msg_clmn, main_input_format, input_folder_name, output_folder_name_mtx,
                         main_output_format,
                         location_l0_clmn, msh_code_clmn, msh_description_clmn, uom_input_clmn,
                         index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
                         original_term_clmn, pn_code_clmn, uom_si_clmn, old_uom_clmn,
                         new_uom_clmn, multiplier_clmn):

    [datamatrix_list, mtx_error] = load_mtx_from_raw_from_list(setup_dict_list,
                                                               mtx_error,
                                                               any_raw_dataset_name_dict_element,
                                                               any_datamatrix_name_dict_element,
                                                               input_file_name_dict_element,
                                                               input_sheet_name_dict_element,
                                                               desired_input_clmns_dict_element,
                                                               desired_clmns_at_std_dict_element,
                                                               key_codes_dict_element, clmn_types_dict_element,
                                                               nomenclature_clmns_dict_element,
                                                               error_msg_clmn, main_input_format, input_folder_name,
                                                               output_folder_name_mtx, main_output_format,
                                                               index_clmn, input_file_clmn, input_sheet_clmn,
                                                               output_report_clmn)
    mtx_nomenclature = datamatrix_list[0]
    mtx_conversion = datamatrix_list[1]
    mtx_part_number = datamatrix_list[2]
    mtx_vendor = datamatrix_list[3]
    mtx_mash = datamatrix_list[4]
    mtx_mash_grain = datamatrix_list[5]
    apply_nomenclature_datamatrices(datamatrix_list, mtx_error, mtx_nomenclature,
                                    original_term_clmn,
                                    index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn)

    [mtx_ppv_historical_volume, mtx_error] = init_mtx_ppv_historical(mtx_ppv_historical_volume_setup_dict,
                                                                     mtx_error, mtx_nomenclature,
                                                                     mtx_conversion, mtx_part_number,
                                                                     enabled_to_all_pn,
                                                                     any_raw_dataset_name_dict_element,
                                                                     any_datamatrix_name_dict_element,
                                                                     input_file_name_dict_element,
                                                                     input_sheet_name_dict_element,
                                                                     desired_input_clmns_dict_element,
                                                                     desired_clmns_at_std_dict_element,
                                                                     key_codes_dict_element,
                                                                     clmn_types_dict_element,
                                                                     nomenclature_clmns_dict_element,
                                                                     input_skiprows_dict_element,
                                                                     clmn_uom_conversion_dict_element,
                                                                     error_msg_clmn, main_input_format,
                                                                     input_folder_name, output_folder_name_mtx,
                                                                     main_output_format,
                                                                     index_clmn, input_file_clmn, input_sheet_clmn,
                                                                     output_report_clmn, original_term_clmn,
                                                                     msh_code_clmn, pn_code_clmn, uom_si_clmn,
                                                                     old_uom_clmn, new_uom_clmn, multiplier_clmn)
    datamatrix_list.append(mtx_ppv_historical_volume)

    [mtx_distillation_schedule, mtx_error] = init_mtx_distillation_schedule(raw_beam_distillation_schedule_setup_dict,
                                                                            raw_beam_bill_of_materials_setup_dict,
                                                                            raw_makers_distillation_schedule_setup_dict,
                                                                            mtx_distillation_schedule_setup_dict,
                                                                            mtx_error, mtx_nomenclature,
                                                                            mtx_conversion, mtx_mash,
                                                                            beam_dist_uom, beam_grain_usage_uom,
                                                                            makers_location, makers_code,
                                                                            makers_msh_description, makers_dist_uom,
                                                                            makers_grain_usage_uom,
                                                                            enabled_to_all_pn,
                                                                            any_raw_dataset_name_dict_element,
                                                                            input_file_name_dict_element,
                                                                            input_sheet_name_dict_element,
                                                                            desired_input_clmns_dict_element,
                                                                            desired_clmns_at_std_dict_element,
                                                                            key_codes_dict_element,
                                                                            clmn_types_dict_element,
                                                                            input_skiprows_dict_element,
                                                                            any_datamatrix_name_dict_element,
                                                                            nomenclature_clmns_dict_element,
                                                                            clmn_uom_conversion_dict_element,
                                                                            error_msg_clmn, main_input_format,
                                                                            input_folder_name,
                                                                            output_folder_name_mtx, main_output_format,
                                                                            location_l0_clmn, msh_code_clmn,
                                                                            msh_description_clmn, uom_input_clmn,
                                                                            index_clmn, input_file_clmn,
                                                                            input_sheet_clmn,
                                                                            output_report_clmn, original_term_clmn,
                                                                            pn_code_clmn, uom_si_clmn, old_uom_clmn,
                                                                            new_uom_clmn, multiplier_clmn)
    datamatrix_list.append(mtx_distillation_schedule)

    [mtx_bill_of_materials, mtx_error] = init_mtx_bill_of_materials(raw_beam_bill_of_materials_setup_dict,
                                                                    raw_makers_bill_of_materials_setup_dict,
                                                                    mtx_bill_of_materials_setup_dict,
                               mtx_error, mtx_nomenclature, mtx_conversion, mtx_mash_grain,
                               beam_dist_uom, beam_grain_usage_uom,
                               makers_location, makers_code, makers_msh_description, makers_dist_uom,
                               makers_grain_usage_uom, enabled_to_all_pn,
                               any_raw_dataset_name_dict_element,
                               input_file_name_dict_element, input_sheet_name_dict_element,
                               desired_input_clmns_dict_element,
                               desired_clmns_at_std_dict_element, key_codes_dict_element, clmn_types_dict_element,
                               input_skiprows_dict_element,
                               any_datamatrix_name_dict_element,
                               nomenclature_clmns_dict_element,
                               clmn_uom_conversion_dict_element,
                               error_msg_clmn, main_input_format, input_folder_name,
                               output_folder_name_mtx, main_output_format,
                               location_l0_clmn, msh_code_clmn, msh_description_clmn,
                               uom_input_clmn, index_clmn, input_file_clmn, input_sheet_clmn,
                               output_report_clmn, original_term_clmn, pn_code_clmn, uom_si_clmn, old_uom_clmn,
                               new_uom_clmn, multiplier_clmn)

    save_datamatrices([mtx_error])
    save_datamatrices(datamatrix_list)

    return [mtx_error, mtx_nomenclature, mtx_conversion, mtx_part_number, mtx_vendor, mtx_mash, mtx_mash_grain,
            mtx_ppv_historical_volume, mtx_distillation_schedule]


def init_mtx_distillation_schedule(raw_beam_distillation_schedule_setup_dict, raw_beam_bill_of_materials_dict,
                                   raw_makers_distillation_schedule_setup_dict,
                                   mtx_distillation_schedule_setup_dict,
                                   mtx_error, mtx_nomenclature, mtx_conversion, mtx_mash,
                                   beam_dist_uom, beam_grain_usage_uom,
                                   makers_location, makers_code, makers_msh_description, makers_dist_uom, 
                                   makers_grain_usage_uom, enabled_to_all_pn,
                                   any_raw_dataset_name_dict_element,
                                   input_file_name_dict_element, input_sheet_name_dict_element,
                                   desired_input_clmns_dict_element,
                                   desired_clmns_at_std_dict_element, key_codes_dict_element, clmn_types_dict_element,
                                   input_skiprows_dict_element, any_datamatrix_name_dict_element,
                                   nomenclature_clmns_dict_element,
                                   clmn_uom_conversion_dict_element,
                                   error_msg_clmn, main_input_format, input_folder_name,
                                   output_folder_name_mtx, main_output_format,
                                   location_l0_clmn, msh_code_clmn, msh_description_clmn,
                                   uom_input_clmn, index_clmn, input_file_clmn, input_sheet_clmn,
                                   output_report_clmn, original_term_clmn, pn_code_clmn, uom_si_clmn, old_uom_clmn,
                                   new_uom_clmn, multiplier_clmn):

    raw_beam_distillation_schedule = RawDataset(name=raw_beam_distillation_schedule_setup_dict
                                                [any_raw_dataset_name_dict_element],
                                                input_directory=Directory(folder=input_folder_name,
                                                                          file=raw_beam_distillation_schedule_setup_dict
                                                                          [input_file_name_dict_element],
                                                                          format=main_input_format,
                                                                          sheet=
                                                                          raw_beam_distillation_schedule_setup_dict
                                                                          [input_sheet_name_dict_element],
                                                                          skiprows=
                                                                          raw_beam_distillation_schedule_setup_dict
                                                                          [input_skiprows_dict_element]),
                                                output_directory=Directory(folder=output_folder_name_mtx,
                                                                           format=main_output_format,
                                                                           file=
                                                                           raw_beam_distillation_schedule_setup_dict
                                                                           [any_raw_dataset_name_dict_element]),
                                                desired_input_clmns=raw_beam_distillation_schedule_setup_dict
                                                [desired_input_clmns_dict_element],
                                                desired_clmns_at_std=raw_beam_distillation_schedule_setup_dict
                                                [desired_clmns_at_std_dict_element],
                                                key_codes=raw_beam_distillation_schedule_setup_dict
                                                [key_codes_dict_element],
                                                clmn_types=raw_beam_distillation_schedule_setup_dict
                                                [clmn_types_dict_element])
    raw_beam_distillation_schedule.init_dataframe(mtx_error, index_clmn, input_file_clmn, input_sheet_clmn,
                                                  output_report_clmn,
                                                  error_msg_clmn)
    raw_beam_distillation_schedule.filter_columns()
    raw_beam_distillation_schedule.dataframe[uom_input_clmn] = beam_dist_uom

    raw_makers_distillation_schedule = RawDataset(name=raw_makers_distillation_schedule_setup_dict
                                                  [any_raw_dataset_name_dict_element],
                                                  input_directory=Directory(folder=input_folder_name,
                                                                            file=
                                                                            raw_makers_distillation_schedule_setup_dict
                                                                            [input_file_name_dict_element],
                                                                            format=main_input_format,
                                                                            sheet=
                                                                            raw_makers_distillation_schedule_setup_dict
                                                                            [input_sheet_name_dict_element],
                                                                            skiprows=
                                                                            raw_makers_distillation_schedule_setup_dict
                                                                            [input_skiprows_dict_element]),
                                                  output_directory=Directory(folder=output_folder_name_mtx,
                                                                             format=main_output_format,
                                                                             file=
                                                                             raw_makers_distillation_schedule_setup_dict
                                                                             [any_raw_dataset_name_dict_element]),
                                                  desired_input_clmns=raw_makers_distillation_schedule_setup_dict
                                                  [desired_input_clmns_dict_element],
                                                  desired_clmns_at_std=raw_makers_distillation_schedule_setup_dict
                                                  [desired_clmns_at_std_dict_element],
                                                  key_codes=raw_makers_distillation_schedule_setup_dict[
                                                      key_codes_dict_element],
                                                  clmn_types=raw_makers_distillation_schedule_setup_dict[
                                                      clmn_types_dict_element])
    raw_makers_distillation_schedule.init_dataframe(mtx_error, index_clmn, input_file_clmn, input_sheet_clmn,
                                                    output_report_clmn,
                                                    error_msg_clmn)
    raw_makers_distillation_schedule.dataframe[location_l0_clmn] = makers_location
    raw_makers_distillation_schedule.dataframe[msh_code_clmn] = makers_code
    raw_makers_distillation_schedule.dataframe[msh_description_clmn] = makers_msh_description
    raw_makers_distillation_schedule.dataframe[uom_input_clmn] = makers_dist_uom

    mtx_distillation_schedule = DataMatrix(name=mtx_distillation_schedule_setup_dict[any_datamatrix_name_dict_element],
                                           output_directory=Directory(folder=output_folder_name_mtx,
                                                                      format=main_output_format,
                                                                      file=
                                                                      mtx_distillation_schedule_setup_dict
                                                                      [any_datamatrix_name_dict_element]),
                                           desired_clmns_at_std=mtx_distillation_schedule_setup_dict
                                           [desired_clmns_at_std_dict_element],
                                           key_codes=mtx_distillation_schedule_setup_dict[key_codes_dict_element],
                                           raw_dataset_list=[raw_beam_distillation_schedule,
                                                             raw_makers_distillation_schedule],
                                           nomenclature_clmns=mtx_distillation_schedule_setup_dict
                                           [nomenclature_clmns_dict_element],
                                           clmn_uom_conversion=mtx_distillation_schedule_setup_dict
                                           [clmn_uom_conversion_dict_element])
    mtx_distillation_schedule.init_dataframe()
    mtx_distillation_schedule.apply_nomenclature(mtx_error, mtx_nomenclature,
                                                 original_term_clmn,
                                                 index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
                                                 error_msg_clmn)
    mtx_distillation_schedule.convert_volume_to_si_uom(mtx_error, mtx_conversion, mtx_mash,
                                                       enabled_to_all_pn,  msh_code_clmn,
                                                       pn_code_clmn, uom_si_clmn, old_uom_clmn, new_uom_clmn,
                                                       multiplier_clmn,
                                                       index_clmn, input_sheet_clmn, input_file_clmn,
                                                       output_report_clmn, error_msg_clmn)

    return [mtx_distillation_schedule, mtx_error]
    

def init_mtx_bill_of_materials(raw_beam_bill_of_materials_setup_dict, raw_makers_bill_of_materials_setup_dict,
                               mtx_bill_of_materials_setup_dict,
                               mtx_error, mtx_nomenclature, mtx_conversion, mtx_mash_grain,
                               beam_dist_uom, beam_grain_usage_uom,
                               makers_location, makers_code, makers_msh_description, makers_dist_uom,
                               makers_grain_usage_uom, enabled_to_all_pn,
                               any_raw_dataset_name_dict_element,
                               input_file_name_dict_element, input_sheet_name_dict_element,
                               desired_input_clmns_dict_element,
                               desired_clmns_at_std_dict_element, key_codes_dict_element, clmn_types_dict_element,
                               input_skiprows_dict_element,
                               any_datamatrix_name_dict_element,
                               nomenclature_clmns_dict_element,
                               clmn_uom_conversion_dict_element,
                               error_msg_clmn, main_input_format, input_folder_name,
                               output_folder_name_mtx, main_output_format,
                               location_l0_clmn, msh_code_clmn, msh_description_clmn,
                               uom_input_clmn, index_clmn, input_file_clmn, input_sheet_clmn,
                               output_report_clmn, original_term_clmn, pn_code_clmn, uom_si_clmn, old_uom_clmn,
                               new_uom_clmn, multiplier_clmn):
    
    raw_beam_bill_of_materials = RawDataset(name=raw_beam_bill_of_materials_setup_dict
                                            [any_raw_dataset_name_dict_element],
                                            input_directory=Directory(folder=input_folder_name,
                                                                      file=raw_beam_bill_of_materials_setup_dict
                                                                      [input_file_name_dict_element],
                                                                      format=main_input_format,
                                                                      sheet=
                                                                      raw_beam_bill_of_materials_setup_dict
                                                                      [input_sheet_name_dict_element],
                                                                      skiprows=
                                                                      raw_beam_bill_of_materials_setup_dict
                                                                      [input_skiprows_dict_element]),
                                            output_directory=Directory(folder=output_folder_name_mtx,
                                                                       format=main_output_format,
                                                                       file=
                                                                       raw_beam_bill_of_materials_setup_dict
                                                                       [any_raw_dataset_name_dict_element]),
                                            desired_input_clmns=raw_beam_bill_of_materials_setup_dict
                                            [desired_input_clmns_dict_element],
                                            desired_clmns_at_std=raw_beam_bill_of_materials_setup_dict
                                            [desired_clmns_at_std_dict_element],
                                            key_codes=raw_beam_bill_of_materials_setup_dict
                                            [key_codes_dict_element],
                                            clmn_types=raw_beam_bill_of_materials_setup_dict
                                            [clmn_types_dict_element])
    raw_beam_bill_of_materials.init_dataframe(mtx_error, index_clmn, input_file_clmn, input_sheet_clmn,
                                              output_report_clmn, error_msg_clmn)
    raw_beam_bill_of_materials.filter_columns()
    raw_beam_bill_of_materials.dataframe[uom_input_clmn] = beam_grain_usage_uom

    raw_makers_bill_of_materials = RawDataset(name=raw_makers_bill_of_materials_setup_dict
                                              [any_raw_dataset_name_dict_element],
                                              input_directory=Directory(folder=input_folder_name,
                                                                        file=
                                                                        raw_makers_bill_of_materials_setup_dict
                                                                        [input_file_name_dict_element],
                                                                        format=main_input_format,
                                                                        sheet=
                                                                        raw_makers_bill_of_materials_setup_dict
                                                                        [input_sheet_name_dict_element],
                                                                        skiprows=
                                                                        raw_makers_bill_of_materials_setup_dict
                                                                        [input_skiprows_dict_element]),
                                              output_directory=Directory(folder=output_folder_name_mtx,
                                                                         format=main_output_format,
                                                                         file=
                                                                         raw_makers_bill_of_materials_setup_dict
                                                                         [any_raw_dataset_name_dict_element]),
                                              desired_input_clmns=raw_makers_bill_of_materials_setup_dict
                                              [desired_input_clmns_dict_element],
                                              desired_clmns_at_std=raw_makers_bill_of_materials_setup_dict
                                              [desired_clmns_at_std_dict_element],
                                              key_codes=raw_makers_bill_of_materials_setup_dict[
                                                  key_codes_dict_element],
                                              clmn_types=raw_makers_bill_of_materials_setup_dict[
                                                  clmn_types_dict_element])
    raw_makers_bill_of_materials.init_dataframe(mtx_error, index_clmn, input_file_clmn, input_sheet_clmn,
                                                    output_report_clmn,
                                                    error_msg_clmn)
    raw_makers_bill_of_materials.dataframe[location_l0_clmn] = makers_location
    raw_makers_bill_of_materials.dataframe[msh_code_clmn] = makers_code
    raw_makers_bill_of_materials.dataframe[uom_input_clmn] = makers_grain_usage_uom

    mtx_bill_of_materials = DataMatrix(name=mtx_bill_of_materials_setup_dict[any_datamatrix_name_dict_element],
                                           output_directory=Directory(folder=output_folder_name_mtx,
                                                                      format=main_output_format,
                                                                      file=
                                                                      mtx_bill_of_materials_setup_dict
                                                                      [any_datamatrix_name_dict_element]),
                                           desired_clmns_at_std=mtx_bill_of_materials_setup_dict
                                           [desired_clmns_at_std_dict_element],
                                           key_codes=mtx_bill_of_materials_setup_dict[key_codes_dict_element],
                                           raw_dataset_list=[raw_beam_bill_of_materials,
                                                             raw_makers_bill_of_materials],
                                           nomenclature_clmns=mtx_bill_of_materials_setup_dict
                                           [nomenclature_clmns_dict_element],
                                           clmn_uom_conversion=mtx_bill_of_materials_setup_dict
                                           [clmn_uom_conversion_dict_element])
    mtx_bill_of_materials.init_dataframe()

    mtx_bill_of_materials.apply_nomenclature(mtx_error, mtx_nomenclature,
                                                 original_term_clmn,
                                                 index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
                                                 error_msg_clmn)
    print(mtx_bill_of_materials.dataframe)
    mtx_bill_of_materials.convert_volume_to_si_uom(mtx_error, mtx_conversion, mtx_mash_grain,
                                                       enabled_to_all_pn,  msh_code_clmn,
                                                       pn_code_clmn, uom_si_clmn, old_uom_clmn, new_uom_clmn,
                                                       multiplier_clmn,
                                                       index_clmn, input_sheet_clmn, input_file_clmn,
                                                       output_report_clmn, error_msg_clmn)
    print(mtx_mash_grain.dataframe)
    print(mtx_bill_of_materials.dataframe)

    return [mtx_bill_of_materials, mtx_error]


def init_mtx_ppv_historical(mtx_ppv_historical_volume_setup_dict,
                            mtx_error, mtx_nomenclature, mtx_conversion, mtx_part_number,
                            enabled_to_all_pn,
                            any_raw_dataset_name_dict_element,
                            any_datamatrix_name_dict_element,
                            input_file_name_dict_element, input_sheet_name_dict_element,
                            desired_input_clmns_dict_element,
                            desired_clmns_at_std_dict_element, key_codes_dict_element, clmn_types_dict_element,
                            nomenclature_clmns_dict_element, input_skiprows_dict_element,
                            clmn_uom_conversion_dict_element,
                            error_msg_clmn, main_input_format, input_folder_name, output_folder_name_mtx,
                            main_output_format,
                            index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, original_term_clmn,
                            msh_code_clmn, pn_code_clmn, uom_si_clmn, old_uom_clmn, new_uom_clmn, multiplier_clmn):

    raw_ppv_historical_volume = RawDataset(name=mtx_ppv_historical_volume_setup_dict[any_raw_dataset_name_dict_element],
                                           input_directory=Directory(folder=input_folder_name,
                                                                     file=mtx_ppv_historical_volume_setup_dict
                                                                     [input_file_name_dict_element],
                                                                     format=main_input_format,
                                                                     sheet=mtx_ppv_historical_volume_setup_dict
                                                                     [input_sheet_name_dict_element],
                                                                     skiprows=mtx_ppv_historical_volume_setup_dict
                                                                     [input_skiprows_dict_element]),
                                           output_directory=Directory(folder=output_folder_name_mtx,
                                                                      format=main_output_format,
                                                                      file=mtx_ppv_historical_volume_setup_dict
                                                                      [any_raw_dataset_name_dict_element]),
                                           desired_input_clmns=mtx_ppv_historical_volume_setup_dict
                                           [desired_input_clmns_dict_element],
                                           desired_clmns_at_std=mtx_ppv_historical_volume_setup_dict
                                           [desired_clmns_at_std_dict_element],
                                           key_codes=mtx_ppv_historical_volume_setup_dict[key_codes_dict_element],
                                           clmn_types=mtx_ppv_historical_volume_setup_dict[clmn_types_dict_element])
    mtx_error = raw_ppv_historical_volume.init_dataframe(mtx_error, index_clmn, input_file_clmn, input_sheet_clmn,
                                                         output_report_clmn,
                                                         error_msg_clmn)
    mtx_ppv_historical_volume = DataMatrix(name=mtx_ppv_historical_volume_setup_dict[any_datamatrix_name_dict_element],
                                           output_directory=Directory(folder=output_folder_name_mtx,
                                                                      format=main_output_format,
                                                                      file=mtx_ppv_historical_volume_setup_dict
                                                                      [any_datamatrix_name_dict_element]),
                                           desired_clmns_at_std=mtx_ppv_historical_volume_setup_dict
                                           [desired_clmns_at_std_dict_element],
                                           key_codes=mtx_ppv_historical_volume_setup_dict[key_codes_dict_element],
                                           raw_dataset_list=[raw_ppv_historical_volume],
                                           nomenclature_clmns=mtx_ppv_historical_volume_setup_dict
                                           [nomenclature_clmns_dict_element],
                                           clmn_uom_conversion=mtx_ppv_historical_volume_setup_dict
                                           [clmn_uom_conversion_dict_element])
    mtx_ppv_historical_volume.init_dataframe()
    mtx_ppv_historical_volume.apply_nomenclature(mtx_error, mtx_nomenclature, original_term_clmn,
                                                 index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
                                                 error_msg_clmn)
    mtx_ppv_historical_volume.convert_volume_to_si_uom(mtx_error, mtx_conversion, mtx_part_number,
                                                       enabled_to_all_pn, pn_code_clmn,
                                                       pn_code_clmn, uom_si_clmn, old_uom_clmn, new_uom_clmn,
                                                       multiplier_clmn,
                                                       index_clmn, input_sheet_clmn, input_file_clmn,
                                                       output_report_clmn, error_msg_clmn)

    return [mtx_ppv_historical_volume, mtx_error]


def merge_and_drop(any_dataframe, df_reference,
                   primary_key_clmn_at_any_dataframe, primary_key_clmn_at_df_reference,
                   new_name_for_primary_key_clmn_at_any_dataframe, code_clmn):
    original_column_list = any_dataframe.columns

    any_dataframe = any_dataframe.merge(df_reference, how='left', left_on=primary_key_clmn_at_any_dataframe,
                                        right_on=primary_key_clmn_at_df_reference)
    any_dataframe.drop_duplicates(inplace=True)
    if primary_key_clmn_at_any_dataframe != code_clmn and primary_key_clmn_at_any_dataframe in any_dataframe.columns:
        any_dataframe = any_dataframe.drop(primary_key_clmn_at_any_dataframe, axis=1, inplace=False)

    equalizer_clmn_names = df_reference.columns

    any_dataframe = any_dataframe.rename(columns={equalizer_clmn_names[1]:
                                                  new_name_for_primary_key_clmn_at_any_dataframe}, inplace=False)
    any_dataframe = any_dataframe[original_column_list]

    return any_dataframe


def merge_and_rename(any_dataframe, df_reference,
                     primary_key_clmn_at_any_dataframe, primary_key_clmn_at_df_reference,
                     new_name_for_primary_key_clmn_at_any_dataframe, code_clmn):

    any_dataframe = any_dataframe.merge(df_reference, how='left', left_on=primary_key_clmn_at_any_dataframe,
                                        right_on=primary_key_clmn_at_df_reference)
    any_dataframe.drop_duplicates(inplace=True)
    # any_dataframe = any_dataframe.drop(primary_key_clmn_at_df_reference, axis=1, inplace=False)
    equalizer_clmn_names = df_reference.columns

    any_dataframe = any_dataframe.rename(columns={equalizer_clmn_names[1]:
                                                  new_name_for_primary_key_clmn_at_any_dataframe}, inplace=False)

    return any_dataframe


def get_multiplier(df_conversion, pn_code, old_uom, new_uom, enabled_to_all_pn,
                   pn_code_clmn, old_uom_clmn, new_uom_clmn, multiplier_clmn):
    # df_conversion.reset_index(inplace=True)

    cond_old_uom = df_conversion[old_uom_clmn] == old_uom
    cond_new_uom = df_conversion[new_uom_clmn] == new_uom
    cond_uom = cond_old_uom & cond_new_uom

    cond_all_pn = df_conversion[pn_code_clmn] == enabled_to_all_pn
    cond_specific_pn = df_conversion[pn_code_clmn] == pn_code
    cond_pn = cond_all_pn | cond_specific_pn

    cond = cond_uom & cond_pn
    multiplier = df_conversion.loc[cond, multiplier_clmn].to_list()

    if len(multiplier) != 0:
        multiplier = df_conversion.loc[cond, multiplier_clmn].to_list()
        multiplier = multiplier[0]
    else:
        multiplier = pd.NA

    return multiplier


#     def dataframe_init(self, mtx_error=[], mtx_nomenclature=[], mtx_conversion=[], mtx_part_number=[],
#                        enabled_to_all_pn=[], pn_code_clmn=[], uom_si_clmn=[],
#                        old_uom_clmn=[], new_uom_clmn=[], multiplier_clmn=[],
#                        index_clmn=[], input_file_clmn=[], input_sheet_clmn=[], output_report_clmn=[], error_msg_clmn=[],
#                        original_term_clmn=[]):
#         # Data loading
#         #     Cleanse
#         #          load
#         #          filter columns
#         #          change column names
#         #          filter rows
#         #          convert data types and round float types
#         #          eliminate NaNs and update error report
#         #          eliminate duplicate indexes and update error report
#         #     Convert
#         #          UoM to SI
#         #          Current to standard currency
#         #          Category to standard reference
#         #          Plant to standard reference
#         #          Supplier names to standard reference
#         #          Supplier plants to standard reference
#         #     Calculate
#         #     Save
#
#         if pd.isna(self.input_file):
#             self.dataframe = pd.DataFrame(columns=self.desired_input_clmns)
#         else:
#             self.load_mtx_xy()
#
#             mtx_error = self.cleanse_mtx_xy(mtx_error,
#                                             index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn)
#
#             mtx_error = self.apply_nomenclature(mtx_error, mtx_nomenclature,
#                                                 original_term_clmn,
#                                                 index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn)
#
#             old_value_clmn = list(self.clmn_uom_conversion.keys())[0]
#             if not pd.isna(old_value_clmn):
#                 mtx_error = self.convert_volume_uom_to_si(mtx_error=mtx_error, mtx_conversion=mtx_conversion,
#                                                           mtx_part_number=mtx_part_number,
#                                                           enabled_to_all_pn=enabled_to_all_pn,
#                                                           pn_code_clmn=pn_code_clmn, uom_si_clmn=uom_si_clmn,
#                                                           old_uom_clmn=old_uom_clmn, new_uom_clmn=new_uom_clmn,
#                                                           multiplier_clmn=multiplier_clmn,
#                                                           index_clmn=index_clmn, input_file_clmn=input_file_clmn,
#                                                           output_report_clmn=output_report_clmn,
#                                                           error_msg_clmn=error_msg_clmn,
#                                                           input_sheet_clmn=input_sheet_clmn)
#
#         return mtx_error

# class MyDataframe:
#     def __init__(self, name,
#                  input_folder=pd.NA, input_file=pd.NA, input_sheet=pd.NA, input_skiprows=0,
#                  output_folder=pd.NA, output_format='.csv',
#                  key_code_clmns=[pd.NA], desired_input_clmns=[pd.NA], desired_clmns_at_std=[pd.NA],
#                  nomenclature_clmns=[pd.NA],
#                  clmn_rename={pd.NA: pd.NA}, clmn_types={pd.NA: pd.NA},
#                  clmn_uom_conversion={pd.NA: [pd.NA, pd.NA, pd.NA]}):
#         # clmn_uom_conversion -> {dict_key: [L0, L1, L2]}
#         # dict_key -> clmn name with float at input UoM (to be converted)
#         # L0 -> clmn name with float at SI UoM
#         # L1 -> clmn name of input UoM
#         # L2  -> clmn name of standard UoM
#         self.name = name
#         self.input_folder = input_folder
#         self.input_file = input_file
#         self.input_sheet = input_sheet
#         self.input_skiprows = input_skiprows
#         self.output_folder = output_folder
#         self.output_format = output_format
#         self.key_code_clmns = key_code_clmns
#         self.desired_input_clmns = desired_input_clmns
#         self.desired_clmns_at_std = desired_clmns_at_std
#         self.nomenclature_clmns = nomenclature_clmns
#         self.clmn_rename = clmn_rename
#         self.clmn_types = clmn_types
#         self.clmn_uom_conversion = clmn_uom_conversion
#         self.dataframe = pd.DataFrame()
#
#     def __str__(self):
#         out_str = "******************** \n" \
#                   "name: {name} \n" \
#                   "input_folder: {input_folder}\n"\
#                   "input_file: {input_file}\n"\
#                   "input_sheet: {input_sheet}\n"\
#                   "output_folder: {output_folder}\n"\
#                   "desired_input_clmns: {desired_input_clmns}\n" \
#                   "desired_clmns_at_std: {desired_clmns_at_std}\n" \
#                   "nomenclature_clmns: {nomenclature_clmns}\n" \
#                   "clmn_rename: {clmn_rename}\n" \
#                   "clmn_types: {clmn_types}\n"\
#                   "clmn_uom_conversion: {clmn_uom_conversion}\n\n"\
#                   "dataframe: {dataframe}\n".format(name=self.name,
#                                                     input_folder=self.input_folder,
#                                                     input_file=self.input_file,
#                                                     input_sheet=self.input_sheet,
#                                                     output_folder=self.output_folder,
#                                                     desired_input_clmns=self.desired_input_clmns,
#                                                     desired_clmns_at_std=self.desired_clmns_at_std,
#                                                     nomenclature_clmns=self.nomenclature_clmns,
#                                                     clmn_rename=self.clmn_rename,
#                                                     clmn_types=self.clmn_types,
#                                                     clmn_uom_conversion=self.clmn_uom_conversion,
#                                                     dataframe=self.dataframe)
#
#         return out_str
#

#
#     def save_dataframe(self):
#         directory = './' + self.output_folder + '/' + self.name + self.output_format
#         self.dataframe.to_csv(directory)
#
#         return
#
#     def load_dataframe(self):
#         directory = './' + self.output_folder + '/' + self.name + self.output_format
#         self.dataframe = pd.read_csv(directory)
#
#         return
#
#     def load_mtx_xy(self):
#         directory = './' + self.input_folder + '/' + self.input_file
#         self.dataframe = pd.read_excel(directory, sheet_name=self.input_sheet, skiprows=self.input_skiprows)
#
#         self.dataframe = self.dataframe[self.desired_input_clmns]
#
#         return
#
#     def cleanse_mtx_xy(self, mtx_error,
#                        index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn):
#         error_msg_nan = 'CLEANSE: NaN on original file'
#         self.dataframe.rename(columns=self.clmn_rename, inplace=True)
#         self.dataframe = self.dataframe[self.desired_clmns_at_std]
#         self.dataframe.dropna(inplace=True, axis=0, subset=self.key_code_clmns)
#         self.assure_type_input()
#         missing_codes = []
#
#         for item in self.key_code_clmns:
#             [self.dataframe, missing_codes_to_append, are_lists_equal] = clean_nan(self.dataframe, item)
#             missing_codes.append(missing_codes_to_append)
#
#         mtx_error = load_mtx_error(mtx_error, self, missing_codes,
#                                    error_msg_nan,
#                                    index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn)
#         return mtx_error
#

#
#     def assure_type_input(self):
#
#         for key, value in self.clmn_types.items():
#             self.dataframe[key].astype(value)
#
#         return
#
#
#
# def load_mtx_error(mtx_error, mtx_xy, missing_codes,
#                    error_msg,
#                    index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn):
#
#     mtx_error_to_append = pd.DataFrame(columns=[index_clmn])
#     kk=0
#
#     for item in list(missing_codes):
#         mtx_error_to_append.loc[kk, index_clmn] = item
#         kk = kk+1
#
#     mtx_error_to_append[input_file_clmn] = mtx_xy.input_file
#     mtx_error_to_append[input_sheet_clmn] = mtx_xy.input_sheet
#     mtx_error_to_append[output_report_clmn] = mtx_xy.name
#     mtx_error_to_append[error_msg_clmn] = error_msg
#
#     if mtx_error.dataframe.empty:
#         mtx_error.dataframe = mtx_error_to_append
#     else:
#         mtx_error.dataframe = mtx_error.dataframe.append(mtx_error_to_append)
#
#     return mtx_error
#
#

#
#
# def list_differential(old_list, new_list):
#     item_diff = []
#     are_list_equal = True
#
#     for old_item in old_list:
#
#         if old_item not in new_list:
#             item_diff.append(old_item)
#             are_list_equal = False
#
#     return [item_diff, are_list_equal]
#
#

#
#
# def save_mtx_xy_dataframe_list(mtx_xy_list):
#
#     for item in mtx_xy_list:
#         item.save_dataframe()
#
#     return
#
#
