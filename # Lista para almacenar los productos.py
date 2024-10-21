# Lista para almacenar los productos
productos = []

def obtener_datos_producto():
    """Obtener datos del producto del usuario con validación."""
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad disponible del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el precio y la cantidad.")
    return {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}

def añadir_producto():
    """Añadir producto a la lista."""
    producto = obtener_datos_producto()
    productos.append(producto)
    print(f"Producto '{producto['nombre']}' añadido con éxito.")

def ver_productos():
    """Mostrar la lista completa de productos."""
    if productos:
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f} - Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos para mostrar.")

def actualizar_producto():
    """Actualizar un producto existente."""
    ver_productos()
    try:
        indice = int(input("Seleccione el número del producto a actualizar: ")) - 1
        if 0 <= indice < len(productos):
            productos[indice] = obtener_datos_producto()
            print("Producto actualizado con éxito.")
        else:
            print("Número de producto inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def eliminar_producto():
    """Eliminar un producto de la lista."""
    ver_productos()
    try:
        indice = int(input("Seleccione el número del producto a eliminar: ")) - 1
        if 0 <= indice < len(productos):
            eliminado = productos.pop(indice)
            print(f"Producto '{eliminado['nombre']}' eliminado con éxito.")
        else:
            print("Número de producto inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def guardar_datos():
    """Guardar la lista de productos en un archivo de texto."""
    with open("productos.txt", 'w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados con éxito.")

def cargar_datos():
    """Cargar los productos desde un archivo de texto."""
    try:
        with open("productos.txt", 'r') as file:
            for linea in file:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({'nombre': nombre, 'precio': float(precio), 'cantidad': int(cantidad)})
        print("Datos cargados con éxito.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos.")

def menu():
    """Menú principal del programa."""
    cargar_datos()
    while True:
        print("\nSeleccione el proceso que desea aplicar")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion.isdecimal():
            opcion = int(opcion)
            if opcion == 1:
                añadir_producto()
            elif opcion == 2:
                ver_productos()
            elif opcion == 3:
                actualizar_producto()
            elif opcion == 4:
                eliminar_producto()
            elif opcion == 5:
                guardar_datos()
                break
            else:
                print("Por favor, introduzca un número del 1 al 5")
        else:
            print("Por favor, introduzca un número válido.")

menu()
