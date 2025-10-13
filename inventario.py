"""Modulo de Gestion de Inventario, Operaciones: alta, baja, modificacion, reabastecimiento y ventas
"""

from datetime import datetime

def validar_codigo(codigo, productos, debe_existir=True):
    """Valida que un código cumpla las condiciones requeridas"""
    if not codigo or len(codigo.strip()) == 0:
        return False, "El código no puede estar vacío"
    
    existe = any(p['codigo'] == codigo for p in productos)
    
    if debe_existir and not existe:
        return False, "El código no existe en el inventario"
    elif not debe_existir and existe:
        return False, "El código ya existe en el inventario"
    
    return True, ""


def validar_precio(precio_str):
    """Valida que el precio sea un número positivo"""
    try:
        precio = float(precio_str)
        if precio <= 0:
            return False, "El precio debe ser mayor a 0"
        return True, precio
    except ValueError:
        return False, "El precio debe ser un número válido"


def validar_stock(stock_str):
    """Valida que el stock sea un número entero no negativo"""
    try:
        stock = int(stock_str)
        if stock < 0:
            return False, "El stock no puede ser negativo"
        return True, stock
    except ValueError:
        return False, "El stock debe ser un número entero"

def alta_producto(productos):
    """Registra un nuevo producto en el inventario"""
    print("\n" + "="*60)
    print("ALTA DE PRODUCTO")
    print("="*60)
    
    try:
        # Solicitar código
        codigo = input("Código del producto: ").strip().upper()
        valido, mensaje = validar_codigo(codigo, productos, debe_existir=False)
        if not valido:
            print(f"{mensaje}")
            return
        
        # Solicitar nombre
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("El nombre no puede estar vacio")
            return
        
        # Solicitar precio
        precio_str = input("Precio: ")
        valido, precio = validar_precio(precio_str)
        if not valido:
            print(f"{precio}")
            return
        
        # Solicitar stock
        stock_str = input("Stock inicial: ")
        valido, stock = validar_stock(stock_str)
        if not valido:
            print(f"{stock}")
            return
        
        # Solicitar stock mínimo
        stock_min_str = input("Stock minimo: ")
        valido, stock_minimo = validar_stock(stock_min_str)
        if not valido:
            print(f"{stock_minimo}")
            return
        
        # Crear producto
        nuevo_producto = {
            'codigo': codigo,
            'nombre': nombre,
            'precio': precio,
            'stock': stock,
            'stock_minimo': stock_minimo,
            'vendidos_hoy': 0
        }
        
        productos.append(nuevo_producto)
        print(f"\nProducto '{nombre}' registrado exitosamente con codigo {codigo}")
        
    except Exception as e:
        print(f"\nError al registrar producto: {e}")


def baja_producto(productos):
    """Elimina un producto del inventario"""
    print("\n" + "="*60)
    print("BAJA DE PRODUCTO")
    print("="*60)
    
    if not productos:
        print("No hay productos en el inventario")
        return
    
    try:
        codigo = input("Codigo del producto a eliminar: ").strip().upper()
        valido, mensaje = validar_codigo(codigo, productos, debe_existir=True)
        if not valido:
            print(f"{mensaje}")
            return
        
        # Buscar y mostrar producto
        for i, producto in enumerate(productos):
            if producto['codigo'] == codigo:
                print(f"\nProducto encontrado:")
                print(f"  Código: {producto['codigo']}")
                print(f"  Nombre: {producto['nombre']}")
                print(f"  Precio: Bs. {producto['precio']:.2f}")
                print(f"  Stock: {producto['stock']}")
                
                confirmacion = input("\n¿Confirma la eliminacion? (s/n): ").strip().lower()
                if confirmacion == 's':
                    productos.pop(i)
                    print(f"\nProducto '{producto['nombre']}' eliminado exitosamente")
                else:
                    print("\nOperacion cancelada")
                return
                
    except Exception as e:
        print(f"\nError al eliminar producto: {e}")