"""Sistema de Gestion - Kiosko Universitario UCB, archivo principal con menú de opciones
"""

from inventario import (
    alta_producto, baja_producto, modificar_producto, reabastecer_producto, registrar_venta, mostrar_inventario)




def mostrar_menu():
     """Muestra el menu principal del sistema"""
     print("\n" + "="*60)
     print("         KIOSKO UNIVERSITARIO UCB - SISTEMA DE GESTIÓN")
     print("="*60)
     print("1.  Alta de producto")
     print("2.  Baja de producto")
     print("3.  Modificar producto")
     print("4.  Reabastecer producto")
     print("5.  Registrar venta")
     print("6.  Mostrar inventario completo")
     print("7.  Buscar producto por nombre")
     print("8.  Buscar producto por código")
     print("9.  Ordenar productos por precio")
     print("10. Ordenar productos por nombre")
     print("11. Ordenar productos por stock")
     print("12. Top 3 productos más vendidos del día")
     print("13. Productos bajo stock mínimo")
     print("14. Estadisticas del dia")
     print("15. Resumen semanal de ventas")
     print("16. Exportar alertas de stock")
     print("0.  Salir y guardar")
     print("="*60)
def main():
    """Funcion principal del sistema"""
    productos, ventas_semana = cargar_datos_inicio()
    print("\n¡Bienvenido al Sistema de Gestión del Kiosko Universitario UCB!")
    print(f"Se han cargado {len(productos)} productos.")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción: ").strip()
            if opcion == "1": # Alta de producto
                alta_producto(productos)
            elif opcion == "2": # Baja de producto
                baja_producto(productos)
            elif opcion == "3":# Modificar producto
                modificar_producto(productos)    
            elif opcion == "4":# Reabastecer producto
                reabastecer_producto(productos)
            elif opcion == "5":# Registrar venta
                registrar_venta(productos, ventas_semana)
            elif opcion == "6":# Mostrar inventario
                mostrar_inventario(productos)
            else:
                print("\nOpcion invalida. Por favor seleccione una opcion del menu.")
                
        except KeyboardInterrupt:
            print("\n\nInterrupcion detectada. Guardando datos...")
            # guardar_datos_salida(productos, ventas_semana)
            print("¡Hasta pronto!")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Por favor, intente nuevamente.")
            
 
            
if __name__ == "__main__":
    main()