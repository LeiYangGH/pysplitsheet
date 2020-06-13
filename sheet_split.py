import pandas as pd
import os


def split_excel_by_column_values(base_path=os.getcwd()
                                 , input_excel=None,
                                 columns=['Winner', 'Loser']):
    '''base_path:工作目录，如果不设定则假定为当前目录
    input_excel: excel文件名（不包含文件夹），如果不设定则扫描base_path里的第一个excel文件
    columns: 以哪些列的值为拆分的文件名
    '''

    if not input_excel:
        input_excel = next(f for f in os.listdir(base_path) if f.endswith('.xlsx'))
    excel_file = os.path.join(base_path, input_excel)
    all_df = pd.read_excel(excel_file, header=[0])
    # all_df.to_excel(os.path.join(base_path, '222.xlsx'))
    groupkeys = set()
    for col in columns:
        groupkeys = groupkeys.union(set(all_df[col]))
    # print(all_df)
    print(all_df.columns.tolist())
    print(groupkeys)
    countries_folder = os.path.join(base_path, 'countries')
    if not os.path.isdir(countries_folder):
        os.mkdir(countries_folder)
    for key in groupkeys:
        key_df = all_df[(all_df['Winner'] == key) | (all_df['Loser'] == key)]  #
        key_file = os.path.join(countries_folder, f'{key}.xlsx')
        key_df.to_excel(key_file)
        print(f'{key}共{len(key_df)}条记录已保存到{key_file}')


if __name__ == '__main__':
    split_excel_by_column_values(base_path=r'C:\Users\LeiYang\Downloads')
