from sqlalchemy import create_engine

def get_mssql_engine(config):
    engine = create_engine('mssql+pyodbc://%s:%s@%s' %
                           (config.username,
                            config.password,
                            config.dsn)
                           )
    return engine


def get_postgres_engine(config):
    engine = create_engine('postgresql://%s:%s@%s/%s' %
                           (config.username,
                            config.password,
                            config.host,
                            config.database)
                           )
    return engine