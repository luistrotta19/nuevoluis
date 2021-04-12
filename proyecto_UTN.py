from tkinter import*
from PIL.ImageTk import PhotoImage
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector
import re

# Variables global
ruta = "C:/team_python"
ID = 0
# Ventana principal con ingreso de clave

ventana1 = Tk()
ventana1.title("Agencia CarFanatics")
ventana1.geometry("750x690")
ventana1.configure(background="Black")
ventana1.iconbitmap(ruta + "/car_icono.ico")

image = tk.PhotoImage(file=ruta + "/car1.PNG")
image = image.subsample(1, 1)
label = tk.Label(image=image)
label.place(x=0, y=0, relwidth=1.0, relheight=1.0)


Label(ventana1, text="Ingrese su nombre", fg="White", bg="Black", font=(
    "arial", 14, "bold")).place_configure(x=295, y=410)

Label(ventana1, text="Ingresar la clave", fg="White", bg="Black", font=(
    "arial", 14, "bold")).place_configure(x=308, y=490)


ingrese_su_nombre = StringVar
ingrese_su_nombre = Entry()
ingrese_su_nombre.place(width=175, height=27, x=300, y=451)

# Por seguridad se coloca "*" para no mostrar la clave
ingrese_la_clave = StringVar
ingrese_la_clave = Entry(ventana1, show="*")
ingrese_la_clave.place(width=175, height=27, x=300, y=525)


def ingresar():
    ingrese_su_nombre.get(), ingrese_la_clave.get() == "agenciaCARF"


Button(ventana1, text="Ingresar", width=9, command=ingresar, font=("arial", 12, "bold")).place(
    x=250, y=600)


def cancelar():
    ventana1.destroy()


Button(ventana1, text="Cancelar", width=9, command=cancelar, font=("arial", 12, "bold")).place(
    x=420, y=600)


ventana1.mainloop()

# Segunda ventana / se crea base de datos y se ingresa los registros


ventana2 = Tk()
ventana2.title("Agencia CarFanatics - Ingresos")
ventana2.geometry("815x690")
ventana2.configure(background="Black")
ventana2.iconbitmap(ruta + "/car_icono.ico")

image = tk.PhotoImage(file=ruta + "/car2.png")
image = image.subsample(1, 1)
label = tk.Label(image=image)
label.place(x=0, y=0, relwidth=1.0, relheight=1.0)


# Se crean las etiquetas

Label(ventana2, text="Marca", fg="White", bg="Black", font=(
    "Arial", 14, "bold")).place_configure(x=5, y=220)

Label(ventana2, text="Modelo", fg="White", bg="Black", font=(
    "Arial", 14, "bold")).place_configure(x=5, y=275)

Label(ventana2, text="Anio", fg="White", bg="Black", font=(
    "Arial", 14, "bold")).place_configure(x=5, y=325)

Label(ventana2, text="Color", fg="White", bg="Black", font=(
    "Arial", 14, "bold")).place_configure(x=5, y=375)

Label(ventana2, text="Valor", fg="White", bg="Black", font=(
    "Arial", 14, "bold")).place_configure(x=350, y=220)

Label(ventana2, text="Disponibilidad", fg="White", bg="Black", font=(
    "Arial", 14, "bold")).place_configure(x=350, y=275)

Label(ventana2, text="Fecha de venta", fg="White", bg="Black", font=(
    "Arial", 14, "bold")).place_configure(x=350, y=325)

Label(ventana2, text="Vendedor", fg="White", bg="Black", font=(
    "arial", 14, "bold")).place_configure(x=350, y=375)

# Se crean las cajas de texto

marca = StringVar
marca = Entry()
marca.place(width=175, height=22, x=85, y=225)

modelo = StringVar
modelo = Entry()
modelo.place(width=175, height=22, x=95, y=280)

anio = StringVar
anio = Entry()
anio.place(width=175, height=22, x=68, y=328)

color = StringVar
color = Entry()
color.place(width=175, height=22, x=75, y=378)

valor = StringVar
valor = Entry()
valor.place(width=175, height=22, x=415, y=225)

disponibilidad = StringVar
disponibilidad = Entry()
disponibilidad.place(width=175, height=22, x=507, y=280)

fecha_de_venta = StringVar
fecha_de_venta = Entry()
fecha_de_venta.place(width=175, height=22, x=510, y=328)

vendedor = StringVar
vendedor = Entry()
vendedor.place(width=175, height=22, x=458, y=378)


# Se crea base de datos

def crearbd():
    try:
        mibase = mysql.connector.connect(
            host="localhost", user="root", passwd="")
        micursor = mibase.cursor()
        micursor.execute("CREATE DATABASE agencia")
        mibase = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="agencia")
        micursor = mibase.cursor()
        micursor.execute("CREATE TABLE ventas(id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, marca VARCHAR(80) COLLATE utf8_spanish2_ci NOT NULL, modelo VARCHAR(80) COLLATE utf8_spanish2_ci NOT NULL, anio YEAR(4), color VARCHAR(80) COLLATE utf8_spanish2_ci NOT NULL, valor decimal(8.3), disponibilidad VARCHAR(80) COLLATE utf8_spanish2_ci NOT NULL, fecha_de_venta DATE, vendedor VARCHAR(80) COLLATE utf8_spanish2_ci NOT NULL)")
        print("Base de datos creada")
    except:
        print("Base de datos existente")


