new_Student = []

while True:
    input
    print ("""
    1.Add a Student Record
    2.Delete a Student Record
    3.Update a Student Record
    4.Read Record
    """)

    ans=input("Enter a number: ")

    if ans=="1":

        D = input("Enter Student Record: ")
        new_Student.append(D)
        print(new_Student)
        print("The Record Saved: ")
        

    elif ans=="2":

        D= input ("Enter a Student Record: ")
        new_Student.remove(D)   
        print("The Record Deleted: ")

    elif ans=="3":
        print(new_Student)
        index = int(input("What record do you want to update? "))
        Update = input("Update record: ")
        new_Student[index -1] = Update
        print(new_Student)

    elif ans=="4":
        print("Record List: ")
        print(new_Student)

    else:
        print("\nNot Valid Choice Try again")
    continue
