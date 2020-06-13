import pandas as pd

excel_file = r'C:\Users\LeiYang\Downloads\matches.xlsx'
all_df = pd.read_excel(excel_file)
print(all_df)
