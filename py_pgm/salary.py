emp=input("enter the type of employee:")
if(emp=="hourly"):
    target=int(input("enter the target weekly work hours:"))
    if(target==20):
        hw=10
        bonus=12
        salary=(20*hw)+(20*bonus)
        print("the salary is:",salary)
    elif(target==32):
        hw = 15
        bonus = 18
        salary = (20 * hw) + (20 * bonus)
        print("the salary is:", salary)
    elif (target == 40):
        hw = 20
        bonus = 24
        salary = (20 * hw) + (20 * bonus)
        print("the salary is:", salary)
elif(emp=="monthly"):
    work=int(input("enter number of working days:"))
    day=int(input("enter the number of days worked:"))
    hour=float(input("enter the hours present per day:"))
    c = int(input("enter number of holidays worked:"))
    ab = work-day
    if(day>=18 and hour>=8):
        print("basic salary granted")
        basic=int(input("enter the basic salary of the employee:"))
        if(basic==3000):
            bonus=270
            deduct=135
            full=300
            salary=basic+(c*bonus)-(ab*deduct)
            if(work==day and ab==0):
                salary=salary+full
                print("the salary is:", salary)
            else:
                salary=salary
                print("the salary is:", salary)
        elif(basic==4000):
            bonus = 360
            deduct = 180
            full = 400
            salary = basic + (c * bonus) - (ab * deduct)
            if (work == day and ab==0):
                 salary = salary + full
                 print("the salary is:", salary)
            else:
                 salary = salary
                 print("the salary is:", salary)
        elif (basic == 5000):
            bonus = 450
            deduct = 225
            full = 500
            salary = basic + (c * bonus) - (ab * deduct)
            if (work == day and ab==0):
                salary = salary + full
                print("the salary is:", salary)
            else:
                salary = salary
                print("the salary is:", salary)
        else:
            pass

    else:
        print("basic salary not granted")
        basic=int(input("enter the basic salary:"))
        if (basic == 3000):
            sal = (basic / 144) * (day*hour)
            bonus = 270
            deduct = 135
            sall = (sal + (c * bonus) - (ab * deduct))/12
            salary=round(sall,12)
            print("the salary is:", salary)
        elif(basic == 4000):
            sal = (basic / 144) * (day*hour)
            bonus = 360
            deduct = 180
            sall = (sal + (c * bonus) - (ab * deduct))/12
            salary=round(sall,2)
            print("the salary is:", salary)
        elif(basic == 5000):
            sal = (basic / 144) * (day*hour)
            bonus = 450
            deduct = 225
            sall = (sal + (c * bonus) - (ab * deduct))
            salary=round(sall,2)
            print("the salary is:", salary)
        else:
            pass
elif(emp=="sales"):
    basic=400000
    sale=int(input("enter the total sale price:"))
    if(sale<=1000000):
        com=0
        sal=(((com/100)*sale)+basic)/12
        salary= round(sal,2)
        print("The monthly salary is:", salary)
    elif(sale > 1000000 and sale <= 3000000):
        com = 1
        sal = (((com / 100) * sale) + basic)/12
        salary = round(sal,2)
        print("The monthly salary is:", salary)
    elif (sale > 3000000 and sale <= 5000000):
        com = 2
        sal = (((com / 100) * sale) + basic)/12
        salary = round(sal,2)
        print("The monthly salary is:", salary)
    elif (sale > 5000000 ):
        com = 3
        sal = (((com / 100) * sale) + basic)/12
        print(sal)
        salary = round(sal,2)
        print("The monthly salary is:", salary)





