

#librerias
import time
from time import sleep
from tqdm import tqdm
import random as rn

#Declarando las variables
valid0 = False
valid1= False
LadoA = LadoB = LadoC= 0
base = altura = 0

#declarando constantes
zero= 0
exit = 5
Triangulo = "Triangulo"
Rectangulo = "Rectangulo"
Paralelogramo = "Paralelogramo"
Cuadrado = "Cuadrado"
metros = " metros"
kilometros = " kilometros"
centimetros = " centímetros"

#Array con palabras de adorno (para que no se hagan repetitivas)
palabras = ["Excelente, ", "Maravilloso, ", "Magnífico, ", "Muy bien, ", "Perfecto, ", "De acuerdo, "]


#funcion encargada de imprimir el menú
def Menu():
    print("*******************************************************************************")
    print("")
    print("Bienvenido al software calculador de perímetros y areas Fabricado por DevKaliper. \n")
    print("Tenemos una serie de figuras geométricas a calcular, este es el menú: \n")
    print("1. Triángulo ")
    print("2. Paralelogramo ")
    print("3. Rectángulo ")
    print("4. Cuadrado ")
    print("")
    print("Presiona 5 para salir")
    print(" ")
    print("*******************************************************************************")
    


#funcion encargada de capturar la opcion del usuario y evaluar que sea un número y no una letra
def numero():
    global valid0
    try:
        num = int(input("introduce el número de la figura que deseas calcular: "))
        
        valid0 = True
        return num

    except ValueError: 
        print("* Colocaste letras, coloca un número. Por favor. * \n")



#funcion encargada de validar que el dato ingresado por el usuario esté en el rango de 1 a 4
def validar(x):
    global valid0
    global valid1
    if x >= 6 or x  <= 0:
        
        print("* Ocurrió un error. El número que colocaste no está en el rango permitido. * \n")
        
        valid0= False

    else:
        
        valid1 = True



#Funcion encargada de captar  la unidad 
def unidades():
    print("\n ")
    print(" * ¿En qué unidad trabajas? * ")

    print("\n ")
    print("1. Metros ")
    print("2. Kilometros ")
    print("3. Centímetros ")
    print("4. No está en lista")
    print("\n ")

    opcion= int(input("* Selecciona el número de la unidad con la que estés trabajando * : "))

    if opcion == 1:
        x = metros
        return  x

    elif opcion == 2:
        x = kilometros
        return  x

    elif opcion == 3:
        x = centimetros
        return  x
    
    else:

        print("\n ")
        print(" * La unidad de tu figura no está comtemplada por el momento. Estaremos añadiendo más unidades en los proximos días *")

        return " unidades"

        
#---------------------------------------------------------Triangulo----------------------------------------------


#funcion encargada de calcular el perímetro del triángulo
def triangulo_perimetro():
    global LadoA
    global LadoB
    global LadoC
    print("\n ")

    #estos bluces for hacen que el titulo se vea encerrado en una cajita de asteríscos
    for x in range (len(Triangulo)+4):
        print ( "*", end="")

    print ("\n* {} *".format(Triangulo))

    for x in range (len(Triangulo)+4):
        print ( "*", end="")
    
    print("\n ")
    print("Excelente, procedamos a calcular el perimetro del Triángulo. ")
    LadoA = int(input("Dame el valor lado A del triangulo (solo el número): "))
    LadoB = int(input("Dame el valor lado B del triangulo (solo el número): "))
    LadoC = int(input("Dame el valor lado C del triangulo (solo el número): "))

    #cambio el resultado a un string para luego poner anexarle la unidad de una forma más facil
    calculoTP = str(LadoA + LadoB + LadoC)
    return calculoTP



#funcion encargada de calcular el area del triangulo
def triangulo_area():
    global base
    global altura

    print("\n ")

    #el rn.choice elige una palagra aleatoria dentro del array "palabras"
    print(rn.choice(palabras) + " ahora procedamos a calcular el area del Triángulo. ")
    base = int(input("Dame el valor de la base del triangulo (solo el número): "))
    altura = int(input("Dame el valor de la altura del triangulo (solo el número): "))

    #cambio el resultado a un string para luego poner anexarle la unidad de una forma más facil
    calculoTA = str((base * altura)/2)
    return calculoTA



