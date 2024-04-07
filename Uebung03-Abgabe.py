#Aufgabe 1

import math

#Punkt definieren
class Punkt:
    def __init__(self,x,y):
        self.x=x
        self.y=y


#Figur
class Figur:
    def __init__(self):
        self.name="Figur"

    def Umfang(self):
        return 0
    
    def __str__(self):
        return self.name
    

#Dreieck
class Dreieck(Figur):
    def __init__(self,A,B,C):
        super().__init__()
        self.A=A
        self.B=B
        self.C=C

    def Umfang(self):
        return (self.A-self.B)+(self.B-self.C)+(self.C-self.A)
    
    def __str__ (self):
        return self.name,self.A,self.B,self.C
    
    
#Rechteck
class Rechteck(Figur):
    def __init__(self,punkt1,punkt2):
        super().__init__("")
        self.p1=punkt1
        self.p2=punkt2

    def Umfang(self):
        return abs((self.p2.x-self.p1.x)*2+(self.p2.y-self.p1.y)*2)
    
    def __str__(self):
        return self.name,self.punkt1,self.punkt2
    

#Kreis
class Kreis(Figur):
    def __init__(self,mittelpunkt,radius):
        super().__init__("")
        self.m=mittelpunkt
        self.r=radius

    def Umfang(self):
        return 2*math.pi*self.r
    
    def __str__(self):
        return self.name, self.m, self.r
        
#Polygon
class Polygon(Figur):
    def __init__(self,l,n):
        super().__init__()
        self.l=l
        self.n=n

    def Umfang(self):
        return self.n*self.l
    
    def __str__(self):
        return self.name,self.n,self.n