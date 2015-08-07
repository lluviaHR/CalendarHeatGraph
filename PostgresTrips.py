import psycopg2

conn = psycopg2.connect(database="xxxxx", user="xxxx", password="xxxxx", host="postgres.xxxxxx.amazonaws.com", port="5432")
print "Opened database successfully"

cur = conn.cursor()
cur.execute('''CREATE TABLE trips13
       (medallion      VARCHAR(100)   NOT NULL,
       	hack_license   VARCHAR(100)  PRIMARY KEY  NOT NULL,
       	vendor_id       CHAR (50)    NOT NULL,
       	rate_code      VARCHAR,
        store_and_fwd_flag CHAR(50),                                 
        pickup_datetime   VARCHAR,                
	    dropoff_datetime  VARCHAR,                 
		passenger_count     VARCHAR,                              
		trip_time_in_secs   VARCHAR,                            
		trip_distance       VARCHAR,                            
		pickup_longitude    VARCHAR,                    
		pickup_latitude     VARCHAR,                     
		dropoff_longitude   VARCHAR,                         
		dropoff_latitude VARCHAR);''')


print "Table created successfully"

# cur = conn.cursor()
# #cur.execute("COPY trips13 FROM '/tripstaxi/trip_data_1.csv' WITH (FORMAT CSV);")

# cur.execute("COPY trips13 FROM '//trip_data_3.csv' DELIMITER ',' csv header")

# # f= StringIO('trip_data_1.csv')
# # cur.copy_from(f, "trips13")
# print "Table populated successfully"

cur = conn.cursor()

cur.execute ("COPY (SELECT date_trunc('day', pickup_dtime) as day, count(*) FROM trips12 group by date_trunc('day', pickup_dtime) ORDER BY date_trunc('day', pickup_dtime) asc) TO '/Volumes/External/tlcdata' CSV HEADER;")
# \COPY (SELECT date_trunc('day', pickup_dtime) as day, count(*) FROM trips12 group by date_trunc('day', pickup_dtime) ORDER BY date_trunc('day', pickup_dtime) asc) TO '/Volumes/External/tlcdata/year12.csv' CSV HEADER;

cur.execute ("SELECT date_trunc('hour', pickup_dtime) as hour, count(*) FROM t13 group by date_trunc('hour', pickup_dtime) ORDER BY date_trunc('hour', pickup_dtime) asc;")
# \COPY (SELECT date_trunc('hour', pickup_dtime) as day, count(*) FROM t12 group by date_trunc('hour', pickup_dtime) ORDER BY date_trunc('hour', pickup_dtime) asc) TO '/Volumes/External/tlcdata/year12hr.csv' CSV HEADER;
# \COPY (SELECT date_trunc('hour', pickup_dtime) as hour, count(*) FROM trips13 group by date_trunc('hour', pickup_dtime) ORDER BY date_trunc('hour', pickup_dtime) asc) TO '/Volumes/External/tlcdata/year13hr.csv' CSV HEADER;

#2013hrs:  8759
#2012hrs:  8783

#favegr
cur.executeS("SELECT date_trunc('hour', pickup_dtime) as hour, avg(trip_distance), avg(trip_time_secs) FROM tt12 group by date_trunc('hour', pickup_dtime) ORDER BY date_trunc('hour', pickup_dtime) asc; ")

cur.execute("COPY (SELECT date_trunc('hour', pickup_dtime) as hour, avg(trip_distance), avg(trip_time_secs) FROM trips12 group by date_trunc('hour', pickup_dtime) ORDER BY date_trunc('hour', pickup_dtime) asc) TO '/Volumes/External/tlcdata/avg12.csv' CSV HEADER;")


conn.commit()
conn.close()
