from cmath import inf
from distutils.log import info
import numpy as np
import pandas as pd


# excel_file='TEST_FILES.xlsx'
# df=pd.read_excel(excel_file)
# # print(df)

# # print(df['Name'].where(df['Occupation']=='Programmer'))
# # programmers =df['Name'].where(df['Occupation']=='Programmer')
# # print(programmers.dropna())

# excel_files=['TEST_FILES.xlsx','TEST_FILES_Copy1.xlsx','TEST_FILES_Copy2.xlsx']

# for individual_excel_file in excel_files:
#     df=pd.read_excel(individual_excel_file)
#     programmers =df['Name'].where(df['Occupation']=='Programmer').dropna()
#     print("File Name: " + individual_excel_file)
#     print(programmers)

# office_supplies='Office_Supplies_Sales.xlsx'
# df=pd.read_excel(office_supplies)
# Order=df['OrderDate'].where(df['Item'] == 'Pencil').dropna()
# print(Order)

initial_workbook='TEST_FILES.xlsx'
info_workbook='Office_Supplies_Sales.xlsx'
output_workbook='output.xlsx'

df_initial =pd.read_excel(initial_workbook)
df_info=pd.read_excel(info_workbook)

# print(df_initial.columns)
# print(df_info.columns)

df_initial.rename(columns={'Code':'Primary Key'}, inplace=True)
df_3=pd.merge(df_initial,df_info[['Name','Code']], on='Code', how='left')
print(df_3)