#--------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------Paralelogramo-----------------------------------------------------------

#funcion encargada de calcular el perímetro del paralelogramo
def paralelo_perimetro():
    global LadoA
    global LadoB
    
    print("\n ")
    
    #estos bluces for hacen que el titulo se vea encerrado en una cajita de asteríscos
    for x in range (len(Paralelogramo)+4):
        print ( "*", end="")

    print ("\n* {} *".format(Paralelogramo))

    for x in range (len(Paralelogramo)+4):
        print ( "*", end="")
    
    print("\n ")
    
    #el rn.choice elige una palagra aleatoria dentro del array "palabras"
    print(rn.choice(palabras) + " ahora procedamos a calcular el perimetro del Paralelogramo. ")
    LadoA = int(input("Dame el valor lado A del Paralelogramo (solo el número): "))
    LadoB = int(input("Dame el valor lado B del Paralelogramo (solo el número): "))
    
    #cambio el resultado a un string para luego poner anexarle la unidad de una forma más facil
    calculoPP = str(2 * (LadoA + LadoB))
    return calculoPP



#funcion encargada de calcular el area del paralelogramo
def paralelo_area():
    global base
    global altura

    print("\n ")
    #el rn.choice elige una palagra aleatoria dentro del array "palabras"
    print(rn.choice(palabras) + " ahora procedamos a calcular el area del Paralelogramo. ")
    base = int(input("Dame el valor de la base del Paralelogramo (solo el número): "))
    altura = int(input("Dame el valor de la altura del Paralelogramo (solo el número): "))

    #cambio el resultado a un string para luego poner anexarle la unidad de una forma más facil
    calculoPA = str((base * altura))
    return calculoPA


#----------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------Rectángulo-------------------------------------------------------------


#funcion encargada de calcular el perímetro del rectangulo
def rectangulo_perimetro():
    global LadoA
    global LadoB
    
    print("\n ")
    
    #estos bluces for hacen que el titulo se vea encerrado en una cajita de asteríscos
    for x in range (len(Rectangulo)+4):
        print ( "*", end="")

    print ("\n* {} *".format(Rectangulo))

    for x in range (len(Rectangulo)+4):
        print ( "*", end="")

    print("\n ")

    #el rn.choice elige una palagra aleatoria dentro del array "palabras"
    print(rn.choice(palabras) + " ahora procedamos a calcular el perimetro del rectangulo. ")
    LadoA = int(input("Dame el valor lado A del rectangulo (solo el número): "))
    LadoB = int(input("Dame el valor lado B del rectangulo (solo el número): "))
    
    #cambio el resultado a un string para luego poner anexarle la unidad de una forma más facil
    calculoRP = str(2 * (LadoA + LadoB))
    return calculoRP



#funcion encargada de calcular el area del rectangulo
def rectangulo_area():
    global base
    global altura

    print("\n ")
    #el rn.choice elige una palagra aleatoria dentro del array "palabras"
    print(rn.choice(palabras) + " ahora  procedamos a calcular el area del rectangulo. ")
    base = int(input("Dame el valor de la base del rectangulo (solo el número): "))
    altura = int(input("Dame el valor de la altura del rectangulo (solo el número): "))

    #cambio el resultado a un string para luego poner anexarle la unidad de una forma más facil
    calculoRA = str((base * altura))
    return calculoRA


#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------Cuadrado-------------------------------------------------------------


