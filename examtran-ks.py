
productos = {
    "8475HD": ["HP", 15.6, "8GB", "HDD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["Acer", 14, "8GB", "SSD", "512GB", "Intel Core i5", "Nvidia MX250"],
    "JJFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080TI"],
    "GFJHD": ["HP", 15.6, "4GB", "HDD", "1T", "Intel Core i3", "Integrada"],
    "HJUHD": ["Asus", 15.6, "12GB", "HDD", "1T", "Intel Core i7", "Nvidia GTX1050"],
    "123FHD": ["Acer", 14, "8GB", "SSD", "1T", "AMD Ryzen 5", "Integrada"],
    "290890,32": ["Acer", 15.6, "8GB", "HDD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "HDD", "1T", "AMD Ryzen 5", "Nvidia GTX1050"]
}

stock = {
    "8475HD": [387990, 10],
    "2175HD": [327990, 4],
    "JJFHD": [424990, 1],
    "GFJHD": [664990, 2],
    "HJUHD": [328990, 2],
    "123FHD": [290890, 32],
    "290890,32": [349990, 7],
    "UWU131HD": [240990, 0],
    "TS1230FHD": [240990, 0]
}

def mostrar_menu():
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Eliminar Producto.")
    print("4. Salir.")

def stock_por_marca(productos, stock):
    marca_consultar = input("Ingrese marca a consultar: ").strip().lower()
    total_stock = 0
    encontrado = False

    for prod_id, prod_info in productos.items():
        if prod_info[0].lower() == marca_consultar:
            encontrado = True
            if prod_id in stock:
                total_stock += stock[prod_id][1]

    if encontrado:
        print(f"El stock es: {total_stock}")
    else:
        print("Marca no encontrada.")

def busqueda_por_precio(productos, stock,precio_min,precio_max):
 

    notebooks_encontrados = []
    for prod_id, info_precio in stock.items():
        precio = info_precio[0]
        if precio_min <= precio <= precio_max:
            notebooks_encontrados.append(prod_id)

    if notebooks_encontrados:
        print(f"Los notebooks entre los precios consultados son: {notebooks_encontrados}")
    else:
        print("No hay notebooks en ese rango de precios.")

def eliminar_producto_por_id(productos, stock):
    modelo_a_eliminar = input("Ingrese modelo a eliminar: ").strip()

    if modelo_a_eliminar in productos and modelo_a_eliminar in stock:
        while True:
            confirmacion = input(f"¿Está seguro de eliminar el producto '{modelo_a_eliminar}'? (sí/no): ").strip().lower()
            if confirmacion == 'sí' or confirmacion == 'si':
                del productos[modelo_a_eliminar]
                del stock[modelo_a_eliminar]
                print("Producto eliminado!!")
                break
            elif confirmacion == 'no':
                print("Operación cancelada.")
                break
            else:
                print("Respuesta no válida. Por favor, ingrese 'sí' o 'no'.")
    else:
        print("¡El producto no existe!")

def principal():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese opción: "))
        except ValueError:
            print("Debe seleccionar una opción válida!!")
            continue

        if opcion == 1:
            stock_por_marca(productos, stock)
        elif opcion == 2:
            while True:
                try:
                    precio_min = int(input("Ingrese precio mínimo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!")
            while True:
                try:
                    precio_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!")
            busqueda_por_precio(productos, stock, precio_min,precio_max)
        elif opcion == 3:
            eliminar_producto_por_id(productos, stock)
        elif opcion == 4:
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida!!")

if __name__ == "__main__":
    principal()
