import tkinter as tk  # Importamos la librería

ventana = tk.Tk()  # Creamos la ventana principal
ventana.title("Motos")  # Le ponemos un título

#... aquí irá el código para añadir widgets ...

ventana.mainloop()  # Mantiene la ventana abierta y a la espera de acciones

import tkinter as tk

# 1. Ventana principal
ventana = tk.Tk()
ventana.title("Lista de Motos")
ventana.geometry("1200x640")  # Ancho x Alto

# Aquí irán los pasos 2 y 3...
 
# --- Formulario de Entrada ---
etiqueta_desc = tk.Label(ventana, text="Marca:")
campo_desc = tk.Entry(ventana, width=60)

etiqueta_fecha = tk.Label(ventana, text="Cilindrada:")
campo_fecha = tk.Entry(ventana)
etiqueta_prio = tk.Label(ventana, text="Número de serie:")
campo_prio = tk.Entry(ventana)
etiqueta_prio1 = tk.Label(ventana, text="Precio:")
campo_prio1 = tk.Entry(ventana)
etiqueta_prio2 = tk.Label(ventana, text="Combustible:")
campo_prio2 = tk.Entry(ventana)

# --- Botones ---
boton_add = tk.Button(ventana, text="Añadir Tarea")
boton_update = tk.Button(ventana, text="Modificar Tarea")
boton_delete = tk.Button(ventana, text="Eliminar Tarea")

# --- Lista de Tareas ---
etiqueta_lista = tk.Label(ventana, text="Tareas Pendientes:")
lista_tareas = tk.Listbox(ventana, width=120, height=10)

# 3. Posicionamiento con Grid
# --- Formulario de Entrada ---
etiqueta_desc.grid(row=0, column=0, padx=10, pady=5, sticky="w")
campo_desc.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="ew")

etiqueta_fecha.grid(row=1, column=0, padx=10, pady=5, sticky="w")
campo_fecha.grid(row=1, column=1, padx=10, pady=5, columnspan=1, sticky="ew")

etiqueta_prio.grid(row=1, column=2, padx=10, pady=5, sticky="w")
campo_prio.grid(row=1, column=3, padx=10, pady=5, columnspan=1, sticky="ew")

etiqueta_prio1.grid(row=1, column=4, padx=10, pady=5, sticky="w")
campo_prio1.grid(row=1, column=5, padx=10, pady=5, columnspan=1, sticky="ew")

etiqueta_prio2.grid(row=1, column=6, padx=10, pady=5, sticky="w")
campo_prio2.grid(row=1, column=7, padx=10, pady=5, columnspan=1, sticky="ew")


# --- Botones ---
boton_add.grid(row=2, column=0, padx=10, pady=10)
boton_update.grid(row=2, column=1, padx=10, pady=10)
boton_delete.grid(row=2, column=2, padx=10, pady=10)

# --- Lista de Tareas ---
etiqueta_lista.grid(row=3, column=0, padx=10, pady=5, sticky="w")
lista_tareas.grid(row=4, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")


# 4. Iniciar el bucle de la aplicación
ventana.mainloop()