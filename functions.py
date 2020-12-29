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
                          skiprows = self.skiprows)

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
                  "Dataframe: {dataframe}"\
                  .format(name=self.name,
                          output_directory=self.output_directory,
                          desired_clmns_at_std=self.desired_clmns_at_std,
                          dataframe=self.dataframe)

        return out_str


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

        mtx_error_to_append[input_file_clmn] = any_dataset.input_directory.file
        mtx_error_to_append[input_sheet_clmn] = any_dataset.input_directory.sheet
        mtx_error_to_append[output_report_clmn] = any_dataset.name
        mtx_error_to_append[error_msg_clmn] = error_msg

        self.dataframe = self.dataframe.append(mtx_error_to_append)

        return


class RegularDataset(DatasetManager):
    def __init__(self, name, output_directory, desired_clmns_at_std, key_codes):
        super().__init__(name, output_directory, desired_clmns_at_std)
        self.key_codes = key_codes

    def __str__(self):
        out_str = "Key codes: {key_codes}\n" \
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
                  "Clmn types: {clmn_types}\n" \
                  .format(desired_input_clmns=self.desired_input_clmns,
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

        return

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
                 clmn_uom_conversion=[]):
        super().__init__(name, output_directory, desired_clmns_at_std, key_codes)
        self.clmn_uom_conversion = clmn_uom_conversion
        self.raw_dataset_list = raw_dataset_list

    def __str__(self):
        out_str = "\nClmns for UoM conversion: {clmn_uom_conversion}\n" \
                  .format(clmn_uom_conversion=self.clmn_uom_conversion)

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
        print(self.raw_dataset_list)
        for item in self.raw_dataset_list:
            self.dataframe = self.dataframe.append(item.dataframe)

        self.dataframe.set_index(self.key_codes, inplace=True)

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