#funcion encargada de calcular el perímetro del cuadrado
def cuadrado_perimetro():
    global LadoA
    
    
    print("\n ")
    
    #estos bluces for hacen que el titulo se vea encerrado en una cajita de asteríscos
    for x in range (len(Cuadrado)+4):
        print ( "*", end="")

    print ("\n* {} *".format(Cuadrado))

    for x in range (len(Cuadrado)+4):
        print ( "*", end="")

    print("\n ")

    #el rn.choice elige una palagra aleatoria dentro del array "palabras"
    print(rn.choice(palabras) + " ahora procedamos a calcular el perimetro del Cuadrado. ")
    LadoA = int(input("Dame el valor lado A del Cuadrado (solo el número): "))
  
    
    #cambio el resultado a un string para luego poner anexarle la unidad de una forma más facil
    calculoCP = str(4 * LadoA)
    return calculoCP



#funcion encargada de calcular el area del Cuadrado
def cuadrado_area():
    global base
    

    print("\n ")
    #el rn.choice elige una palagra aleatoria dentro del array "palabras"
    print(rn.choice(palabras) + " ahora  procedamos a calcular el area del Cuadrado. ")
    base = int(input("Dame el valor del lado del Cuadrado (solo el número): "))
    

    #cambio el resultado a un string para luego poner anexarle la unidad de una forma más facil
    calculoCA = str((base ** 2))
    return calculoCA


#-----------------------------------------------------------------------------------------------------------------------




#funcion encargada de retornar los calculos de acuerdo a la figura elegida "y" será la unidad de los valores
def opcion(x, y):
    if x == 1:
        Pt= triangulo_perimetro() + y 
        At=triangulo_area() + y
        resultado1= "El perimetro del triangulo es de: {} y su area es de: {} ".format(Pt,At)
        return resultado1

    elif x == 2:
        Pp= paralelo_perimetro() + y
        Ap= paralelo_area() + y
        resultado2 = "El perimetro del Paralelogramo es de: {} y su area es de: {} ".format(Pp,Ap)
        return resultado2
        
    elif x == 3:
        Pr= rectangulo_perimetro() + y
        Ar= rectangulo_area() + y
        resultado3= "El perimetro del rectangulo es de: {} y su area es de: {} ".format(Pr,Ar)
        return resultado3
    
    elif x == 4:
        Pc= cuadrado_perimetro() + y
        Ac= cuadrado_area() + y
        resultado4= "El perimetro del cuadrado es de: {} y su area es de: {} ".format(Pc,Ac)
        return resultado4


#funcion principal
def main():

    #globalizando todas las variables que usaré para que la funcion las capte
    global LadoA, LadoB, LadoC, valid0, valid1, base, altura

    #"zero" está valorizado con el número 0 para así poder reutilizar las mismas variables.
    LadoA = LadoB = LadoC= zero
    base = altura = zero
    figura = zero

    #cont es un contador
    cont= zero

    #bucle en el cual correrá todo el programa, hasta que el usuario desee salir
    while figura != exit:
        valid0 = False
        valid1= False
        figura = zero

        #Si el contador es mayor a 0 entonces es porque ya se ha jugado más de una vez.
        if cont > zero:
            #este time.sleep es para que la pantalla de menú tenga un delay de 2,5 segundos después de cada partida
            time.sleep(2.5)
        
        
        Menu()

       #Bucle que evalua si la opcion elegida es valida, si no es valida, estará pidiendo una opcion correcta indefinidamente.
        while valid1 == False:
            if valid0 == False:
                figura= numero()
            
            if valid0 == True:
                validar(figura)


        #si el numero elegido por el usuario es una de las opciones permitidas y no el 4 para salir, entonces se procede a invocar a la funcion "unidad" para saber en qué unidad estarán los valores, luego se invoca a la funcion "opcion" dandole como parametro la opcion del usuario y la unidad. Todo esto se almacenará en la variable "calculator"

        if figura != 5:
            
            unidad= unidades()

            calculator= opcion(figura, unidad)

            # este for dará el efecto de una barra de progreso
            print("\n ")
            for i in tqdm(range(10)):
                sleep(0.2)
            
            #se imprimen los calculos
            print("\n ")
            print(calculator)
            print("\n ")

        
                
        #contador incrementando
        cont=cont + 1
        
    #si el usuario elige salir    
    print("Gracias por preferir a Dev kalilper.")
   

if __name__ == "__main__":
    main()

 