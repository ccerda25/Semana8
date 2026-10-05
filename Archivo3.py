nombres = input("Dime tus nombres: ")
apellidos = input("Dime tus apellidos: ")
edad = input("Dime tus edad: ")
carrera = input("Dime tus carrera: ")

datos = f"Nombre: {nombres.title()}\nApellidos:{apellidos.title()}\nEdad:{edad.title()}\nCarrera:{carrera.title()}\n"

with open("estudiantes.txt", "w", encoding="utf-8") as archivo:
    archivo.write(datos)

print("Archivo creado")