def load_mtx_from_raw(mtx_error, error_msg_clmn,
                      raw_nomenclature_name, mtx_nomenclature_name,
                      input_file_name, input_sheet_name, input_format,
                      input_folder_name,
                      desired_clmns_at_std, key_codes, clmn_types,
                      output_folder_name,
                      index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn):

    any_raw_dataset = RawDataset(name=raw_nomenclature_name,
                                 input_directory=Directory(folder=input_folder_name, file=input_file_name,
                                                           format=input_format,
                                                           sheet=input_sheet_name),
                                 output_directory=Directory(folder=output_folder_name, format='.csv',
                                                            file=raw_nomenclature_name),
                                 desired_input_clmns=['From', 'To'],
                                 desired_clmns_at_std=desired_clmns_at_std,
                                 key_codes=key_codes,
                                 clmn_types=clmn_types)

    any_raw_dataset.init_dataframe(mtx_error, index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
                                    error_msg_clmn)

    any_datamatrix = DataMatrix(name=any_raw_dataset.name,
                                output_directory=Directory(folder=output_folder_name, format='.csv',
                                                           file=mtx_nomenclature_name),
                                desired_clmns_at_std=desired_clmns_at_std,
                                key_codes=key_codes,
                                raw_dataset_list=[any_raw_dataset])

    any_datamatrix.init_dataframe()

    return any_datamatrix

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
#     def apply_nomenclature(self, mtx_error, mtx_nomenclature,
#                            original_term_clmn,
#                            index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn, error_msg_clmn):
#
#         if not pd.isna(self.nomenclature_clmns[0]):
#             # missing_codes = []
#             error_msg_nomenclature = 'Nomenclature not found'
#
#             item_key_code = self.key_code_clmns[0]
#
#             for item_nomenclature in self.nomenclature_clmns:
#
#                 self.dataframe = merge_and_drop(self.dataframe, mtx_nomenclature.dataframe, item_nomenclature,
#                                                 original_term_clmn, item_nomenclature, item_key_code)
#
#             [self.dataframe, missing_codes, are_lists_equal] = clean_nan(self.dataframe, item_key_code)
#
#             mtx_error = load_mtx_error(mtx_error, self, missing_codes,
#                                        error_msg_nomenclature,
#                                        index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
#                                        error_msg_clmn)
#         return mtx_error
#
#     def assure_type_input(self):
#
#         for key, value in self.clmn_types.items():
#             self.dataframe[key].astype(value)
#
#         return
#
#     def convert_volume_uom_to_si(self, mtx_error, mtx_conversion, mtx_part_number,
#                                  enabled_to_all_pn,
#                                  pn_code_clmn, uom_si_clmn, old_uom_clmn, new_uom_clmn, multiplier_clmn,
#                                  index_clmn, input_sheet_clmn, input_file_clmn, output_report_clmn, error_msg_clmn):
#         # clmn_uom_conversion = {pd.NA: [pd.NA, pd.NA, pd.NA]}):
#         # # clmn_uom_conversion -> {dict_key: [L0, L1, L2]}
#         # # dict_key -> clmn name with float at input UoM (to be converted)
#         # # L0 -> clmn name with float at SI UoM
#         # # L1 -> clmn name of input UoM
#         # # L2  -> clmn name of standard UoM
#         error_msg_convert_volume = 'Volume UoM conversion'
#         # add columns: standard UoM, value at standard UoM OK
#         # access mtx_part_number to get standard UoM OK
#         # add column: multiplier OK
#         # find multiplier OK
#         # apply multiplier to value at standard UoM OK
#         # drop multiplier OK
#         # clear NaN
#         # update mtx_error
#         self.include_standard_clmn(mtx_part_number, pn_code_clmn, uom_si_clmn)
#         self.calculate_volume_at_si(mtx_conversion, enabled_to_all_pn, pn_code_clmn, old_uom_clmn, new_uom_clmn,
#                                     multiplier_clmn)
#         [self.dataframe, missing_codes, are_lists_equal] = clean_nan(self.dataframe, pn_code_clmn)
#
#         mtx_error = load_mtx_error(mtx_error, self, missing_codes,
#                                    error_msg_convert_volume,
#                                    index_clmn, input_file_clmn, input_sheet_clmn, output_report_clmn,
#                                    error_msg_clmn)
#
#         return mtx_error
#
#     def include_standard_clmn(self, mtx_part_number, pn_code_clmn, uom_si_clmn):
#
#         mtx_uom_si = mtx_part_number.dataframe.reset_index()
#         mtx_uom_si = mtx_uom_si[[pn_code_clmn, uom_si_clmn]]
#
#         self.dataframe = merge_and_drop(self.dataframe, mtx_uom_si, pn_code_clmn, pn_code_clmn, uom_si_clmn,
#                                         pn_code_clmn)
#         return
#
#     def calculate_volume_at_si(self, mtx_conversion,
#                                enabled_to_all_pn, pn_code_clmn, old_uom_clmn, new_uom_clmn, multiplier_clmn):
#
#         old_value_clmn = list(self.clmn_uom_conversion.keys())[0]
#         value_list = list(self.clmn_uom_conversion.values())[0]
#         new_value_clmn = value_list[0]
#         input_uom_clmn = value_list[1]
#         si_uom_clmn = value_list[2]
#
#         df_conversion = mtx_conversion.dataframe.reset_index()
#
#         self.dataframe[new_value_clmn] = self.dataframe.apply(lambda row: row[old_value_clmn] * get_multiplier(
#                                                                                df_conversion=df_conversion,
#                                                                                pn_code=row[pn_code_clmn],
#                                                                                old_uom=row[input_uom_clmn],
#                                                                                new_uom=row[si_uom_clmn],
#                                                                                pn_code_clmn=pn_code_clmn,
#                                                                                enabled_to_all_pn=enabled_to_all_pn,
#                                                                                old_uom_clmn=old_uom_clmn,
#                                                                                new_uom_clmn=new_uom_clmn,
#                                                                                multiplier_clmn=multiplier_clmn), axis=1)
#
#
#         return
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
# def merge_and_drop(mtx_xy, df_equalizer,
#                    df_merge_clmn, equalizer_merge_clmn, new_clmn_name, code_clmn):
#
#     # old_part_number_bgt_list = mtx_xy[code_clmn]
#     # old_part_number_bgt_list = [str(item) for item in old_part_number_bgt_list]
#
#     mtx_xy = mtx_xy.merge(df_equalizer, how='left', left_on=df_merge_clmn, right_on=equalizer_merge_clmn)
#
#     if df_merge_clmn != code_clmn and df_merge_clmn in mtx_xy.columns:
#         mtx_xy = mtx_xy.drop(df_merge_clmn, axis=1, inplace=False)
#     if equalizer_merge_clmn != code_clmn and equalizer_merge_clmn in mtx_xy.columns:
#         mtx_xy = mtx_xy.drop(equalizer_merge_clmn, axis=1, inplace=False)
#
#     equalizer_clmn_names = df_equalizer.columns
#
#     mtx_xy = mtx_xy.rename(columns={equalizer_clmn_names[1]: new_clmn_name}, inplace=False)
#
#     # new_part_number_bgt_list = mtx_xy[code_clmn]
#     # new_part_number_bgt_list = [str(item) for item in new_part_number_bgt_list]
#     #
#     # [missing_codes, are_lists_equal] = list_differential(old_part_number_bgt_list, new_part_number_bgt_list)
#
#     return mtx_xy
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
# def get_multiplier(df_conversion, pn_code, old_uom, new_uom, enabled_to_all_pn,
#                    pn_code_clmn, old_uom_clmn, new_uom_clmn, multiplier_clmn):
#
#     # df_conversion.reset_index(inplace=True)
#
#     cond_old_uom = df_conversion[old_uom_clmn] == old_uom
#     cond_new_uom = df_conversion[new_uom_clmn] == new_uom
#     cond_uom = cond_old_uom & cond_new_uom
#
#     cond_all_pn = df_conversion[pn_code_clmn] == enabled_to_all_pn
#     cond_specific_pn = df_conversion[pn_code_clmn] == pn_code
#     cond_pn = cond_all_pn | cond_specific_pn
#
#     cond = cond_uom & cond_pn
#     multiplier = df_conversion.loc[cond, multiplier_clmn].to_list()
#
#     if len(multiplier) != 0:
#         multiplier = df_conversion.loc[cond, multiplier_clmn].to_list()
#         multiplier = multiplier[0]
#     else:
#         multiplier = pd.NA
#
#     return multiplier
#
# return