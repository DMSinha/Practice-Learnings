#To collapse all the path
import os,sys
from os.path import dirname, join, abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..')))

#Calling fuction from payment details
#######from Payment import paymet_details #### Commented it to avoid cricular error


#Create a Function Inside Course Details
def course_details():
    print("This is my course details")


#Calling function paymentdetails
######paymet_details.payment() #### Commented it to avoid cricular error

#So despite importing Payment pcakge, it's giving message as No Module "Payment". This is because
#while executing, it's not able to find the path of Payment folder. 
#To make it identify, we need to collapse all the paths- for this import os & sys module