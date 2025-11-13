import tkinter as tk
from tkinter import messagebox
import math

# Constante de cobertura por caja
COBERTURA_POR_CAJA = 2.26

# Función que realiza los cálculos
def calcular():
    try:
        # Obtener valores del usuario
        tamanioPiso = float(entry_tamanio.get())
        valorCaja = float(entry_valor.get())

        # Cálculos
        cantidadCajas = tamanioPiso / COBERTURA_POR_CAJA
        valorTotal = cantidadCajas * valorCaja
        cajas_reales = math.ceil(cantidadCajas)
        costo_real = cajas_reales * valorCaja

        # Mostrar resultados en los labels
        resultado1.config(text=f"Cantidad de cajas (exacta): {cantidadCajas:.3f}")
        resultado2.config(text=f"Costo total estimado: ${valorTotal:,.2f}")
        resultado3.config(text=f"Cajas a comprar (redondeadas): {cajas_reales} unidades")
        resultado4.config(text=f"Costo final redondeado: ${costo_real:,.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Cerámica y Costo")
ventana.geometry("420x360")
ventana.resizable(False, False)
ventana.configure(bg="#e8f0f2")

# Título
titulo = tk.Label(ventana, text="Calculadora de Material de Cerámica", 
                  font=("Arial", 14, "bold"), bg="#e8f0f2")
titulo.pack(pady=10)

# Campo: tamaño del piso
frame1 = tk.Frame(ventana, bg="#e8f0f2")
frame1.pack(pady=5)
tk.Label(frame1, text="Tamaño del piso (m²):", bg="#e8f0f2", font=("Arial", 11)).grid(row=0, column=0, padx=5)
entry_tamanio = tk.Entry(frame1, width=15, font=("Arial", 11))
entry_tamanio.grid(row=0, column=1)

# Campo: valor por caja
frame2 = tk.Frame(ventana, bg="#e8f0f2")
frame2.pack(pady=5)
tk.Label(frame2, text="Valor por caja ($):", bg="#e8f0f2", font=("Arial", 11)).grid(row=0, column=0, padx=5)
entry_valor = tk.Entry(frame2, width=15, font=("Arial", 11))
entry_valor.grid(row=0, column=1)

# Botón Calcular
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular,
                         bg="#007acc", fg="white", font=("Arial", 12, "bold"),
                         width=20, height=1)
btn_calcular.pack(pady=15)

# Resultados
resultado1 = tk.Label(ventana, text="", bg="#e8f0f2", font=("Arial", 11))
resultado1.pack()
resultado2 = tk.Label(ventana, text="", bg="#e8f0f2", font=("Arial", 11))
resultado2.pack()
resultado3 = tk.Label(ventana, text="", bg="#e8f0f2", font=("Arial", 11, "bold"))
resultado3.pack(pady=5)
resultado4 = tk.Label(ventana, text="", bg="#e8f0f2", font=("Arial", 11, "bold"))
resultado4.pack()

# Nota final
nota = tk.Label(ventana, text="*El cálculo considera el redondeo hacia arriba para evitar faltantes.",
                bg="#e8f0f2", fg="gray", font=("Arial", 9, "italic"))
nota.pack(pady=10)

# Iniciar la ventana
ventana.mainloop()

