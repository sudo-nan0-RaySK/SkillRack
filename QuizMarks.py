file=input().rstrip()
regList=[]
def print_file():
    print("Input file")
    f=open(file,'r')
    for line in f.readlines():
        print(line,end='')
    f.close()
def segregated_marks():
    print('Consolidated data')
    f = open(file, 'r')
    record=[]
    for line in f.readlines():
        temp=line.split(" ")
        temp=[x.strip() for x in temp]
        record.append(temp)
    f.close()
    for student in record:
        if student[0] in [x[0] for x in regList]:
            for x in regList:
                if x[0]==student[0]:
                    x+=student[1:]
        else:
            regList.append(student)
    regList.sort(key= lambda x:x[0])
    for student in regList:
        print(" ".join(student))
def print_average():
    print("Consolidated data with average")
    for student in regList:
        el=list(map(int,student[1:]))
        if len(el)>0:
            avg=round(sum(el)/len(el))
            student.append(str(avg))
        else:
            avg=0
            student.append(str(avg))
    regList.sort(key= lambda x:eval(x[-1]))
    for i in regList:
        print(' '.join(i))
def singular(regno):
    print('Consolidated data with average for a given student')
    for i in regList:
        if i[0].strip()==regno:
            print(' '.join(i))
print_file()
segregated_marks()
print_average()
regno=input().rstrip()
singular(regno)
