
wrd1=raw_input().rstrip()
wrd2=raw_input().rstrip()
wrd3=raw_input().rstrip()
 
list12=[]
list10=[]
list123=[]
listAll=[]
 
for char in wrd1:
    if char not in wrd3 and char in wrd2 :
        if char not in list12:
            list12.append(char)
for char in wrd1:
    if char not in wrd3 and char not in wrd2:
        if char not in list10:
            list10.append(char)
for char in wrd1:
    if char  in wrd3 and  char in wrd2:
        if char not in list123:
            list123.append(char)
for char in wrd1:
    if char not in listAll:
        listAll.append(char)
for char in wrd2:
    if char not in listAll:
        listAll.append(char)
for char in wrd3:
    if char not in listAll:
        listAll.append(char)   
       
list123.sort()
list12.sort()
list10.sort()
listAll.sort()
print(list123)
print(list12)  
print(list10)
print(listAll)
