import TaxiDatabase
from blueprint import * 
from Taximaps import * 
import subprocess as sp
import time 
import psycopg2
import sys
import random
import getpass



conn = psycopg2.connect(
    database ="taxidatabase", user = "postgres", password ="postgres", host ="localhost", port = "5432"
)
conn.autocommit = True

cursor = conn.cursor()

small = ['Alto-(blue)','Alto-(yellow)','Alto-(black)','Alto-(green)','Alto-(white)','Alto-(golden)','Santro-(grey)',
'Santro-(white)','Santro-(pink)','Figo-(green)','Figo-(black)','Figo-(white)','Figo-(orange)','Nissan-(orange)','Nissan-(blue)',
'Nissan-(cream)']

big = ['Amaze-(grey)','Amaze-(black)','Amaze-(blue)','Amaze-(cream)','Amaze-(white)','City-(white)','City-(black)','City-(grey)',
'City-(blue)','City-(brown)','Sunny-(white)','Sunny-(pink)','Sunny-(red)','Sunny-(golden)','Etios-(grey)','Etios-(black)','Etios-(white)',
'Etios-(blue)']

suv = ['Buick Encore-(blue)','Ford Escape-(white)','Nissan Rogue-(pink)','Fortuner-(grey)','Toyota RAV4-(grey)','Honda CR-V-(brown)',
'Mazda CX-3-(black)','Acura RDX-(black)']


current_obj = None
curr_name = None
current_session_obj = None

class Client_curr:
    def __init__(self,client_id,wallet_id,first_name,last_name,phone,city):
        self.client_id = client_id
        self.wallet_id = wallet_id
        self.first_name = first_name
        self.last_name = last_name 
        self.phone = phone
        self.city = city

def initialize_current_obj():
    fp = open("meta.dat","r")
    ls = fp.read()
    listme = ls.split(",")
    print(listme)
    current_id = int(listme[-1])
    print(current_id)
    if current_id != 404:
        sql = """ select * from client where client_id = """+str(current_id)
        cursor.execute(sql)
        row = cursor.fetchall()
        print(row)
        global current_obj 
        current_obj= Client_curr(str(row[0][0]),str(row[0][1]),str(row[0][2]),str(row[0][3]),str(row[0][4]),str(row[0][5]))
        global curr_name 
        curr_name = str(row[0][2])+" "+str(row[0][3])
        global current_session_obj
        current_session_obj = current_id
        time.sleep(1)           #client_id , #wallet_id , #fname, #lname , phone , city



def login():
    ### Just for testing 
    #print(current_obj,curr_name,current_session_obj)
    #time.sleep(5)
    fp = open("meta.dat","r")
    mylist = list(map(int,fp.read().split(",")))
    fp.close()
    if(mylist[-1] == 404):
        sp.call("clear",shell = True)
        print("\t\t\t\t                 Destination Travels \n\n"+"\t\t\t                     Ab Khulenge Naye Raaste...")
        print()
        print("\t\t1. Sign In (already have an account )          |             2.Sign Up (Coming First time )")
        print("\n")
        print("\t\t3. Exit                                        |             4.About",end = '\n\n')
    
        choice = -1
        while choice != 1 and choice != 2 and choice != 3 and choice != 4:
            choice = int(input("\t\tEnter the choice :"))
        
        if(choice == 1):
            fname = input("\tEnter First  Name :")
            lname = input("\tEnter Last   Name :")
            password = input("\tEnter password :")
            sql = """
            select Exists(Select 1 from client where client_id = """ +str(password) + " and first_name ="+"\'"+fname+"\'" +" and last_name ="+"\'"+lname+"\'" +")"
            cursor.execute(sql)
            rows = cursor.fetchall()
            if(rows[0][0]==True):
                print("Successfully Logged in ")
                fp = open("meta.dat","w")
                mylist[-1] = int(password)
                mylist = list(map(str,mylist))
                mylist = ','.join(mylist)
                fp.write(mylist)
                fp.close()
                initialize_current_obj()
                
                    
            elif(rows[0][0] == False):
                print("\n\tWrong Credentials !!!")
                time.sleep(2)
                login()
        elif(choice == 2):
            make_client()
        elif(choice == 3):
            exit()
        elif(choice == 4):
            disp_only()
            login()

    elif(mylist[-1] != 404):
        initialize_current_obj()


def disp_only():
    fastfeatures()
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$---------------------  About Us  ---------------------$$$\n\n")
    print("\n\tWelcome , User \n")
    print("Our mission is to provide fast and safe intercity travel ")
    print("Anytime .. Anywhere")
    print("\n\n\n\n\n")
    print("Would Love to hear you at : "+ u"\u260E"+"        1800-1200-6000  press q to  back ")
    a = ' '
    while(a!='Q' or a != 'q'):
        a = input()
        if(a=='Q' or a == 'q'):
            features()
            return
    if(a=='Q' or a == 'q'):
        features()
        return

 

