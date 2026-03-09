# ========================================
# Calculo de determinantes
# ========================================

# Calculo mediante la formula de Laplace
def det_laplace(matriz, n=None):
    if n is None:
        n = len(matriz)

    if n == 1:
        return matriz[0][0]
    
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    det = 0
    for j in range(n):
        submatriz = [fila[:j] + fila[j+1:] for fila in matriz[1:]]
        det += ((-1)**j) * matriz[0][j] * det_laplace(submatriz)
    return det

# Eliminación mediante metodo de Gauss
def det_gauss(matriz, n=None):
    if n is None:
        n = len(matriz)

    A = [fila[:] for fila in matriz]
    determinante = 1

    for i in range(n):
        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    determinante *= -1
                    break
                    
        if A[i][i] == 0:
            return 0 
        
        determinante *= A[i][i]

        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    return determinante

# 
# Formatos
#

# Funciones de rectay plano
def formatear_ecuacion(coeficientes, variables):
    terminos = []

    for i, (c, var) in enumerate(zip(coeficientes, variables)):
        if round(c, 4) == 0: continue

        if not terminos:
            signo = "" if c > 0 else "-"
        else:
            signo = " + " if c > 0 else " - "

        abs_c = abs(c)
        if abs_c == 1 and var != "":
            str_c = ""
        else:
            str_c = f"{abs_c:g}"

        terminos.append(f"{signo}{str_c}{var}")

    return "".join(terminos) if terminos else "0"

# ========================================
# A) Regla de Cramer
# ========================================

# Se declara un parametro opcional metodo_det para elegir entre los metodos de calculo de determinantes
def regla_de_cramer(matriz_A, b, metodo_det=det_gauss):
    n = len(matriz_A)
    
    determinante = metodo_det(matriz_A, n)

    if abs(determinante) < 1e-9:
        raise ValueError("El sistema no tiene solución única")

    soluciones = []

    for i in range(n):

        matriz_Ai = [fila[:] for fila in matriz_A]

        for j in range(n):
            matriz_Ai[j][i] = b[j]

        determinante_i = metodo_det(matriz_Ai, n)

        soluciones.append(determinante_i / determinante)

    return soluciones

# ========================================
# B) Geometría 2D
# ========================================

# Área de triangulos
def area_triangulo(puntos, metodo_det=det_gauss):

    matriz = [[p[0], p[1], 1] for p in puntos]

    determinante = metodo_det(matriz, 3)

    area = abs(determinante) / 2

    return area

# Prueba de colinealidad
def colinealidad(puntuntos, metodo_det=det_gauss):

    matriz = [[p[0], p[1], 1] for p in puntuntos]

    determinante = metodo_det(matriz, 3)

    return abs(determinante) < 1e-9

# Ecuación de la recta
def ecuacion_recta(p1, p2, metodo_det=det_gauss):

    A = p1[1] - p2[1]
    B = -(p1[0] - p2[0])
    C = metodo_det([[p1[0], p1[1]], [p2[0], p2[1]]], 2)

    resultado = formatear_ecuacion([A, B, C], ["x", "y", ""])
    return f"{resultado} = 0"

# ========================================
# C) Geometría 3D
# ========================================

# Volumen de un Tetraedro
def volumen_tetraedro(puntos, metodo_det=det_gauss):

    matriz = [[p[0], p[1], p[2], 1.0] for p in puntos]

    det = metodo_det(matriz, 4)

    volumen = abs(det) / 6

    return volumen

# Prueba de Coplanaridad
def son_coplanares(puntos, metodo_det=det_gauss):

    matriz = [[p[0], p[1], p[2], 1.0] for p in puntos]

    determinante = metodo_det(matriz, 4)

    return abs(determinante) < 1e-9

# Ecuación del Plano
def ecuacion_plano(puntos, metodo_det=det_gauss):

    p1, p2, p3 = puntos

    A = metodo_det([
        [p1[1], p1[2], 1],
        [p2[1], p2[2], 1],
        [p3[1], p3[2], 1]
    ])
    
    B = -metodo_det([
        [p1[0], p1[2], 1],
        [p2[0], p2[2], 1],
        [p3[0], p3[2], 1]
    ])
    
    C = metodo_det([
        [p1[0], p1[1], 1],
        [p2[0], p2[1], 1],
        [p3[0], p3[1], 1]
    ])
    
    D = -metodo_det([
        [p1[0], p1[1], p1[2]],
        [p2[0], p2[1], p2[2]],
        [p3[0], p3[1], p3[2]]
    ])

    resultado = formatear_ecuacion([A, B, C, D], ["x", "y", "z", ""])
    return f"{resultado} = 0"