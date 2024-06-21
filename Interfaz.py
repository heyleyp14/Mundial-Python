import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from Equipo import Equipo
from Estadio import Estadio
from Grupo import Grupo
from Mundial import Mundial
from Partido import Partido
from Jugador import Jugador

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

class MundialGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Mundial de Fútbol")
        self.master.configure(bg="#C5CAE9")
        center_window(self.master,400,450)

        self.label = tk.Label(master, text="Bienvenido al Mundial de Fútbol", font=("Arial", 18), bg="#C5CAE9")
        self.label.pack(pady=10)

        self.imagen = Image.open("imagen.png")
        self.imagen = self.imagen.resize((200, 200))
        self.imagen = ImageTk.PhotoImage(self.imagen)

        self.label_imagen = tk.Label(master, image=self.imagen, bg="#C5CAE9")
        self.label_imagen.pack()

        self.mundial = Mundial()

        botones = [
            ("Registrar Grupo", self.abrir_ventana_registrar_grupo),
            ("Registrar Estadio", self.abrir_ventana_registrar_estadio),
            ("Generar Fixture", self.generar_fixture),
            ("Salir", self.salir)
        ]

        max_button_width = max(len(texto) for texto, _ in botones) + 4

        button_width = 20
        button_padx = 10
        button_pady = 5

        for texto, comando in botones:
            btn = tk.Button(master, text=texto, width=max_button_width, command=comando, bg="#E0E0E0", font=("Arial", 12))
            btn.pack(pady=button_pady, padx=button_padx)

    def abrir_ventana_registrar_grupo(self):
        ventana_registrar_grupo = tk.Toplevel(self.master)
        ventana_registrar_grupo.title("Registrar Grupo")
        center_window(ventana_registrar_grupo, 400, 300)
        ventana_registrar_grupo.configure(bg="#E8EAF6")

        tk.Label(ventana_registrar_grupo, text="Nombre del Grupo:", font=("Arial", 12), bg="#E8EAF6").pack(pady=10)
        nombre_grupo = tk.Entry(ventana_registrar_grupo, font=("Arial", 12))
        nombre_grupo.pack(pady=5)

        tk.Label(ventana_registrar_grupo, text="Cantidad de Equipos:", font=("Arial", 12), bg="#E8EAF6").pack(pady=10)
        cantidad_equipos = tk.Entry(ventana_registrar_grupo, font=("Arial", 12))
        cantidad_equipos.pack(pady=5)

        btn_registrar = tk.Button(ventana_registrar_grupo, text="Registrar", command=lambda: self.registrar_grupo(nombre_grupo.get(), cantidad_equipos.get()))
        btn_registrar.pack(pady=20)

    def abrir_ventana_registrar_estadio(self):
        ventana_registrar_estadio = tk.Toplevel(self.master)
        ventana_registrar_estadio.title("Registrar Estadio")
        center_window(ventana_registrar_estadio, 400, 300)
        ventana_registrar_estadio.configure(bg="#E8EAF6")

        tk.Label(ventana_registrar_estadio, text="Nombre del Estadio:", font=("Arial", 12), bg="#E8EAF6").pack(pady=10)
        nombre_estadio = tk.Entry(ventana_registrar_estadio, font=("Arial", 12))
        nombre_estadio.pack(pady=5)

        tk.Label(ventana_registrar_estadio, text="Ciudad del Estadio:", font=("Arial", 12), bg="#E8EAF6").pack(pady=10)
        ciudad_estadio = tk.Entry(ventana_registrar_estadio, font=("Arial", 12))
        ciudad_estadio.pack(pady=5)

        tk.Label(ventana_registrar_estadio, text="Capacidad del Estadio:", font=("Arial", 12), bg="#E8EAF6").pack(pady=10)
        capacidad_estadio = tk.Entry(ventana_registrar_estadio, font=("Arial", 12))
        capacidad_estadio.pack(pady=5)

        btn_registrar = tk.Button(ventana_registrar_estadio, text="Registrar", command=lambda: self.registrar_estadio(nombre_estadio.get(), ciudad_estadio.get(), capacidad_estadio.get()))
        btn_registrar.pack(pady=20)

    def registrar_grupo(self, nombre_grupo, cantidad_equipos):
        try:
            cantidad_equipos = int(cantidad_equipos)
            equipos = []
            for i in range(cantidad_equipos):
                nombre_equipo = simpledialog.askstring("Registrar Equipo", f"Ingrese el nombre del equipo {i + 1}:")
                entrenador = simpledialog.askstring("Registrar Equipo", f"Ingrese el nombre del entrenador del equipo {i + 1}:")
                cantidad_jugadores = int(simpledialog.askstring("Registrar Equipo", f"Ingrese la cantidad de jugadores en el equipo {i + 1}:"))
                jugadores = []
                for j in range(cantidad_jugadores):
                    nombre_jugador = simpledialog.askstring("Registrar Jugador", f"Ingrese el nombre del jugador {j + 1}:")
                    edad = int(simpledialog.askstring("Registrar Jugador", f"Ingrese la edad del jugador {j + 1}:"))
                    posicion = simpledialog.askstring("Registrar Jugador",
                                                      f"Ingrese la posición del jugador {j + 1}:")
                    jugador = Jugador(nombre_jugador, edad, posicion)
                    jugadores.append(jugador)
                equipo = Equipo(nombre_equipo, entrenador, jugadores)
                equipos.append(equipo)
            grupo = Grupo(nombre_grupo, equipos)
            self.mundial.registrar_grupo(grupo)
            self.mostrar_info("Registro", "Grupo registrado con éxito.")
        except ValueError:
            messagebox.showerror("Error", "La cantidad de equipos debe ser un número entero.")

    def registrar_estadio(self, nombre_estadio, ciudad_estadio, capacidad_estadio):
        try:
            capacidad_estadio = int(capacidad_estadio)
            estadio = Estadio(nombre_estadio, ciudad_estadio, capacidad_estadio)
            self.mundial.registrar_estadio(estadio)
            self.mostrar_info("Registro", "Estadio registrado con éxito.")
        except ValueError:
            messagebox.showerror("Error", "La capacidad del estadio debe ser un número entero.")

    def generar_fixture(self):
        info = self.mundial.generar_fixture()
        self.mostrar_info("Fixture", info)

    def mostrar_info(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def salir(self):
        self.master.quit()


root = tk.Tk()
app = MundialGUI(root)
root.mainloop()

