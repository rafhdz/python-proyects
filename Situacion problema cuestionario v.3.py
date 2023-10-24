import PySimpleGUI as sg #se mencionan librerias de terceros a utilizar
#descargar la libreria PySimpleGUI

pt = 10 

def resultados_ab(): #se mencionan todas las funciones a ser utilizadas
    print(f'Perfil: nombre {nom_user} , carrera / area de especialización {estatus_user}')
    print(f'Resultados: {pt} de {total} puntos')
      
def rank_ab(pt,total):
    percent = (pt / total) * 100
    return percent
    

pt_c = 20

def resultados_c():
    print(f'Perfil: nombre {nom_user} , carrera / area de especialización {estatus_user}')
    print(f'Resultados: {pt_c} de {total_uni} puntos')
    
def rank_c(pt,total):
    percent_c = (pt_c / total) * 50
    return percent_c

        
def estructura_pregunta_a_1(p_a,op_1a,op_2a,op_3a):
    layout = [[sg.Text(p_a)],[sg.Button(op_1a)],[sg.Button(op_2a)],[sg.Button(op_3a)]]
    window = sg.Window("Pregunta pensamiento logico para la computación", layout)
    while True:
        event, value = window.read()
        if event == op_1a or event == sg.WIN_CLOSED:
            break
        else:
            print("Incorrecto")
    window.close()

def estructura_pregunta_a_2(p_a,op_1a,op_2a,op_3a):
    layout = [[sg.Text(p_a)],[sg.Button(op_1a)],[sg.Button(op_2a)],[sg.Button(op_3a)]]
    window = sg.Window("Pregunta pensamiento logico para la computación", layout)
    while True:
        event, value = window.read()
        if event == op_2a or event == sg.WIN_CLOSED:
            break
        else:
            print("Incorrecto")
    window.close()

def estructura_pregunta_a_3(p_a,op_1a,op_2a,op_3a):
    layout = [[sg.Text(p_a)],[sg.Button(op_1a)],[sg.Button(op_2a)],[sg.Button(op_3a)]]
    window = sg.Window("Pregunta pensamiento logico para la computación", layout)
    while True:
        event, value = window.read()
        if event == op_3a or event == sg.WIN_CLOSED:
            break
        else:
            print("Incorrecto")
    window.close()
    
def estructura_pregunta_b_1(p_b,op_1b,op_2b,op_3b):
    layout = [[sg.Text(p_b)],[sg.Button(op_1b)],[sg.Button(op_2b)],[sg.Button(op_3b)]]
    window = sg.Window("Pregunta pensamiento logico para la computación", layout)
    while True:
        event, value = window.read()
        if event == op_1b or event == sg.WIN_CLOSED:
            break
        else:
            print("Incorrecto")
    window.close()
    
def estructura_pregunta_b_2(p_b,op_1b,op_2b,op_3b):
    layout = [[sg.Text(p_b)],[sg.Button(op_1b)],[sg.Button(op_2b)],[sg.Button(op_3b)]]
    window = sg.Window("Pregunta pensamiento logico para la computación", layout)
    while True:
        event, value = window.read()
        if event == op_2b or event == sg.WIN_CLOSED:
            break
        else:
            print("Incorrecto")
    window.close()

def estructura_pregunta_b_3(p_b,op_1b,op_2b,op_3b):
    layout = [[sg.Text(p_b)],[sg.Button(op_1b)],[sg.Button(op_2b)],[sg.Button(op_3b)]]
    window = sg.Window("Pregunta pensamiento logico para la computación", layout)
    while True:
        event, value = window.read()
        if event == op_3b or event == sg.WIN_CLOSED:
            break
        else:
            print("Incorrecto")

    window.close()
   
print("Bienvenido al cuestionario computacional") #introdución al programa, con la función print
print("****************************************************************")
print("Con este se pueden aprender habilidades esenciales")
print("para el uso efectivo el los computadores")
print("****************************************************************")
#Paso 1: registro del usuario
print("Se necesitara hacer un registro para comenzar un cuestionario")
nom_user = input("Introduce tu nombre: ")
estatus_user = input("Introduce tu carrera o area de especialización: ")
#Paso 2: selección de prueba
print("****************************************************************")
print("A continuación se seleccionara el o los cuestionarios a cursar")
print("Menú:")
print("Introducir 'A' = cuestionario pensamiento logico para la computación")
print("Introducir 'B' = cuestionario pensamiento etico computacional")
print("Introducir 'C' = hacer ambos cuestionarios")
quiz_select = input("Teclear la opción de su preferencia :")
quiz_select = quiz_select.lower()
if quiz_select == "a":
    print("Usted selecciono el cuestionario de:\npensamiento logico para la computación")
elif quiz_select == "b":
    print("Usted selecciono el cuestionario de:\npensamiento etico computacional")
