"""Modulo de buasquedas y ordenamientos aca se Implementa busqueda lineal, binaria y algoritmos de ordenamiento"""

def buscar_lineal_nombre(productos, nombre_buscar):
    """Busqueda lineal por nombre"""
    resultados = []
    nombre_buscar = nombre_buscar.lower()
    
    for producto in productos:
        if nombre_buscar in producto['nombre'].lower():
            resultados.append(producto)
    
    return resultados

def buscar_binaria_codigo(productos_ordenados, codigo_buscar):
    """Busqueda binaria por codigo, lo unico que requiere es que la lista este ordenada por codigo"""
    izq = 0
    der = len(productos_ordenados) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        codigo_medio = productos_ordenados[medio]['codigo']
        
        if codigo_medio == codigo_buscar:
            return productos_ordenados[medio]
        elif codigo_medio < codigo_buscar:
            izq = medio + 1
        else:
            der = medio - 1
    return None
def ordenar_burbuja(productos, clave, ascendente=True):
    """Ordenamiento burbuja, para obtener el valor a comparar"""
    n = len(productos)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascendente:
                condicion = clave(productos[j]) > clave(productos[j + 1])
            else:
                condicion = clave(productos[j]) < clave(productos[j + 1])
            
            if condicion:
                productos[j], productos[j + 1] = productos[j + 1], productos[j]


def ordenar_seleccion(productos, clave, ascendente=True):
    """Ordenamiento por seleccion para obtener el valor a comparar"""
    n = len(productos)
    
    for i in range(n):
        idx_seleccionado = i
        
        for j in range(i + 1, n):
            if ascendente:
                condicion = clave(productos[j]) < clave(productos[idx_seleccionado])
            else:
                condicion = clave(productos[j]) > clave(productos[idx_seleccionado])
            
            if condicion:
                idx_seleccionado = j
        
        productos[i], productos[idx_seleccionado] = productos[idx_seleccionado], productos[i]
def buscar_por_nombre(productos):
    """Funcion para busqueda lineal por nombre"""
    print("\n" + "="*60)
    print("BUSCAR PRODUCTO POR NOMBRE")
    print("="*60)
    
    if not productos:
        print("No hay productos en el inventario")
        return
    
    try:
        nombre = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip()
        
        if not nombre:
            print("Debe ingresar un nombre")
            return
        
        resultados = buscar_lineal_nombre(productos, nombre)
        
        if not resultados:
            print(f"\nNo se encontraron productos con '{nombre}'")
            return
        
        print(f"\n Se encontraron {len(resultados)} producto(s):\n")
        print(f"{'Código':<10} {'Nombre':<25} {'Precio':>10} {'Stock':>8}")
        print("-" * 60)
        
        for producto in resultados:
            print(f"{producto['codigo']:<10} {producto['nombre']:<25} "
                  f"Bs. {producto['precio']:>6.2f} {producto['stock']:>8}")
    
    except Exception as e:
        print(f"\nError en la busqueda: {e}")


def buscar_por_codigo(productos):
    """Funcion para busqueda binaria por codigo"""
    print("\n" + "="*60)
    print("BUSCAR PRODUCTO POR CODIGO")
    print("="*60)
    
    if not productos:
        print("No hay productos en el inventario")
        return
    
    try:
        # Ordena los productos por codigo para realizar la busqueda binaria
        productos_ordenados = productos.copy()
        ordenar_seleccion(productos_ordenados, lambda p: p['codigo'], ascendente=True)
        
        codigo = input("Ingrese el codigo exacto a buscar: ").strip().upper()
        
        if not codigo:
            print("Debe ingresar un codigo")
            return
        
        resultado = buscar_binaria_codigo(productos_ordenados, codigo)
        
        if not resultado:
            print(f"\nNo se encontro producto con codigo '{codigo}'")
            return
        
        print(f"\nProducto encontrado:\n")
        print(f"  Código: {resultado['codigo']}")
        print(f"  Nombre: {resultado['nombre']}")
        print(f"  Precio: Bs. {resultado['precio']:.2f}")
        print(f"  Stock: {resultado['stock']}")
        print(f"  Stock mínimo: {resultado['stock_minimo']}")
        print(f"  Vendidos hoy: {resultado['vendidos_hoy']}")
        
        if resultado['stock'] <= resultado['stock_minimo']:
            print(f"\n !!! ALERTA: Stock bajo el minimo")
    
    except Exception as e:
        print(f"\nError en la busqueda: {e}")