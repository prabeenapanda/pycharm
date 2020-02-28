def testcode():
    try:
        day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satuday', 'Sunday']
        print(day)
        string = input("Enter a day from the list: ")
        num = int(input("Enter a number between 1 to 7: "))
        indexed = 0
        for i in day:
            if i==string:
                indexed = day.index(i)
        indexed += num
        print("Day is: ",day[indexed])
    except IndexError:
        print("Updating")
testcode()
