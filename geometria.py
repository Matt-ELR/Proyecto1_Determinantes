def det_gauss(A, n=None):
    if n is None:
        n = len(A)

    A = [fila[:] for fila in A]
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

# A) Regla de Cramer
def regla_de_cramer(A, b):
    n = len(A)
    
    determinante = det_gauss(A)

    if determinante == 0:
        raise ValueError("El sistema no tiene solución única")

    soluciones = []

    for i in range(n):

        Ai = [fila[:] for fila in A]

        for j in range(n):
            Ai[j][i] = b[j]

        determinante_i = det_gauss(Ai, n)

        soluciones.append(determinante_i / determinante)

    return soluciones


# B) Geometría 2D
# Área de triangulos
def area_triangulo(p1, p2, p3):
    #Declaración de la matriz
    M = np.array([
        [p1[0], p1[1], 1],
        [p2[0], p2[1], 1],
        [p3[0], p3[1], 1]
    ])

    if p1==p2 or p2==p3 or p1==p3: #Si un renglon es iual a otro
        area = 0.0
    else:
        #Cálculo del determinante
        det = (
        M[0,0]*(M[1,1]*M[2,2] - M[1,2]*M[2,1]) - 
        M[0,1]*(M[1,0]*M[2,2] - M[1,2]*M[2,0]) +
        M[0,2]*(M[1,0]*M[2,1] - M[1,1]*M[2,0])
        )

        #determinante = det_gauss(matriz, 3)
        #area = abs(determinante) / 2

        area = abs(det) / 2.0

    return area
    


def ecuacion_recta(p1, p2):                                                                                   
    

    a = y1 - y2
    b = x2 - x1
    c = x1*y2 - x2*y1

    return f"{a}x + {b}y + {c} = 0"

# C) Geometría 3D
def volumen_tetraedro(p1, p2, p3, p4):

    matriz = [
        [p1[0], p1[1], p1[2], 1],
        [p2[0], p2[1], p2[2], 1],
        [p3[0], p3[1], p3[2], 1],
        [p4[0], p4[1], p4[2], 1]
    ]

    det = det_gauss(matriz, 4)

    volumen = abs(det) / 6

    return volumen


def son_coplanares(p1, p2, p3, p4, tol=1e-9):

    matriz = [
        [p1[0], p1[1], p1[2], 1],
        [p2[0], p2[1], p2[2], 1],
        [p3[0], p3[1], p3[2], 1],
        [p4[0], p4[1], p4[2], 1]
    ]

    det = det_gauss(matriz, 4)

    return abs(det) < 1e-9


def ecuacion_plano(p1, p2, p3):

    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3

    v1 = [x2 - x1, y2 - y1, z2 - z1]
    v2 = [x3 - x1, y3 - y1, z3 - z1]

    a = v1[1] * v2[2] - v1[2] * v2[1]
    b = v1[2] * v2[0] - v1[0] * v2[2]
    c = v1[0] * v2[1] - v1[1] * v2[0]
    d = -(a * x1 + b * y1 + c * z1)

    return f"{a}x + {b}y + {c}z + {d} = 0"