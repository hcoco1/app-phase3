#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship  # Updated import here
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from termcolor import colored

Base = declarative_base()

class State(Base):
    __tablename__ = 'States'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    abbreviation = Column(String(255))
    population = Column(Integer)
    capital = Column(String(255))
    area = Column(Float)
    
    # ORM relationships
    counties = relationship('County', back_populates='state')
    cities = relationship('City', backref='state')

    def __repr__(self):
        return f"<State(id={self.id}, name={self.name}, abbreviation={self.abbreviation}, population={self.population}, capital={self.capital}, area={self.area})>"

class County(Base):
    __tablename__ = 'Counties'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    area = Column(Float)
    
    state_id = Column(Integer, ForeignKey('States.id'))
    state = relationship('State', back_populates='counties')
    
    # ORM relationships
    cities = relationship('City', back_populates='county')

    def __repr__(self):
        return f"<County(id={self.id}, name={self.name}, population={self.population}, area={self.area}, state_id={self.state_id})>"

class City(Base):
    __tablename__ = 'Cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    area = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    
    state_id = Column(Integer, ForeignKey('States.id'))
    county_id = Column(Integer, ForeignKey('Counties.id'))  # Foreign key to Counties table
    
    # ORM relationships
    county = relationship('County', back_populates='cities')

    def __repr__(self):
        return f"<City(id={self.id}, name={self.name}, population={self.population}, area={self.area}, latitude={self.latitude}, longitude={self.longitude}, state_id={self.state_id}, county_id={self.county_id})>"

if __name__ == '__main__':
    # Create an SQLite database and the tables
    engine = create_engine('sqlite:///geodata.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
# 2. ✅ Create a record and add it to the database
    
# Create a new state
new_state = State(name="California", abbreviation="CA", population=2000000, capital="Sacramento", area=5000)

# Create a new city and associate it with the new state
new_city = City(name="Los Angeles", population=100000, area=250, latitude=12.345, longitude=67.890, state=new_state)

# Create a new county and associate it with the new state
new_county = County(name="Smith County", population=500000, area=1000, state=new_state)

# Since cities and counties are associated with the state, adding the state will also add its associated cities and counties
session.add(new_state)

# Commit the session to persist changes to the database
session.commit()

print(f"Added state: {new_state.name} with city: {new_city.name} and county: {new_county.name}")

session.close()










# 3. ✅ Query all states. 

#    all_states = session.query(State).all()
#    for state in all_states:
#        print(colored(state, 'blue'))
#    session.close()




# 4. ✅ Query all students by name.
# 5. ✅ Query all students by name, and order by name. 
# 6. ✅ Query all students by name, order by name, descending.
# 7. ✅ Limit student query to 1 result
# 8. ✅ Use the SQLAlchemy func.count function to report how many student entries exist.
# 9. ✅ Filter student query results by name
# 10. ✅ Update the student data for a single column. 
# 11. ✅ Delete a student database entry/row. 