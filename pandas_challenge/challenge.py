import pandas as pd
import json


def read_data(file):
    """ Reads a file into a pandas dataframe.

    :param file:
    :return: Pandas Dataframe
    """


def get_grantors_grantees(df):
    """ Extracts lists of grantors and grantees for each document in dataframe and returns a dictionary.

    {
    "0149319": {"grantors": ["EVERSON ENERGY LP"], "grantees": ["AMERICAN ENERGY ASSOCIATES LLC"]},
    "0149318": {"grantors": ["LOZANO, HECTOR M"], "grantees": ["MARTINEZ, LINO M"]},
    "0149313": {"grantors": ["BROWN III, ROBERT E"], "grantees": ["EXCO OPERATING COMPANY LP"]}
    }

    :param df:
    :return:
    """


if __name__ == "__main__":
    index_file = read_data("Index_133634.txt")
    output = get_grantors_grantees(index_file)

    # Compare your results to the expected_output
    with open('expected_output.json', 'r') as f:
        expected_output = f.read()

    assert json.dumps(output, sort_keys=True) == expected_output