elif quiz_select == "c":
    print("Usted selecciono ambos cuestionarios")

#definición de variables externas
total_uni = 0 
contador = 0

#se toma la lectura de los recursos externos
file_a1 = open("opciones_a.txt","r")
#opciones de respuesta mostradas en cuestionario, para sección a
cont_a1 = file_a1.readlines()
file_a1.close()
file_a2 = open("preguntas_a.txt","r")
#preguntas mostradas en cuestionario, para sección a
cont_a2 = file_a2.readlines()
file_a2.close()
file_b1 = open("opciones_b.txt","r")
#opciones de respuesta mostradas en cuestionario, para sección b
cont_b1 = file_b1.readlines()
file_b1.close()
file_b2 = open("preguntas_b.txt","r")
#preguntas mostradas en cuestionario, para sección b
cont_b2 = file_b2.readlines()
file_b2.close()

for x in range(len(cont_a2)):
    cont_a2[x] = str(x+1) + ". " + cont_a2[x]

for y in range(len(cont_b2)):
    cont_b2[y] = str(y+1) + ". " + cont_b2[y]
   
#cada una de las 10 preguntas cuenta con 3 opción en cada opción por lo que hay 30
#opiciones para cada cuestionario
while contador == 0:#se controlan la cantidad de pruebas a tomar con la función while
    if quiz_select == "a" or quiz_select == "c": #Paso 3: se toman las pruebas correspondientes
        total = 10
        estructura_pregunta_a_1(cont_a2[0],cont_a1[0],cont_a1[1],cont_a1[2])
        estructura_pregunta_a_3(cont_a2[1],cont_a1[3],cont_a1[4],cont_a1[5])
        estructura_pregunta_a_2(cont_a2[2],cont_a1[6],cont_a1[7],cont_a1[8])
        estructura_pregunta_a_3(cont_a2[3],cont_a1[9],cont_a1[10],cont_a1[11])
        estructura_pregunta_a_1(cont_a2[4],cont_a1[12],cont_a1[13],cont_a1[14])
        estructura_pregunta_a_1(cont_a2[5],cont_a1[15],cont_a1[16],cont_a1[17])
        estructura_pregunta_a_3(cont_a2[6],cont_a1[18],cont_a1[19],cont_a1[20])
        estructura_pregunta_a_2(cont_a2[7],cont_a1[21],cont_a1[22],cont_a1[23])
        estructura_pregunta_a_1(cont_a2[8],cont_a1[24],cont_a1[25],cont_a1[26])
        estructura_pregunta_a_2(cont_a2[9],cont_a1[27],cont_a1[28],cont_a1[29])
#se muestran los resultados para la opción A
        if quiz_select == "a":
            resultados_ab()
            res_ab = rank_ab(pt,total)
            print(f'El porcentage de puntos es {res_ab}')
            contador += 1
        if quiz_select == "c":
            total_uni += total 
        
    if quiz_select == "b" or quiz_select == "c":
        total = 10
        estructura_pregunta_b_1(cont_b2[0],cont_b1[0],cont_b1[1],cont_b1[2])
        estructura_pregunta_b_2(cont_b2[1],cont_b1[3],cont_b1[4],cont_b1[5])
        estructura_pregunta_b_1(cont_b2[2],cont_b1[6],cont_b1[7],cont_b1[8])
        estructura_pregunta_b_1(cont_b2[3],cont_b1[9],cont_b1[10],cont_b1[11])
        estructura_pregunta_b_1(cont_b2[4],cont_b1[12],cont_b1[13],cont_b1[14])
        estructura_pregunta_b_1(cont_b2[5],cont_b1[15],cont_b1[16],cont_b1[17])
        estructura_pregunta_b_1(cont_b2[6],cont_b1[18],cont_b1[19],cont_b1[20])
        estructura_pregunta_b_2(cont_b2[7],cont_b1[21],cont_b1[22],cont_b1[23])
        estructura_pregunta_b_2(cont_b2[8],cont_b1[24],cont_b1[25],cont_b1[26])
        estructura_pregunta_b_1(cont_b2[9],cont_b1[27],cont_b1[28],cont_b1[29])
#se muestran los resultados para la opción B
        
#asumir que los puntos son tomados en cuenta de acuerdo al avance es decir
#que las incorrectas no se le restan de los puntos a partir de las correctas
        
        if quiz_select == "b":
            resultados_ab()
            res_ab = rank_ab(pt,total)
            print(f'El porcentage de puntos es {res_ab}')
            contador += 1    
        if quiz_select == "c":
            total_uni += total 
#se muestran los resultados para la opción C
    if quiz_select == "c":
        resultados_c()
        res = rank_c(pt,total)
        print(f'El porcentage de puntos es {res}')
        contador += 1