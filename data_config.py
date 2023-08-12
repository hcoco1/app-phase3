from models import State, County, City

states_to_add = [
    State(name="Alabama", abbreviation="AL", population=4903185, capital="Montgomery", area=52420),
    State(name="Alaska", abbreviation="AK", population=731545, capital="Juneau", area=665384),
    State(name="Arizona", abbreviation="AZ", population=7278717, capital="Phoenix", area=113990),
    State(name="Arkansas", abbreviation="AR", population=3017804, capital="Little Rock", area=53179),
    State(name="California", abbreviation="CA", population=39538223, capital="Sacramento", area=163695),
    State(name="Colorado", abbreviation="CO", population=5773714, capital="Denver", area=104094),
    State(name="Connecticut", abbreviation="CT", population=3565287, capital="Hartford", area=5543),
    State(name="Delaware", abbreviation="DE", population=989948, capital="Dover", area=2489),
    State(name="Florida", abbreviation="FL", population=21538187, capital="Tallahassee", area=65758),
    State(name="Georgia", abbreviation="GA", population=10617423, capital="Atlanta", area=59425),
    State(name="Hawaii", abbreviation="HI", population=1455271, capital="Honolulu", area=10932),
    State(name="Idaho", abbreviation="ID", population=1787065, capital="Boise", area=83569),
    State(name="Illinois", abbreviation="IL", population=12671821, capital="Springfield", area=57914),
    State(name="Indiana", abbreviation="IN", population=6732219, capital="Indianapolis", area=36420),
    State(name="Iowa", abbreviation="IA", population=3155070, capital="Des Moines", area=56273),
    State(name="Kansas", abbreviation="KS", population=2913314, capital="Topeka", area=82278),
    State(name="Kentucky", abbreviation="KY", population=4467673, capital="Frankfort", area=40408),
    State(name="Louisiana", abbreviation="LA", population=4648794, capital="Baton Rouge", area=52378),
    State(name="Maine", abbreviation="ME", population=1344212, capital="Augusta", area=35380),
    State(name="Maryland", abbreviation="MD", population=6045680, capital="Annapolis", area=12406),
    State(name="Massachusetts", abbreviation="MA", population=6892503, capital="Boston", area=10554),
    State(name="Michigan", abbreviation="MI", population=9986857, capital="Lansing", area=96714),
    State(name="Minnesota", abbreviation="MN", population=5639632, capital="Saint Paul", area=86936),
    State(name="Mississippi", abbreviation="MS", population=2976149, capital="Jackson", area=48432),
    State(name="Missouri", abbreviation="MO", population=6137428, capital="Jefferson City", area=69707),
    State(name="Montana", abbreviation="MT", population=1068778, capital="Helena", area=147040),
    State(name="Nebraska", abbreviation="NE", population=1934408, capital="Lincoln", area=77348),
    State(name="Nevada", abbreviation="NV", population=3080156, capital="Carson City", area=110572),
    State(name="New Hampshire", abbreviation="NH", population=1359711, capital="Concord", area=9349),
    State(name="New Jersey", abbreviation="NJ", population=8882190, capital="Trenton", area=8723),
    State(name="New York", abbreviation="NY", population=10617423, capital="New York", area=59425)
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
    },
]
