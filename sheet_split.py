import pandas as pd
import os

base_path = r'C:\Users\LeiYang\Downloads'
excel_file = os.path.join(base_path, '111.xlsx')
all_df = pd.read_excel(excel_file, header=[0])
countries = set((all_df['Winner'] + all_df['Loser']))
print(all_df)
print(countries)
countries_folder = os.path.join(base_path, f'countries')
if not os.path.isdir(countries_folder):
    os.mkdir(countries_folder)
for country in countries:
    # print(country)
    country_df = all_df[(all_df['Winner'] == country) | (all_df['Loser'] == country)]
    country_file = os.path.join(countries_folder, f'{country}.xlsx')
    print(country_file)
    country_df.to_excel(country_file)
