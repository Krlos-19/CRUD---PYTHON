import os
from departamento import Departamento
from cargos import Cargo
from empleados import Empleado
from varios import Menu
import verificar as veri

def Buscar(cod,tipo):
    if tipo==1:
        for c in Cargo.cargos:
            if cod == c["codigo"]:
                valor=c["cargo"]
    elif tipo==2:
        for d in Departamento.departamentos:
            if cod == d["codigo"]:
                valor=d["depto"]
    return valor

men=Menu()
lis1=["1) Cargo","2) Departamento","3) Empleados", "4) Salir"]
lis2=["1) Ingreso","2) Consulta","3) Salir"]
opcion=""
while opcion !="4":
    os.system("cls")
    opcion=men.menus(lis1,"FICHA PERSONAL")
    
    if opcion=="1":
        opc=""
        while opc != "3":
            os.system("cls")
            opc=men.menus(lis2,"MANTENIMIENTO DE CARGO")
            os.system("cls")
            if opc == "1":
                print("*"*20,"INGRESOS DE CARGOS","*"*20)
                dato_cargo=veri.dato("Cargo",1)
                car=Cargo(dato_cargo)
                cargo1=car.registro()
                Cargo.cargos.append(cargo1)
                input("Datos ingresados satisfacctoriamente, presione una tecla para continuar...")
            elif opc == "2":
                print("*"*10,"LISTADO DE CARGOS","*"*10)
                print("Codigo"," "*5,"Descripccion")
                for car in Cargo.cargos:
                    cod=car["codigo"]
                    des=car["cargo"]
                    print(" "*2,cod," "*8,des)
                print("*"*39) 
                input("Presiones una tecla para continuar")
    
    elif opcion=="2":
        opc=""
        while opc != "3":
            os.system("cls")
            opc=men.menus(lis2,"MANTENIMIENTO DE DEPARTAMENTO")
            os.system("cls")
            if opc == "1":
                print("*"*20,"INGRESOS DE DEPARTAMENTO","*"*20)
                dato_dep=veri.dato("Departamento",5)
                dep=Departamento(dato_dep)
                dep1=dep.registro()
                Departamento.departamentos.append(dep1)
                input("Datos ingresados satisfacctoriamente, presione una tecla para continuar...")
            elif opc == "2":
                print("*"*10,"LISTADO DE DEPARTAMENTOS","*"*10)
                print("Codigo"," "*5,"Descripccion")
                for dep in Departamento.departamentos:
                    cod=dep["codigo"]
                    des=dep["depto"]
                    print(" "*2,cod," "*8,des)
                print("*"*45)
                input("Presiones una tecla para continuar")
    
    elif opcion=="3":
        opc=""
        while opc != "3":
            os.system("cls")
            opc=men.menus(lis2,"MANTENIMIENTO DE LOS EMPLEADO")
            os.system("cls")
            if opc == "1":
                print("*"*20,"INGRESOS DE EMPLEADOS","*"*20)
                dato_nombre=veri.dato("Nombre",5)
                dato_cedula=veri.LongCedula()
                dato_cargo=veri.verCargo()
                dato_depto=veri.verDepto()
                dato_sueldo=veri.veriSueldo()
                emp=Empleado(dato_nombre,dato_cedula,dato_cargo,dato_depto,dato_sueldo)
                emp1=emp.registro()
                Empleado.empleados.append(emp1)
                input("Datos ingresados satisfacctoriamente, presione una tecla para continuar...")
            elif opc == "2":
                print("*"*50,"EMPLEADOS","*"*50)
                print("Codigo"," "*2,"Nombre"," "*15,"Cedula"," "*5,"Cargo"," "*15,"Departamento"," "*8,"Sueldo")
                for em in Empleado.empleados:
                    cod=em["codigo"]
                    nombre=em["nombre"]
                    cedula=em["cedula"]
                    cargo=Buscar(em["cargo"],1)
                    depto=Buscar(em["departamento"],2)
                    sueldo=em["sueldo"]
                    print(" ",cod," "*6,nombre," "*(20-len(nombre)),cedula," "*1,cargo," "*(20-len(cargo)),depto," "*(20-len(depto)),sueldo)
                print("*"*111)
                input("Presiones cualquier tecla  para continuar")
    
    elif opcion=="4":
        break
                    

#ESTE ES UN CAMBIO NUEVO PARA LA PRACTICA EN CLASE DE GESTIÓN DE CONFIGURACIÓN. :D D: