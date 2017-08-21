class structure:
    def __init__(self,facilities,academics,infra):
        self.facilities=facilities
        self.academics=academics
        self.infra=infra
        self.total=self.facilities+self.academics+self.infra
def main():
    n=int(input())
    listOfClgs=[]
    fac=0
    ac=0
    inf=0
    for i in range(0,n):
        fac=int(input())
        ac=int(input())
        inf=int(input())
        if fac in range(0,26) and ac in range(0,51) and inf in range(0,26):
            obj=structure(fac,ac,inf)
            listOfClgs.append(obj)
        else:
            print("Invalid  Choice")
        
    listOfClgs.sort( key=lambda x:x.total,reverse=True)
    for j in listOfClgs:
        print(j.total)
main()
