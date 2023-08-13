from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import City, Facility

# Define your database connection URL
DATABASE_URL = "sqlite:///geodata.db"  # Replace with your actual database URL

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define your city_facilities_data
city_facilities_data = [
    {"city_name": "Montgomery", "facility_name": "Public School"},
    # ... more data ...
]

# Loop through the data and populate the associations
for data in city_facilities_data:
    city_name = data["city_name"]
    facility_name = data["facility_name"]

    city = session.query(City).filter_by(name=city_name).first()
    facility = session.query(Facility).filter_by(name=facility_name).first()

    if city and facility:
        city.facilities.append(facility)

session.commit()
