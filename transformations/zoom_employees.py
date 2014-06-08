from staticloaders.zoominfo_may_2014 import *
import numpy as np


def bin_employees(value):
    if value >= 50000:
        norm_value = ('50,000 and above', 11)
    elif value >= 25000 and value < 50000:
        norm_value = ('25,000 to 50,000', 77)
    elif value >= 10000 and value < 25000:
        norm_value = ('10,000 to 25,000', 78)
    elif value >= 5000 and value < 10000:
        norm_value = ('5,000 to 10,000', 79)
    elif value >= 1000 and value < 5000:
        norm_value = ('1,000 to 5,000', 80)
    elif value >= 500 and value < 1000:
        norm_value = ('500 to 1,000', 81)
    elif value >= 100 and value < 500:
        norm_value = ('100 to 500', 82)
    elif value >= 50 and value < 100:
        norm_value = ('50 to 100', 15)
    elif value >= 10 and value < 50:
        norm_value = ('10 to 50', 83)
    elif value >= 1 and value < 10:
        norm_value = ('Less than 10', 84)
    else:
        norm_value = (None, None)
    return norm_value


def load_data():
    data = load_zoom_employees()
    return data


def map_columns(df):
    df['norm_num_employees'] = df['employees'].map(lambda x: bin_employees(x)[0])
    df['nmvid'] = df['employees'].map(lambda x: bin_employees(x)[1])
    df['nmvid'] = df['nmvid'].map(lambda x: 0 if isinstance(x, np.NaN) else x)   # TODO FIX
    return df


def main():
    data = load_data()
    data = map_columns(data)
    data.to_csv('target/zoominfo_employees.csv', index=False)
    print 'Done.'


if __name__ == '__main__':
    main()