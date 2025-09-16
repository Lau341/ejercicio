# Tkinter
Tkinter es la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). Está basada en Tcl/Tk y permite desarrollar aplicaciones con elementos gráficos como ventanas, botones, etiquetas, cuadros de texto, menús, etc.

## Resumen:
- Interfaz de Tcl/Tk: Tkinter es un wrapper de la biblioteca gráfica Tcl/Tk.
- Elementos gráficos: Permite crear botones, etiquetas, menús, cuadros de texto, etc.
- Multiplataforma: Funciona en Windows, macOS y Linux.
- Fácil de usar: No requiere instalación adicional, ya que está incluida por defecto en Python.
- Aplicaciones sencillas: Ideal para proyectos con interfaces gráficas simples.
- Estructura basada en objetos: Utiliza un enfoque basado en objetos y eventos (ej. clic en botones).

## Ejemplo básico:

```
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera app")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()

ventana.mainloop()
```
