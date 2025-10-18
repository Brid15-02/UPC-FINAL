# ============================================================
# ALUMNO 1: VALIDACIONES
# Funciones: pedidos[], es_numero_valido(), validar_numero()
# ============================================================

pedidos = []


def es_numero_valido(texto, tipo="int"):
    if not texto or texto == "":
        return False

    # Permitir signo negativo al inicio
    if texto[0] == '-':
        texto = texto[1:]

    if tipo == "int":
        # Verificar que todos sean dígitos
        return texto.isdigit()

    elif tipo == "float":
        # Permitir un punto decimal
        if '.' in texto:
            partes = texto.split('.')
            if len(partes) != 2:
                return False
            return partes[0].isdigit() and partes[1].isdigit()
        else:
            return texto.isdigit()

    return False


def validar_numero(mensaje, tipo="int", minimo=None, intentos=3):
    if intentos == 0:
        print(" Demasiados intentos fallidos")
        return None

    entrada = input(mensaje).strip()

    # Validar si es número
    if not es_numero_valido(entrada, tipo):
        print(f" Entrada inválida. Debe ser un número {tipo}. Intentos restantes: {intentos - 1}")
        return validar_numero(mensaje, tipo, minimo, intentos - 1)

    # Convertir a número
    if tipo == "int":
        valor = int(entrada)
    else:
        valor = float(entrada)

    # Validar mínimo si se especifica
    if minimo is not None and valor < minimo:
        print(f" El valor debe ser mayor o igual a {minimo}")
        return validar_numero(mensaje, tipo, minimo, intentos - 1)

    return valor

# ============================================================
# FIN ALUMNO 1
# ============================================================


# ============================================================
# ALUMNO 2: BÚSQUEDA Y CÁLCULOS
# Funciones: buscar_cliente(), calcular_descuento(), mostrar_pedidos()
# ============================================================

def buscar_cliente(nombre_buscar, lista, indice=0, resultados=None):
    if resultados is None:
        resultados = []

    # Caso base: llegamos al final
    if indice >= len(lista):
        return resultados

    # Si el nombre coincide
    if nombre_buscar.lower() in lista[indice]["cliente"].lower():
        resultados.append(lista[indice])

    # Llamada recursiva
    return buscar_cliente(nombre_buscar, lista, indice + 1, resultados)


def calcular_descuento(total):
    if total >= 500:
        return total * 0.15
    elif total >= 300:
        return total * 0.10
    elif total >= 100:
        return total * 0.05
    else:
        return 0


def mostrar_pedidos(lista, indice=0):
    # Caso base
    if indice >= len(lista):
        return

    p = lista[indice]
    print(f"\n{'=' * 60}")
    print(f" PEDIDO #{indice + 1}")
    print(f"{'=' * 60}")
    print(f" Cliente:        {p['cliente']}")
    print(f" Producto:       {p['producto']}")
    print(f" Cantidad:       {p['cantidad']} unidades")
    print(f" Precio Unit.:   S/ {p['precio']:.2f}")
    print(f" Subtotal:       S/ {p['total']:.2f}")

    if p.get('descuento', 0) > 0:
        porcentaje = (p['descuento'] / p['total']) * 100
        print(f" Descuento:      S/ {p['descuento']:.2f} ({porcentaje:.1f}%)")
        print(f" TOTAL FINAL:    S/ {p['total_final']:.2f}")
    else:
        print(f" TOTAL FINAL:    S/ {p['total']:.2f}")

    print(f"{'=' * 60}")

    # Llamada recursiva
    mostrar_pedidos(lista, indice + 1)

# ============================================================
# FIN ALUMNO 2
# ============================================================


# ============================================================
# ALUMNO 3: OPERACIONES Y REGISTRO
# Funciones: suma_totales(), suma_descuentos(), suma_cantidades(),
#            encontrar_maximo(), registrar_pedido(), ver_pedidos(), buscar_pedidos()
# ============================================================

def suma_totales(lista, indice=0):
    if indice >= len(lista):
        return 0
    return lista[indice]['total_final'] + suma_totales(lista, indice + 1)


def suma_descuentos(lista, indice=0):
    if indice >= len(lista):
        return 0
    return lista[indice]['descuento'] + suma_descuentos(lista, indice + 1)


def suma_cantidades(lista, indice=0):
    if indice >= len(lista):
        return 0
    return lista[indice]['cantidad'] + suma_cantidades(lista, indice + 1)


def encontrar_maximo(lista, campo, indice=0, max_actual=None):
    if indice >= len(lista):
        return max_actual

    if max_actual is None or lista[indice][campo] > max_actual[campo]:
        max_actual = lista[indice]

    return encontrar_maximo(lista, campo, indice + 1, max_actual)


def registrar_pedido():
    print("\n" + "=" * 60)
    print(" REGISTRO DE NUEVO PEDIDO")
    print("=" * 60)

    # Solicitar nombre del cliente
    cliente = input(" Ingrese nombre del cliente: ").strip()
    if not cliente or cliente == "":
        print(" El nombre del cliente no puede estar vacío")
        return

    # Solicitar producto
    producto = input(" Ingrese producto: ").strip()
    if not producto or producto == "":
        print(" El nombre del producto no puede estar vacío")
        return

    # Validar cantidad
    cantidad = validar_numero(" Ingrese cantidad: ", "int", minimo=1)
    if cantidad is None:
        print(" Registro cancelado por cantidad inválida")
        return

    # Validar precio
    precio = validar_numero(" Ingrese precio unitario: S/ ", "float", minimo=0.01)
    if precio is None:
        print(" Registro cancelado por precio inválido")
        return

    # Calcular totales
    total = cantidad * precio
    descuento = calcular_descuento(total)
    total_final = total - descuento

    # Crear pedido
    pedido = {
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "total": total,
        "descuento": descuento,
        "total_final": total_final
    }

    # Agregar a lista
    pedidos.append(pedido)

    # Confirmación
    print("\n" + "=" * 60)
    print(" PEDIDO REGISTRADO EXITOSAMENTE")
    print("=" * 60)
    print(f" Subtotal:     S/ {total:.2f}")
    if descuento > 0:
        porcentaje = (descuento / total) * 100
        print(f" Descuento:    S/ {descuento:.2f} ({porcentaje:.1f}%)")
        print(f" Total Final:  S/ {total_final:.2f}")
    else:
        print(f" Total Final:  S/ {total_final:.2f}")
    print("=" * 60)


