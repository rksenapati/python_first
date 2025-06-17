studentLists={"Rajesh":'90',"Kiran":'85',"name1":'80'}
getUserName = str(input("Enter student name: "))
if getUserName in studentLists:
    print("{}'s mark :".format(getUserName),studentLists[getUserName])
else:
    print("Student name dfnot found")