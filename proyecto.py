import json 
def estadisticas_global(): 
    file=open("parqueaderos.json","r")
    registro=json.load(file)
    valores=registro.values()

    archivo=open("estadistica.txt","w")

    total_parqueos=0
    total=0
    vehiculos=0
    piso=0
    n=0
    for llave in registro:
        piso+=1
        for x in (registro[llave]):
            for d in range (len(x)):
                total+=1
                if x[d]==0:
                    vehiculos+=1     
        total=vehiculos/total
        total_parqueos=total*100
        total_parqueos=round(total_parqueos,2)
        archivo.write(str(piso))
        archivo.write(" piso\n")
        archivo.write("El porcentaje total de carros parqueados fue de->  ")
        archivo.write(str(total_parqueos))
        archivo.write("%\n\n")
        total_parqueos=0
        vehiculos=0
        total=0

    for i in (valores):
        for j in i:
            for n in j:
                total+=1
                if n==0:
                    vehiculos+=1
    total=vehiculos/total
    total_parqueos=total*100
    total_parqueos=round(total_parqueos,2)
    archivo.write("El porcentaje total de carros parqueados en el parqueadero fue de de->  ")
    archivo.write(str(total_parqueos))
    archivo.write("%\n\n")
    archivo.close()
    return
def estadisticas_tipos():
    archivo=open("estadistica_tipos.txt","w")
    global carpeta
    carpeta=open("estadisticas_parqueaderos.json","r")
    diccionario=json.load(carpeta)

    tipo1=diccionario["parqueos"].count(1)
    tipo2=diccionario["parqueos"].count(2)
    tipo3=diccionario["parqueos"].count(3)
    tipo4=diccionario["parqueos"].count(4)

    archivo.write("la cantidad de Automoviles parqueados es de ")
    archivo.write(str(tipo1))
    archivo.write("\n\n")
    archivo.write("la cantidad de Automoviles electricos parqueados es de ")
    archivo.write(str(tipo2))
    archivo.write("\n\n")
    archivo.write("la cantidad de Motocicletas parqueados es de ")
    archivo.write(str(tipo3))
    archivo.write("\n\n")
    archivo.write("la cantidad de Discapacitados parqueados es de ")
    archivo.write(str(tipo4))
    archivo.write("\n\n")
    archivo.close()
def estadistica_usuario():
    carpeta=open("estadisticas_parqueaderos.json","r")
    diccionario=json.load(carpeta)
    archivo=open("estadistica_usuario.txt","w")
    usu1=diccionario["tipo_usuarios"].count("Estudiante")
    usu2=diccionario["tipo_usuarios"].count("Personal Administrativo")
    usu3=diccionario["tipo_usuarios"].count("Profesor")
    usu4=diccionario["tipo_usuarios"].count("Visitante")

    archivo.write("la cantidad de Estudiantes parqueados es de ")
    archivo.write(str(usu1))
    archivo.write("\n\n")
    archivo.write("la cantidad de Personal Administrativo parqueados es de ")
    archivo.write(str(usu2))
    archivo.write("\n\n")
    archivo.write("la cantidad de Profesor parqueados es de ")
    archivo.write(str(usu3))
    archivo.write("\n\n")
    archivo.write("la cantidad de Visitante parqueados es de ")
    archivo.write(str(usu4))
    archivo.close()

def sacar_vehiculo():
    file=open("usuarios.json","r")
    registro=json.load(file)
    global valor 
    valor=registro.get("usuarios")
    m=0
    cobro=0
    horas=eval(input("Cuantas horas estuvo en el parqueadero?\n"))
    placa=input("Ingrese la placa de su vehiculo\n")
    for i in range (len(valor)):
        if valor[i][3]== placa and valor [i][5]!="Mensualidad":
            m=1
            if valor [i][2]=="Estudiante":
                cobro=horas*1000
                print("Total a pagar: "+str(cobro))
            elif valor [i][2]=="Personal Administrativo":
                cobro=horas*1500
                print("Total a pagar: "+str(cobro))
            elif valor [i][2]=="Profesor":
                cobro= horas* 2000
                print("Total a pagar: "+str(cobro))
            elif valor [i][2]=="visitante":
                cobro=horas*3000
                print("Total a pagar: "+str(cobro))
            return 
        else:
            print("No es necesario pagar, vuelva pronto")
            m=1
            break #saca del bucle 
    if m ==0:
        print("Vehiculo no registrado")
        cobro=horas*3000
        print("Total a pagar: "+str(cobro))
    return round(cobro)

def verificacion_placas():
    file=open("usuarios.json","r")
    registro=json.load(file)
    valor=registro.get("usuarios")
    m=0
    for i in range (len(valor)):
        m=1
        tipo=valor[i][4]
        if tipo=="Motocicleta":
            tipo=3
        elif tipo=="Automovil":
            tipo=1
        elif tipo =="Automovil electrico":
            tipo=2 
        else:
            tipo= 4               

