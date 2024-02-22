#To collapse all the path
import os,sys
from os.path import dirname, join, abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..')))

#Calling fuction from course details
from Course import course_details


#Create a Function Payment Details here
def payment():
    print("This is my Payment Details")

course_details.course_details()
