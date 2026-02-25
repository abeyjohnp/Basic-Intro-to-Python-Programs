number=int(input("Enter the total number of students : "))
register=[]
marks=[]
maximum=0
topper=0
s=0
for i in range(0,number):
    name=input("Enter the name of the student : ")
    reg_num=int(input("Enter the register number : "))
    register.append(reg_num)
    list=[]
    for i in range(3):
        curr_marks=int(input("Enter the mark of subject",i+1," out of 100",))
        list.append(curr_marks)
    marks.append(list)
    for i in range(3):
        if i>=90:
            print("Subject ",i+1," secured A GRADE")
        elif i>=75:
            print("Subject ",i+1," secured B GRADE")
        elif i>= 50:
            print("Subject ",i+1," secured B GRADE")
        else:
            print("Failed in subject ",i+1)
    if (sum(list)>maximum):
        maximum=sum(list)
        topper=i
    s+=sum(list)

avg=s/number
print("Total mark of class is : ",s)
print("Average mark of class is : ",avg)
print("Topper is : ",register[topper])
