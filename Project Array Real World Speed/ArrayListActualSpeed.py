#Blake Reidinger
# Date 10/31/2023

from ArrayList import ArrayList
from Client import Client 
from Quicksort import Quicksort
from datetime import date
import time   #Use this libary to time the code executions
import random # Use to generate random numbers 
import sys # use to terminate the application early 

# Display name and date in output 
print("Name:", "Blake Reidinger")
print("Date:", date.today())
print()

#Create a list
clients = []

input_file_name = 'ClientData.csv'
with open(input_file_name) as infile:
    for line in infile:
        #split the line based on the commas
        s = line.split(',')
        client_id = int( s[0] ) #Convert the default string to an integer
        f_name = s[1]
        l_name = s[2]
        phone = s[3]
        email = s[4]
        #Create a client object using data from the file
        clt = Client(client_id, f_name, l_name, phone, email)
        #Add the client object to the list
        clients.append(clt)
        
#Sort the clients list
Quicksort.sort(clients)
        
#How many client objects do we have? 
num_records = len(clients)

#Create an ArrayList object
my_array_list = ArrayList()

# Scenario 1: Printer Queue or Call Queue
section_title = "Scenario: Printer Queue or Call Queue"
print(section_title)
print("-" * len(section_title))

#How long does it take to add the client recrods to the ArrayList? 
start_time = time.time()

for i in range(num_records):
    my_array_list.append(clients[i])
    
    
end_time = time.time()
total_time = end_time - start_time
print("Seconds to add records: {:.6f}".format(total_time))

#How long does it take to remove records from the front of the ArrayList?
start_time = time.time()

for i in range(num_records):
    my_array_list.remove_at(0)

end_time= time.time()
total_time = end_time - start_time
print("Seconds to remove records from front: {}".format(total_time))


# Scenario 2: Customer Service Center
answer = input("Continue (y/n)? ")
if answer.lower() != "y":
    sys.exit()   #End application
section_title = "Scenario: Customer Service"
print(section_title)
print("-" * len(section_title))

# add clients to the ArrayList
for i in range(num_records):
    my_array_list.append(clients[i])

#How long does it take to randomly display 1000 records? 
start_time = time.time()

for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    #print( my_array_list.search(Client(random_num)))
    print( my_array_list.search_sorted(Client(random_num)))
    
   
end_time = time.time()
total_time = end_time - start_time
print("Seconds to display random records: {:.6f}".format(total_time))

# Scenario 3: Call Center
answer = input("Continiue (y/n)? ")
if answer.lower() != "y":
    sys.exit()   #End application
    
section_title = "Scenario: Call Center"
print(section_title)
print("-" * len(section_title))



#How long does it take to add records, randomly display 1000 records
#   and randomly remove 1000 records? 
start_time = time.time()

# add records
current_id = 100001 + num_records + 1
for i in range(1000):
    my_array_list.append(Client(current_id))
    current_id += 1
    
#Display random records


for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    #print( my_array_list.search(Client(random_num)))
    print( my_array_list.search_sorted(Client(random_num)))
    
#Remove randm records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print( my_array_list.search(Client(random_num)))
    
    
    
   
end_time = time.time()
total_time = end_time - start_time
print("Seconds to add, display, and remove records: {:.6f}".format(total_time))
