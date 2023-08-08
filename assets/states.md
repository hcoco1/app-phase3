create table states (
	StateName VARCHAR(50),
	Abbreviation VARCHAR(50),
	Population INT,
	Capital VARCHAR(50),
	Area INT
);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Illinois', 'IL', 572416, 'Chicago', 74810);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Texas', 'TX', 3856813, 'Houston', 261061);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Alabama', 'AL', 1400268, 'Birmingham', 62206);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Indiana', 'IN', 650597, 'Crawfordsville', 254996);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Missouri', 'MO', 3858148, 'Kansas City', 217318);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Texas', 'TX', 1737126, 'El Paso', 294710);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Oklahoma', 'OK', 1743791, 'Tulsa', 204646);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Delaware', 'DE', 2432814, 'Newark', 272971);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Arizona', 'AZ', 1481513, 'Gilbert', 219024);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('California', 'CA', 1642739, 'San Jose', 193225);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('District of Columbia', 'DC', 3706174, 'Washington', 1912);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Tennessee', 'TN', 2967424, 'Nashville', 199990);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Florida', 'FL', 4615458, 'Lehigh Acres', 78523);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('District of Columbia', 'DC', 4920035, 'Washington', 248355);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Texas', 'TX', 2168666, 'San Antonio', 262329);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('California', 'CA', 3117431, 'Hayward', 173099);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('New Jersey', 'NJ', 1421164, 'Trenton', 156607);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Connecticut', 'CT', 3461452, 'Hartford', 191523);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Missouri', 'MO', 3427132, 'Independence', 255529);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('California', 'CA', 2439614, 'San Diego', 129468);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('California', 'CA', 2193038, 'Santa Ana', 102624);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Tennessee', 'TN', 2891787, 'Memphis', 294847);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Ohio', 'OH', 4509421, 'Cincinnati', 83227);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Nebraska', 'NE', 2422350, 'Omaha', 96799);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Alabama', 'AL', 3185584, 'Birmingham', 272678);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('California', 'CA', 2576565, 'Sacramento', 115602);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('New York', 'NY', 2399022, 'Brooklyn', 23004);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Florida', 'FL', 951409, 'Lakeland', 178540);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Missouri', 'MO', 645449, 'Kansas City', 24520);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Hawaii', 'HI', 2741680, 'Honolulu', 108045);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Minnesota', 'MN', 2966503, 'Minneapolis', 60602);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Arizona', 'AZ', 3171934, 'Phoenix', 299855);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Florida', 'FL', 3668237, 'Miami', 168243);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Massachusetts', 'MA', 4936117, 'Newton', 60788);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Pennsylvania', 'PA', 506268, 'Harrisburg', 26013);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Virginia', 'VA', 28388, 'Roanoke', 87413);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Illinois', 'IL', 2563009, 'Rockford', 51444);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Ohio', 'OH', 1539044, 'Youngstown', 92506);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Illinois', 'IL', 4259604, 'Chicago', 111302);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('California', 'CA', 413314, 'Fresno', 82672);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Illinois', 'IL', 2742938, 'Chicago', 163512);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Georgia', 'GA', 3907138, 'Marietta', 290593);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Utah', 'UT', 3140692, 'Salt Lake City', 87912);
insert into states (StateName, Abbreviation, Population, Capital, Area) values ('Pennsylvania', 'PA', 1793878, 'Wilkes Barre', 258703);





1. Adding Only One State:
To add just a state, you'd create an instance of the State class and then add it to the session:

# Create a new state
new_state = State(name="StateName", abbreviation="SN", population=1000000, capital="StateCapital", area=4000)

# Add the new state to the session
session.add(new_state)

# Commit the session to persist the change to the database
session.commit()











     



	  # Add all provided states using instances of the State class
    states_to_add = [
		        State(name='Illinois', abbreviation='IL', population=572416, capital='Chicago', area=74810),
        State(name='Texas', abbreviation='TX', population=3856813, capital='Houston', area=261061),
        State(name='Alabama', abbreviation='AL', population=1400268, capital='Birmingham', area=62206),
        State(name='Indiana', abbreviation='IN', population=650597, capital='Crawfordsville', area=254996),
        State(name='Missouri', abbreviation='MO', population=3858148, capital='Kansas City', area=217318),
        State(name='Oklahoma', abbreviation='OK', population=1743791, capital='Tulsa', area=204646),
        State(name='Delaware', abbreviation='DE', population=2432814, capital='Newark', area=272971),
        State(name='Arizona', abbreviation='AZ', population=1481513, capital='Gilbert', area=219024),
        State(name='California', abbreviation='CA', population=1642739, capital='San Jose', area=193225),
        State(name='District of Columbia', abbreviation='DC', population=3706174, capital='Washington', area=1912),
        State(name='Tennessee', abbreviation='TN', population=2967424, capital='Nashville', area=199990),
        State(name='Florida', abbreviation='FL', population=4615458, capital='Lehigh Acres', area=78523),
        State(name='District of Columbia', abbreviation='DC', population=4920035, capital='Washington', area=248355),
        State(name='New Jersey', abbreviation='NJ', population=1421164, capital='Trenton', area=156607),
        State(name='Connecticut', abbreviation='CT', population=3461452, capital='Hartford', area=191523),
        State(name='Missouri', abbreviation='MO', population=3427132, capital='Independence', area=255529),
        State(name='Ohio', abbreviation='OH', population=4509421, capital='Cincinnati', area=83227),
        State(name='Nebraska', abbreviation='NE', population=2422350, capital='Omaha', area=96799),
        State(name='New York', abbreviation='NY', population=2399022, capital='Brooklyn', area=23004),
        State(name='Hawaii', abbreviation='HI', population=2741680, capital='Honolulu', area=108045),
        State(name='Minnesota', abbreviation='MN', population=2966503, capital='Minneapolis', area=60602),
        State(name='Massachusetts', abbreviation='MA', population=4936117, capital='Newton', area=60788),
        State(name='Pennsylvania', abbreviation='PA', population=506268, capital='Harrisburg', area=26013)
     
    ]

    session.add_all(states_to_add)
    session.commit()