Button(ventana2, text="CrearBD", width=9, command=crearbd, font=("Arial", 12, "bold")).place(
    x=110, y=622)


def miconexion():
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="agencia")
    return mibase


# Se crea tabla con ingreso de datos
def alta():
    print("Alta de datos")

    cadena = marca.get()
    patron = "^[A-Za-z]+(?i:[_-][A-Za-z]+)*$"
    if(re.match(patron, cadena)):
        Label(ventana2, text="Cadena valida:" + marca.get(), fon=(
            "Arial", 12, "bold")).place(x=590, y=170)
        print("Valido")

        mibase = miconexion()
        print(mibase)
        micursor = mibase.cursor()
        sql = "INSERT INTO ventas (marca, modelo, anio, color, valor, disponibilidad, fecha_de_venta, vendedor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (marca.get(), modelo.get(), anio.get(), color.get(), valor.get(),
                 disponibilidad.get(), fecha_de_venta.get(), vendedor.get())
        micursor.execute(sql, datos)
        mibase.commit()
    else:
        Label(ventana2, text="Cadena No valida: " + marca.get(),
              font=("Arial", 12, "bold")).place(x=590, y=170)
        print("No validado")

    global ID
    ID += 1
    tree.insert("", "end", text=str(ID), values=(marca.get(), modelo.get(), anio.get(
    ), color.get(), valor.get(), disponibilidad.get(), fecha_de_venta.get(), vendedor.get()))
    mostrar()

# Mensaje al ingresar nuevos datos a la base
    messagebox.showinfo(
        message="El nuevo registro se ha realizado de manera exitosa.", title="Ingresos")


Button(ventana2, text="Alta", width=9, command=alta, font=("Arial", 12, "bold")).place(
    x=268, y=622)


def busqueda():
    mibase = mysql.connector.connect(host="localhost", user="root", passwd="",
                                     database="agencia")
    micursor = mibase.cursor()

    sql = "SELECT * FROM ventas"
    micursor.execute(sql)
    resultado = micursor.fetchall()
    for x in resultado:
        print(x)


def mostrar():
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="agencia"
    )
    micursor = mibase.cursor()
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        micursor.execute("SELECT * FROM ventas")
        for row in micursor:
            tree.insert(
                "",
                0,
                text=row[0],
                values=(
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                ),
            )
    except:
        pass


def borrar():
    global ID
    ID -= 1

    cur_item = tree.focus()
    diccionario = tree.item(cur_item)
    id = diccionario["text"]
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="agencia")

    micursor = mibase.cursor()
    sql = "DELETE FROM ventas WHERE id= '%s'"
    dato = (id,)
    micursor.execute(sql, dato)
    mibase.commit()
    print(micursor.rowcount, "Registro borrado")
    messagebox.showinfo("Aviso",
                        "Se ha eliminado el registro.")


Button(ventana2, text="Borrar", width=9, command=borrar, font=("Arial", 12, "bold")).place(
    x=435, y=622)


# def actualizacion():
# mibase = mysql.connector.connect(host="localhost", user="root", passwd="",database = "agencia")
# micursor = mibase.cursor()

# sql = "UPDATE ventas

# micursor.execute(sql)
# mibase.commit()

# print(micursor.rowcount, "Cantidad de registros afectados.")


def salir():
    valor = messagebox.askquestion("Aviso", "¿Esta seguro que desea salir?")
    if valor == "yes":
        ventana2.destroy()


Button(ventana2, text="Salir", width=9, command=salir, font=("Arial", 12, "bold")).place(
    x=595, y=622)


# Se muestra la carga de datos en el Treeview

tree = ttk.Treeview(height=8, columns=(
    "#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"))
tree.place(x=0, y=430)
tree.column("#0", width=50, minwidth=50, anchor=CENTER)
tree.column("#1", width=100, minwidth=100, anchor=CENTER)
tree.column("#2", width=100, minwidth=100, anchor=CENTER)
tree.column("#3", width=85, minwidth=85, anchor=CENTER)
tree.column("#4", width=90, minwidth=90, anchor=CENTER)
tree.column("#5", width=95, minwidth=95, anchor=CENTER)
tree.column("#6", width=95, minwidth=95, anchor=CENTER)
tree.column("#7", width=100, minwidth=100, anchor=CENTER)
tree.column("#8", width=100, minwidth=100, anchor=CENTER)

tree.heading("#0", text="ID", anchor=CENTER)
tree.heading("#1", text="Marca", anchor=CENTER)
tree.heading("#2", text="Modelo", anchor=CENTER)
tree.heading("#3", text="Anio", anchor=CENTER)
tree.heading("#4", text="Color", anchor=CENTER)
tree.heading("#5", text="Valor", anchor=CENTER)
tree.heading("#6", text="Disponibilidad", anchor=CENTER)
tree.heading("#7", text="Fecha de venta", anchor=CENTER)
tree.heading("#8", text="Vendedor", anchor=CENTER)


ventana2.mainloop()
