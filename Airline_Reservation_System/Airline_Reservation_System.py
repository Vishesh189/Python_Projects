print("**********************************************************************************************************")
print("*                                                                                                        *")                                                 
print("*                                     Welcome to Airline reservation System                              *")
print("*                                                                                                        *")                                                                                                                              
print("**********************************************************************************************************")
print("                                                                                                 ")
print("                                                  Delhi Airline's                                ")
print("                                            ---------------------------                          ")
restart = ('Y')

f = open("E://passenger.txt","a+")
f.write("Name~age~sex~contact no.~email id~date")
f.write("\n")
f.close
 
while restart != ('N','NO','n','no'):
    print("1.Check Flight Timing")
    print("2.Check Ticket Prices")
    print("3.Ticket Reservation")
    print("4.Review your ticket details")
    print("5.Passengers guidelines")
    print("6.Airline's database")
    print("7.Exit")

    option = int(input("\nEnter your option : "))
 
    if option == 1:
        
        print(" DESTINATIONS      -      TIMINGS")
        print("DELHI-BENGALURU    -       10:40")
        print("DELHI-MUMBAI       -       07:55")
        print("DELHI-DUBAI        -       10:10")
        print("DELHI-CHENNAI      -       21:10")
        print("DELHI-HYDERABAD    -       00:45")
        print()
        print("-----------------------------------")
        print()

        continue

    elif option == 2:
        print(" DESTINATIONS      -      TICKETS PRICES")
        print("DELHI-BENGALURU    -          3385 RS/-")
        print("DELHI-MUMBAI       -          2953 RS/-")
        print("DELHI-DUBAI        -          8200 RS/-")
        print("DELHI-CHENNAI      -          2838 RS/-")
        print("DELHI-HYDERABAD    -          2669 RS/-")
        print()
        print("-----------------------------------")
        print() 
        
        continue
    
    elif option == 3:

        print("Please select your destination :")
        print("1.DELHI-BENGALURU")
        print("2.DELHI-MUMBAI")
        print("3.DELHI-DUBAI")
        print("4.DELHI-CHENNAI") 
        print("5.DELHI-HYDERABAD")
        print()
        print("-----------------------------------")
        print() 
        
        Destination = int(input("Select your destination : "))
        people = int(input("\nEnter no. of Ticket you want : "))
       
        name_l = []
        age_l = []
        sex_l = []
        f= open("E://passenger.txt","a+")
        
       
        for p in range(people):
            name = input("\nName : ")
            name_l.append(name)
            age  = input("\nAge  : ")
            age_l.append(age)
            sex  = input("\nMale or Female : ")
            sex_l.append(sex)
        
        contact_no = input("\nEnter your phone no. here : ")
        email_id = input("\nEnter your email id : ")
        date_1 = input("\nPlease enter the date of your trip : ")
        
        name_w=str(name_l) 
        age_w=str(age_l)
        sex_w=str(sex_l)
        f.write(str(name_w+"~"+age_w+"~"+sex_w+"~"+contact_no+"~"+email_id+"~"+date_1+"\n"))
        f.close()
        
        print()
        print("-----------------------------------")
        print() 
        
        if Destination == 1:
            
            print("Your destination is BENGALURU")
            print("The price you need to pay per ticket is 3385 RS/-")
            price = 3385 * people
            print("The total price you pay :",price)

        elif Destination == 2:
            
            print("Your destination is MUMBAI")
            print("The price you need to pay per ticket is 2953 RS/-")
            price = 2953 * people
            print("The total price you pay :",price,"RS/-")

        elif Destination == 3:
            
            print("Your destination is DUBAI")
            print("The price you need to pay per ticket is 8200 RS/-")
            price = 8200 * people
            print("The total price you pay :",price,"RS/-")
      
        elif Destination == 4:
            
            print("Your destination is CHENNAI")
            print("The price you need to pay per ticket is 2838 RS/-")
            price = 2838 * people
            print("The total price you pay :",price,"RS/-")      
      
        elif Destination == 5:
            
            print("Your destination is HYDERABAD")
            print("The price you need to pay per ticket is 2669 RS/-")
            price = 2669 * people
            print("The total price you pay :",price,"RS/-")
            print()
        else:
            print("invalid choice please select a destination from the list")
        print()
        print("A small game for upto 50% discount")
        print("Rules :- Select a random no. between 1-6 if your selected no. comes,you will win")
        luck = int(input("enter a no. between 1-6 :- "))
        
        import random
        a=random.randint(1,6)     
   
        if luck == a:
            
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&")
            print("$Congrats you have won 46.56% discount$")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&")
            print()
            
            import math
            new_price = math.floor(53.44*price/100)
            print("The new price is :- ",new_price," RS/-")
            
        else:
            
            print(a)
            print("--------------------------------")
            print("ohh sorry !better luck next time")
            print("--------------------------------")
             
   
    elif option == 4:
        print("Name : ", name_l)
        print("Age  : ", age_l)
        print("Sex : ",sex_l)
        print("phone no. : ",contact_no)
        print("email id : ",email_id)
        print()
        continue

    elif option == 5:
        
        print("""#.The weight of your luggage should not be more than 20kg or extra chargers will be applied.If
your luggage found to be more than 20kg you need to pay 350/-rs extra per kg.(it will charge you full amount if
its just more than 20 kg).Any sharp thing,metal thing,imflameable thing,or any other thing is not allowed in the
flight.If any thing fount that should not suppose to be with the passengers they will not allowed to attend their
flight.Passengers have to cheakin before 30 minute of the departure time of their flight.If you have any other
questions plz ask through our email.(airlinesupport@gmail.com) """)
        print()
        print("------------------------------------------------------------------------------------------------")
        continue
    
    elif option == 6:
        p = int(input("""Password required only authorised person allowed to access this information,please
input the password : """))
        
        if p == 3456:
            
            print("     ++++++++++++++++++++++++++++++")
            print("     +Welcome to airlines database+")
            print("     ++++++++++++++++++++++++++++++")
            print()
            import os
            while(True) :
                print("1) Enter new passenger")
                print("2) Searching a passenger")
                print("3) Editing a passenger record")
                print("4) Deleting a  passenger record")
                print("5) All passengers record")
                print("6) exit admin option")
                print()
                ch=int(input("enter your choice : "))
                
                if ch==1 :
                
                    print("Please select your destination : ")
                    print("1.DELHI-BENGALURU")
                    print("2.DELHI-MUMBAI")
                    print("3.DELHI-DUBAI")
                    print("4.DELHI-CHENNAI") 
                    print("5.DELHI-HYDERABAD")
                    print()
                    print("-----------------------------------")
                    print() 
                    Destination = int(input("Select your destination : "))
                    people = int(input("\nEnter no. of Ticket you want : "))
                    name_l= []
                    age_l = []
                    sex_l= []
                  
                    f= open("E://passenger.txt","a+")
                    for p in range(people):
                        name = str(input("\nName : "))
                        name_l.append(name)
                        age  = str(input("\nAge  : "))
                        age_l.append(age)
                        sex  = str(input("\nMale or Female : "))
                        sex_l.append(sex)
                    contact_no = str(input("\nEnter your phone no. here : "))
                    email_id = str(input("\nEnter your email id : "))
                    date_1 = str(input("\nPlease enter the date of your trip : "))
                    name_w=str(name_l) 
                    age_w=str(age_l)
                    sex_w=str(sex_l)
                    f.write(str(name_w+"~"+age_w+"~"+sex_w+"~"+contact_no+"~"+email_id+"~"+date_1+"\n"))
                    f.close()
                    print()
                    print("-----------------------------------")
                    print() 
                    if Destination == 1:
                        print("Your destination is BENGALURU")
                        print("The price you need to pay per ticket is 3385 RS/-")
                        price = 3385 * people
                        print("The total price you pay :",price)
                    elif Destination == 2:
                        print("Your destination is MUMBAI")
                        print("The price you need to pay per ticket is 2953 RS/-")
                        price = 2953 * people
                        print("The total price you pay :",price,"RS/-")
                    elif Destination == 3:
                        print("Your destination is DUBAI")
                        print("The price you need to pay per ticket is 8200 RS/-")
                        price = 8200 * people
                        print("The total price you pay :",price,"RS/-")
                    elif Destination == 4:
                        print("Your destination is CHENNAI")
                        print("The price you need to pay per ticket is 2838 RS/-")
                        price = 2838 * people
                        print("The total price you pay :",price,"RS/-")      
                    elif Destination == 5:
                        print("Your destination is HYDERABAD")
                        print("The price you need to pay per ticket is 2669 RS/-")
                        price = 2669 * people
                        print("The total price you pay :",price,"RS/-")
                    print()

                if ch==2 :
                    
                    fh_w=open("E://passenger.txt","r")
                    email_id=str(input("enter the passenger email id to search : "))

                    s=' '
                    while(s) :
                        s = fh_w.readline()
                        L = s.split("~")
                        if len(s)>0 :
                            if (L[4]) == email_id :
                                print("passenger name : ",L[0])
                                print("passenger age : ",L[1])
                                print("passenger sex :",L[2])
                                print("passenger contact no. : ",L[3])
                                print("passenger email id : ",L[4])
                                print("destination date : ",L[5])
                        
                            
                    fh_w.close()
                                
                if ch==3 :
                    fh_r= open("E://passenger.txt","r")
                    fh_w= open("E://temp.txt","w")
                    email_id=str(input("enter the passenger email id to search : "))
                    s=' '
                    while(s) :
                        s = fh_r.readline()
                        L = s.split("~")
                        if len(s)>0 :
                            if (L[4]) == email_id :
                                  print("Please select your destination :")
                                  print("1.DELHI-BENGALURU")
                                  print("2.DELHI-MUMBAI")
                                  print("3.DELHI-DUBAI")
                                  print("4.DELHI-CHENNAI") 
                                  print("5.DELHI-HYDERABAD")
                                  print()
                                  print("-----------------------------------")
                                  print() 
                                  Destination = int(input("Select your destination : "))
                                  people = int(input("\nEnter no. of Ticket you want : "))
                                  name_l= []
                                  age_l = []
                                  sex_l= []
                                  
                                  for p in range(people):
                                      name = str(input("\nName : "))
                                      name_l.append(name)
                                      age  = str(input("\nAge  : "))
                                      age_l.append(age)
                                      sex  = str(input("\nMale or Female : "))
                                      sex_l.append(sex)
                                  contact_no = str(input("\nEnter your phone no. here : "))
                                  email_id = str(input("\nEnter your email id : "))
                                  date_1 = str(input("\nPlease enter the date of your trip : "))
                                  name_w=str(name_l) 
                                  age_w=str(age_l)
                                  sex_w=str(sex_l)
                                  ticket_1=str(people)
                                  fh_w.write(str(name_w+"~"+age_w+"~"+sex_w+"~"+contact_no+"~"+email_id+"~"+ticket_1+"~"+date_1+"\n"))
                                  print()
                                  print("-----------------------------------")
                                  print() 
                                  if Destination == 1:
                                      print("Your destination is BENGALURU")
                                      print("The price you need to pay per ticket is 3385 RS/-")
                                      price = 3385 * people
                                      print("The total price you pay :",price)
                                  elif Destination == 2:
                                      print("Your destination is MUMBAI")
                                      print("The price you need to pay per ticket is 2953 RS/-")
                                      price = 2953 * people
                                      print("The total price you pay :",price,"RS/-")
                                  elif Destination == 3:
                                      print("Your destination is DUBAI")
                                      print("The price you need to pay per ticket is 8200 RS/-")
                                      price = 8200 * people
                                      print("The total price you pay :",price,"RS/-")
                                  elif Destination == 4:
                                      print("Your destination is CHENNAI")
                                      print("The price you need to pay per ticket is 2838 RS/-")
                                      price = 2838 * people
                                      print("The total price you pay :",price,"RS/-")      
                                  elif Destination == 5:
                                      print("Your destination is HYDERABAD")
                                      print("The price you need to pay per ticket is 2669 RS/-")
                                      price = 2669 * people
                                      print("The total price you pay :",price,"RS/-")
                                  print()
                        
                                  break
                            
                            else:
                                fh_w.write(s)
                                  
                                      

                    fh_w.close()
                    fh_r.close()
                    os.remove("E://passenger.txt")
                    os.rename("E://temp.txt","E://passenger.txt")
                if ch==4 :
                    fh_r = open("E://passenger.txt","r")
                    fh_w = open("E://temp.txt","w")
                    email_id = input("enter the passenger email id to delete")
                    s =' '
                    while(s) :
                        s = fh_r.readline()
                        L = s.split("~")
                        if len(s)>0 :
                            if (L[4]) != email_id :
                                fh_w.write(s)
                    fh_w.close()
                    fh_r.close()
                    os.remove("E://passenger.txt")
                    os.rename("E://temp.txt","E://passenger.txt")
                if ch==5 :
                    fh_w=open("E://passenger.txt","r")
                    s=' '
                    while(s) :
                        s = fh_w.readline()
                        L = s.split("~")
                        if len(s)>0 :
                                print("passenger name : ",L[0])
                                print("passenger age : ",L[1])
                                print("passenger sex :",L[2])
                                print("passenger contact no. : ",L[3])
                                print("passenger email id : ",L[4])
                                print("flight date : ",L[5])
                if ch==6 :
                    print()
                    print("-----------------------------------")
                    print() 
                    break

            continue
           
        else:

            print()
            print("************Incorect password************")
            print()
            
            continue
        
    elif option == 7:
        
        break

    restart = str(input("\nDid you forgot someone? y/n: "))

    if restart in ('y','YES','yes','Yes'):
        restart = ('Y')
        continue    
    
    else:

        print("\nTotal Ticket :    ",people)
        print("\nYour Destination : ",Destination)
   
    print("Ticket :  ",end=" ")
    
    for p in range(1,people+1):
        print(p,end=",")
    print()
    print("Name : ", name_l)
    print("Age  : ", age_l)
    print("Sex : ",sex_l)
    print("Date : ",date_1)
    print()
    import datetime
    x=datetime.datetime.now()
    print(x)
    print()
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("::Thanks for choosing Delhi airlines your ticket has been booked::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print()

        
    
