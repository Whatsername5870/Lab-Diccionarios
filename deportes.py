"""
Hecho por Darío Espinoza y Marbel Brenes
Fecha de inicio: 7/05/2022 11:00 p.m
Fecha de última actualización: 
Versión: 3.10.3
"""
#Importación de Librerías

import re
barra = "-"*50
baseDatos={}
#Declaración de Funciones de Validar
def validarCodigo(cod):
    #Funcionalidad: Valida el ingreso del código.
    #Entradas: cod(str)
    #Salidas: Valores booleanos en caso de cumplirse la condición
    if re.match('^T{1}?E{1}?C{1}\d{2}$',cod):
        return True
    return False

def validarNombreyLugar(ptexto):
    #Funcionalidad: Valida el ingreso del código.
    #Entradas: cod(str)
    #Salidas: Valores booleanos en caso de cumplirse la condición      
    if re.match('^\D{5,50}$',ptexto):   #Acá puse D para todo lo que no sea número, pero no sé si sea la mejor opción
        return True                 #El nombre no dice nada de máximo pero validé que fuera 50 por aquello, no sé si hacemos una diferente
    return False

def validarExp(ptexto):   #Hice 2 porque para la experiencia pide que sea más de 50
    if re.match('^\D{5,250}$',ptexto):
        return True
    return False


def agregarDeporte(cod,nombre,exp,lugar):
    #Funcionalidad: Agrega el dato del deporte a la base de datos.
    #Entradas: cod(str),nombre(str),exp(str),lugar(str).
    #Salidas: Ejecuta la dfunción de agregarDeporte
    lista=[]
    lista.append(nombre)  
    lista.append(exp)
    lista.append(lugar)   #Hice una lista con los datos del nombre, explicación y lugar | no sé si haya una mejor forma de apendar los 3 a la vez :/
    baseDatos[cod]=lista       #
    return baseDatos


def modificarDeporte(cod):
    #Funcionalidad: Agrega el dato del deporte a la base de datos.          
    #Entradas: cod(str),nombre(str),exp(str),lugar(str).
    #Salidas: Ejecuta la dfunción de agregarDeporte                        
    #Mae ahí en el documento dice que busque el nombre del deporte y que si está que lo cambie,
    #Pero no tiene como mucho sentido si la gracia es hacerlo con un código que sea la llave para el diccionario
    #Entonces voy a buscarlo por Código, ese de TEC##. En el de eliminar sí lo pide por código, 
    #No sé si esque a la profe se le fue o así, pero por mientras lo hice, si no lo cambiamos, todo bien
    return True

from email.mime import base
import re
barra = "-"*50
baseDatos={}
from Funciones import *


def obtenerModificar():
    #Funcionalidad: Muestra al usuario la interfaz para el ingreso de datos.
    #Entradas: N/A
    #Salidas: Ejecuta la dfunción de agregarDeporte
    cod=input('Ingrese el código del deporte en el siguiente formato "TEC##" a buscar. Ejemplo(TEC02): ')

    if validarCodigo(cod):
        if validarEnBase(cod):
            nuevo=input('Ingrese el nuevo nombre a cambiar: ')
            if validarNombreyLugar(nuevo):
                op=input('¿Desea confirmar los cambios?\n1-Sí\n2-No\n')
                if validarFormatoOp(op):
                    if validarOpcion(op):
                        modificarDeporte(cod,nuevo)
                        return print('Nombre modificado exitosamente!')
                    print('El cambio no se modificó.')
                print('Debe ingresar solamente 1 o 0.')
                return obtenerModificar()
            print('Debe ingresar un texto de entre 5 a 50 caracteres') 
            return obtenerModificar()
        print('El deporte que desea modificar, no existe registrado en la base de datos del TEC en la Sede Central.')
        return obtenerModificar()
    print('Debe ingresar el código del deporte en el siguiente formato: "TEC##". Ejemplo(TEC02)')
    return obtenerModificar()