def logout():
    fp = open("meta.dat","r")
    ls = list(map(int,fp.read().split(',')))
    ls[-1] = 404
    ls = list(map(str,ls))
    ls = ','.join(ls)
    fp.close()
    fp = open("meta.dat","w")
    fp.write(ls)
    fp.close()
    global current_obj 
    current_obj= None
    global curr_name 
    curr_name = None
    global current_session_obj
    current_session_obj = None


def features():
    tmp = sp.call('clear',shell=True)
    print("Loading ",end='')
    #time.sleep(1)
    print(".",end = '')
    #time.sleep(1)
    print("..")
    time.sleep(0.5)
    tmp = sp.call('clear',shell=True)

def fastfeatures():
    tmp = sp.call('clear',shell=True)
    print("Loading ",end='')
    print(".",end = '')
    #time.sleep(1)
    print("..")
    time.sleep(0.25)
    tmp = sp.call('clear',shell=True)

def signup_feature():
    tmp = sp.call('clear',shell=True)
    print("Creating your account .",end='')
    time.sleep(1)
    print('.',end = '')
    time.sleep(1)
    tmp = sp.call('clear',shell=True)
    print("Success !")
    return 

def home():
    tmp = sp.call('clear',shell=True)
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$---------------------Our Services---------------------$$$\n\n")
    print("\n\tWelcome ,"+curr_name+"\n")
    print("\t 1.Accounts                                   2.Ride Now\n\n")
    print("\t 3.Admin                                      4.Careers (Driving)\n\n")
    print("\t 5.Exit                                       6.About \n\n")
    print("\t\t\tEnter your choice :",end = '')
    choice = int(input())
    if(choice ==1):#             #Accounts
        features()
        accounts()
    if(choice == 2):            #ride_now
        features()
        ride_now()
    if(choice == 3): 
        features()           #Admin
        response = call_admin()
        if(response == -1):
            pass
        elif(response == 0):
            features()
            admin_menu()
    if(choice == 4):
        features()            #Careers
        get_careers()
    if(choice == 5):
        cursor.close()
        exit()
    if(choice == 6):
        features()
        display_about()     #works fine 
    home()

def accounts():
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$---------------------   Accounts ---------------------$$$\n\n")
    print("\n\tWelcome ,"+curr_name+"\n")
    print("\t 1.My Rides                                     2.Rate Card\n\n")
    print("\t 3.Back                                         4.Exit\n\n")
    print("\t 5.About                                        6.Log Out\n\n")
    print("\t 7.My Wallet\n\n")
    print("\t\t\tEnter your choice :",end = '')
    choice1 = int(input())
    # if(choice1 ==1): # works fine 
    #     make_client()
    #     features()
    #     accounts()
    if(choice1 == 1):
        fetch_my_rides()
        features()
        accounts()
    elif(choice1 == 2):#works fine
        print_rate_card()
        features()
        accounts()
    elif(choice1 == 3):#works fine 
        pass
    elif(choice1 == 4):#works fine 
        cursor.close()
        exit()        
    elif(choice1 == 5):#works fine 
        display_about()
        features()
        accounts()
    elif(choice1 == 6):
        logout()
        login()
    elif(choice1 == 7):
        add_balance()
        features()
        accounts()
    return 

def add_balance():
    features()
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    sql = """
    Select balance from client natural join
    wallet where client_id = """+str(current_obj.client_id) 
    cursor.execute(sql)
    balance = cursor.fetchall()
    print("Your e-wallet balance :"+"₹ "+str(balance[0][0]))
    out = ''
    while out != 'n' and out != 'N':
        out = input("Do you want to add money to e-wallet Y/n:")
        if(out == 'Y' or out == 'y'):
            value = -1
            while value <= 0:
                value = float(input("Enter the amount to add :"))
            new_bal = float(balance[0][0]) + value
            sql = """
            UPDATE wallet 
            set balance = """+str(new_bal)+" where wallet_id ="+str(current_obj.wallet_id)+"returning balance;"
            cursor.execute(sql)
            print("Payment successful")
            break
    if(out == 'n' or out == 'N'):
        return
    add_balance()


