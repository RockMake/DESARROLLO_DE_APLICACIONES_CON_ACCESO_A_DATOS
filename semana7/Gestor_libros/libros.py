# Ejercicio: Sistema de Gestión de Libros
# Descripción del problema
# Desarrolla un programa en Python que permita gestionar un catálogo de libros. El programa debe interactuar con una base de datos SQLite para realizar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar). Además, el sistema debe permitir exportar la lista completa de libros almacenados en la base de datos a un archivo de texto (libros.txt).
# El programa debe seguir los principios de POO, asegurando que cada clase tenga una única responsabilidad.
# ________________________________________
# Requisitos del programa
# 1.	Base de datos :
# •	Usa SQLite para almacenar los datos de los libros.
# •	La tabla libros debe tener los siguientes campos:
# •	id (clave primaria, autoincremental)
# •	titulo (texto)
# •	autor (texto)
# •	anio_publicacion (entero)
# 2.	Operaciones CRUD :
# •	Crear : Agregar un nuevo libro al catálogo.
# •	Leer : Mostrar todos los libros o buscar un libro por su ID.
# •	Actualizar : Modificar los datos de un libro existente.
# •	Eliminar : Eliminar un libro del catálogo.
# 3.	Exportación a archivo :
# •	El programa debe permitir exportar todos los libros almacenados en la base de datos a un archivo de texto llamado libros.txt. Cada línea del archivo debe contener los detalles de un libro en el siguiente formato:
# ID: 1 , Título: El Quijote, Autor: Miguel de Cervantes, Año: 1605
# 4.	Principios de POO :
# •	Divide el programa en clases, siguiendo el principio de responsabilidad única.
# •	Ejemplo de clases sugeridas:
# •	Libro: Representa un libro individual.
# •	BaseDeDatos: Maneja la conexión y operaciones con la base de datos.
# •	GestorLibros: Implementa la lógica de negocio para gestionar los libros.
# •	Exportador: Se encarga de exportar los datos a un archivo de texto.


import sqlite3
import tkinter as tk
from tkinter import messagebox


class BaseDeDatos:
    def __init__(self, db_name="libros.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                anio_publicacion INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def ejecutar_consulta(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        self.connection.commit()

    def obtener_datos(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.connection.close()


class GestorLibros:
    def __init__(self, db):
        self.db = db

    def agregar_libro(self, titulo, autor, anio_publicacion):
        self.db.ejecutar_consulta(
            "INSERT INTO libros (titulo, autor, anio_publicacion) VALUES (?, ?, ?)",
            (titulo, autor, anio_publicacion)
        )

    def obtener_libros(self):
        return self.db.obtener_datos("SELECT * FROM libros")

    def buscar_libro(self, libro_id):
        return self.db.obtener_datos("SELECT * FROM libros WHERE id = ?", (libro_id,))

    def actualizar_libro(self, libro_id, titulo, autor, anio_publicacion):
        self.db.ejecutar_consulta(
            "UPDATE libros SET titulo = ?, autor = ?, anio_publicacion = ? WHERE id = ?",
            (titulo, autor, anio_publicacion, libro_id)
        )

    def eliminar_libro(self, libro_id):
        self.db.ejecutar_consulta("DELETE FROM libros WHERE id = ?", (libro_id,))


class Exportador:
    @staticmethod
    def exportar_a_txt(libros, archivo="libros.txt"):
        with open(archivo, "w") as f:
            for libro in libros:
                f.write(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Año: {libro[3]}\n")


class Interfaz:
    def __init__(self, root, gestor_libros):
        self.root = root
        self.gestor_libros = gestor_libros
        self.root.title("Gestion de Libros")

        # Widgets
        self.titulo_principal = tk.Label(root, text="Gestor de libros por: Duvan Ramirez", font=("Arial", 16, "bold"), pady=10)
        self.titulo_principal.grid(row=0, column=0, columnspan=2)
        
        self.titulo_label = tk.Label(root, text="Título:", padx=10 , pady=10)
        self.titulo_label.grid(row=1, column=0)
        
        self.titulo_entry = tk.Entry(root)
        self.titulo_entry.grid(row=1, column=1, padx=10 , pady=10)
    

        self.autor_label = tk.Label(root, text="Autor:" , padx=10 , pady=10)
        self.autor_label.grid(row=2, column=0)
        self.autor_entry = tk.Entry(root)
        self.autor_entry.grid(row=2, column=1)

        self.anio_label = tk.Label(root, text="Año de Publicación:" , padx=10 , pady=10)
        self.anio_label.grid(row=3, column=0)
        self.anio_entry = tk.Entry(root)
        self.anio_entry.grid(row=3, column=1)

        self.agregar_button = tk.Button(root, text="Agregar Libro", command=self.agregar_libro, bg='#9FB3DF', fg='#333333')
        self.agregar_button.config(bg='#f0f0f0', fg='#333333')
        self.agregar_button.grid(row=4, column=0, columnspan=2 , padx=10 , pady=10)

        self.lista_libros = tk.Listbox(root, width=50)
        self.lista_libros.grid(row=6, column=0, columnspan=2)
        self.cargar_libros()
        
        
        self.eliminar_button = tk.Button(root, text="Eliminar Libro", command=self.eliminar_libro)
        self.eliminar_button.config(bg='#F7374F', fg='#F1EFEC')
    
        self.eliminar_button.grid(row=7, column=0, columnspan=1, padx=10 , pady=10)
        
        
        self.exportar_button = tk.Button(root, text="Exportar a TXT", command=self.exportar_libros, bg='#f0f0f0', fg='#333333', )
        self.exportar_button.config(bg='#f0f0f0', fg='#333333')
        self.exportar_button.grid(row=7, column=1, columnspan=2 , padx=10 , pady=10)

    def agregar_libro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        anio = self.anio_entry.get()

        if titulo and autor and anio.isdigit():
            self.gestor_libros.agregar_libro(titulo, autor, int(anio))
            self.cargar_libros()
            self.titulo_entry.delete(0, tk.END)
            self.autor_entry.delete(0, tk.END)
            self.anio_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "completa todos los campos correctamente.")

    def cargar_libros(self):
        self.lista_libros.delete(0, tk.END)
        libros = self.gestor_libros.obtener_libros()
        for libro in libros:
            self.lista_libros.insert(tk.END, f"ID: {libro[0]}, Titulo: {libro[1]}, Autor: {libro[2]}, Ano: {libro[3]}")

    def exportar_libros(self):
        libros = self.gestor_libros.obtener_libros()
        Exportador.exportar_a_txt(libros)
        messagebox.showinfo("Exportacioon", "Los libros han sido exportados a libros.txt")
    
    def eliminar_libro(self):
        libros = self.lista_libros.curselection()
        if libros:
            libro_id = self.lista_libros.get(libros[0]).split(",")[0].split(":")[1].strip()
            self.gestor_libros.eliminar_libro(libro_id)
            self.cargar_libros()
        else:
            messagebox.showerror("Error", "Selecciona un libro para eliminar.")
    


if __name__ == "__main__":
    db = BaseDeDatos()
    gestor = GestorLibros(db)
    root = tk.Tk()
    app = Interfaz(root, gestor)
    root.mainloop()
    db.cerrar_conexion()