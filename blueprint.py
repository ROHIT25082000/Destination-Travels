import psycopg2
import pickle
conn = psycopg2.connect(
    database ="taxidatabase", user = "postgres", password ="postgres", host ="localhost", port = "5432"
)
conn.autocommit = True

cursor = conn.cursor()


class Client:
    #fp = open("meta.dat","r")
    #mystr = fp.read().split(',')
    CLIENT_ID = None#int(mystr[0])
    WALLET_ID = None#int(mystr[1])
    mystr = None # List 
    #fp.close()
    def __init__(self,first_name,last_name,phone,city,balance):
        Client.set_class_var_client() # set them 
        self.client_id = Client.CLIENT_ID
        self.wallet_id = Client.WALLET_ID
        self.first_name = first_name
        self.last_name = last_name 
        self.phone =  phone
        self.city = city
        sql = """
        INSERT INTO client(client_id,wallet_id,first_name,last_name,phone_number,city)
        VALUES ("""+str(self.client_id)+","+str(self.wallet_id)+","+"\'"+str(self.first_name)+"\'"+","+"\'"+str(self.last_name)+"\'"+","+"\'"+str(self.phone)+"\'"+","+"\'"+str(self.city)+"\'"+")"
        cursor.execute(sql)
        
        obj = Wallet(Client.WALLET_ID,balance)
        Client.increment_number_of_client()
        Client.change()

    @classmethod 
    def set_class_var_client(cls):
        fp = open("meta.dat","r")
        cls.mystr = fp.read().split(',')
        cls.CLIENT_ID = int(cls.mystr[0])
        cls.WALLET_ID = int(cls.mystr[1])
        fp.close()

    @classmethod
    def get_client_num(cls):
        return (cls.CLIENT_ID - 123450)
    @classmethod  
    def increment_number_of_client(cls):
        cls.CLIENT_ID+=1
        print("Increased Inclie ",cls.CLIENT_ID)
        fp = open("meta.dat","w")
        Client.mystr[0] = str(Client.CLIENT_ID)
        put = ','.join(Client.mystr)
        fp.write(put)
        fp.close()
    @classmethod
    def decrement_number_of_client(cls):
        cls.CLIENT_ID-=1
        fp = open("meta.dat","w")
        Client.mystr[0] = str(Client.CLIENT_ID)
        put = ','.join(Client.mystr)
        fp.write(put)
        fp.close()
    @classmethod 
    def change(cls):
        cls.WALLET_ID += 1
        fp = open("meta.dat","w")
        Client.mystr[1] = str(Client.WALLET_ID)
        put = ','.join(Client.mystr)
        fp.write(put)
        fp.close()

class Cabtype:
    cabtype_num = 0
    def __init__(self,type_of_cab,cost_per_km):
        self.type_of_cab = type_of_cab
        self.cost_per_km = cost_per_km
        sql = """
            INSERT INTO cabtype(type_of_cab,charge_perKm)
            VALUES ("""+"\'"+str(self.type_of_cab)+"\'"+","+"\'"+str(self.cost_per_km)+"\'"+")"
        cursor.execute(sql)
        Cabtype.increment_number_of_cabtype()

    @classmethod
    def get_cab_type_num(cls):
        return cls.cabtype_num
    
    @classmethod
    def increment_number_of_cabtype(cls):
        cls.cabtype_num+=1
       

    @classmethod
    def decrement_number_of_cabtype(cls):
        cls.cabtype_num-=1
    

class Cab:
    #fp = open("meta.dat","r")
    mystr = None#fp.read().split(',')
    CAB_ID =None# int(mystr[2])
    #fp.close()
    def __init__(self,cab_name,cab_no,cab_type):
        Cab.set_class_var_cab() #set them
        self.cab_id = Cab.CAB_ID        # auto generated 
        self.cab_name = cab_name
        self.cab_no = cab_no
        self.cab_type = cab_type
        sql = """
        INSERT INTO cab(cab_id,cab_name,cab_no,cab_type)
        VALUES ("""+"\'"+str(self.cab_id)+"\'"+","+"\'"+str(self.cab_name)+"\'"+","+"\'"+str(self.cab_no)+"\'"+","+"\'"+self.cab_type+"\'"+")"
        cursor.execute(sql)
        Cab.increment_number_of_cabs()
    
    @classmethod
    def set_class_var_cab(cls):
        fp = open("meta.dat","r")
        cls.mystr = fp.read().split(',')
        cls.CAB_ID = int(cls.mystr[2])
        fp.close()
        



    @classmethod
    def get_num_cabs(cls):
        return (cls.CAB_ID - 10000)
   
    @classmethod
    def increment_number_of_cabs(cls):
        #print("I am incremented ")
        cls.CAB_ID +=1
        fp = open("meta.dat","w")
        Cab.mystr[2] = str(Cab.CAB_ID)
        put = ','.join(Cab.mystr)
        fp.write(put)
        fp.close()
    
    @classmethod
    def decrement_number_of_cabs(cls):
        cls.CAB_ID -= 1
        fp = open("meta.dat","w")
        Cab.mystr[2] = str(Cab.CAB_ID)
        put = ','.join(Cab.mystr)
        fp.write(put)
        fp.close()
    
    

