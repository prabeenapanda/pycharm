#Take the input from the user for(Total number of people, toatl number of busses, Number of seats for bus). Based on the input
#Decide whether there is sufficient busses or not and give solution for how many extra busses required.
import math
people=int(input("enter number of people:"))
bus=int(input("enter number of buses:"))
seat=int(input("enter number of seats per bus:"))
if((bus*seat)==people):
    print("sufficient")
elif((bus*seat)<people):
    s=people-(bus*seat)
    b=math.ceil(s/bus)
    print("seats needed are:",s)
    print("buses needed are",b)
elif((bus*seat)>people):
    s=(bus*seat)-people
    print("seats left:",s)