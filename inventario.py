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
                print(f"  Codigo: {producto['codigo']}")
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
    
def modificar_producto(productos):
    """Modifica los datos de un producto existente"""
    print("\n" + "="*60)
    print("MODIFICAR PRODUCTO")
    print("="*60)
    
    if not productos:
        print("No hay productos en el inventario")
        return
    
    try:
        codigo = input("Codigo del producto a modificar: ").strip().upper()
        valido, mensaje = validar_codigo(codigo, productos, debe_existir=True)
        if not valido:
            print(f"{mensaje}")
            return
        
        # Buscar producto
        for producto in productos:
            if producto['codigo'] == codigo:
                print(f"\nProducto actual:")
                print(f"  1. Nombre: {producto['nombre']}")
                print(f"  2. Precio: Bs. {producto['precio']:.2f}")
                print(f"  3. Stock: {producto['stock']}")
                print(f"  4. Stock mínimo: {producto['stock_minimo']}")
                
                campo = input("\n¿Que campo desea modificar? (1-4): ").strip()
                
                if campo == '1':
                    nuevo_nombre = input("Nuevo nombre: ").strip()
                    if nuevo_nombre:
                        producto['nombre'] = nuevo_nombre
                        print("Nombre actualizado")
                    else:
                        print("El nombre no puede estar vacio")
                        
                elif campo == '2':
                    nuevo_precio_str = input("Nuevo precio: ")
                    valido, nuevo_precio = validar_precio(nuevo_precio_str)
                    if valido:
                        producto['precio'] = nuevo_precio
                        print("Precio actualizado")
                    else:
                        print(f"{nuevo_precio}")
                        
                elif campo == '3':
                    nuevo_stock_str = input("Nuevo stock: ")
                    valido, nuevo_stock = validar_stock(nuevo_stock_str)
                    if valido:
                        producto['stock'] = nuevo_stock
                        print("Stock actualizado")
                    else:
                        print(f"{nuevo_stock}")
                        
                elif campo == '4':
                    nuevo_min_str = input("Nuevo stock minimo: ")
                    valido, nuevo_min = validar_stock(nuevo_min_str)
                    if valido:
                        producto['stock_minimo'] = nuevo_min
                        print("Stock minimo actualizado")
                    else:
                        print(f"{nuevo_min}")
                else:
                    print("Opcion invalida")
                return
                
    except Exception as e:
        print(f"\nError al modificar producto: {e}")
def reabastecer_producto(productos):
    """Agregue stock a un producto existente"""
    print("\n" + "="*60)
    print("REABASTECER PRODUCTO")
    print("="*60)
    
    if not productos:
        print("No hay productos en el inventario")
        return
    
    try:
        codigo = input("Código del producto: ").strip().upper()
        valido, mensaje = validar_codigo(codigo, productos, debe_existir=True)
        if not valido:
            print(f"{mensaje}")
            return
        
        # Buscar producto
        for producto in productos:
            if producto['codigo'] == codigo:
                print(f"\nProducto: {producto['nombre']}")
                print(f"Stock actual: {producto['stock']}")
                
                cantidad_str = input("Cantidad a añadir: ")
                valido, cantidad = validar_stock(cantidad_str)
                if not valido:
                    print(f"{cantidad}")
                    return
                
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0")
                    return
                
                producto['stock'] += cantidad
                print(f"\nStock actualizado. Nuevo stock: {producto['stock']}")
                return

    except Exception as e:
        print(f"\nError al reabastecer: {e}")
        
def registrar_venta(productos, ventas_semana):
    """Registra una venta y actualiza el inventario"""
    print("\n" + "="*60)
    print("REGISTRAR VENTA")
    print("="*60)
    
    if not productos:
        print("No hay productos en el inventario")
        return
    
    try:
        codigo = input("Codigo del producto: ").strip().upper()
        valido, mensaje = validar_codigo(codigo, productos, debe_existir=True)
        if not valido:
            print(f"{mensaje}")
            return
        
        # Buscar producto
        for producto in productos:
            if producto['codigo'] == codigo:
                print(f"\nProducto: {producto['nombre']}")
                print(f"Precio: Bs. {producto['precio']:.2f}")
                print(f"Stock disponible: {producto['stock']}")
                
                cantidad_str = input("Cantidad a vender: ")
                valido, cantidad = validar_stock(cantidad_str)
                if not valido:
                    print(f"{cantidad}")
                    return
                
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0")
                    return
                
                if cantidad > producto['stock']:
                    print(f"Stock insuficiente. Solo hay {producto['stock']} unidades")
                    return
                
                # Registrar venta
                total = producto['precio'] * cantidad
                producto['stock'] -= cantidad
                producto['vendidos_hoy'] += cantidad
                
                # Actualizar matriz semanal
                dia = datetime.now().weekday()  # 0=Lunes, 6=Domingo
                hora = datetime.now().hour
                
                # Determinar franja (0= Manana, 1= Tarde, 2 = Noche)
                if 6 <= hora < 12:
                    franja = 0
                elif 12 <= hora < 18:
                    franja = 1
                else:
                    franja = 2
                
                ventas_semana[dia][franja] += total
                
                print(f"\nVenta registrada exitosamente")
                print(f"   Cantidad: {cantidad}")
                print(f"   Total: Bs. {total:.2f}")
                print(f"   Stock restante: {producto['stock']}")
                
                if producto['stock'] <= producto['stock_minimo']:
                    print(f"\nALERTA: Stock bajo el minimo ({producto['stock_minimo']})")
                
                return
                
    except Exception as e:
        print(f"\nError al registrar venta: {e}")
def mostrar_inventario(productos):
    """Muestra todos los productos del inventario"""
    print("\n" + "="*60)
    print("INVENTARIO COMPLETO")
    print("="*60)
    
    if not productos:
        print("No hay productos en el inventario")
        return
    
    print(f"\n{'Código':<10} {'Nombre':<25} {'Precio':>10} {'Stock':>8} {'Mín.':>6}")
    print("-" * 60)
    
    for producto in productos:
        alerta = " !!! " if producto['stock'] <= producto['stock_minimo'] else ""
        print(f"{producto['codigo']:<10} {producto['nombre']:<25} "
              f"Bs. {producto['precio']:>6.2f} {producto['stock']:>8} "
              f"{producto['stock_minimo']:>6}{alerta}")
    
    print(f"\nTotal de productos: {len(productos)}")