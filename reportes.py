"""Modulo de Reportes y Estadisticas - Genera reportes de ventas, productos y estadisticas"""

def top_vendidos(productos):
    """Muestra los 3 productos mas vendidos del dia"""
    print("\n" + "="*60)
    print("TOP 3 PRODUCTOS MAS VENDIDOS DEL DIA")
    print("="*60)
    
    if not productos:
        print("No hay productos en el inventario")
        return
    
    # Filtrar productos con ventas
    vendidos = [p for p in productos if p['vendidos_hoy'] > 0]
    
    if not vendidos:
        print("\nNo se han registrado ventas el dia de hoy")
        return
    
    # Ordenar por vendidos_hoy descendente
    vendidos_ordenados = sorted(vendidos, key=lambda p: p['vendidos_hoy'], reverse=True)
    
    # Tomar top 3
    top3 = vendidos_ordenados[:3]
    
    print(f"\n{'Pos':<5} {'Codigo':<10} {'Nombre':<25} {'Vendidos':>10} {'Ingresos':>12}")
    print("-" * 65)
    
    for i, producto in enumerate(top3, 1):
        ingresos = producto['vendidos_hoy'] * producto['precio']
        print(f"{i:<5} {producto['codigo']:<10} {producto['nombre']:<25} "
              f"{producto['vendidos_hoy']:>10} Bs. {ingresos:>8.2f}")
    
    total_vendidos = sum(p['vendidos_hoy'] for p in top3)
    total_ingresos = sum(p['vendidos_hoy'] * p['precio'] for p in top3)
    
    print("-" * 65)
    print(f"{'TOTAL TOP 3':<41} {total_vendidos:>10} Bs. {total_ingresos:>8.2f}")


def productos_bajo_stock(productos):
    """Muestra productos con stock igual o menor al minimo"""
    print("\n" + "="*60)
    print("PRODUCTOS BAJO STOCK MINIMO")
    print("="*60)
    
    if not productos:
        print("No hay productos en el inventario")
        return
    
    alertas = [p for p in productos if p['stock'] <= p['stock_minimo']]
    
    if not alertas:
        print("\nTodos los productos tienen stock adecuado")
        return
    
    print(f"\n !!! Se encontraron {len(alertas)} producto(s) con alerta:\n")
    print(f"{'Codigo':<10} {'Nombre':<25} {'Stock':>8} {'Minimo':>8} {'Diferencia':>12}")
    print("-" * 65)
    
    for producto in alertas:
        diferencia = producto['stock'] - producto['stock_minimo']
        print(f"{producto['codigo']:<10} {producto['nombre']:<25} "
              f"{producto['stock']:>8} {producto['stock_minimo']:>8} "
              f"{diferencia:>12}")
    
    print("\n Sugerencia!!: Reabastecer estos productos pronto")
