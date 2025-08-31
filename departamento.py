class Departamento:
    secuencia=2
    departamentos=[{"codigo":1,"depto":"Logistica"},{"codigo":2,"depto":"Compras"}]
    def __init__(self, descrip):
        Departamento.secuencia+=1
        self.codigo=Departamento.secuencia
        self.descripcion=descrip
    
    def registro(self):
        return{"codigo":self.codigo,"depto":self.descripcion}
    
    def mostrar(self):
        print("{} - {} ".format(self.codigo, self.descripcion))
"""        
dep=Departamento("Finanzas")
dep.mostrar()
dep1=dep.registro()
print(dep1)
Departamento.departamentos.append(dep1)
print(Departamento.departamentos)
"""
