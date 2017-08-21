class structure:
    def __init__(self,height,ID):
        self.height=height
        self.ID=ID
def main():
    n=int(input())
    listOfPlants=[]
    ht=0
    val=0
    for i in range(0,n):
        val=(input())
        ht=int(input())
        obj=structure(ht,val)
        listOfPlants.append(obj)
    listOfPlants.sort( key=lambda x:x.height)
    for j in listOfPlants:
        print(j.ID)
main()
