from models import State, County, City

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
        population=973764,
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
        name="Hawaii",
        abbreviation="HI",
        population=1455271,
        capital="Honolulu",
        area=10932,
    ),
    State(
        name="Idaho", abbreviation="ID", population=1787065, capital="Boise", area=83569
    ),
    State(
        name="Illinois",
        abbreviation="IL",
        population=12671821,
        capital="Springfield",
        area=57914,
    ),
    State(
        name="Indiana",
        abbreviation="IN",
        population=6732219,
        capital="Indianapolis",
        area=36420,
    ),
    State(
        name="Iowa",
        abbreviation="IA",
        population=3155070,
        capital="Des Moines",
        area=56273,
    ),
    State(
        name="Kansas",
        abbreviation="KS",
        population=2913314,
        capital="Topeka",
        area=82278,
    ),
    State(
        name="Kentucky",
        abbreviation="KY",
        population=4467673,
        capital="Frankfort",
        area=40408,
    ),
    State(
        name="Louisiana",
        abbreviation="LA",
        population=4648794,
        capital="Baton Rouge",
        area=52378,
    ),
    State(
        name="Maine",
        abbreviation="ME",
        population=1344212,
        capital="Augusta",
        area=35380,
    ),
    State(
        name="Maryland",
        abbreviation="MD",
        population=6045680,
        capital="Annapolis",
        area=12406,
    ),
    State(
        name="Massachusetts",
        abbreviation="MA",
        population=6892503,
        capital="Boston",
        area=10554,
    ),
    State(
        name="Michigan",
        abbreviation="MI",
        population=9986857,
        capital="Lansing",
        area=96714,
    ),
    State(
        name="Minnesota",
        abbreviation="MN",
        population=5639632,
        capital="Saint Paul",
        area=86936,
    ),
    State(
        name="Mississippi",
        abbreviation="MS",
        population=2976149,
        capital="Jackson",
        area=48432,
    ),
    State(
        name="Missouri",
        abbreviation="MO",
        population=6137428,
        capital="Jefferson City",
        area=69707,
    ),
    State(
        name="Montana",
        abbreviation="MT",
        population=1068778,
        capital="Helena",
        area=147040,
    ),
    State(
        name="Nebraska",
        abbreviation="NE",
        population=1934408,
        capital="Lincoln",
        area=77348,
    ),
    State(
        name="Nevada",
        abbreviation="NV",
        population=3080156,
        capital="Carson City",
        area=110572,
    ),
    State(
        name="New Hampshire",
        abbreviation="NH",
        population=1359711,
        capital="Concord",
        area=9349,
    ),
    State(
        name="New Jersey",
        abbreviation="NJ",
        population=8882190,
        capital="Trenton",
        area=8723,
    ),
    State(
        name="New Mexico",
        abbreviation="NM",
        population=2117522,
        capital="Santa Fe",
        area=121590,
    ),
    State(
        name="New York",
        abbreviation="NY",
        population=19453561,
        capital="Albany",
        area=54555,
    ),
    State(
        name="North Carolina",
        abbreviation="NC",
        population=10488084,
        capital="Raleigh",
        area=53819,
    ),
    State(
        name="North Dakota",
        abbreviation="ND",
        population=762062,
        capital="Bismarck",
        area=70698,
    ),
    State(
        name="Ohio",
        abbreviation="OH",
        population=11689100,
        capital="Columbus",
        area=44826,
    ),
    State(
        name="Oklahoma",
        abbreviation="OK",
        population=3956971,
        capital="Oklahoma City",
        area=69903,
    ),
    State(
        name="Oregon",
        abbreviation="OR",
        population=4217737,
        capital="Salem",
        area=98379,
    ),
    State(
        name="Pennsylvania",
        abbreviation="PA",
        population=12801989,
        capital="Harrisburg",
        area=46054,
    ),
    State(
        name="Rhode Island",
        abbreviation="RI",
        population=1059361,
        capital="Providence",
        area=1545,
    ),
    State(
        name="South Carolina",
        abbreviation="SC",
        population=5148714,
        capital="Columbia",
        area=32020,
    ),
    State(
        name="South Dakota",
        abbreviation="SD",
        population=884659,
        capital="Pierre",
        area=77116,
    ),
    State(
        name="Tennessee",
        abbreviation="TN",
        population=6829174,
        capital="Nashville",
        area=42144,
    ),
    State(
        name="Texas",
        abbreviation="TX",
        population=28995881,
        capital="Austin",
        area=268596,
    ),
    State(
        name="Utah",
        abbreviation="UT",
        population=3271616,
        capital="Salt Lake City",
        area=84897,
    ),
    State(
        name="Vermont",
        abbreviation="VT",
        population=623989,
        capital="Montpelier",
        area=9616,
    ),
    State(
        name="Virginia",
        abbreviation="VA",
        population=8535519,
        capital="Richmond",
        area=42775,
    ),
    State(
        name="Washington",
        abbreviation="WA",
        population=7614893,
        capital="Olympia",
        area=71298,
    ),
    State(
        name="West Virginia",
        abbreviation="WV",
        population=1792147,
        capital="Charleston",
        area=24230,
    ),
    State(
        name="Wisconsin",
        abbreviation="WI",
        population=5822434,
        capital="Madison",
        area=65496,
    ),
    State(
        name="Wyoming",
        abbreviation="WY",
        population=578759,
        capital="Cheyenne",
        area=97813,
    ),
]


