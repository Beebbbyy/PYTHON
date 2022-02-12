import pandas as pd

excel_file_1='TEST_FILES.xlsx'
excel_file_2='TEST_FILES2_2.xlsx'

df1= pd.read_excel(excel_file_1)
df2=pd.read_excel(excel_file_2)

# print(df1.columns)
# print(df2.columns)

# print(df1['Name'].isin(df2['Name']))

filtered_df_1=df1.loc[(df1['Name'].isin(df2['Name']))]
# print(filtered_df_1)
filtered_df_2=df1.loc[~(df1['Name'].isin(df2['Name']))]
# print(filtered_df_2)
filtered_df_3=df1.loc[(df1['Name'].isin(df2['Name'])) | (df1['Interview Score']>4)]
# print(filtered_df_3)

all_df=pd.merge(df1,df2, how='outer', on='Name')
#print(all_df.columns)

filtered_df_4=all_df.loc[(all_df['YR EXPERIENCE']<5) & (all_df['Group Interview Score']>3 )]
print(filtered_df_4)

filtered_df_4.to_excel("output.xlsx")