class Driver:
    #fp = open("meta.dat","r")
    mystr = None #fp.read().split(',')
    DRIVER_ID = None # int(mystr[3])
    #fp.close()
    def __init__(self,first_name,last_name,salary,experience,age,phone_number,driver_cab_id):
        Driver.set_class_var_driver()
        self.driver_id = Driver.DRIVER_ID
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.experience = experience 
        self.age = age
        self.phone_number = phone_number
        self.driver_cab_id = driver_cab_id
        sql = """
        INSERT INTO driver(driver_id,first_name,last_name,salary,experience,age,phone_number,driver_cab_id)
         VALUES ("""+"\'"+str(self.driver_id)+"\'"+","+"\'"+self.first_name+"\'"+","+"\'"+self.last_name+"\'"+","+"\'"+str(self.salary)+"\'"+","+"\'"+str(self.experience)+"\'"+","+"\'"+str(self.age)+"\'"+","+"\'"+str(phone_number)+"\'"+","+"\'"+str(self.driver_cab_id)+"\'"+")"
        cursor.execute(sql)
        Driver.increment_number_of_driver()
    
    @classmethod 
    def set_class_var_driver(cls):
        fp = open("meta.dat","r")
        cls.mystr = fp.read().split(',')
        cls.DRIVER_ID = int(cls.mystr[3])
        fp.close()



    @classmethod
    def get_driver_num(cls):
        return (Driver.DRIVER_ID - 50000)
#njkfnskdjfnsdjnfskdnfskjdnfsjkdnfsjdnfksjdnfkjn
    @classmethod
    def increment_number_of_driver(cls):
        cls.DRIVER_ID +=1
        fp = open("meta.dat","w")
        Driver.mystr[3] = str(Driver.DRIVER_ID)
        put = ','.join(Driver.mystr)
        fp.write(put)
        fp.close()

    
    @classmethod     
    def decrement_number_of_driver(cls):
        cls.DRIVER_ID -=1
        fp = open("meta.dat","w")
        Driver.mystr[3] = str(Driver.DRIVER_ID)
        put = ','.join(Driver.mystr)
        fp.write(put)
        fp.close()

class Ride:
    number_of_rides = 0
    
    def __init__(self, client_id, driver_id, ride_start_time, ride_end_time, source, destination, ride_status, ride_fare, ride_otp):
        self.client_id = client_id 
        self.driver_id = driver_id 
        self.ride_start_time = ride_start_time
        self.ride_end_time = ride_end_time 
        self.source = source
        self.destination = destination 
        self.ride_status = ride_status
        self.ride_fare = ride_fare 
        self.ride_otp = ride_otp
        
        sql = """
        INSERT INTO ride(client_id, driver_id, ride_start_time, ride_end_time, source, destination, ride_status, ride_fare, ride_otp)
        VALUES ("""+"\'"+str(self.client_id)+"\'"+","+"\'"+str(self.driver_id)+"\'"+","+"\'"+str(self.ride_start_time)+"\'"+","+"\'"+str(self.ride_end_time)+"\'"+","+"\'"+str(self.source)+"\'"+","+"\'"+str(self.destination)+"\'"+","+"\'"+str(self.ride_status)+"\'"+","+"\'"+str(self.ride_fare)+"\'"+","+"\'"+str(self.ride_otp)+"\'"+")"
        cursor.execute(sql)
        


class Wallet:
    number_of_wallets = 0
    def __init__(self,wallet_id,balance = 0):
        self.wallet_id = wallet_id
        self.balance = balance
        sql = """
        INSERT INTO wallet(wallet_id,balance)
        VALUES ("""+"\'"+str(self.wallet_id)+"\'"+","+"\'"+str(self.balance)+"\'"+")"
        cursor.execute(sql)
        Wallet.increase()

    @classmethod
    def increase(cls):
        cls.number_of_wallets+=1
    @classmethod
    def get_wallet_num(cls):
        return cls.number_of_wallets
    @classmethod
    def decrease(cls):
        cls.number_of_wallets-=1