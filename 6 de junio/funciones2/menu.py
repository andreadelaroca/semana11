import modelos.clases as m
import dao.operaciones as o

lista = o.EstudianteDao()

def menu():
    print("""  
1. Agregar
2. Mostrar
3. Salir
Digite la opción a realizar: """)
    
def agregar_estudiante():
    print("Digite los siguientes datos: ")
    nombre = input("Nombres: ")
    apellido = input("Apellidos: ")
    carrera = input("Carrera: ")
    promedio = int(input("Promedio: "))
    estudiante = m.Estudiante(nombre, apellido, carrera, promedio)
    lista.agregar(estudiante)
    
def mostrar_estudiante():
    print("Registros almacenados")
    for est in lista.mostrar():
        print(estudiante)
        
def main():
    while(True):
        menu()
        opcion = input()
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiante()
        elif opcion == "3":
            print("Adiós")
            break
        else:
            print("Opción inválida")
