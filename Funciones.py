"""
Hecho por Darío Espinoza y Marbel Brenes
Fecha de inicio: 7/05/2022 11:00 p.m
Fecha de última actualización: 
Versión: 3.10.3
"""
#Importación de Librerías
from email.mime import base    #Mae esto se puso solo, no sé que es JAJA
import re
barra = "-"*50
baseDatos={}
from Funciones import *
#Declaración de Funciones de Validar
def validarCodigo(cod):
    #Funcionalidad: Valida el ingreso del código.
    #Entradas: cod(str)
    #Salidas: Valores booleanos en caso de cumplirse la condición
    if re.match('^T{1}?E{1}?C{1}\d{2}$',cod):
        return True
    return False

def validarNombreyLugar(ptexto):
    #Funcionalidad: Valida el ingreso de datos.
    #Entradas: cod(str)
    #Salidas: Valores booleanos en caso de cumplirse la condición      
    if re.match('^\D{5,50}$',ptexto):   #Acá puse D para todo lo que no sea número, pero no sé si sea la mejor opción
        return True                 #El nombre no dice nada de máximo pero validé que fuera 50 por aquello, no sé si hacemos una diferente
    return False

def validarExp(ptexto):
    #Funcionalidad: Valida el ingreso de datos.
    #Entradas: cod(str)
    #Salidas: Valores booleanos en caso de cumplirse la condición
    #Hice 2 porque para la experiencia pide que sea más de 50
    if re.match('^\D{5,250}$',ptexto):
        return True
    return False

def validarEnBase(cod):
    #Funcionalidad: Valida que el código esté en la base de datos
    #Entradas: cod(str)
    #Salidas: Valores booleanos en caso de cumplirse la condición
    if cod in baseDatos:
        return True
    return False

def validarOpcion(op):
    #Funcionalidad: Determina el sexo del votante
    #Entradas:op(str)
    #Salidas:Valores booleanos
    if op=='1':
        return True
    return False

def validarFormatoOp(op):
    #Funcionamiento: Valida que la cedula que se introduzca tenga un formato correcto
    #Entrada: donante(str), cedula a verificar
    #Salida: True si es un formato valido o False si es invalido    
    if not re.match("^[1|2]{1}$",op):
        return False
    return True

#Funciones de Proceso

def agregarDeporte(cod,nombre,exp,lugar):
    #Funcionalidad: Agrega el dato del deporte a la base de datos.
    #Entradas: cod(str),nombre(str),exp(str),lugar(str).
    #Salidas: Ejecuta la dfunción de agregarDeporte
    lista=[]
    lista.append(nombre)  
    lista.append(exp)
    lista.append(lugar)   #Hice una lista con los datos del nombre, explicación y lugar | no sé si haya una mejor forma de apendar los 3 a la vez :/
    baseDatos[cod]=lista       
    return baseDatos

def modificarDeporte(cod,nuevo):
    #Funcionalidad: Agrega el dato del deporte a la base de datos.          
    #Entradas: cod(str),nombre(str),exp(str),lugar(str).
    #Salidas: Ejecuta la dfunción de agregarDeporte                        
    #Mae ahí en el documento dice que busque el nombre del deporte y que si está que lo cambie,
    #Pero no tiene como mucho sentido si la gracia es hacerlo con un código que sea la llave para el diccionario
    #Entonces voy a buscarlo por Código, ese de TEC##. En el de eliminar sí lo pide por código, 
    #No sé si esque a la profe se le fue o así, pero por mientras lo hice, si no lo cambiamos, todo bien
    baseDatos[cod][0]=nuevo
    return ""

def eliminarDeporte(cod):
    #Funcionalidad: Elimna el deporte de la base de datos
    #Entradas: cod(str)
    #Salidas: Elimna el deporte de la base de datos
    del baseDatos[cod]
    return ""