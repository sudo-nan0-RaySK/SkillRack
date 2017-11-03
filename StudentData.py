import math
#a
def file_read():
    f=open("student.txt",'r')
    for line in f.read():
        print(line,end='')
    f.close()
    print('\r')

#b
def sort_contnts():
    records=[]

    f=open("student.txt",'r')
    for line in f.readlines():
        temp=line.split(',')
        temp = [x.strip() for x in temp]
        records.append(temp)
    f.close()
    records.sort(key=lambda x: x[0])
    records.sort(key= lambda x:x[3],reverse=True)

    for lists in records:
        el=','.join(lists)
        print(el)

#c
def min_max_age():
    records = []

    f = open("student.txt", 'r')
    for line in f.readlines():
        temp = line.split(',')
        temp = [x.strip() for x in temp]
        records.append(temp)
    f.close()
    records.sort(key= lambda x:(x[2],x[0]))
    sum=0
    for lists in records:
        sum+=int(lists[2])
    avg=sum/len(records)
    max=int(records[-1][2])
    min=int(records[0][2])
    return (min,max,int(round(avg,2)))

#d
def avg_cgpa():

    records = []
    f = open("student.txt", 'r')
    for line in f.readlines():
        temp = line.split(',')
        temp = [x.strip() for x in temp]
        records.append(temp)
    f.close()
    sum=0
    for lists in records:
        sum+=float(lists[3])
    avg=sum/len(records)
    return round(avg,2)
#e
def above_avg():
    records = []
    f = open("student.txt", 'r')
    for line in f.readlines():
        temp = line.split(',')
        temp = [x.strip() for x in temp]
        records.append(temp)
    f.close()
    avg_gpa=avg_cgpa()
    avg_age=min_max_age()[2]
    min_age=min_max_age()[0]

    resultSet=[]

    for lists in records:
        if float(float(lists[3]))>=float(avg_gpa) and int(lists[2]) in range(min_age,avg_age+1):
            resultSet.append(lists[0])

    resultSet.sort()
    for i in resultSet:
        print(i)


def min_max_aged_students():
    records = []
    f = open("student.txt", 'r')
    for line in f.readlines():
        temp = line.split(',')
        temp = [x.strip() for x in temp]
        records.append(temp)
    f.close()
    min_age = min_max_age()[0]
    max_age = min_max_age()[1]
    records.sort(key=lambda x: (x[3],x[0]))
    maxList=[]
    minList=[]

    for lists in records:
        if int(lists[2])==max_age:
            maxList.append(lists)

    for lists in records:
        if int(lists[2])==min_age:
            minList.append(lists)
    maxList.sort(key= lambda x:x[0])
    minList.sort(key= lambda x:x[0])

    for lists in maxList:
        print(','.join(lists))

    for lists in minList:
        print(','.join(lists))


file_read()
sort_contnts()
min_max_aged_students()
print(avg_cgpa())
above_avg()








