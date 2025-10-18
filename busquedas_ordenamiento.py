"""Modulo de buasquedas y ordenamientosaca se Implementa busqueda lineal, binaria y algoritmos de ordenamiento"""

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
