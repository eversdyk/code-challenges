"""
Clean/Parse Land Grant Data and save as json file.
Working Version - Currently Output File is missing some titles.
"""

import json
import pandas as pd
RAW_DATA_PATH = 'Index_133634.txt'
OUTPUT_PATH = 'Cliff_E_output.json'


def remove_exclamations(series):
    """
    param series: pandas series as string type
    return: pandas series as list type with exclamation marks gone
    """
    return series.str.replace('\!', ',').str.split(',')


def refine_data(filepath):
    """
    read pipe-format data, clean in pandas, return python dictionary
    """
    df = pd.read_csv(filepath, sep='|', dtype=str, index_col=False)
    names_col_list = [
        'GRANTOR.LNAME',
        'GRANTOR.FNAME',
        'GRANTOR.MNAME',
        'GRANTOR.TITLE',
        'GRANTEE.LNAME',
        'GRANTEE.FNAME',
        'GRANTEE.MNAME',
        'GRANTEE.TITLE'
        ]
    names_df = df[names_col_list].apply(lambda x: remove_exclamations(x), axis=1)
    names_df['INST'] = df['INST.NUM']
    names_df.set_index('INST', inplace=True)
    data = names_df.to_dict('index')
    for i in list(data):
        grantees = [' '.join(list(a)).strip() for a in zip(data[i]['GRANTEE.LNAME'], data[i]['GRANTEE.FNAME'], data[i]['GRANTEE.MNAME'], data[i]['GRANTEE.TITLE'])]
        grantors = [' '.join(list(a)).strip() for a in zip(data[i]['GRANTOR.LNAME'], data[i]['GRANTOR.FNAME'], data[i]['GRANTOR.MNAME'], data[i]['GRANTOR.TITLE'])]
        data[i] = {
            'grantees': grantees,
            'grantors': grantors
        }
    return data


def create_file(formatted_dict):
    """
    write python dictionary to json
    """
    with open(OUTPUT_PATH, 'w') as filename:
        json.dump(formatted_dict, filename)


if __name__=='__main__':
    formatted_dict = refine_data(RAW_DATA_PATH)
    create_file(formatted_dict)
