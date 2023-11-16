#name Blake Reidinger
# Date 11/9/23

from Queue import Queue
from call import Call
from datetime import date

import time     #Use to pause the application 
import random   #Use to generate random number 

# Display authors name and the date in the output 
print("Name:", "Blake Reidinger")
print("Date:", date.today())
print()


#Create a list 
calls = [] 

#Read call records into the list
input_file_name = "CallsData.csv"
with open (input_file_name) as infile:
    for line in infile:
        #Split the line based on the commas
        s = line.split(',')
        client_id = int( s[0] )
        client_name = s[1]
        client_phone = s[2]
        # create a Call pbject based on the data from the line
        a_call = Call(client_id, client_name, client_phone)
        #Add the call object to the list 
        calls.append(a_call)

# Queue object for our calls 
calls_waiting = Queue()
call_number = 0 

# How long is the simulation 
seconds = int( input("How many seconds do you want to simulate? "))

#Run the simulation for the given number of seconds 
for i in range (seconds):
    print("-" * 40)
    time.sleep(2)     #Puase the appliaction for given number of seconds
    random_event = random.randint(1, 3) 
    # do the event based on the random number generated
    if random_event == 1:
        print("Call received. Caller added to queue. ")
        calls_waiting.enqueue( calls[call_number])
        call_number += 1      #set up the next call 
        print("\tNumber of calls waiting in queue: ", calls_waiting.get_length())
    elif random_event ==2:
        print("Call sent to representative for service. ")
        if calls_waiting.get_length() > 0:
            print("Caller information: ")
            print(calls_waiting.dequeue())
        else:
            print("The call waiting queue is empty.")  
        print("\tNumber of calls waiting in queue:", calls_waiting.get_length())
    else:
        print("Nothing happened during this second in time. ")
        print("\tNumber of calls waiting in queue:", calls_waiting.get_length())
print("\nThe 'Automatic Call Distributor' simulation has been completed. ")
       
    
        
    
    
        