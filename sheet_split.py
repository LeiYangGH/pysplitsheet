import pandas as pd

excel_file = r'C:\Users\LeiYang\Downloads\matches.xlsx'
all_df = pd.read_excel(excel_file)
countries = set(all_df['colb'])
print(all_df)
print(countries)
