from sqlalchemy import create_engine
from cli_models import Base, State, County, City
engine = create_engine("sqlite:///geodata.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
