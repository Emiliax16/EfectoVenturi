
# -*- coding: utf-8 -*-


class Venturi:
    def __init__(self,rho,Q,P1,R1,R2):
        self.a1=int(rho)
        self.a2=int(Q)*0.001
        self.a3=P1*1000
        self.a4=(int(R1)*0.01)**2*3.1416 #(m2)
        self.a5=(int(R2)*0.01)**2*3.1416  #(m2)
        
    def velocidades(self):
        #CONTINUIDAD
        V1=self.a2/self.a4
        V1 = round(V1, 2)
        V2=self.a2/self.a5
        V2 = round(V2, 2)
        return V1,V2
        
    def presiones(self):
        V1,V2=self.velocidades()
        #BERNULLI
        P1=self.a3
        P1 = round(P1, 2)
        P2=P1+(V1**2-V2**2)*(self.a1/2)
        P2 = round(P2, 2)
        return P1,P2
    
    def alturas(self):
        P1,P2=self.presiones()
        H1=P1/(self.a1*9.81) * 100
        H1 = round(H1, 2)
        H2=P2/(self.a1*9.81) * 100
        H2 = round(H2, 2)
        dif=round(abs(H1-H2), 2)
        return H1,H2,dif
    



'''    
v=Venturi(1050,4,0.98,5,4).velocidades()
print(v)
x=Venturi(1050,4,0.98,5,4).presiones()
print(x)
y=Venturi(1050,4,0.98,5,4).alturas()
print(y)
'''
