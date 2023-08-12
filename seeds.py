from models import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_config import states_to_add  # Importing the list from data_config.py

print("🌱 Seeding DB...")
engine = create_engine('sqlite:///geodata.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(State).delete()

# Since you've already imported the list, you can directly use it here.
session.bulk_save_objects(states_to_add)
session.commit()

print("✅ Done seeding!")
