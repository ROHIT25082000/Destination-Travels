import psycopg2
conn = psycopg2.connect(
    database ="taxidatabase", user = "postgres", password ="postgres", host ="localhost", port = "5432"
)
conn.autocommit = True

cursor = conn.cursor()

sql = """
CREATE TABLE client(
    client_id int primary key,
    wallet_id int unique not null,
    first_name VARCHAR(30) not null,
    last_name VARCHAR(30) not null,
    phone_number CHAR(10) unique not null,
    city VARCHAR(25) not null
)
"""

cursor.execute(sql)

sql = """
CREATE TABLE cabtype(
    type_of_cab VARCHAR(25) primary key,
    charge_perKm FLOAT not null
)
"""
cursor.execute(sql)

sql = """
CREATE TABLE cab(
    cab_id int primary key,
    cab_name VARCHAR(40) not null,
    cab_no VARCHAR(25) not null,
    cab_type VARCHAR(25) not null references cabtype(type_of_cab)
)
"""
cursor.execute(sql)

sql = """ 
CREATE  TABLE driver(
    driver_id int primary key,
    first_name VARCHAR(30) not null,
    last_name VARCHAR(30) not null,
    salary FLOAT not null,
    experience int not null,
    age int not null check (age - experience >= 20),
    phone_number CHAR(10) unique not null,
    driver_cab_id int references cab(cab_id) on delete set null
)
"""
cursor.execute(sql)

sql = """
CREATE TABLE wallet(
    wallet_id int not null references client(wallet_id),
    balance float not null
);
"""
cursor.execute(sql)

sql = """
CREATE TABLE ride(
    client_id int not null references client(client_id), 
    driver_id int not null references driver(driver_id),
    ride_start_time timestamp not null,
    ride_end_time timestamp not null,
    source VARCHAR(300) not null,
    destination VARCHAR(300) not null,
    ride_status char not null,
    ride_fare float not null,
    ride_otp int not null,
    PRIMARY KEY(client_id,driver_id,ride_start_time,ride_end_time)
)
"""
cursor.execute(sql)

sql_view = """
        CREATE VIEW driver_working_hours as 
        select driver_id ,first_name||' '||last_name as Fullname ,age,phone_number, cab_type ,total_ride_time from cab join driver on cab.cab_id = driver.driver_cab_id natural join (select driver_id  ,SUM((cast(ride_end_time as date) - cast(ride_start_time as date))*24) as total_ride_time from ride natural join driver group by driver_id) as t order by total_ride_time DESC;
    """
cursor.execute(sql_view)

sql_trigger = """
create or replace function tell_about_wallet()
returns trigger language plpgsql as $$
begin
    return case 
    when new.balance < 0 then null
    else new
    end;
end $$;
"""
cursor.execute(sql_trigger)

sql = """
create trigger tell_about_wallet
before insert or update on wallet
for each row execute procedure tell_about_wallet();
"""
cursor.execute(sql)


cursor.close()
print("Success ")

















