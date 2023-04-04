class fruit:#5---------------------------------
    def __init__(self,Type,weight):
        self.t = Type
        self.w = weight
        self.isFresh = True
    
    def info(self):
        print("I am a ", self.t," my weight is ",self.w,"oz")
        if self.isFresh:
            print("I walked out the house looking so fresh so clean, I look scrumptious")
        else:
            print("I walked out the house lookin like I came from the McDonalds drive through with how greasy and crusty I am rn bruh fr")
    
    def rot(self):
        self.isFresh = False
    



banan = fruit("Bornana", 30)
orang = fruit("orange", 5)

banan.info()
orang.info()

banan.rot()
orang.rot()

banan.info()
orang.info()

marbles = [4,6,2,9]# 5-----------------------------

print(marbles[1])
for i in range(len(marbles)):
    print(marbles[i]*5)
    
print(marbles[:])
