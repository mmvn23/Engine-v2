import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# List of inputs (excel files):
#   1) Budget
#   2) Actuals
#   3) Predecessor
#   4) Forecast
#   5) Baseline
#   6) UoM and FX conversions
#   7) Project mapping

#############################                Input Variables                      ######################################
report_month = 4

### Data cleaning
filename_bgt = './inputs/PAF.xlsx'
filename_bgt_csv = './outputs/budget.csv'
code_column = 'code'
description_column = 'description'
category_column = 'category'
location_column = 'location'
bgt_price_column = 'bgt_price'
bgt_currency_column = 'bgt_currency'
bgt_uom_column = 'bgt_uom'
bgt_per_column = 'bgt_per'
savings_type_column = 'savings_type'
bgt_month_column = 'month'
bgt_volume_column = 'bgt_volume'
bgt_columns_conversion = {'Part Number': code_column,
                          'Description': description_column,
                          'Category': category_column,
                          'Plant': location_column,
                          'PAF price': bgt_price_column,
                          'FX': bgt_currency_column,
                          'Unity': bgt_uom_column,
                          '1 or 1,000? ': bgt_per_column,
                          'PL or BS?': savings_type_column,
                          'vol 01': '1',
                          'vol 02': '2',
                          'vol 03': '3',
                          'vol 04': '4',
                          'vol 05': '5',
                          'vol 06': '6',
                          'vol 07': '7',
                          'vol 08': '8',
                          'vol 09': '9',
                          'vol 10': '10',
                          'vol 11': '11',
                          'vol 12': '12'}
bgt_id_vars = [code_column, description_column, category_column, location_column, bgt_price_column, bgt_currency_column,
               bgt_uom_column, bgt_per_column, savings_type_column]

# security opportunity: check if all expected columns are part of new file

#############################                1) DATA CLEANING                     ######################################
### load conversion excel file
df_wide_bgt = pd.read_excel(filename_bgt)


### load budget, actuals, forecast, baseline, UoM and FX and project mapping

### organize data in a structured dataframe
# change column and index names
df_wide_bgt.rename(columns=bgt_columns_conversion, inplace=True)

# from wide to long format
df_long_bgt = pd.melt(frame=df_wide_bgt, id_vars=bgt_id_vars, value_vars=None, var_name=bgt_month_column,
                      value_name=bgt_volume_column)

### convert data types
df_long_bgt.astype({bgt_price_column: float, bgt_volume_column: float, bgt_per_column: float, bgt_month_column: int})

### verify NaN and prepare a PN with errors
### convert price and volume into budget price UoM
# convert uom and FX names to a codified version

### save data-frame on CSV
df_long_bgt.to_csv(filename_bgt_csv)




print(df_long_bgt)


#############################                   2) CALCULATION ENGINE                      #############################

#############################                    3) REPORT GENERATOR                       #############################

#############################                  4) WEB INTERFACE (input)                    #############################

#############################               5) INTERACTIVE INTERFACE (output)              #############################