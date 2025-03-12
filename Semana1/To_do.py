class Tareas():

    def __init__(self, archivo):
        self.archivo = archivo

    def agregar_tarea(self, tarea):
        try:
            with open(self.archivo, 'a') as file:
                file.write(tarea + '\n')
            print(f"Tarea agregada: {tarea}")
        except Exception as e:
            print(f"Error al agregar la tarea: {e}")

    def mostrar_tareas(self):
        try:
            with open(self.archivo, 'r') as file:
                tareas = file.readlines()
                if not tareas:
                    print("No hay tareas para mostrar.")
                else:
                    print("Tareas pendientes:")
                    for i, tarea in enumerate(tareas, 1):
                        print(f"{i}. {tarea.strip()}")
        except FileNotFoundError:
            print("El archivo no existe.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def marcar_completada(self, numero_tarea):
        try:
            with open(self.archivo, 'r') as file:
                tareas = file.readlines()

            if numero_tarea < 1 or numero_tarea > len(tareas):
                print("Número de tarea inválido.")
                return

            tarea_eliminada = tareas.pop(numero_tarea - 1)

            with open(self.archivo, 'w') as file:
                file.writelines(tareas)

            print(f"Tarea completada: {tarea_eliminada.strip()}")
        except FileNotFoundError:
            print("El archivo no existe.")
        except Exception as e:
            print(f"Error al modificar el archivo: {e}")

# Crear instancia de la clase
gestor_tareas = Tareas("tareas.txt")

def menu():
    while True:
        print("\nMenú de opciones")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")
        
        try:
            opcion = int(input("Elija una opción: "))
        except ValueError:
            print("Error: Debes ingresar un número.")
            continue

        match opcion:
            case 1:
                tarea = input("Ingrese la nueva tarea: ")
                gestor_tareas.agregar_tarea(tarea)
            case 2:
                gestor_tareas.mostrar_tareas()
            case 3:
                gestor_tareas.mostrar_tareas()
                try:
                    num = int(input("Ingrese el número de la tarea a marcar como completada: "))
                    gestor_tareas.marcar_completada(num)
                except ValueError:
                    print("Error: Debes ingresar un número válido.")
            case 4:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

# Ejecutar menú
menu()