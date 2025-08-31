class Cargo:
    secuencia=2
    cargos=[{"codigo":1,"cargo":"Analista"},{"codigo":2,"cargo":"Jefe"}]
    def __init__(self, descrip):
        Cargo.secuencia+=1
        
        self.codigo=Cargo.secuencia
        self.descripcion=descrip
    
    def registro(self):
        return{"codigo":self.codigo,"cargo":self.descripcion}
    
    def mostrar(self):
        print("{} - {} ".format(self.codigo, self.descripcion))
"""        
car=Cargo("Analista")
car.mostrar()
car1=car.registro()
print(car1)
Cargo.cargos.append(car1)
print(Cargo.cargos)
"""