def disponibilidad():

    archivo=open("tipos_parqueaderos.json","r")
    global parking
    parking=json.load(archivo)
    piso1=parking.get("Piso1")
    piso2=parking.get("Piso2")
    piso3=parking.get("Piso3")
    piso4=parking.get("Piso4")
    piso5=parking.get("Piso5")
    piso6=parking.get("Piso6")
    global num
    num=verificacion_placas()
    total=0
    piso=0
    global pisos
    pisos=[piso1,piso2,piso3,piso4,piso5,piso6]
    for p in range (len(pisos)):
        n=pisos[p]
        if num==1 or num==3:
            for i in (n):
                for j in i:
                    if j==num:
                        total+=1
            primer_piso=total
            piso+=1
            total=0
            if total==0:
                print("no hay parqueaderos disponibles")
                verificacion_placas()                
            print("Hay",primer_piso,"parqueaderos disponibles en el piso",piso)
        elif num==2 or num==4:
            for i in (n):
                for j in i:
                    if j==num or j==1:
                        total+=1
            primer_piso=total
            piso+=1
            total=0
            print("Hay",primer_piso,"parqueaderos disponibles en el piso",piso)
            
    return 
def seleccion_piso():
    global piso_elegido
    piso_elegido=eval(input("\nA que piso desea ir\n1)piso-1\n2)piso-2\n3)piso-3\n4)piso-4\n5)piso-5\n6)piso-6\n"))
    print("le recoramos que tiene que escoger el parqueadero dependiendo del tipo de vehiculo que tiene")
    print("1 = automovil \n 2 = automovil electrico \n 3 = motocicleta \n 4 = discapacitado")
    h=pisos
    linea=""
    file=open("tipos_parqueaderos.json","r")
    if piso_elegido==1:
        piso1=parking.get("Piso1")
        for i in range(len(piso1)):
            print(piso1[i])
        if num==1 or num==3:
            for i in (h[0]):
                for j in i:
                    if j==num:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""
        elif num==2 or num==4:
            for i in (h[0]):
                for j in i:
                    if j==num or j==1:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""

    elif piso_elegido==2:
        piso2=parking.get("Piso2")
        for i in range(len(piso2)):
            print(piso2[i])
        if num==1 or num==3:
            for i in (h[1]):
                for j in i:
                    if j==num:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""
        elif num==2 or num==4:
            for i in (h[1]):
                for j in i:
                    if j==num or j==1:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""

    elif piso_elegido==3:
        piso3=parking.get("Piso3")
        for i in range(len(piso3)):
            print(piso3[i])
        if num==1 or num==3:
            for i in (h[2]):
                for j in i:
                    if j==num:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""
        elif num==2 or num==4:
            for i in (h[2]):
                for j in i:
                    if j==num or j==1:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""

    elif piso_elegido==4:
        piso4=parking.get("Piso4")
        for i in range(len(piso4)):
            print(piso4[i])
        if num==1 or num==3:
            for i in (h[3]):
                for j in i:
                    if j==num:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""
        elif num==2 or num==4:
            for i in (h[3]):
                for j in i:
                    if j==num or j==1:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""

    elif piso_elegido==5:
        piso5=parking.get("Piso5")
        for i in range(len(piso5)):
            print(piso5[i])
        if num==1 or num==3:
            for i in (h[4]):
                for j in i:
                    if j==num:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""
        elif num==2 or num==4:
            for i in (h[4]):
                for j in i:
                    if j==num or j==1:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""

    elif piso_elegido==6:
        piso6=parking.get("Piso6")
        for i in range(len(piso6)):
            print(piso6[i])
        if num==1 or num==3:
            for i in (h[5]):
                for j in i:
                    if j==num:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""
        elif num==2 or num==4:
            for i in (h[5]):
                for j in i:
                    if j==num or j==1:
                        j="0"
                        linea+=j
                    else:
                        j="x"
                        linea+=j
                print(linea)
                linea=""
        else:
            print("piso no existente ")
            seleccion_piso()

    return
