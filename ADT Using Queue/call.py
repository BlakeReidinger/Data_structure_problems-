# Name Blake Reidinger
# Date 11/8/23

from time import strftime    #Used for current date and time

class Call:
    def __init__(self, client_id=0, client_name="Unknown", client_phone = "Unknown"):
                 """Initialize the attributes"""
                 self.client_id = client_id
                 self.client_name = client_name
                 self.client_phone = client_phone
                 self.call_date = strftime("%m/%d/%Y")
                 self.call_time = strftime("%H:%M")
                 
    # __str__() methos is automatically called when you string the object
    def __str__(self):
        return str(self.client_id) + ", " + self.client_name + \
            "\n\tPhone: " + self.client_phone + \
                "\tDate/Time: " + self.call_date + " @ " + self.call_time
                