class Empleado:
    secuencia=1
    empleados=[{"codigo":1,"nombre":"Dan","cedula":"0914192182","cargo":1,"departamento":1,"sueldo":500.50}]
    def __init__(self, nombre,cedula,codCargo,codDepartamento,sueldo):
        Empleado.secuencia+=1
        self.codigo=Empleado.secuencia
        self.nombre=nombre
        self.cedula=cedula
        self.cargo=codCargo
        self.departamento=codDepartamento
        self.sueldo=sueldo
    
    def registro(self):
        return{"codigo":self.codigo,"nombre":self.nombre,"cedula":self.cedula,"cargo":self.cargo,"departamento":self.departamento,"sueldo":self.sueldo}
    
    def mostrar(self):
        print("{} - {} - {} - {} - {} - {}".format(self.codigo, self.nombre,self.cedula, self.cargo,self.departamento, self.sueldo))
"""       
emp=Empleado("Lupita","1234567890",2,2,500)
emp.mostrar()
emp1=emp.registro()
print(emp1)
Empleado.empleados.append(emp1)
print(Empleado.empleados)
"""
