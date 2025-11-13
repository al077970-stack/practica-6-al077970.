# practica-6-al077970.
Calculadora de Cerámica y Costo

Este programa en Python permite calcular la cantidad de cajas de cerámica necesarias para cubrir un piso, así como el costo total estimado y real del material, considerando el redondeo hacia arriba para evitar faltantes.
Fue desarrollado utilizando Tkinter, la librería estándar de interfaces gráficas de Python.

📋 Descripción del problema

Al instalar cerámica o loseta, es importante saber cuántas cajas se deben comprar y cuál será el costo total.
Cada caja de cerámica tiene una cobertura estándar (en este caso, 2.26 m² por caja).
El usuario ingresa:

El tamaño del piso (en metros cuadrados)

El precio de cada caja

El programa realiza los cálculos automáticamente y muestra:

La cantidad exacta de cajas necesarias.

El costo estimado (sin redondeo).

La cantidad real de cajas a comprar (redondeada hacia arriba).

El costo final considerando el redondeo.

🧮 Fórmulas utilizadas

Cobertura por caja (constante):

COBERTURA_POR_CAJA
=
2.26
 
𝑚
2
COBERTURA_POR_CAJA=2.26m
2

Cantidad de cajas exacta:

cantidadCajas
=
tamanioPiso
COBERTURA_POR_CAJA
cantidadCajas=
COBERTURA_POR_CAJA
tamanioPiso
	​


Costo estimado:

valorTotal
=
cantidadCajas
×
valorCaja
valorTotal=cantidadCajas×valorCaja

Cajas reales (redondeadas hacia arriba):

cajas_reales
=
⌈
cantidadCajas
⌉
cajas_reales=⌈cantidadCajas⌉

Costo final redondeado:

costo_real
=
cajas_reales
×
valorCaja
costo_real=cajas_reales×valorCaja
💻 Interfaz gráfica

La interfaz gráfica fue desarrollada con Tkinter e incluye:

Campos de entrada para:

Tamaño del piso (m²)

Valor por caja ($)

Botón principal: "Calcular"

Etiquetas dinámicas que muestran los resultados del cálculo.

Un diseño limpio y claro con colores suaves.

🧰 Requisitos

Python 3.8 o superior

Librerías estándar (no requiere instalación adicional):

tkinter

math

🚀 Ejecución del programa

Guarda el archivo con el nombre:

calculadora_ceramica.py


Ejecuta el programa en una terminal o entorno como IDLE o VS Code:

python calculadora_ceramica.py


Se abrirá una ventana donde podrás ingresar los datos y obtener el resultado.

🪄 Ejemplo de uso

Entrada:

Tamaño del piso: 25 m²

Valor por caja: $380.00
