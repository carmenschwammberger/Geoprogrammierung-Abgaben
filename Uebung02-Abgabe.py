#Aufgabe 1

class Vector3:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

#Vektor in Zeichenkette
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
        
#Addition    
    def __add__(self,other):
        return (self.x+other.x,self.y+other.y,self.z+other.z)
    
#Subtraktion    
    def __sub__(self,other):
        return (self.x-other.x,self.y-other.y,self.z-other.z)
    
#Komponentenweise Multiplikation    
    def __mul__(self,other):
        return (self.x*other.x,self.y*other.y,self.z*other.z)
    
#Multiplikation mit Skalar
    def __mul__(self,other):
        if type(other)==float or type(other)==int:
            return (self.x*other,self.y*other)
        else:
            print ("Das Skalar muss integer oder float sein")

#Kreuzprodukt
    def corss(b):
        return (((a.y*b.z)-(a.z*b.y)),((a.z*b.x)-(a.x*b.z)),((a.x*b.y)-(a.y*b.x)))

#Skalarprodukt
    def dot(b):
        return ((a.x*b.x)+(a.y*b.y)+(a.z*b.z))
    

#Vektor normalisieren
    def normalize(self):
        n=(self.x**2+self.y**2+self.z**2)**0.5
        return (1/n)*self
    
a=Vector3(3,4,2)
b=Vector3(2,1,0)

#Test
c=a*b
d=a.dot(b)
e=a.cross(b)