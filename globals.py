from sqlalchemy.orm import sessionmaker

from database.config import AlchemySandboxConfig
from database import get_mssql_engine

# end this with a slash
DATA_DIR = '/home/cmcfarland/Dropbox/WProjects/Zoominfo_2014/appended/'

SANDBOX_CONFIG = AlchemySandboxConfig()

alchemy_sandbox_engine = get_mssql_engine(SANDBOX_CONFIG)
AlchemySandboxSession = sessionmaker(bind=alchemy_sandbox_engine)

