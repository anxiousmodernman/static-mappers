from staticloaders.zoominfo_may_2014 import *
from mappings import *


def load_data():
    data = load_zoom_position_level()
    return data


def map_columns(df, maps):
    df['norm_position_level'] = df['z_pos_level'].map(lambda x: maps[x][0] if x in maps.keys() else None)
    df['nmvid'] = df['z_pos_level'].map(lambda x: maps[x][1] if x in maps.keys() else 0)
    df['nmvid'].fillna(0)
    df.nmvid = df.nmvid.astype('int64')
    return df


def main():
    data = load_data()
    data = map_columns(data, position_level_mappings)
    data.to_csv('target/zoominfo_position_level.csv', index=False)
    print 'Done.'


if __name__ == '__main__':
    main()