import pandas as pd
from globals import DATA_DIR

# hardcoded values for specific files
def load_zoom_pos_func():
    path = ''.join([DATA_DIR, 'smartbrief_function.csv'])
    columns = ['recordid', 'email', 'match_status', 'zoomid', 'title', 'position_function']
    df = pd.read_table(path, names=columns, sep=',', skiprows=0)
    return df


def load_zoom_company_type():
    path = ''.join([DATA_DIR, 'missing_norm_company_type_appended.csv'])
    #email,Zoom company ID,Industry label,Secondary industry label
    columns = ['email', 'zoom_company_id', 'industry_label', 'secondary_industry_label']
    df = pd.read_table(path, names=columns, sep=',', skiprows=0)
    return df


def load_zoom_position_level():
    path = ''.join([DATA_DIR, 'missing_norm_position_level_appended.csv'])
    # email,Zoom Individual ID,Management Level
    columns = ['email', 'zoomid', 'z_pos_level']
    df = pd.read_csv(path, names=columns, sep=',', skiprows=1)
    return df


def load_zoom_employees():
    path = ''.join([DATA_DIR, 'missing_norm_num_employees_appended.csv'])
    # email,Zoom company ID,Employees
    columns = ['email', 'zoom_company_id', 'employees']
    df = pd.read_csv(path, names=columns, sep=',', skiprows=1)
    return df

