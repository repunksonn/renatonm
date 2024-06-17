import os

trabajadores = []

def registrar_trabajador():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    cargo = input("Ingrese cargo (CEO, Desarrollador, Analista de datos): ")
    sueldo_bruto = float(input("Ingrese sueldo bruto: "))

    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    liquido_pagar = sueldo_bruto - desc_salud - desc_afp

    trabajadores.append({
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "sueldo_bruto": sueldo_bruto,
        "desc_salud": desc_salud,
        "desc_afp": desc_afp,
        "liquido_pagar": liquido_pagar
    })

def listar_trabajadores():
    for trabajador in trabajadores:
        print("Nombre: {} {}".format(trabajador["nombre"], trabajador["apellido"]))
        print("Cargo: {}".format(trabajador["cargo"]))
        print("Sueldo Bruto: {}".format(trabajador["sueldo_bruto"]))
        print("Descuento Salud: {}".format(trabajador["desc_salud"]))
        print("Descuento AFP: {}".format(trabajador["desc_afp"]))
        print("Líquido a Pagar: {}".format(trabajador["liquido_pagar"]))
        print("")

def imprimir_planilla():
    cargo = input("Ingrese cargo para imprimir planilla (CEO, Desarrollador, Analista de datos): ")
    file_name = "planilla_{}.txt".format(cargo)
    
    with open(file_name, "w") as file:
        for trabajador in trabajadores:
            if trabajador["cargo"] == cargo:
                file.write("Nombre: {} {}\n".format(trabajador["nombre"], trabajador["apellido"]))
                file.write("Cargo: {}\n".format(trabajador["cargo"]))
                file.write("Sueldo Bruto: {}\n".format(trabajador["sueldo_bruto"]))
                file.write("Descuento Salud: {}\n".format(trabajador["desc_salud"]))
                file.write("Descuento AFP: {}\n".format(trabajador["desc_afp"]))
                file.write("Líquido a Pagar: {}\n".format(trabajador["liquido_pagar"]))

def salir_programa():
    print("Saliendo del programa...")
    os._exit(0)

while True:
    print("1. Registrar trabajador")
    print("2. Listar trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_trabajador()
    elif opcion == "2":
        listar_trabajadores()
    elif opcion == "3":
        imprimir_planilla()
    elif opcion == "4":
        salir_programa()
    else:
        print("Opción inválida. Inténtelo de nuevo.")