import numpy as np


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

        area = abs(det) / 2.0

    return area
    


def ecuacion_recta(p1, p2):                                                                                   
    

    return 0


def volumen_tetraedro(p1, p2, p3, p4):
    

    return 0


def son_coplanares(p1, p2, p3, p4, tol=1e-9):
    

    return 0


def ecuacion_plano(p1, p2, p3):
    

    return 0