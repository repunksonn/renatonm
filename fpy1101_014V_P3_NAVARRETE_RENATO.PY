import os 
os.system("cls")

tipo=""
marca=""
patente=""
precio=""
multas=""
dueño=""
contaminantes=""

autos=[
            {tipo:"",marca:"",patente:"",precio:"",multas:"",dueño:"", contaminantes:""},
            
]
      
def lista():
    ipo=input("que tipo de auto")
    marca=input("que tipo de marca")
    patente=input("ingrese patente")
    precio=input("ingrese valor del vehiculo")
    if precio >=5000000:
     print("datos ingresado")

    elif precio <5000000:
            print("ingrese nuevamente")

    multas=input("tiene multas")
    contaminantes=int(input("ingrese dentro de 1500 a 3500"))
    if contaminantes <1500 and contaminantes > 3500:
         print("intente denuevo")
    dueño=input("nombre del dueño")

def busc():
    for tipo,dueño in autos[0]:

        print(autos[0] ["patente"])
    
def impr():
      if contaminantes>1500 and  contaminantes<3500:
        print(autos[0])
        print("a pasado ")
          



print("bienvenidos")
print("------menu------")
print("1)grabar\n2)buscar\nimprimir\nsalir")
opcion=0
while True:
    opcion=int(input("ingrese la opcion"))
    if opcion ==1:
        print("a elegido grabar")
        print(lista())
    elif opcion==2:
        print("que decea buscar")
        print(busc())
                
    elif opcion==3:
        print("imprimir resultado")
        print(impr())
    elif opcion==4:
        print("salir")
        break
        
    else :
        ("opcion no valida")


    



