import os
import numpy as np
import time
import funciones_consultamed as fc

tamaño = 2  # cantidad máxima de pacientes
opcion = ""  # seleccion del usuario
rut = ""  # rut del paciente
nombre = ""  # Nombre del paciente
edad = 0  # edad del paciente
arr_ruts = np.empty(tamaño, dtype=object)
arr_nombres = np.empty(tamaño, dtype=object)
arr_edades = np.empty(tamaño, dtype=int)

while True:
    os.system("cls")
    opcion = str(input('''
          *****MENÚ*****
          1.-Ingreso datos
          2.-Busqueda por rut
          3.-Imprimir ficha médica menores de edad
          4.-Salir
          Seleccione opción:'''))

    if opcion == "1":
        os.system("cls")
        print('''Ingreso de datos''')
        for k in range(tamaño):
            print(f'''Paciente {k+1}''')
            nombre = str(input("Ingrese nombre:")).strip().upper()
            while not (fc.validar_nombre(nombre)):
                print("ERROR, NO PUEDE SER VACÍO")
                nombre = str(input("Ingrese nombre:")).strip().upper()
            arr_nombres[k] = nombre

            rut = str(input("Ingrese rut:")).upper().strip()
            while not (fc.validar_rut(rut)):
                print("ERROR, NO PUEDE ESTAR VACÍO")
                rut = str(input("Ingrese rut:")).upper().strip()
            arr_ruts[k] = rut

            edad = int(input("Ingrese edad:"))
            while not (fc.validar_edad(edad)):
                print("NO PUEDE SER NEGATIVO")
                edad = int(input("Ingrese edad:"))
            arr_edades[k] = edad
            
            fc.imprimir_ficha_medica(rut,nombre,edad)
            

        os.system("pause")

    if opcion == "2":
        os.system("cls")
        print("Busqueda de paciente por rut")
        rut=str(input("Ingrese rut paciente a buscar:")).strip().upper()
        if rut in arr_ruts:
            #SOLO SABEMOS QUE ESTÁ ALMACENADO,AHORA DEBEMOS DETERMINAR EN QUE POSICIÓN
            for k in range(tamaño):
                if rut == arr_ruts[k]:
                    posicion=k
            fc.imprimir_ficha_medica(arr_ruts[k],arr_nombres[k],arr_edades[k])
        else:
             print("NO EXISTE EN EL SISTEMA")      
        os.system("pause")

    if opcion == "3":
        os.system("cls")
        print("")
        os.system("pause")

    if opcion == "4":
        os.system("cls")
        break
        os.system("pause")