cities = [
    {
        "name": "Montgomery",
        "population": 198525,
        "area": 159.8,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Alabama",
        "county_name": 1846,
    },
    {
        "name": "Juneau",
        "population": 32113,
        "area": 2716.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Alaska",
        "county_name": 1906,
    },
    {
        "name": "Phoenix",
        "population": 1680992,
        "area": 517.6,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Arizona",
        "county_name": 1912,
    },
    {
        "name": "Little Rock",
        "population": 197312,
        "area": 116.2,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Arkansas",
        "county_name": 1821,
    },
    {
        "name": "Sacramento",
        "population": 513624,
        "area": 97.9,
        "latitude": 0,
        "longitude": 0,
        "state_name": "California",
        "county_name": 1854,
    },
    {
        "name": "Denver",
        "population": 727211,
        "area": 153.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Colorado",
        "county_name": 1867,
    },
    {
        "name": "Hartford",
        "population": 122105,
        "area": 17.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Connecticut",
        "county_name": 1875,
    },
    {
        "name": "Dover",
        "population": 38079,
        "area": 22.4,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Delaware",
        "county_name": 1777,
    },
    {
        "name": "Tallahassee",
        "population": 194500,
        "area": 95.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Florida",
        "county_name": 1824,
    },
    {
        "name": "Atlanta",
        "population": 506811,
        "area": 133.5,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Georgia",
        "county_name": 1868,
    },
    {
        "name": "Honolulu",
        "population": 345064,
        "area": 68.4,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Hawaii",
        "county_name": 1845,
    },
    {
        "name": "Boise",
        "population": 228959,
        "area": 63.8,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Idaho",
        "county_name": 1865,
    },
    {
        "name": "Springfield",
        "population": 114230,
        "area": 54,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Illinois",
        "county_name": 1837,
    },
    {
        "name": "Indianapolis",
        "population": 876384,
        "area": 361.5,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Indiana",
        "county_name": 1825,
    },
    {
        "name": "Des Moines",
        "population": 214237,
        "area": 75.8,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Iowa",
        "county_name": 1857,
    },
    {
        "name": "Topeka",
        "population": 125310,
        "area": 56,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Kansas",
        "county_name": 1856,
    },
    {
        "name": "Frankfort",
        "population": 27679,
        "area": 14.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Kentucky",
        "county_name": 1792,
    },
    {
        "name": "Baton Rouge",
        "population": 220236,
        "area": 76.8,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Louisiana",
        "county_name": 1880,
    },
    {
        "name": "Augusta",
        "population": 18681,
        "area": 55.4,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Maine",
        "county_name": 1832,
    },
    {
        "name": "Annapolis",
        "population": 39174,
        "area": 6.73,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Maryland",
        "county_name": 1694,
    },
    {
        "name": "Boston",
        "population": 692600,
        "area": 89.6,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Massachusetts",
        "county_name": 1630,
    },
    {
        "name": "Lansing",
        "population": 118210,
        "area": 35,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Michigan",
        "county_name": 1847,
    },
    {
        "name": "Saint Paul",
        "population": 308096,
        "area": 52.8,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Minnesota",
        "county_name": 1849,
    },
    {
        "name": "Jackson",
        "population": 160628,
        "area": 104.9,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Mississippi",
        "county_name": 1821,
    },
    {
        "name": "Jefferson City",
        "population": 42838,
        "area": 27.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Missouri",
        "county_name": 1826,
    },
    {
        "name": "Helena",
        "population": 3215,
        "area": 14,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Montana",
        "county_name": 1875,
    },
    {
        "name": "Lincoln",
        "population": 289102,
        "area": 74.6,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Nebraska",
        "county_name": 1867,
    },
    {
        "name": "Carson City",
        "population": 55916,
        "area": 143.4,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Nevada",
        "county_name": 1861,
    },
    {
        "name": "Concord",
        "population": 43627,
        "area": 64.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "New Hampshire",
        "county_name": 1808,
    },
    {
        "name": "Trenton",
        "population": 83203,
        "area": 7.66,
        "latitude": 0,
        "longitude": 0,
        "state_name": "New Jersey",
        "county_name": 1784,
    },
    {
        "name": "Santa Fe",
        "population": 84683,
        "area": 37.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "New Mexico",
        "county_name": 1610,
    },
    {
        "name": "Albany",
        "population": 96460,
        "area": 21.4,
        "latitude": 0,
        "longitude": 0,
        "state_name": "New York",
        "county_name": 1797,
    },
    {
        "name": "Raleigh",
        "population": 474069,
        "area": 114.6,
        "latitude": 0,
        "longitude": 0,
        "state_name": "North Carolina",
        "county_name": 1792,
    },
    {
        "name": "Bismarck",
        "population": 73529,
        "area": 26.9,
        "latitude": 0,
        "longitude": 0,
        "state_name": "North Dakota",
        "county_name": 1883,
    },
    {
        "name": "Columbus",
        "population": 898553,
        "area": 210.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Ohio",
        "county_name": 1816,
    },
    {
        "name": "Oklahoma City",
        "population": 655057,
        "area": 620.3,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Oklahoma",
        "county_name": 1910,
    },
    {
        "name": "Salem",
        "population": 174365,
        "area": 45.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Oregon",
        "county_name": 1855,
    },
    {
        "name": "Harrisburg",
        "population": 49528,
        "area": 8.11,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Pennsylvania",
        "county_name": 1812,
    },
    {
        "name": "Providence",
        "population": 179883,
        "area": 18.5,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Rhode Island",
        "county_name": 1900,
    },
    {
        "name": "Columbia",
        "population": 131674,
        "area": 125.2,
        "latitude": 0,
        "longitude": 0,
        "state_name": "South Carolina",
        "county_name": 1786,
    },
    {
        "name": "Pierre",
        "population": 13646,
        "area": 13,
        "latitude": 0,
        "longitude": 0,
        "state_name": "South Dakota",
        "county_name": 1889,
    },
    {
        "name": "Nashville",
        "population": 670820,
        "area": 525.9,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Tennessee",
        "county_name": 1826,
    },
    {
        "name": "Austin",
        "population": 978908,
        "area": 305.1,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Texas",
        "county_name": 1839,
    },
    {
        "name": "Salt Lake City",
        "population": 200567,
        "area": 109.1,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Utah",
        "county_name": 1858,
    },
    {
        "name": "Montpelier",
        "population": 7855,
        "area": 10.2,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Vermont",
        "county_name": 1805,
    },
    {
        "name": "Richmond",
        "population": 230436,
        "area": 60.1,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Virginia",
        "county_name": 1780,
    },
    {
        "name": "Olympia",
        "population": 46478,
        "area": 16.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Washington",
        "county_name": 1853,
    },
    {
        "name": "Charleston",
        "population": 46536,
        "area": 31.6,
        "latitude": 0,
        "longitude": 0,
        "state_name": "West Virginia",
        "county_name": 1885,
    },
    {
        "name": "Madison",
        "population": 259680,
        "area": 68.7,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Wisconsin",
        "county_name": 1838,
    },
    {
        "name": "Cheyenne",
        "population": 64235,
        "area": 21.1,
        "latitude": 0,
        "longitude": 0,
        "state_name": "Wyoming",
        "county_name": 1869,
    }
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

facilities_to_add = [
    {
        "name": "Public School",
        "description": "An educational institution for children aged 5-18",
        "facility_type": "Education",
    },
    {
        "name": "Public Library",
        "description": "A facility where people can borrow books and access digital resources",
        "facility_type": "Education",
    },
    {
        "name": "Public Hospital",
        "description": "A healthcare institution providing treatment with specialized medical and nursing staff",
        "facility_type": "Healthcare",
    },
    {
        "name": "Community Park",
        "description": "A green area reserved for recreational activities, often equipped with playgrounds, benches, and sports fields",
        "facility_type": "Recreation",
    },
    {
        "name": "Police Station",
        "description": "A building where local police officers work and where people can report crimes",
        "facility_type": "Safety and Security",
    },
    {
        "name": "Fire Station",
        "description": "A building housing emergency equipment and personnel for firefighting",
        "facility_type": "Safety and Security",
    },
    {
        "name": "Public Gym",
        "description": "A facility equipped with exercise machines and weights for physical fitness",
        "facility_type": "Recreation",
    },
    {
        "name": "Municipal Office",
        "description": "An office where local government administrative activities take place",
        "facility_type": "Government",
    },
    {
        "name": "Public Swimming Pool",
        "description": "A facility where individuals can swim, often overseen by lifeguards",
        "facility_type": "Recreation",
    },
    {
        "name": "Post Office",
        "description": "A facility where mail is processed and sent, and where people can buy postage stamps, send packages, etc.",
        "facility_type": "Communication",
    },
]


city_facilities_to_add = [
    
    {"city_name": "Montgomery", "facility_name": "Public School"},
    {"city_name": "Montgomery", "facility_name": "Public Library"},
    {"city_name": "Montgomery", "facility_name": "Community Park"},
    {"city_name": "Juneau", "facility_name": "Public Hospital"},
    {"city_name": "Juneau", "facility_name": "Community Park"},
    {"city_name": "Phoenix", "facility_name": "Public Gym"},
    {"city_name": "Phoenix", "facility_name": "Police Station"},
    {"city_name": "Little Rock", "facility_name": "Fire Station"},
    {"city_name": "Sacramento", "facility_name": "Public Swimming Pool"},
    {"city_name": "Denver", "facility_name": "Municipal Office"},
    {"city_name": "Hartford", "facility_name": "Post Office"},
    {"city_name": "Dover", "facility_name": "Public School"},
    {"city_name": "Dover", "facility_name": "Police Station"},
    {"city_name": "Tallahassee", "facility_name": "Public Library"},
    {"city_name": "Tallahassee", "facility_name": "Community Park"},
    {"city_name": "Atlanta", "facility_name": "Public Gym"},
    {"city_name": "Atlanta", "facility_name": "Municipal Office"},
    {"city_name": "Honolulu", "facility_name": "Public School"},
    {"city_name": "Honolulu", "facility_name": "Public Swimming Pool"},
    {"city_name": "Boise", "facility_name": "Public Library"},
    {"city_name": "Boise", "facility_name": "Police Station"},
    {"city_name": "Springfield", "facility_name": "Fire Station"},
    {"city_name": "Indianapolis", "facility_name": "Public Gym"},
    {"city_name": "Indianapolis", "facility_name": "Public Hospital"},
    {"city_name": "Des Moines", "facility_name": "Public School"},
    {"city_name": "Des Moines", "facility_name": "Community Park"},
    {"city_name": "Topeka", "facility_name": "Public Library"},
    {"city_name": "Topeka", "facility_name": "Municipal Office"},
    {"city_name": "Frankfort", "facility_name": "Public School"},
    {"city_name": "Frankfort", "facility_name": "Fire Station"},
    {"city_name": "Baton Rouge", "facility_name": "Public Library"},
    {"city_name": "Baton Rouge", "facility_name": "Police Station"},
    {"city_name": "Augusta", "facility_name": "Public Hospital"},
    {"city_name": "Augusta", "facility_name": "Community Park"},
    {"city_name": "Annapolis", "facility_name": "Public School"},
    {"city_name": "Annapolis", "facility_name": "Public Library"},
    {"city_name": "Boston", "facility_name": "Public Gym"},
    {"city_name": "Boston", "facility_name": "Municipal Office"},
    {"city_name": "Lansing", "facility_name": "Public Hospital"},
    {"city_name": "Lansing", "facility_name": "Public Swimming Pool"},
    {"city_name": "Saint Paul", "facility_name": "Public School"},
    {"city_name": "Saint Paul", "facility_name": "Public Library"},
    {"city_name": "Jackson", "facility_name": "Fire Station"},
    {"city_name": "Jefferson City", "facility_name": "Public Gym"},
    {"city_name": "Jefferson City", "facility_name": "Municipal Office"},
    {"city_name": "Helena", "facility_name": "Public School"},
    {"city_name": "Helena", "facility_name": "Public Hospital"},
    {"city_name": "Lincoln", "facility_name": "Public Library"},
    {"city_name": "Lincoln", "facility_name": "Police Station"},
    {"city_name": "Carson City", "facility_name": "Fire Station"},
    {"city_name": "Concord", "facility_name": "Public Gym"},
    {"city_name": "Concord", "facility_name": "Municipal Office"},
    {"city_name": "Trenton", "facility_name": "Public School"},
    {"city_name": "Trenton", "facility_name": "Public Library"},
    {"city_name": "Santa Fe", "facility_name": "Public Hospital"},
    {"city_name": "Santa Fe", "facility_name": "Community Park"},
    {"city_name": "Albany", "facility_name": "Public School"},
    {"city_name": "Albany", "facility_name": "Police Station"},
    {"city_name": "Raleigh", "facility_name": "Public Library"},
    {"city_name": "Raleigh", "facility_name": "Municipal Office"},
    {"city_name": "Bismarck", "facility_name": "Public School"},
    {"city_name": "Bismarck", "facility_name": "Public Library"},
    {"city_name": "Columbus", "facility_name": "Public Gym"},
    {"city_name": "Columbus", "facility_name": "Police Station"},
    {"city_name": "Oklahoma City", "facility_name": "Fire Station"},
    {"city_name": "Oklahoma City", "facility_name": "Public Swimming Pool"},
    {"city_name": "Salem", "facility_name": "Public School"},
    {"city_name": "Salem", "facility_name": "Public Library"},
    {"city_name": "Harrisburg", "facility_name": "Public Gym"},
    {"city_name": "Harrisburg", "facility_name": "Municipal Office"},
    {"city_name": "Providence", "facility_name": "Public Hospital"},
    {"city_name": "Providence", "facility_name": "Community Park"},
    {"city_name": "Columbia", "facility_name": "Public School"},
    {"city_name": "Columbia", "facility_name": "Public Library"},
    {"city_name": "Pierre", "facility_name": "Public Gym"},
    {"city_name": "Pierre", "facility_name": "Municipal Office"},
    {"city_name": "Nashville", "facility_name": "Public School"},
    {"city_name": "Nashville", "facility_name": "Police Station"},
    {"city_name": "Austin", "facility_name": "Public Hospital"},
    {"city_name": "Austin", "facility_name": "Community Park"},
    {"city_name": "Salt Lake City", "facility_name": "Public School"},
    {"city_name": "Salt Lake City", "facility_name": "Police Station"},
    {"city_name": "Montpelier", "facility_name": "Fire Station"},
    {"city_name": "Richmond", "facility_name": "Public Gym"},
    {"city_name": "Richmond", "facility_name": "Municipal Office"},
    {"city_name": "Olympia", "facility_name": "Public Hospital"},
    {"city_name": "Olympia", "facility_name": "Public Library"},
    {"city_name": "Charleston", "facility_name": "Public Gym"},
    {"city_name": "Charleston", "facility_name": "Police Station"},
    {"city_name": "Madison", "facility_name": "Fire Station"},
    {"city_name": "Madison", "facility_name": "Public Swimming Pool"},
    {"city_name": "Cheyenne", "facility_name": "Public School"},
    {"city_name": "Cheyenne", "facility_name": "Public Library"},
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
    }
]