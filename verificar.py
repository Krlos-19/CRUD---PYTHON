from cargos import Cargo
from departamento import Departamento

#En esta funcion verificara que este dento de los rangos establecidos de caractares.
#Pedira al usuario el dato verifica y si es correcto regresa el dato en caso de que no
#Volvera a pedir el dato hasta que ingrese el correcto
def dato(texto,min_long):
    while True:
        dato=input("{}: ".format(texto))
        if (len(dato)>=min_long and len(dato)<=20):
            break
        else:
            print("Longitud del texto fuera de rango ({} a 20 caracteres)".format(min_long))
            continue
    return dato

#En esta funcion pedira al usuario la cedula vverifica primero si contiene 10 digitos
#Si ingreso 10 digitos procede a verificar que sean numeros solamente
def LongCedula():
    while True:
        cedula=input("Cedula: ")
        if len(cedula)==10:
            ver=True
            for d in cedula:
                if (d in '1234567890')==False:
                    ver=False
            if ver:
                break
            else:
                print("Debe contener solo numeros")
                continue     
        else:
            print("Debe contener 10 digitos")
    return cedula
#En esta funcion solicita elcodigo del cargo y verifica con la clase Cargo
#que el codigo exista
def verCargo():
    while True:
        cod_cargo=int(input("Codigo cargo: "))
        if cod_cargo<=99 and cod_cargo>0:
            ver=False
            for car in Cargo.cargos:
                if car["codigo"]==cod_cargo:
                    ver=True
            if ver:
                break
            else:
                print("El codigo del cargo no existe.")
                continue
        else:
            print("Fuera de rango.")
    return cod_cargo
#En esta funcion solicita elcodigo del departamento y verifica con la clase Departamento
#que el codigo exista
def verDepto():
    while True:
        cod_depto=int(input("Codigo Departamento: "))
        if cod_depto<=99 and cod_depto>0:
            ver=False
            for dep in Departamento.departamentos:
                if dep["codigo"]==cod_depto:
                    ver=True
            if ver:
                break
            else:
                print("El codigo del cargo no existe.")
                continue
        else:
            print("Fuera de rango.")
    return cod_depto

def veriSueldo():
    sueldo=float(input("Sueldo: "))
    return sueldo
         
"""
print(dato("Cargo",1))
print(dato("Departamento",5))
print(LongCedula())
print(verCargo())
print(verDepto())
"""


    