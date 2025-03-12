
productos = [
    {"id": 1, "nombre": "Camiseta", "precio": 19.99, "stock": 50},
    {"id": 2, "nombre": "Zapatos", "precio": 59.99, "stock": 20},
    {"id": 3, "nombre": "Gorra", "precio": 19.99, "stock": 20}
]
clientes = [
    {"nombre": "Sasuke", "correo": "sasuke@correo", "direccion": "Calle 33 KRA 54"},
    {"nombre": "Naruto", "correo": "naruto@correo", "direccion": "KRA 48 CL 52"},
    {"nombre": "Shakira", "correo": "shakira@correo", "direccion": "KRA 20 CL 52"}
]
pedidos = [
    {"id_pedido": 101, "cliente":clientes[0], "productos":[(productos[0]), (productos[1])]},
    {"id_pedido": 102, "cliente":clientes[1], "productos":[(productos[1]), (productos[2])]},
    {"id_pedido": 103, "cliente":clientes[2], "productos":[(productos[2]), (productos[0])]}
]


def menu():
    while True:
        print("\nMenu de opciones")
        print("1 Verificar productos")
        print("2 ver clientes")
        print("3 ver pedidos")
        print("4 Agregar un producto")
        print("5 Confirmar estado de pedido")
        print("6 Buscar pedido por correo")
        

        opcion = int(input("Elija una opción: "))

        match opcion:
            case 1:
                print("\nLista de productos:")
                for producto in productos:
                    print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Stock: {producto['stock']}")
            case 2:
                print("\nLisa de clientes")
                for cliente in clientes:
                    print(f"Nombre: {cliente['nombre']}, Correo: {cliente['correo']}, direccion: {cliente['direccion']}")
            case 3:
                print("\nLista de pedidos:")
                for pedido in pedidos:
                    print(f"ID_pedido: {pedido['id_pedido']}, Cliente: {pedido['cliente']['nombre']}, Estado: {pedido.get('estado', 'Pendiente')}")
                    print("Productos:")
                    for prod in pedido["productos"]:
                        print(f"   - {prod['nombre']}")
menu()
