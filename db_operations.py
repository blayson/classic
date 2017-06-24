#!/usr/bin/env python3

# for install psycopg2 for Python 3 use sudo apt-get install python3-psycopg2

import psycopg2

database_name = "test_database"
user_name = "test_master"
host_name = "test-database.cvzlexvifitu.eu-central-1.rds.amazonaws.com"
port = "5432"
passwd = "testpassword"

create_commands = (
			"""
				CREATE TABLE Users (
					user_id SERIAL PRIMARY KEY,
					name VARCHAR (50) UNIQUE NOT NULL,
					surname VARCHAR (50) UNIQUE NOT NULL,
					age INTEGER NOT NULL,
					foto BYTEA,
					contact VARCHAR (100)
				)
			""",
			"""
				CREATE TABLE Airport_City (
					airport_abbr VARCHAR (3) PRIMARY KEY,
					city_name VARCHAR (50) NOT NULL
				)
			""",
			"""
				CREATE TABLE Trips (
					trip_id SERIAL PRIMARY KEY,
					dest VARCHAR (3) NOT NULL,
					date DATE NOT NULL,
					time TIME NOT NULL,
					time_diff INTEGER NOT NULL,
					max_cap INTEGER NOT NULL,

					CONSTRAINT dest_to_airport_abbr FOREIGN KEY (dest)
      				REFERENCES Airport_City (airport_abbr) MATCH SIMPLE
      				ON UPDATE NO ACTION ON DELETE NO ACTION	
				)
			""",
			"""
				CREATE TABLE Flights (
					flight_id SERIAL PRIMARY KEY,
					from_tmsp INTEGER NOT NULL,
					to_tmsp INTEGER NOT NULL,
					cost INTEGER NOT NULL,
					duration INTEGER NOT NULL,
					from_location VARCHAR (3) NOT NULL,

					CONSTRAINT from_loc_to_airport_abbr FOREIGN KEY (from_location)
					REFERENCES Airport_City (airport_abbr) MATCH SIMPLE
      				ON UPDATE NO ACTION ON DELETE NO ACTION
				)
			"""
	)

drop_commands = (
			"""
			DROP TABLE Users
			""",
			"""
			DROP TABLE Trips
			""",
			"""
			DROP TABLE Flights
			""",
			"""
			DROP TABLE Airport_City
			"""
	)

def create_tables():
	try:
	    conn = psycopg2.connect(dbname = database_name, user = user_name, host = host_name, port = port, password = passwd)
	    cur = conn.cursor()
	    
	    for command in create_commands:
	    	cur.execute(command)

	    for command in drop_commands:
	    	cur.execute(command)

	    cur.close()
	    conn.commit()

	    print("All is OK")

	except Exception as e:
	    print(e)
	    print("I am unable to connect to the database")

	finally:
	    if conn is not None:
	        conn.close()

if __name__ == '__main__':
	create_tables()
