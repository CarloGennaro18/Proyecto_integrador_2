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