def ver_pedidos():
    print("\n" + "=" * 60)
    print(" LISTA DE TODOS LOS PEDIDOS")
    print("=" * 60)

    if len(pedidos) == 0:
        print("\n No hay pedidos registrados en el sistema")
        print("   Primero debe registrar al menos un pedido")
        return

    print(f"\n Total de pedidos: {len(pedidos)}")
    mostrar_pedidos(pedidos)


def buscar_pedidos():
    print("\n" + "=" * 60)
    print(" BUSCAR PEDIDOS POR CLIENTE")
    print("=" * 60)

    if len(pedidos) == 0:
        print("\n No hay pedidos registrados para buscar")
        return

    nombre = input("\n Ingrese nombre del cliente a buscar: ").strip()

    if not nombre or nombre == "":
        print(" Debe ingresar un nombre para buscar")
        return

    # Búsqueda recursiva
    resultados = buscar_cliente(nombre, pedidos)

    if len(resultados) == 0:
        print(f"\n No se encontraron pedidos para el cliente '{nombre}'")
        print("   Intente con otro nombre o verifique la ortografía")
    else:
        print(f"\n Se encontraron {len(resultados)} pedido(s) para '{nombre}':")
        mostrar_pedidos(resultados)

# ============================================================
# FIN ALUMNO 3
# ============================================================


# ============================================================
# ALUMNO 4: ANÁLISIS Y MENÚ
# Funciones: analisis_ventas(), menu_principal(), main
# ============================================================

def analisis_ventas():
    print("\n" + "=" * 60)
    print(" ANÁLISIS DE VENTAS")
    print("=" * 60)

    if len(pedidos) == 0:
        print("\n No hay pedidos registrados para analizar")
        return

    # Cálculos usando recursividad
    ventas_totales = suma_totales(pedidos)
    total_descuentos = suma_descuentos(pedidos)
    total_unidades = suma_cantidades(pedidos)
    promedio_venta = ventas_totales / len(pedidos)

    # Producto más vendido
    producto_mas_vendido = encontrar_maximo(pedidos, 'cantidad')

    # Cliente con mayor compra
    cliente_mayor_compra = encontrar_maximo(pedidos, 'total_final')

    # Mostrar resultados
    print(f"\n RESUMEN GENERAL")
    print(f"{'─' * 60}")
    print(f" Total de pedidos:        {len(pedidos)}")
    print(f" Total unidades vendidas: {total_unidades}")
    print(f" Ventas totales:          S/ {ventas_totales:.2f}")
    print(f" Descuentos otorgados:    S/ {total_descuentos:.2f}")
    print(f" Promedio por venta:      S/ {promedio_venta:.2f}")

    print(f"\n DESTACADOS")
    print(f"{'─' * 60}")
    print(f" Producto más vendido:")
    print(f"   - {producto_mas_vendido['producto']}")
    print(f"   - Cantidad: {producto_mas_vendido['cantidad']} unidades")
    print(f"   - Cliente: {producto_mas_vendido['cliente']}")

    print(f"\n Cliente con mayor compra:")
    print(f"   - {cliente_mayor_compra['cliente']}")
    print(f"   - Total: S/ {cliente_mayor_compra['total_final']:.2f}")
    print(f"   - Producto: {cliente_mayor_compra['producto']}")
    print("=" * 60)


def menu_principal():
    print("\n" + "=" * 60)
    print(" SISTEMA DE GESTIÓN DE PEDIDOS")
    print("=" * 60)
    print("1. Registrar Pedido")
    print("2. Ver Todos los Pedidos")
    print("3. Buscar Pedidos por Cliente")
    print("4. Análisis de Ventas")
    print("5. Salir del Sistema")
    print("=" * 60)

    opcion = validar_numero(" Seleccione una opción (1-5): ", "int")

    if opcion is None:
        print("\n Opción inválida, intente nuevamente")
        menu_principal()
        return

    if opcion == 1:
        registrar_pedido()
        input("\n Presione ENTER para continuar...")
        menu_principal()

    elif opcion == 2:
        ver_pedidos()
        input("\n Presione ENTER para continuar...")
        menu_principal()

    elif opcion == 3:
        buscar_pedidos()
        input("\n Presione ENTER para continuar...")
        menu_principal()

    elif opcion == 4:
        analisis_ventas()
        input("\n Presione ENTER para continuar...")
        menu_principal()

    elif opcion == 5:
        print("\n" + "=" * 60)
        print(" Gracias por usar el Sistema de Gestión de Pedidos")
        print(" Desarrollado con Python y Recursividad")
        print("=" * 60)
        return

    else:
        print("\n Opción inválida. Por favor seleccione entre 1 y 5")
        input("\n Presione ENTER para continuar...")
        menu_principal()


if __name__ == "__main__":
    menu_principal()

# ============================================================
# FIN ALUMNO 4
# ============================================================