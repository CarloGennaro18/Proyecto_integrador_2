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
def estadisticas_dia(productos):
    """Muestra estadisticas de ventas del dia"""
    print("\n" + "="*60)
    print("ESTADISTICAS DEL DIA")
    print("="*60)
    
    if not productos:
        print("No hay productos en el inventario")
        return
    
    # Calcular estadisticas
    total_ventas = sum(p['vendidos_hoy'] for p in productos)
    
    if total_ventas == 0:
        print("\nNo se han registrado ventas el dia de hoy")
        return
    
    total_ingresos = sum(p['vendidos_hoy'] * p['precio'] for p in productos)
    productos_vendidos = len([p for p in productos if p['vendidos_hoy'] > 0])
    
    # Calcular ticket promedio (considerando cada unidad como una transaccion)
    ticket_promedio = total_ingresos / total_ventas if total_ventas > 0 else 0
    
    print(f"\nRESUMEN de ventas del dia:\n")
    print(f"  Total de unidades vendidas: {total_ventas}")
    print(f"  Productos diferentes vendidos: {productos_vendidos} de {len(productos)}")
    print(f"  Ingresos totales: Bs. {total_ingresos:.2f}")
    print(f"  Ticket promedio por unidad: Bs. {ticket_promedio:.2f}")
    
    # Producto mas vendido
    mas_vendido = max(productos, key=lambda p: p['vendidos_hoy'])
    if mas_vendido['vendidos_hoy'] > 0:
        print(f"\nProducto mas vendido:")
        print(f"  {mas_vendido['nombre']} ({mas_vendido['vendidos_hoy']} unidades)")
    
    # Producto con mayores ingresos
    ingresos_por_producto = [(p, p['vendidos_hoy'] * p['precio']) for p in productos]
    mayor_ingreso = max(ingresos_por_producto, key=lambda x: x[1])
    if mayor_ingreso[1] > 0:
        print(f"\nProducto con mayores ingresos:")
        print(f"  {mayor_ingreso[0]['nombre']} (Bs. {mayor_ingreso[1]:.2f})")
def resumen_semanal(ventas_semana):
    """Muestra el resumen de ventas de la semana por dia y franja horaria"""
    print("\n" + "="*60)
    print("RESUMEN SEMANAL DE VENTAS")
    print("="*60)
    
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    franjas = ['Mañana', 'Tarde', 'Noche']
    
    # Verifica si hay ventas
    total_semana = sum(sum(dia) for dia in ventas_semana)
    
    if total_semana == 0:
        print("\n No se han registrado ventas en la semana")
        return
    
    print(f"\n{'Dia':<12} {'Manana':>12} {'Tarde':>12} {'Noche':>12} {'Total Dia':>15}")
    print("-" * 65)
    
    totales_franja = [0.0, 0.0, 0.0]
    
    for i, dia in enumerate(dias):
        total_dia = sum(ventas_semana[i])
        
        print(f"{dia:<12} Bs. {ventas_semana[i][0]:>8.2f} "
              f"Bs. {ventas_semana[i][1]:>8.2f} "
              f"Bs. {ventas_semana[i][2]:>8.2f} "
              f"Bs. {total_dia:>11.2f}")
        
        for j in range(3):
            totales_franja[j] += ventas_semana[i][j]
    
    print("-" * 65)
    print(f"{'TOTAL':<12} Bs. {totales_franja[0]:>8.2f} "
          f"Bs. {totales_franja[1]:>8.2f} "
          f"Bs. {totales_franja[2]:>8.2f} "
          f"Bs. {total_semana:>11.2f}")
    
    # Estadisticas adicionales
    print(f"\nAnalisis:")
    
    # Dia con mas ventas
    max_dia_idx = max(range(7), key=lambda i: sum(ventas_semana[i]))
    max_dia_total = sum(ventas_semana[max_dia_idx])
    if max_dia_total > 0:
        print(f"Mejor dia: {dias[max_dia_idx]} (Bs. {max_dia_total:.2f})")
    
    # Franja con mas ventas
    max_franja_idx = totales_franja.index(max(totales_franja))
    if totales_franja[max_franja_idx] > 0:
        print(f"Mejor franja: {franjas[max_franja_idx]} (Bs. {totales_franja[max_franja_idx]:.2f})")
    
    # Promedio diario
    promedio_dia = total_semana / 7
    print(f"Promedio por dia: Bs. {promedio_dia:.2f}")