def seleccion_puesto():
    lista1=pisos
    fila=-1
    columna=-1
    n=0
    for k in range (len(lista1)):
        if n>0:
            print("\nTipo de vehiculo incompatible con el parqueadero")
            fila=-1
            columna=-1
        n+=1
        fila+=int(input("\ningrese la fila en la que desea parquear, con un numero:\n"))
        columna+=int(input("ingrese la columna en la que desea parquear, con un numero:\n"))
        if piso_elegido==1:
            if lista1[0][fila][columna]==num:
               parking["Piso1"][fila][columna]=0
               print("bienvenido")
               with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
            elif lista1[0][fila][columna]==num or lista1[0][fila][columna]==1:
                parking["Piso1"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
        elif piso_elegido==2:
            if lista1[1][fila][columna]==num:
                parking["Piso2"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
            elif lista1[1][fila][columna]==num or lista1[1][fila][columna]==1 :
                parking["Piso2"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
        elif piso_elegido==3:
            if lista1[2][fila][columna]==num:
                parking["Piso3"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
            elif lista1[2][fila][columna]==num or lista1[2][fila][columna]==1:
                parking["Piso3"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
        elif piso_elegido==4:
            if lista1[3][fila][columna]==num:
                parking["Piso4"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
            elif lista1[3][fila][columna]==num or lista1[3][fila][columna]==1 :
                parking["Piso4"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
        elif piso_elegido==5:
            if lista1[4][fila][columna]==num:
                parking["Piso5"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
            elif lista1[4][fila][columna]==num or lista1[4][fila][columna]==1 :
                parking["Piso5"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
        elif piso_elegido==6:
            if lista1[5][fila][columna]==num:
                parking["Piso6"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
            elif lista1[5][fila][columna]==num or lista1[5][fila][columna]==1 :
                parking["Piso6"][fila][columna]=0
                print("bienvenido")
                with open("parqueaderos.json","w") as archivo:
                    json.dump(parking,archivo)
                    archivo.close()
                    return
#menu 
opc=0
while opc!=5:
    opc=int(input("Buenas, que le gustaria hacer? \n oprima la opcion que quiera\n 1) Ingresar vehiculo\n 2) Registrar un nuevo vehiculo \n 3) Retirar vehiculo \n 4) Estadisticas\n"))

    if opc == 1:#ingresar vehiculo
        file=open("usuarios.json","r")
        registro=json.load(file)
        valor=registro.get("usuarios")
        placa=input("ingrese la placa de su vehiculo\n(no olvide ingresar las letras en mayuscula)\n")
        for i in range (len(valor)):
            if valor[i][3]== placa:  
                disponibilidad()
                seleccion_piso()
                seleccion_puesto()
            else:
                opc=2
        opc=int(input("si desea seguir oprima la opcion que quiera, de resto oprima 5 para terminar\n"))
        if opc ==5:
            break

    elif opc == 2:#registro de vehiculo
        pregunta=""
        file=open("usuarios.json","r",encoding="utf-8")
        registro=json.load(file)
        while pregunta != 1:
            nombre_completo=str(input("Ingrese su nombre completo:\n "))
            Nombre=nombre_completo.capitalize()
            numero_identificacion=int(input("Ingrese su numero de identificacion:\n "))
            m=0
            for llave in registro:
                for j in range (len(registro[llave])):
                    if registro[llave][j][1]==numero_identificacion:
                        m=1
                        pregunta=""
            if m==0:
                tipo_usuario=str(input("Ingrese que tipo de usuariuo es\n->Estudiante\n->profesor\n->personal administrativo:\n "))
                usuario=tipo_usuario.capitalize()
                placa=str(input("Ingrese la placa de su vehiculo\n "))
                tipo_vehiculo=str(input("Ingrese que tipo de vehiculo desea registar\n->Automovil\n->Automovil electrico\n->Motocicleta\n->discapacitado\n "))
                vehiculo=tipo_vehiculo.capitalize()
                plan_pago=str(input("Ingrese que plan de pago desea\n->Mensual\n->Diario\n "))
                pago=plan_pago.capitalize()
                registro["usuarios"].append([Nombre,numero_identificacion,usuario,placa,vehiculo,pago])
            else:
                print("no puede registar dos vehiculos con la misma cedula")
            if m==0:
                pregunta=eval(input("1)Desea grabar el registro y salir\n2)desea grabar y registrar un nuevo vehiculo\n"))
                if pregunta==1:
                    with open("usuarios.json","w",encoding="utf-8") as archivo:
                        json.dump(registro,archivo)
                        archivo.close()
                else:
                    with open("usuarios.json","w",encoding="utf-8") as archivo:
                        json.dump(registro,archivo)
                        archivo.close()
        opc=int(input("si desea seguir oprima la opcion que quiera, de resto oprima 5 para terminar\n"))
        if opc ==5:
            break

    elif opc == 3:#sacar vehiculo
        sacar_vehiculo()
        opc=int(input("si desea seguir oprima la opcion que quiera, de resto oprima 5 para terminar\n"))
        if opc ==5:
            break     

    elif opc==4:#estadisticas
        seleccion=int(input("que reporte desea actualizar\n1)Cantidad de vehículos estacionados según el tipo de usuario\n2)Cantidad de vehículos estacionados según el tipo de vehículo\n3)Porcentaje de ocupación del parqueadero\n"))
        if seleccion==1:
            estadistica_usuario()
        elif seleccion==2:
            estadisticas_tipos()
        else:
            estadisticas_global()
        opc=int(input("si desea seguir oprima la opcion que quiera, de resto oprima 5 para terminar\n"))
        if opc ==5:
            break