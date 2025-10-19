"""Modulo de Entrada/Salida de Archivos - Maneja la persistencia en CSV y binario"""
import csv
import pickle
import os

def crear_productos_demo():
    """Crea productos de demostracion para el inicio"""
    return [
        {
            'codigo': 'A1-001',
            'nombre': 'Regla 30cm',
            'precio': 6.5,
            'stock': 20,
            'stock_minimo': 5,
            'vendidos_hoy': 0
        },
        {
            'codigo': 'A1-002',
            'nombre': 'Lapicero azul',
            'precio': 3.0,
            'stock': 45,
            'stock_minimo': 10,
            'vendidos_hoy': 0
        },
        {
            'codigo': 'B1-010',
            'nombre': 'Hojas bond A4',
            'precio': 8.0,
            'stock': 12,
            'stock_minimo': 4,
            'vendidos_hoy': 0
        },
        {
            'codigo': 'B1-011',
            'nombre': 'Cuaderno 100 hojas',
            'precio': 15.0,
            'stock': 30,
            'stock_minimo': 8,
            'vendidos_hoy': 0
        },
        {
            'codigo': 'C2-200',
            'nombre': 'Lapiz HB',
            'precio': 2.5,
            'stock': 25,
            'stock_minimo': 6,
            'vendidos_hoy': 0
        },
        {
            'codigo': 'C2-201',
            'nombre': 'Borrador blanco',
            'precio': 2.0,
            'stock': 40,
            'stock_minimo': 10,
            'vendidos_hoy': 0
        },
        {
            'codigo': 'D3-100',
            'nombre': 'Marcador permanente',
            'precio': 5.5,
            'stock': 18,
            'stock_minimo': 5,
            'vendidos_hoy': 0
        },
        {
            'codigo': 'D3-101',
            'nombre': 'Resaltador amarillo',
            'precio': 4.0,
            'stock': 22,
            'stock_minimo': 7,
            'vendidos_hoy': 0
        },
        {
            'codigo': 'E4-050',
            'nombre': 'Corrector liquido',
            'precio': 7.0,
            'stock': 15,
            'stock_minimo': 5,
            'vendidos_hoy': 0
        },
        {
            'codigo': 'E4-051',
            'nombre': 'Tijera escolar',
            'precio': 9.5,
            'stock': 10,
            'stock_minimo': 3,
            'vendidos_hoy': 0
        }
    ]


def crear_matriz_ventas():
    """Crea matriz de ventas semanal (7 días x 3 franjas)"""
    # 7 dias (0=Lunes, 6=Domingo), 3 franjas (0=Manana, 1=Tarde, 2=Noche)
    return [[0.0 for _ in range(3)] for _ in range(7)]

def leer_csv(archivo):
    """Lee productos desde archivo CSV - Retorna lista de productos o None si hay error"""
    try:
        productos = []
        with open(archivo, 'r', encoding='utf-8') as f:
            lector = csv.DictReader(f, delimiter=';')
            for fila in lector:
                try:
                    producto = {
                        'codigo': fila['codigo'].strip(),
                        'nombre': fila['nombre'].strip(),
                        'precio': float(fila['precio']),
                        'stock': int(fila['stock']),
                        'stock_minimo': int(fila['stock_minimo']),
                        'vendidos_hoy': int(fila.get('vendidos_hoy', 0))
                    }
                    productos.append(producto)
                except (ValueError, KeyError) as e:
                    print(f" !!! Fila corrupta ignorada: {e}")
                    continue
        return productos
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f" !!! Error al leer CSV: {e}")
        return None

def escribir_csv(archivo, productos):
    """Escribe productos en archivo CSV"""
    try:
        with open(archivo, 'w', encoding='utf-8', newline='') as f:
            campos = ['codigo', 'nombre', 'precio', 'stock', 'stock_minimo', 'vendidos_hoy']
            escritor = csv.DictWriter(f, fieldnames=campos, delimiter=';')
            escritor.writeheader()
            escritor.writerows(productos)
        return True
    except Exception as e:
        print(f"Error al escribir CSV: {e}")
        return False


def cargar_binario(archivo):
    """Carga datos desde archivo binario usando pickle"""
    try:
        with open(archivo, 'rb') as f:
            datos = pickle.load(f)
        return datos
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"!!! Error al cargar binario: {e}")
        return None


def guardar_binario(archivo, datos):
    """Guarda datos en archivo binario usando pickle"""
    try:
        with open(archivo, 'wb') as f:
            pickle.dump(datos, f)
        return True
    except Exception as e:
        print(f"Error al guardar binario: {e}")
        return False

def cargar_datos_inicio():
    """Carga datos al iniciar el sistema - Prioriza CSV, crea datos demo si no existe"""
    print("\n Cargando datos del sistema...")
    
    # Carga desde CSV
    productos = leer_csv('datos.csv')
    
    if productos is None:
        print("No se encontro datos.csv, creando productos para una demostracion...")
        productos = crear_productos_demo()
        escribir_csv('datos.csv', productos)
    else:
        print(f"Datos cargados desde datos.csv")
    
    # Crea matriz de ventas semanal
    ventas_semana = crear_matriz_ventas()
    
    return productos, ventas_semana


def guardar_datos_salida(productos, ventas_semana):
    """Guarda datos al salir del sistema (CSV y binario)"""
    # Guardar en CSV
    if escribir_csv('datos.csv', productos):
        print("Datos guardados en datos.csv")
    
    # Guardar en binario
    datos_completos = {
        'productos': productos,
        'ventas_semana': ventas_semana
    }
    if guardar_binario('datos.bin', datos_completos):
        print("Snapshot guardado en datos.bin")


def exportar_alertas(productos):
    """Exporta productos bajo stock minimo a alertas.csv"""
    try:
        alertas = [p for p in productos if p['stock'] <= p['stock_minimo']]
        
        if not alertas:
            print("\nNo hay productos bajo stock minimo.")
            return
        
        if escribir_csv('alertas.csv', alertas):
            print(f"\nSe exportaron {len(alertas)} productos con alerta a alertas.csv")
        else:
            print("\nError al exportar alertas")
            
    except Exception as e:
        print(f"\nError al exportar alertas: {e}")