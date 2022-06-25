import pandas as pd

def import_data(path):
    df = pd.read_csv(path)
    return df


def missing_values(df):
    '''
    :param data: dataframe
    :return: dataframe with features, number of missing values and percentage of missing values, sort the dataframe by number of missing values
    '''

    missing_values = pd.DataFrame(df.isnull().sum()).reset_index()
    missing_values.columns = ['feature', 'missing_values']
    missing_values['percentage_missing_values'] = (missing_values['missing_values'] / len(df)) * 100
    missing_values = missing_values.sort_values('missing_values', ascending=False)
    return missing_values

