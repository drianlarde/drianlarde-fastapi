import databases
import ormar
import sqlalchemy

metadata = sqlalchemy.MetaData()
databases = databases.Database("sqlite:///sqlite.db")
engine = sqlalchemy.create_engine("sqlite:///sqlite.db")

class MainMata(ormar.ModelMeta):
    metadata = metadata
    database = databases

