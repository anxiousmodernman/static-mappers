import pandas as pd
from staticloaders.zoominfo_may_2014 import *
from mappings import *


def load_data():
    data = load_zoom_company_type()
    return data


def map_columns(df, maps):
    df['norm_company_type'] = df['industry_label'].map(lambda x: maps[x][0] if x in maps.keys() else None)
    df['nmvid'] = df['industry_label'].map(lambda x: maps[x][1] if x in maps.keys() else 0)
    df['nmvid'].fillna(0)
    df.nmvid = df.nmvid.astype('int64')
    return df


def main():
    data = load_data()
    data = map_columns(data, company_type_mappings)
    data.to_csv('target/zoominfo_company_type.csv', index=False)
    print 'Done.'


if __name__ == '__main__':
    main()