def obtenerEliminar():
    #Funcionalidad: Muestra al usuario la interfaz para el ingreso de datos.
    #Entradas: N/A
    #Salidas: Ejecuta la función de eliminarDeporte
    cod=input('Ingrese el código del deporte en el siguiente formato "TEC##" a buscar. Ejemplo(TEC02): ')
    if validarCodigo(cod):
        if validarEnBase(cod):
            op=input('¿Desea confirmar los cambios?\n1-Sí\n2-No\n')
            if validarFormatoOp(op):
                if validarOpcion(op):
                    eliminarDeporte(cod)
                    return print('Deporte eliminado satisfactoriamente')
                print('El deporte no se eliminó')
                return obtenerEliminar()
            print('Debe ingresar solamente 1 o 0.')
            return obtenerEliminar()
        print('El deporte que desea eliminar, no existe registrado en la base de datos del TEC en la Sede Central.')
        return obtenerEliminar()
    print('Debe ingresar el código del deporte en el siguiente formato: "TEC##". Ejemplo(TEC02)')
    return obtenerEliminar()


def obtenerAgregar():
    #Funcionalidad: Muestra al usuario la interfaz para el ingreso de datos.
    #Entradas: N/A

    #Salidas: Ejecuta la dfunción de agregarDeporte

    cod=input('Ingrese el código del deporte en el siguiente formato: "TEC##" Ejemplo(TEC02): ')
    if validarCodigo(cod):
        nombre=input('Ingrese el nombre del deporte (Mayor a 5 caracteres): ')
        if validarNombreyLugar(nombre):
            exp=input('Ingrese una corta explicación del deporte (Mayor a 5 caracteres pero menor a 250): ')
            if validarExp(exp):
                lugar=input('Ingrese el lugar en dónde se desarrolla (Mayor a 5 caracteres pero menor a 50): ')
                if validarNombreyLugar(lugar):
                    return agregarDeporte(cod,nombre,exp,lugar) 
                print('Debe ingresar un texto de entre 5 a 50 caracteres')
                return obtenerAgregar()
            print('Debe ingresar un texto de entre 5 a 250 caracteres')
            return obtenerAgregar()
        print('Debe ingresar un texto de entre 5 a 50 caracteres')
        return obtenerAgregar()
    print('Debe ingresar el código del deporte en el siguiente formato: "TEC##". Ejemplo(TEC02)')
    return obtenerAgregar()




#Menú Principal

def subMenu():
    #Funcionamiento: Submenú de la opción 4, muestra 3 opciones de buscar.
    #Entrada: N/D
    #Salida: Ejecuta la respectiva función.
    print("\nBuscar por: \n")
    op = input("""    1. Información completa de todos los deportes
    2. Información de un deporte
    3. Deportes según lugar\n
Elija la opción que guste: """)
    if op == "1":

        return 
    elif op =="2":
        return 
    elif op== "3":
        return 

        subMenu1()
        return menu()
    elif op =="2":
        return menu()
    elif op== "3":
        return menu() 

    else:
        print("Eligió una opción que no esta dentro de las permitidas.")
        return menu()


def subMenu1():
    for i in baseDatos:
        print('Código: ',i,'\nDeporte: ',baseDatos[i][0],'\nExplicación: ',baseDatos[i][1],'\nLugar: ',baseDatos[i[2]]) 

#Menú Principal

def menu():
    #Funcionamiento: Menú principal, pide si quiere codificar o decodificar
    #Entrada: N/D
    #Salida: Información solicitada.
    print("\n_____Laboratorio de Diccionarios_____\n")
    op = input("""    1. Registrar un deporte
    2. Modificar el nombre de un deporte
    3. Eliminar un deporte
    4. Buscar por…
    5. Salir\n
Elija la opción que guste: """)
    if op == "1":
        print(barra)
        print("Registrar un deporte")
        return obtenerAgregar()
    elif op == "2":
        print(barra)
        print("Modificar el nombre de un deporte")
        return 
    elif op == "3":
        print(barra)
        print("Eliminar un deporte")
        obtenerAgregar()
        return menu()
    elif op == "2":
        print(barra)
        print("Modificar el nombre de un deporte")
        obtenerModificar()
        return menu()
    elif op == "3":
        print(barra)
        print("Eliminar un deporte")
        obtenerEliminar()
        return 
    elif op== "4":
        return subMenu()
    elif op== "5":
        return "\nHas salido del programa.\nHasta pronto!!!"
    else:
        print("Eligió una opción que no esta dentro de las permitidas.")
        return menu()


print(menu())