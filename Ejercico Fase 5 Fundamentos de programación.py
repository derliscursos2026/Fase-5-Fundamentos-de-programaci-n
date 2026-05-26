# Derlis Judith Meza Gonzalez
# Grupo: 213022_252
# Programa: Ingeniería Multimedia
# Código Fuente: Autoría Propia

# Problema 5 – Control de horas trabajadas y sobretiempo

# Matriz de datos: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
# Cada fila representa un recurso y las horas trabajadas cada día.
recursos = [
    ["Ana García", 8, 8, 8, 8, 8],      # 40 horas → Horario Estándar
    ["Luis Pérez", 9, 9, 8, 8, 9],      # 43 horas → Sobretiempo
    ["Marta López", 7, 7, 7, 7, 7],     # 35 horas → Horario Estándar
    ["Carlos Ruiz", 10, 9, 10, 9, 10]   # 48 horas → Sobretiempo
]

UMBRAL_SOBRETIEMPO = 40

def calcular_total_horas(fila):
    """Recibe una fila de la matriz [nombre, lunes, ..., viernes]
       y retorna la suma de las horas (de lunes a viernes)."""
    # Las horas están desde el índice 1 hasta el 5 (incluido)
    horas = fila[1:6]  # slicing
    return sum(horas)

def clasificar_jornada(total_horas):
    """Retorna 'Sobretiempo' si total_horas > 40, de lo contrario 'Horario Estándar'."""
    if total_horas > UMBRAL_SOBRETIEMPO:
        return "Sobretiempo"
    else:
        return "Horario Estándar"

def generar_informe(matriz):
    """Genera y muestra el informe de horas semanales y clasificación."""
    print("\n=== INFORME DE HORAS TRABAJADAS ===\n")
    print(f"{'Nombre':<20} {'Total horas':<15} {'Clasificación':<20}")
    print("-" * 55)
    for recurso in matriz:
        nombre = recurso[0]
        total = calcular_total_horas(recurso)
        clasificacion = clasificar_jornada(total)
        print(f"{nombre:<20} {total:<15} {clasificacion:<20}")
    print("\n=== Fin del informe ===")

# Ejecución principal
if __name__ == "__main__":
    generar_informe(recursos)
    