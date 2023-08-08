#!/usr/bin/env python3

import click
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create SQLite database and connect
engine = create_engine('sqlite:///geodata.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class State(Base):
    __tablename__ = 'states'
    StateID = Column(Integer, primary_key=True)
    StateName = Column(String)
    Abbreviation = Column(String)
    Population = Column(Integer)
    Capital = Column(String)
    Area = Column(Float)

class County(Base):
    __tablename__ = 'counties'
    CountyID = Column(Integer, primary_key=True)
    CountyName = Column(String)
    Population = Column(Integer)
    Area = Column(Float)
    StateID = Column(Integer, ForeignKey('states.StateID'))

class City(Base):
    __tablename__ = 'cities'
    CityID = Column(Integer, primary_key=True)
    CityName = Column(String)
    Population = Column(Integer)
    Latitude = Column(Float)
    Longitude = Column(Float)
    StateID = Column(Integer, ForeignKey('states.StateID'))
    CountyID = Column(Integer, ForeignKey('counties.CountyID'))

class CityCounty(Base):
    __tablename__ = 'citycounties'
    CityCountyID = Column(Integer, primary_key=True)
    CityID = Column(Integer, ForeignKey('cities.CityID'))
    CountyID = Column(Integer, ForeignKey('counties.CountyID'))

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    """Create the database tables."""
    Base.metadata.create_all(engine)
    click.echo('Initialized the database.')

if __name__ == '__main__':
    cli()



