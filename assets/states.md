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
