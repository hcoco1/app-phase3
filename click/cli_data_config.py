from cli_models import State, County, City

states_to_add = [
    State(
        name="Alabama",
        abbreviation="AL",
        population=4903185,
        capital="Montgomery",
        area=52420,
    ),
    State(
        name="Alaska",
        abbreviation="AK",
        population=731545,
        capital="Juneau",
        area=665384,
    ),
    State(
        name="Arizona",
        abbreviation="AZ",
        population=7278717,
        capital="Phoenix",
        area=113990,
    ),
    State(
        name="Arkansas",
        abbreviation="AR",
        population=3017804,
        capital="Little Rock",
        area=53179,
    ),
    State(
        name="California",
        abbreviation="CA",
        population=39538223,
        capital="Sacramento",
        area=163695,
    ),
    State(
        name="Colorado",
        abbreviation="CO",
        population=5773714,
        capital="Denver",
        area=104094,
    ),
    State(
        name="Connecticut",
        abbreviation="CT",
        population=3565287,
        capital="Hartford",
        area=5543,
    ),
    State(
        name="Delaware",
        abbreviation="DE",
        population=989948,
        capital="Dover",
        area=2489,
    ),
    State(
        name="Florida",
        abbreviation="FL",
        population=21538187,
        capital="Tallahassee",
        area=65758,
    ),
    State(
        name="Georgia",
        abbreviation="GA",
        population=10617423,
        capital="Atlanta",
        area=59425,
    ),
    State(
        name="New York",
        abbreviation="NY",
        population=10617423,
        capital="New York",
        area=59425,
    ),
]

counties_to_add = [
    {
        "name": "Orange",
        "population": 1393452,  # As of 2019
        "area": 903,  # Square miles
        "state_name": "Florida",
        "city_name": "Orlando",
    },
    {
        "name": "Seminole",
        "population": 471826,  # As of 2019
        "area": 309,  # Square miles
        "state_name": "Florida",
        "city_name": "Orlando",
    },
    {
        "name": "Lake County",
        "population": 367118,  # As of 2019
        "area": 953,  # Square miles
        "state_name": "Florida",
        "city_name": "Orlando",
    },
    {
        "name": "Osceola",
        "population": 375751,  # As of 2019
        "area": 1325,  # Square miles
        "state_name": "Florida",
        "city_name": "Orlando",
    },
    {
        "name": "Miami Dade",
        "population": 2716940,  # As of 2019
        "area": 1898,  # Square miles
        "state_name": "Florida",
        "city_name": "Miami",
    },
    {
        "name": "Broward",
        "population": 1952778,  # As of 2019
        "area": 1209,  # Square miles
        "state_name": "Florida",
        "city_name": "Fort Lauderdale",
    },
    {
        "name": "Palm Beach",
        "population": 1496770,  # As of 2019
        "area": 1969,  # Square miles
        "state_name": "Florida",
        "city_name": "West Palm Beach",
    },
    {
        "name": "Hillsborough",
        "population": 1471968,  # As of 2019
        "area": 1020,  # Square miles
        "state_name": "Florida",
        "city_name": "Tampa",
    },
    {
        "name": "Pinellas",
        "population": 974996,  # As of 2019
        "area": 274,  # Square miles
        "state_name": "Florida",
        "city_name": "St. Petersburg",
    },
    {
        "name": "Duval",
        "population": 957755,  # As of 2019
        "area": 762,  # Square miles
        "state_name": "Florida",
        "city_name": "Jacksonville",
    },
    {
        "name": "Lee",
        "population": 770577,  # As of 2019
        "area": 785,  # Square miles
        "state_name": "Florida",
        "city_name": "Fort Myers",
    },
    {
        "name": "Polk",
        "population": 724777,  # As of 2019
        "area": 1798,  # Square miles
        "state_name": "Florida",
        "city_name": "Lakeland",
    },
    {
        "name": "Kings (Brooklyn)",
        "population": 2559903,  # As of 2019
        "area": 69,  # Square miles
        "state_name": "New York",
        "city_name": "Brooklyn",
    },
    {
        "name": "Queens",
        "population": 2253858,  # As of 2019
        "area": 108,  # Square miles
        "state_name": "New York",
        "city_name": "Queens",
    },
    {
        "name": "New York (Manhattan)",
        "population": 1628706,  # As of 2019
        "area": 22.7,  # Square miles
        "state_name": "New York",
        "city_name": "Manhattan",
    },
    {
        "name": "Suffolk",
        "population": 1476601,  # As of 2019
        "area": 912,  # Square miles
        "state_name": "New York",
        "city_name": "Riverhead",
    },
    {
        "name": "Bronx",
        "population": 1472654,  # As of 2019
        "area": 42,  # Square miles
        "state_name": "New York",
        "city_name": "The Bronx",
    },
    {
        "name": "Nassau",
        "population": 1356924,  # As of 2019
        "area": 285,  # Square miles
        "state_name": "New York",
        "city_name": "Mineola",
    },
    {
        "name": "Westchester",
        "population": 967506,  # As of 2019
        "area": 432,  # Square miles
        "state_name": "New York",
        "city_name": "White Plains",
    },
    {
        "name": "Erie",
        "population": 918702,  # As of 2019
        "area": 1044,  # Square miles
        "state_name": "New York",
        "city_name": "Buffalo",
    },
    {
        "name": "Monroe",
        "population": 741770,  # As of 2019
        "area": 657,  # Square miles
        "state_name": "New York",
        "city_name": "Rochester",
    },
    {
        "name": "Richmond (Staten Island)",
        "population": 476143,  # As of 2019
        "area": 57,  # Square miles
        "state_name": "New York",
        "city_name": "Staten Island",
    },
]

cities_to_add = [
    {
        "name": "Orlando",
        "population": 1393452,  # Population from Orange county
        "area": 903,  # Area from Orange county
        "latitude": 28.5383,
        "longitude": -81.3792,
        "state_name": "Florida",
        "county_name": "Orange",
    },
    {
        "name": "Sanford",  # Changed city name for Seminole county
        "population": 471826,  # Population from Seminole county
        "area": 309,  # Area from Seminole county
        "latitude": 28.8025,
        "longitude": -81.2691,
        "state_name": "Florida",
        "county_name": "Seminole",
    },
    {
        "name": "Tavares",  # Changed city name for Lake County
        "population": 367118,  # Population from Lake County
        "area": 953,  # Area from Lake County
        "latitude": 28.8042,
        "longitude": -81.7256,
        "state_name": "Florida",
        "county_name": "Lake County",
    },
    {
        "name": "Kissimmee",  # Changed city name for Osceola county
        "population": 375751,  # Population from Osceola county
        "area": 1325,  # Area from Osceola county
        "latitude": 28.2916,
        "longitude": -81.4076,
        "state_name": "Florida",
        "county_name": "Osceola",
    },
    {
        "name": "Miami",
        "population": 2716940,  # Population from Miami Dade county
        "area": 1898,  # Area from Miami Dade county
        "latitude": 25.7617,
        "longitude": -80.1918,
        "state_name": "Florida",
        "county_name": "Miami Dade",
    },
    {
        "name": "New York City",  # Sample city for New York state
        "population": 1628706,  # Population from New York (Manhattan) county
        "area": 22.7,  # Area from New York (Manhattan) county
        "latitude": 40.7128,
        "longitude": -74.0060,
        "state_name": "New York",
        "county_name": "New York (Manhattan)",
    }
]

    
    