def get_careers():
    features()
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$-------------------- Driving Careers -------------------$$$\n\n")
    #getting the available vacancy 
    sql = """
     select count(*) from (
        select cab_id
        from cab
        except
        select driver_cab_id 
        from driver) as t
    """
    cursor.execute(sql)
    vacancy = cursor.fetchall()
    print("At present we have " +str(vacancy[0][0])+" driver Vacancies")
    if(vacancy[0][0] > 0):
        print("\nEnter the following to join as a cab driver")
        salary = 10000
        fname = input("Enter the first name (30 char max) :    ")
        while(len(fname)>30):
            fname = input("Enter correctly ")
        lname = input("Enter the last name  (30 char max) :    ")
        while(len(lname)>30):
            lname = input("Enter correctly ")
        phone = input("Enter ten digit phone :            +91-:")
        while(not check_num(phone)):
            phone = input("Enter correctly (0-9)              :")
        while len(phone)!=10:
            phone = input("Enter correctly (0-9)              :")
        age = -1
        while(age < 20 or age > 60): 
            age = int(input("Enter the your age :"))
        experience = -1
        while(experience < 0):
            experience = int(input("Enter your experience :"))
        
        sql = """
        select cab_id 
        from cab
        except 
        select driver_cab_id
        from driver
        LIMIT 1
        """
        cursor.execute(sql)
        row = cursor.fetchall()
        driver_cab_id = int(row[0][0])
        while True:
            try:
                obj = Driver(fname,lname,salary,experience,age,phone,driver_cab_id) 
                break
            except:
                print("That phone number already exists try a different number or age is less: ERROR",sys.exc_info()[0])
                phone = input("Enter ten digit phone again correctly :            +91-:")
                while(not check_num(phone)):
                    phone = input("Enter correctly (0-9)              :")
                while len(phone)!=10:
                    phone = input("Enter correctly (0-9)              :")
                while(age < 20 or age > 60): 
                    age = int(input("Enter the your age :"))
                    experience = -1
                while(experience < 0):
                     experience = int(input("Enter your experience :"))   
        sa = ' '
            #ask = input("Want to do any other addtions Y|n")
        while(sa!='Y' or sa != 'y'):                            ####### works well 
            sa = input("Want more to join Y|n :")
            if(sa=='Y' or sa == 'y'):
                get_careers()
                break
            else:
                a = ' '
                while(a!='Q' or a != 'q'):
                    a = input("press q to go back : ")
                    if(a=='Q' or a == 'q'):
                        features()
                        return
                    if(a=='Q' or a == 'q'):
                        features()
                        return                                 #######  works well 
            
    
    
    
    elif(vacancy[0][0] == 0):
        print("+------------------------------------------------------------------------+")
        print("|                                                                        |")
        print("|                Getting new vacancies soon .... :)                      |")
        print("|                                                                        |")
        print("|                                                                        |")
        print("| for career support "+u"\u260E"+" 9880218337 24 Lines                   |")
        print("+------------------------------------------------------------------------+")
        time.sleep(6)

def call_admin():
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$--------------------    Admin User   -------------------$$$\n\n")    
    name = input("Enter the admin usersname  :")
    print("Enter the admin password :")
    password = getpass.getpass()
    for i in range(3):
        if(name == "postgres" and password == "postgres"):
            return 0
        else:
            print("Wrong credentials ...! Try again:")
            name = input("Enter the admin usersname  :")
            print("Enter the admin password :")
            password = getpass.getpass()
    tm = sp.call('clear',shell=True)
    print("Too many failed attempts ...... ")
    print("Access Denied .........  :(")
    time.sleep(2)
    return -1


def admin_menu():
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$----------   Admin menu (**access granted**)  -------------$$$\n\n")  
    print("1.View revenue generated                     2.Set cabs_types\n\n")
    print("3.Set more cabs                              4.Exit \n\n")
    print("5.Back                                       6.About Software\n\n")
    print("7.View driver ride time...\n\n")
    print("\t\t\tEnter your choice :",end = '')
    choice2 = int(input())
    if(choice2 == 1):
        show_revenue()
        features()
        admin_menu()
    elif(choice2 == 2):
        set_cab_types()
        features()
        admin_menu()
        features()
    elif(choice2 == 3):
        set_more_cabs()
        features()
        admin_menu()
    elif(choice2 == 4):
        cursor.close()
        exit()
    elif(choice2 == 5):
        pass
    elif(choice2 == 6):
        features()
        about_software()
        admin_menu()
    elif(choice2 == 7):
        features()
        show_driver()
        sp.call("clear",shell= True)
        admin_menu()
    return

def show_driver():
    features()
    print("The following shows the ride time of various drivers who have completed the ride Successfully !")
    sql = "SELECT * FROM driver_working_hours "
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(format("Driver Id","<10")+" | "+format("Full Name","<15")+" | "+format("Age","<5")+" | "+format("Phone Number","<11")+" | "+format("Cab type","<10")+" | "+format("Total Ride Time","<10")+" | ")
    print("-------------------------------------------------------------------------------------------")
    for row in rows:
        print(format(str(row[0]),"<10")+" | "+format(str(row[1]),"<15")+" | "+format(str(row[2]),"<5")+" | "+format(str(row[3]),"<11")+"  | "+format(str(row[4]),"<10")+" | "+format(str(row[5]),"<10")+" | ")

    print("press q to go back ")
    rep = ''
    while rep != 'q' or rep != 'Q':
        rep = input()
        if(rep == 'Q' or rep == 'q'):
            return
        

def show_revenue():
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$----------   Admin menu (**access granted**)  -------------$$$\n\n")
    print("Following is the revenue generated till now .. ")
    sql = """
    select cab_type , sum(ride_fare) as Total_revenue_generated
    from ride natural join driver join cab on driver.driver_cab_id = cab.cab_id 
    where  ride_status = 'D' group by cab_type;
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("  "+format("Cab_type",'<25')+"|"+" "+format("Total revenue Generated per cab type",'<40'))
    print("---------------------------+-------------------------------------")
    for row in rows:
        print("  "+format(str(row[0]),'<25')+"|"+" ₹"+format(str(row[1]),'<30'))
    print("---------------------------+-------------------------------------")
    print("  "+format("Total ",'<25')+"|"+" ₹",end = '')
    sql = """
    select sum(ride_fare) as Total_revenue_generated
    from ride natural join driver join cab on driver.driver_cab_id = cab.cab_id 
    where  ride_status = 'D';
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(format(str(row[0]),'<25'))
    
    

    print("press q to go back")
    rep = ''
    while rep != 'q' or rep != 'Q':
        rep = input()
        if(rep == 'Q' or rep == 'q'):
            return


