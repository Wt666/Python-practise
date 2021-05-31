class Calculator:
    name = 'Good Calculator'
    price = 18
    def __init__(self,hight,width,weight):

    #self.name=name
    #self.price=price
        self.hight=hight
        self.w=width
        self.weight=weight
    def add(self,x,y):
        print(self.name)
        result=x+y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)  
