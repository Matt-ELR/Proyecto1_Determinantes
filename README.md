<div align="center">

<img src="Imagenes/Caratula/Logo_IPN.png" alt="Logo IPN" width="200" align="left">
<img src="Imagenes/Caratula/Logo_UPIIT.png" alt="Logo UPIIT" width="150" align="right">

<br><br><br>

# Proyecto Primer Parcial
## Aplicaciones de los determinantes con interfaz gráfica (Tkinter)

<br>

**Instituto Politécnico Nacional** <br>
*Unidad Profesional Interdisciplinaria de Ingeniería Campus Tlaxcala*

<br><br>
</div>

---

### 👥 Datos del Equipo

**Integrantes:**
* Flores Rodríguez, Alan
* Lelis Ramírez, Mattias Emile
* López Martínez, Amaya Alinda
* Morales García, José Miguel
* Zamora Flores, Daniel

**📘 Curso:** D202 - Álgebra Lineal  
**👨‍🏫 Profesor:** Muñoz Toriz, Juan Pablo  
**📅 Fecha:** 11 de marzo de 2026  

---

## 📌 Descripción
Este proyecto implementa las aplicaciones clásicas de los determinantes utilizando el lenguaje Python y una interfaz gráfica desarrollada con Tkinter. El sistema permite resolver sistemas de ecuaciones lineales y realizar cálculos de geometría analítica en 2D y 3D.

Cumpliendo estrictamente con los requisitos académicos, **no se utilizaron bibliotecas externas** como NumPy. Toda la lógica matemática, incluyendo el cálculo de determinantes por eliminación de Gauss y expansión de Laplace, fue implementada desde cero.

---

## 🛠️ Estructura del Programa y Módulos

El proyecto está diseñado de forma modular para garantizar la calidad del código, separando la interfaz de la lógica matemática:

* **Módulo Lógico:** `geometria.py` contiene el "motor" matemático del proyecto, incluye las funciones para calcular determinantes y dar formato legible a los resultados.
* **Módulo de Cramer:** Implementado en `regla_de_cramer.py`. Resuelve sistemas de ecuaciones $n \times n$ (donde $2 \le n \le 5$). Identifica correctamente cuando $det(A) = 0$ y el sistema no tiene solución única.
* **Módulo 2D:** Accesible vía `menu_geometria_2d.py`. Incluye el cálculo del área de un triángulo (`triangulo.py`), prueba de colinealidad (`colinealidad.py`) y la obtención de la ecuación de la recta de la forma $Ax + By + C = 0$ (`recta.py`).
* **Módulo 3D:** Accesible vía `menu_geometria_3d.py`. Calcula el volumen de un tetraedro (`tetraedro.py`), prueba de coplanaridad (`coplanaridad.py`) y la ecuación del plano de la forma $Ax + By + Cz + D = 0$ (`plano.py`).
* **Interfaz Principal:** `menu.py` sirve como el punto de entrada, integrando las vistas de forma clara.

---

## 🚀 Instrucciones de Ejecución

1.  Asegúrese de tener instalado **Python 3.9** o una versión superior.
2.  Descargue y extraiga todos los archivos `.py` en un mismo directorio.
3.  Abra una terminal o línea de comandos en dicho directorio.
4.  Ejecute el archivo principal con el siguiente comando:
    ```bash
    python main.py
    ```

---

## 📊 Casos de Prueba Obligatorios

A continuación se presentan las evidencias de funcionamiento de la aplicación con los casos de prueba solicitados:

### A. Regla de Cramer ($3 \times 3$)
Se resolvió el sistema del ejemplo de la diapositiva, obteniendo exitosamente $x_1 = \frac{4}{5}$ ($0.8$).
<div align="center">
    <img src="Imagenes/Regla de Cramer - Prueba.png" alt="Prueba Cramer" width="500">
</div>

### B. Geometría 2D: Ecuación de la Recta
Se ingresaron los puntos $(2, 4)$ y $(-1, 3)$, devolviendo la ecuación en su formato equivalente $Ax + By + C = 0$.
<div align="center">
    <img src="Imagenes/Recta - Prueba.png" alt="Prueba Recta" width="500">
</div>

### C. Geometría 3D: Volumen del Tetraedro
Se ingresaron los cuatro puntos del ejemplo de la clase, reportando un volumen exacto de $12$ unidades cúbicas.
<div align="center">
    <img src="Imagenes/Tetreaedro - Prueba.png" alt="Prueba Tetraedro" width="500">
</div>

### C. Geometría 2D: Área y Colinealidad
Ejemplos propios demostrando el cálculo de un área distinta de cero y un caso de colinealidad donde el determinante es $0$.
| Área de Triángulo | Prueba de Colinealidad |
| :---: | :---: |
| <img src="Imagenes/Triangulo - Prueba.png" width="500"> | <img src="Imagenes/Colinealidad - Pruba.png" width="500"> |