def set_cab_types():
    features()
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$----------   Admin menu (**access granted**)  -------------$$$\n\n") 
    print("1.Launch new cab types with rate:\n")
    print("2.List all types with rates :\n")
    print("3.Modify rate or type :\n")
    print("4.Delete a cab type :\n")
    print("5.Back\n")
    print("6.Exit\n")
    print("\t\tEnter choice :",end='')
    choice4 = int(input())
    if(choice4 == 1):
        typeof = input("Enter type_of_cab : (24 char max)")
        while(len(typeof)>25):
            typeof = input("Enter correctly")
        cost_per_km = float(input("Enter cost_per_km :"))
        while(cost_per_km < 1):
            cost_per_km = float(input("Enter correctly :"))
        while True:
            try:
                obj = Cabtype(typeof,cost_per_km)
                break
            except:
                print("That name already existed try a different name : ERROR",sys.exc_info()[0])
                typeof = input("Enter type_of_cab : (24 char max)")
        
        print("Looks cool.. \|/ :)")
        a = input("\nPress q to go back :")
        if(a =='Q' or a == 'q'):
            set_cab_types()
    elif(choice4 == 2):
        sql = """
        SELECT * from cabtype order by charge_perKm
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        tp = sp.call('clear',shell=True)
        print("  "+format("Cab_type",'<25')+"|"+"  "+format("Cost per Km",'<25'))
        print("-----------------------------------------------------------------")
        for row in rows:
            print("  "+format(str(row[0]),'<25')+"|"+"  "+format(str(row[1]),'<25'))
        a = input("\nPress q to go back :")
        if(a =='Q' or a == 'q'):
            set_cab_types()    
    elif(choice4 == 3):
        features()
        print("Current situation :")
        sql = """
        SELECT * from cabtype order by charge_perKm
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("  "+format("Cab_type",'<25')+"|"+"  "+format("Cost per Km",'<25'))
        print("-----------------------------------------------------------------")
        for row in rows:
            print("  "+format(str(row[0]),'<25')+"|"+"  "+format(str(row[1]),'<25'))
        print()
        name_type = input("Enter type to modify:")
        sql = """select exists(select 1 from cabtype where type_of_cab = """+"\'"+name_type+"\'"+")"
        cursor.execute(sql)
        row = cursor.fetchall()
        while(row[0]==(False,)):
            print(name_type +" "+ "Not found")
            name_type = input("Enter type correctly:")
            sql = """select exists(select 1 from cabtype where type_of_cab = """+"\'"+name_type+"\'"+")"
            cursor.execute(sql)
            row = cursor.fetchall()
        new_rate = input("Enter the new rate for "+name_type+" type :")
        
        while float(new_rate) < 0:
            new_rate = input("Enter the new rate for "+name_type+" type correctly > 0:")
        
        sql = """
        UPDATE cabtype
        SET charge_perKm = """+str(new_rate)+"WHERE type_of_cab = "+"\'"+name_type+"\'"
        
        cursor.execute(sql)
        aa = input("press q to go back")
        
        if(aa == 'q' and aa == 'Q'):
            set_cab_types()

    elif(choice4 == 4):
        features()
        print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
        print("\n\t$$$----------   Admin menu (**access granted**)  -------------$$$\n\n") 
        
        print("Current situation :")
        sql = """
        SELECT * from cabtype order by charge_perKm
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("  "+format("Cab_type",'<25')+"|"+"  "+format("Cost per Km",'<25'))
        print("-----------------------------------------------------------------")
        for row in rows:
            print("  "+format(str(row[0]),'<25')+"|"+"  "+format(str(row[1]),'<25'))
        print()

        name_type = input("Enter the cabtype to delete : ")
        
        sql = """select exists(select 1 from cabtype where type_of_cab = """+"\'"+name_type+"\'"+")"
        cursor.execute(sql)
        row = cursor.fetchall()
        while(row[0]==(False,)):
            print(name_type +" "+ "Not found")
            name_type = input("Enter type correctly:")
            sql = """select exists(select 1 from cabtype where type_of_cab = """+"\'"+name_type+"\'"+")"
            cursor.execute(sql)
            row = cursor.fetchall()

        sql = """
        SELECT COUNT(*) from cab where cab_type = """+"\'"+name_type+"\'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        print()
        print("There are at present "+str(rows[0][0])+" cabs of type "+name_type)
        print("A deletion will affect "+str(rows[0][0])+" cabs ")
        if(rows[0][0]==0):
            print("You can safely delete this type of cab from the database \n")
            ORDER = input("Press \'Y\' or \'y\' to delete :")
            while(True):
                ORDER = input("Press \'Y\' or \'y\' correctly again to delete :")
                if(ORDER.upper() == 'Y'):
                    sql = "Delete from cabtype where type_of_cab ="+"\'"+name_type+"\'"
                    cursor.execute(sql)
                    print("Deleted Successfully")
                    break
            time.sleep(2)
        elif(rows[0][0]> 0):
            print()             # recent change ... 
            sql = """
            SELECT count(*) from cabtype;
            """
            cursor.execute(sql)
            number = int(cursor.fetchall()[0][0])
            ans = ' '
            if number >= 2 :
                print("Suggestion : You can also convert "+name_type+" to any other available cabtype this will result in no driver job losses")
                while(ans != 'Y' or ans != 'y'):
                    ans = input("\nDo you want to go with cabtype conversion ?  Y/n")
                    if ans == 'Y' or ans == 'y':
                        new_type = input("Now enter the type of cab to convert "+name_type+" :")
                        sql = """select exists(select 1 from cabtype where type_of_cab = """+"\'"+new_type+"\'"+")"
                        cursor.execute(sql)
                        row = cursor.fetchall()
                        while(row[0]==(False,)):
                            print(name_type +" "+ "Not found")
                            new_type = input("Enter type correctly:")
                            sql = """select exists(select 1 from cabtype where type_of_cab = """+"\'"+new_type+"\'"+")"
                            cursor.execute(sql)
                            row = cursor.fetchall()
                        sql = """
                        Update cab 
                        set cab_type = """+"\'"+new_type+"\'"+"where cab_type ="+"\'"+name_type+"\'"
                        cursor.execute(sql)
                        sql = """
                        DELETE from cabtype
                        where type_of_cab = """ + "\'"+name_type+"\'"
                        cursor.execute(sql)
                        break
                    elif ans == 'N' or ans == 'n':
                        break
            if ans =='N'or ans == 'n' or number < 2:
                sql = """
                DELETE from cab
                where cab_type ="""+"\'"+name_type+"\'"
                cursor.execute(sql)
                #result = cursor.fetchall()
                print(" cabs deleted Successfully of type "+name_type)
                sql = "Delete from cabtype where type_of_cab ="+"\'"+name_type+"\'"
                cursor.execute(sql)
                print("Deleted Successfully cabtype "+name_type)
                print("The Drivers of "+name_type+" cabs are now set null they will get a job based on available vancancies .")
                sql = """
                select count(*) from driver 
                where driver_cab_id is NULL;
                """
                cursor.execute(sql)
                null_drivers = int(cursor.fetchall()[0][0])
                print("Total jobless drivers due to deletion : "+str(null_drivers))
                for i in range(null_drivers):
                    sql = """
                        select cab_id 
                        from cab
                        except 
                        select driver_cab_id
                        from driver
                        LIMIT 1
                        """
                    cursor.execute(sql)
                    row = cursor.fetchall()
                    if row == []:
                        print("No extra cabs for these "+str(null_drivers - i)+" jobless drivers")
                        time.sleep(8)
                        return
                    cabid = int(row[0][0])          #####################
                    sql = """
                        select driver_id from driver
                        where driver_cab_id is NULL
                        LIMIT 1
                        """
                    cursor.execute(sql)
                    row = cursor.fetchall()
                    driverid = int(row[0][0])

                    sql = """
                        UPDATE driver
                        set driver_cab_id = """+str(cabid)+"where  driver_id ="+str(driverid)
                    cursor.execute(sql) 
                                                    #######################
                    time.sleep(8)      

    elif(choice4 == 5):
        pass
    elif(choice4 == 6):
        cursor.close()
        exit()
    return 


def set_more_cabs():
    
    features()
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$----------   Admin menu (**access granted**)  -------------$$$\n\n") 
    print("Current situation :")
    sql = """
    select type_of_cab, charge_perkm,(SELECT count(*) from cab where cab_type = type_of_cab) from cabtype order by charge_perkm
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("  "+format("Cab_type",'<25')+"|"+"  "+format("Cost per Km",'<25')+"|"+"  "+format("number of cars",'<25'))
    print("-----------------------------------------------------------------------------------------------")
    for row in rows:
        print("  "+format(str(row[0]),'<25')+"|"+"  "+format(str(row[1]),'<25')+"|"+"  "+format(str(row[2]),'<25'))
    print()

    name_type = input("Enter type of cabs to add :")
    sql = """select exists(select 1 from cabtype where type_of_cab = """+"\'"+name_type+"\'"+")"
    cursor.execute(sql)
    row = cursor.fetchall()
    while(row[0]==(False,)):
        print(name_type +" "+ "Not found")
        name_type = input("Enter type correctly:")
        sql = """select exists(select 1 from cabtype where type_of_cab = """+"\'"+name_type+"\'"+")"
        cursor.execute(sql)
        row = cursor.fetchall()    
    quantity = int(input("Enter the quantity of cabs of type "+name_type+" :"))
    sql = """
    SELECT charge_perKm from cabtype where type_of_cab = """+"\'"+name_type+"\'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    value_per_km = float(rows[0][0])
    if(value_per_km <= 10):
        for i in range(quantity):
            cab_name = random.choice(small)
            cab_no =random.randrange(1000,9999)
            obj = Cab(cab_name,cab_no,name_type)
    elif(value_per_km >10 and value_per_km <=30):
        for i in range(quantity):
            cab_name = random.choice(big)
            cab_no =random.randrange(1000,9999)
            obj = Cab(cab_name,cab_no,name_type)
    elif(value_per_km > 30):
        for i in range(quantity):
            cab_name = random.choice(suv)
            cab_no =random.randrange(1000,9999)
            Cab(cab_name,cab_no,name_type)
    sql = """
          select count(*) from driver 
          where driver_cab_id is NULL;
          """
    cursor.execute(sql)
    null_drivers = int(cursor.fetchall()[0][0])
    ########################################
    for i in range(null_drivers):
        sql = """
            select cab_id 
            from cab
            except 
            select driver_cab_id
            from driver
            LIMIT 1
            """
        cursor.execute(sql)
        row = cursor.fetchall()
        if row == []:
            print("No extra cabs for these "+str(null_drivers - i)+" jobless drivers")
            time.sleep(8)
            return
        cabid = int(row[0][0])          #####################
        sql = """
                select driver_id from driver
                where driver_cab_id is NULL
                LIMIT 1
                """
        cursor.execute(sql)
        row = cursor.fetchall()
        driverid = int(row[0][0])
        sql = """
            UPDATE driver
            set driver_cab_id = """+str(cabid)+"where  driver_id ="+str(driverid)
        cursor.execute(sql) 

    ########################################
    sa = ' '
    #ask = input("Want to do any other addtions Y|n")
    while(sa!='Y' or sa != 'y'):                            ####### works well 
        sa = input("Want to do any other addtions Y|n :")
        if(sa=='Y' or sa == 'y'):
            set_more_cabs()
            break
        else:
            a = ' '
            while(a!='Q' or a != 'q'):
                a = input("press q to go back : ")
                if(a=='Q' or a == 'q'):
                    features()
                    return
                if(a=='Q' or a == 'q'):
                    features()
                    return                                 #######  works well 


def about_software():
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$----------   Admin menu (**access granted**)  -------------$$$\n\n")  
    print("Software Details ...")
    print("+--------------------------------------------------------+")
    print("| Written by - Rohit Vishwakarma (PESU)                  |")
    print("| Tools used * .Python 3.7                               |")
    print("|            * .PostreSQL 11                             |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("|                                                        |")
    print("| for technical support "+u"\u260E"+"9880218337 24 Lines |")
    print("+--------------------------------------------------------+")
    print("Press \'q\' to go back")    
    a = input()
    while(a!='Q' or a != 'q'):
        a = input()
        if(a=='Q' or a == 'q'):
            features()
            return
    if(a=='Q' or a == 'q'):
        features()
        return


def ride_now():
    features()
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    if curr_name != None:
        print("\n\tWelcome ,"+curr_name+"\n")
        print("---------------------------------------------------------------------------")
    if(current_session_obj == 403):
        print("You are not logged in please log In or Create Account")
        print("+---------------------------------------------------------+")
        print("| for technical support "+u"\u260E "+"9880218337 24 Lines |")
        print("+---------------------------------------------------------+")
    else:

        source_location = 'Your Location '
        if current_obj != None and current_session_obj != None:
            sql = """select fname from client where client_id ="""+current_obj.first_name
            print("Enter the following  :")
            print("\t1.Pick up from your current location > :\n")
            print("\t2.Enter a different Pick Up Location > :")
            print()
            choice_num = 0
            while choice_num != 1 or choice_num != 2 :
                choice_num = int(input("Enter your Choice : "))
                if choice_num == 1 or choice_num == 2:
                    break
            if(True):
                if(choice_num == 2):
                    source_location = input("Enter your source location :")
                destination_location = input("Enter the destination_location :")
                print('Getting cabs for you ')
                print("Various Cabtypes in service :")
                sql = """
                SELECT * from cabtype order by charge_perKm
                """
                cursor.execute(sql)
                rows = cursor.fetchall()
                print("  "+format("Cab_type",'<25')+"|"+"  "+format("Cost per Km",'<25'))
                print("-----------------------------------------------------------------")
                for row in rows:
                    print("  "+format(str(row[0]),'<25')+"|"+"  "+format(str(row[1]),'<25'))
                print()

                name_type = input("Enter the cabtype to choose : ")
                
                sql = """select exists(select 1 from cabtype where type_of_cab = """+"\'"+name_type+"\'"+")"
                cursor.execute(sql)
                row = cursor.fetchall()
                while(row[0]==(False,)):
                    print(name_type +" "+ "Not found")
                    name_type = input("Enter type correctly:")
                    sql = """select exists(select 1 from cabtype where type_of_cab = """+"\'"+name_type+"\'"+")"
                    cursor.execute(sql)
                    row = cursor.fetchall()
                rate_per_km = 0
                sql = """
                SELECT charge_perKm from cabtype
                where type_of_cab = """+"\'"+name_type+"\'"
                cursor.execute(sql)
                row = cursor.fetchall()
                rate_per_km = float(row[0][0])
                if(choice_num == 1):
                    s1,s2,dis = get_distance_cost(source_location,destination_location,True)
                else:
                    s1,s2,dis = get_distance_cost(source_location,destination_location,False)
                print("Cost per km :"+str(rate_per_km)+"Km")
                print()
                print("Distance :"+str(round(dis,2))+"Km.")
                print("Total Ride Fare : "+str(round(dis*rate_per_km,2)))
                total_time = int(dis/38.7)*3600 + int((dis/38.7 - int(dis/38.7))*60)*60
                print("Estimated Time for journey :"+str(int(dis/38.7))+" hrs "+ str(int((dis/38.7 - int(dis/38.7))*60))+ " min")
                print("\nFinding Rides for you ...")
                sql = """
                select driver_id from (
                select * from driver join cab on driver.driver_cab_id = cab.cab_id where cab_type ="""+"\'"+name_type+"\'" +")"+" as t "+""" 
                except 
                select driver_id from 
                ride where ride_status = 'C'
                LIMIT 1
                """
                cursor.execute(sql)
                row = cursor.fetchall()
                if(row == []):
                    print("Sorry we are having all rides booked at the moment ..... Try again in some time.")
                else:
                    from datetime import datetime,timedelta
                    dd = str(row[0][0])
                    ride_start_time = datetime.now()
                    ride_end_time = datetime.now() + timedelta(seconds =total_time)
                    ride_payment = "wallet"
                    ride_status = 'C'
                    ride_fee = str(round(dis*rate_per_km,2))
                    ride_otp = str(random.randint(1000,9999))
                    obj = Ride(current_obj.client_id,dd,ride_start_time,ride_end_time,s1,s2,ride_status,ride_fee,ride_otp)
                    sp.call('clear',shell=True)
                    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
                    print("Your ride details : ")
                    sql = """select first_name,last_name,cab_name,phone_number,cab_type,cab_no from cab join driver on cab.cab_id = driver.driver_cab_id
                    where driver_id ="""+"\'"+dd+"\'"
                    cursor.execute(sql)
                    row = cursor.fetchall()
                    # print(row) #
                    # time.sleep(10) #
                    print()
                    print("Start location   : "+s1)
                    print()
                    print("Drop location    : "+s2)
                    print()
                    print()
    
                    print("Driver Name      : "+str(row[0][0])+" "+str(row[0][1]))
                    print("Cab_name         : "+str(row[0][2])+str(row[0][5]))
                    print("Driver phone_num : "+str(row[0][3]))
                    print("Cab_type         : "+str(row[0][4]))
                    print("Ride Fare        : "+"₹ "+str(ride_fee))
                    print("Ride Otp         : "+str(ride_otp))
                    print("Distance         : "+str(round(dis,2))+" Km.")
                    print("Estimated Time   : "+str(int(dis/38.7))+" hrs "+ str(int((dis/38.7 - int(dis/38.7))*60))+ " min")
                    print()
                    print()
                    print("Cab arriving in 10 min ..")
                    time.sleep(5)
                    out = '' 
                    while out != 'n' and out != 'N':
                        out = input("Do you want to cancel the ride Y/n:")
                        if(out == 'Y' or out == 'y'):
                            sql = """
                            UPDATE ride
                            set ride_status = 'X'
                            where client_id = """+str(current_obj.client_id)+"and driver_id ="+str(dd)+" and  ride_start_time ="+"\'"+str(ride_start_time)+"\'"+" and ride_end_time ="+"\'"+str(ride_end_time)+"\'"
                            cursor.execute(sql)
                            return 
                    print("Cab has arrived  > ")
                    print()
                    resp_otp = -1
                    for i in range(3):
                        resp_otp = input("Enter ride otp :")
                        if(resp_otp == ride_otp):
                            print("Ride has started ...")
                            sql = """
                            UPDATE ride
                            set ride_status = 'D'
                            where client_id = """+str(current_obj.client_id)+"and driver_id ="+str(dd)+" and  ride_start_time ="+"\'"+str(ride_start_time)+"\'"+" and ride_end_time ="+"\'"+str(ride_end_time)+"\'"
                            cursor.execute(sql)
                            
                            sql = """
                            Select balance from client natural join
                            wallet where client_id = """+str(current_obj.client_id) 
                            cursor.execute(sql)
                            balance = cursor.fetchall()
                            #print(balance)
                            balance_new = float(balance[0][0]) - float(ride_fee)
                            transaction = []
                            while transaction == []: 
                                sql = """
                                UPDATE wallet 
                                set balance = """+str(balance_new)+" where wallet_id ="+str(current_obj.wallet_id)+"returning balance;"
                                cursor.execute(sql)
                                transaction = cursor.fetchall()
                                #print(transaction)
                                time.sleep(5)
                                if transaction == []:
                                    print("You have insufficient balance in wallet! \nplease add atleast "+str(-1*balance_new)+" To complete this ride.")
                                    topup = -1
                                    while topup < (-1*balance_new):
                                        topup = float(input("Enter money to add alteast "+str(-1*balance_new)+" :"))
                                    increased_balance = balance[0][0] + topup
                                    sql = """
                                    UPDATE wallet 
                                    set balance = """+str(increased_balance)+" where wallet_id ="+str(current_obj.wallet_id)+"returning balance;"
                                    cursor.execute(sql)
                                    trans = cursor.fetchall()
                                    print("Increased balance of your wallet "+str(increased_balance))
                                    balance_new = float(increased_balance) - float(ride_fee)

                                elif(transaction[0][0] >= 0):
                                    print("Payment successful")
                                    break

                            print("Thanks for riding with us ..")
                            time.sleep(5)
                            return
                    print("Exceeded Correct otp limit ")
    time.sleep(5) 


def display_about():
    fastfeatures()
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$---------------------  About Us  ---------------------$$$\n\n")
    print("\n\tWelcome ,"+curr_name+"\n")
    print("Our mission is to provide fast and safe intercity travel ")
    print("Anytime .. Anywhere")
    print("\n\n\n\n\n")
    print("Would Love to hear you at : "+ u"\u260E"+"        1800-1200-6000  press q to  back ")
    a = ' '
    while(a!='Q' or a != 'q'):
        a = input()
        if(a=='Q' or a == 'q'):
            features()
            return
    if(a=='Q' or a == 'q'):
        features()
        return


def print_rate_card():
    fastfeatures()
    sql = """
        SELECT * from cabtype order by charge_perKm
        """
    cursor.execute(sql)
    rows = cursor.fetchall()
    tp = sp.call('clear',shell=True)
    print("  "+format("Cab_type",'<25')+"|"+"  "+format("Cost per Km",'<25'))
    print("-----------------------------------------------------------------")
    for row in rows:
        print("  "+format(str(row[0]),'<25')+"|"+"  "+format(str(row[1]),'<25'))
    print()
    print("Would Love to hear you at : "+ u"\u260E"+"        1800-1200-6000  press q to  back ")
    a = ' ' 
    while(a!='Q' or a != 'q'):
        a = input()
        if(a=='Q' or a == 'q'):
            features()
            return
    if(a=='Q' or a == 'q'):
        features()
        return


def fetch_my_rides():
    features()
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\tWelcome ,"+curr_name+"\n")
    print("Your Rides ")
    sql = """
    select * from ride
    where client_id ="""+str(current_obj.client_id)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Driver id        : "+str(row[1]))
        print("Ride_start_time  : "+str(row[2]))
        print("Ride_end_time    : "+str(row[3]))
        print("Pick up location : "+str(row[4]))
        print("drop location    : "+str(row[5]))
        print("ride_status      : "+str(row[6]))
        print("ride_fare        : Rs "+str(row[7]))
        print("\n\n")
    
    print("press q to go back")
    rep = ''
    while rep != 'q' or rep != 'Q':
        rep = input()
        if(rep == 'Q' or rep == 'q'):
            return


def check_num(phone):   #works alright  
    ls = ['0','1','2','3','4','5','6','7','8','9']
    for i in phone:
        if i not in ls:
            return False
    return True         #works alright 
        
def make_client():      #works alright
    features()
    print("\t\t\t    Destination Travels \n\n"+"\t\t\t Ab Khulenge Naye Raaste...")
    print("\n\t$$$---------------------  Sign Up  ----------------------$$$\n\n\n")
    print("Fill the following")
    balance = 0
    fname = input("Enter the first name (30 char max) :    ")
    while(len(fname)>30):
        fname = input("Enter correctly ")
    lname = input("Enter the last name  (30 char max) :    ")
    while(len(lname)>30):
        lname = input("Enter correctly ")
    phone = input("Enter ten digit phone :            +91-:")
    while(not check_num(phone)):
        phone = input("Enter correctly (0-9)              :")
    while len(phone)!=10:
        phone = input("Enter correctly (0-9)              :")
    city = input("Enter city        (25 char max)     :     ")
    while(len(city)>30):
        city = input("Enter correctly ")
    print("Do you want to add money to your e- wallet (Y/n):")
    aa = input()
    if(aa == 'Y' or aa == 'y'):
        balance = float(input("Enter amount  (< 10000) :     "))
        while balance > 10000 or balance < 0:
            balance = float(input("Enter amount  (< 10000) :     "))
    
    while True:
        try:
            currentone = Client(fname,lname,phone,city,balance)
            print("Your account is created")
            print("First name : "+str(currentone.first_name))
            print("Last name  : "+str(currentone.last_name))
            print("Password   : "+str(currentone.client_id))
            print("Please note the above ...")
            time.sleep(13)
            break
        except:
            print("That phone number already exists try a different number : ERROR",sys.exc_info()[0])
            phone = input("Enter ten digit phone again correctly :            +91-:")
            while(not check_num(phone)):
                phone = input("Enter correctly (0-9)              :")
            while len(phone)!=10:
                phone = input("Enter correctly (0-9)              :")    
    signup_feature()    #works alright 
    login()
    home()

if __name__ == "__main__":
    login()
    home()
