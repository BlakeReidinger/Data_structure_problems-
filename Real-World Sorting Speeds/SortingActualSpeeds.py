# Blake Reidinger
# Date 11/18/2023

from MergeSort import MergeSort
from Client import Client
from datetime import date
import time     # Use to time our code execution

# Display name and date in output 
print("Name:", "Blake Reidinger")
print("Date:", date.today())
print()

#input_file_name = 'ClientData100.csv'
#input_file_name = 'ClientData1000.csv'
#input_file_name = 'ClientData10000.csv'
input_file_name = 'ClientData100000.csv'


#Create a list
clients = []

#Read the records from the ClientData.csv file
#Into Client objects and place the Client objects into the list 
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
        
        
#How many client objects do we have? 
num_records = len(clients)


# Scenario: Sorting Records from a data file
section_title = "Scenario: Sorting" + str(num_records) + "Records"
print(section_title)
print("-" * len(section_title))

#How long does it take to sort the records. 
start_time = time.time()

# Call the static sort method in the class
MergeSort.sort(clients)  
    

end_time= time.time()
total_time = end_time - start_time
print("Seconds to sort {0} records: {1:.6f}".format(num_records, total_time))


# Display the sorted list
#for clt in clients:
 #   print(clt)
    
   
