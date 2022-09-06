from cmath import log
import getpass
from cProfile import label
from cgitb import text
from tkinter import *
import tkinter
from turtle import width 
import os
from cv2 import inpaint
import pandas as pd
from numpy import empty
import conexiones
import xlwings as xw
from tkinter import messagebox



#Principal Frame Menu
root = Tk()
root.title("SMC - Ripley Chile")
root.resizable(True, False)
root.geometry("650x250")
root.resizable(width=False, height=False)







def Chile():
    frameOne = Frame()

    def clear_text():
        firstEntry.delete(0, END)

    def button_command():
        inputNumber = firstEntry.get()
        input2 = inputNumber.split(",")
        for i in range(len(input2)):
            list = [input2[i]]
            print('SKU: ' + str(i))
            variantSKU = conexiones.variantSKU_WritterCL(list)
            idSeller = conexiones.idSeller_WritterCL(list)
        # print(variantSKU, idSeller)
        
        df = pd.DataFrame({'sku_Variante': variantSKU, 'id_Seller':idSeller})
        df_2 = pd.DataFrame()
        listaVacia = []
        print(df)
        app=xw.App(visible=False)
        wb = app.books.open(r'ApiToFile\Archivo-Publicacion.xlsx')  
        # wb = xw.Book(r'dependencies/republicar_productos(4).xlsx')
        ws = wb.sheets['Data']
        ws.range('A4').options(index=False,header=None).value = df

        wb.save()
        wb.close()
        app.quit()
        variantSKU.clear()
        idSeller.clear()
        df = df_2

        print("Terminó la importación")
        messagebox.showinfo('STATUS', 'Tu archivo está listo!')

        return  inputNumber





    all_commands = lambda: [button_command()]
    cleancommands = lambda: [clear_text()]

    firstEntry = Entry(root, width= 40)
    firstEntry.place(x = 200, y = 30)

    labelEntry = Label( text = "Ingrese el SKU: ")
    labelEntry.place(x= 20, y=30)

    btn = Button(root, text="Generar", command = all_commands, width= 15 )
    btn.place(x = 500, y = 17)

    btn2 = Button(root, text="Limpiar", command = cleancommands, width= 15 )
    btn2.place(x = 500, y = 46)

    labelVersion = Label( text="v 0.2.1")
    labelVersion.place(x = 555 , y = 230)

    labelDev = Label( text= "by A.M")
    labelDev.place(x = 600, y = 230)
    
    
    frameOne.config(width=550, height=60)
    frameOne.config(bd=0)
    frameOne.config(relief="sunken")
    frameOne.pack()

    image2 = PhotoImage(file=r"ApiToFile\dependencias\chileIMG.png")

    lbCountry = Label(image=image2)
    lbCountry.config(bd=6)
    lbCountry.image2 = image2
    lbCountry.pack()
    lbCountry.place(x=120, y=20)
        

    frameTwo = Frame()
    userPC = getpass.getuser()
    frameTwo.pack()
    frameTwo.config(width=640, height=125)
    frameTwo.config(bd=4)
    frameTwo.config(relief="sunken")
    labelGD = Label(font=('Helvetica', 10, 'bold'), text=f"¡Bienvenido {userPC}!").place(x= 240, y= 100)
    labelLog = Label(font=('Helvetica', 8), text=f"* RECORDATORIOS").place(x= 25, y= 130)
    recordatorio_1 = Label(font=('Helvetica', 9), text=f"- Los SKU deben estar separados por comas.").place(x= 25, y= 160)
    recordatorio_2 = Label(font=('Helvetica', 9), text=f"- El listado no debe contener saltos de linea").place(x= 25, y= 180)
    frameTwo.place(x=5, y=86)



def Peru():
    
    frameOne = Frame()
    def clear_text():
        firstEntry.delete(0, END)

    def button_command():
        inputNumber = firstEntry.get()
        input2 = inputNumber.split(",")
        for i in range(len(input2)):
            list = [input2[i]]
            print('SKU: ' + str(i))
            variantSKU = conexiones.variantSKU_WritterPE(list)
            idSeller = conexiones.idSeller_WritterPE(list)
        # print(variantSKU, idSeller)
        
        df = pd.DataFrame({'sku_Variante': variantSKU, 'id_Seller':idSeller})
        df_2 = pd.DataFrame()
        listaVacia = []
        print(df)
        app=xw.App(visible=False)
        wb = app.books.open(r'ApiToFile\Archivo-Publicacion.xlsx')  
        # wb = xw.Book(r'dependencies/republicar_productos(4).xlsx')
        ws = wb.sheets['Data']
        ws.range('A4').options(index=False,header=None).value = df

        wb.save()
        wb.close()
        app.quit()
        variantSKU.clear()
        idSeller.clear()
        df = df_2

        print("Terminó la importación")
        messagebox.showinfo('STATUS', 'Tu archivo está listo!')

        return  inputNumber



    all_commands = lambda: [button_command()]
    cleancommands = lambda: [clear_text()]

    firstEntry = Entry(root, width= 40)
    firstEntry.place(x = 200, y = 30)

    labelEntry = Label( text = "Ingrese el SKU: ")
    labelEntry.place(x= 20, y=30)

    btn = Button(root, text="Generar", command = all_commands, width= 15 )
    btn.place(x = 500, y = 17)

    btn2 = Button(root, text="Limpiar", command = cleancommands, width= 15 )
    btn2.place(x = 500, y = 46)

    labelVersion = Label( text="v 0.2.1")
    labelVersion.place(x = 555 , y = 230)

    labelDev = Label( text= "by A.M")
    labelDev.place(x = 600, y = 230)
    
 
    
    frameOne.config(width=550, height=60)
    frameOne.config(bd=0)
    frameOne.config(relief="sunken")
    frameOne.pack()

    image3 = PhotoImage(file=r"ApiToFile\dependencias\peruIMG.png")
   
    lbCountry = Label(image=image3)
    lbCountry.config(bd=6)
    lbCountry.image3 = image3
    lbCountry.pack()
    lbCountry.place(x=120, y=20)

    frameTwo = Frame()
    userPC = getpass.getuser()
    frameTwo.pack()
    frameTwo.config(width=640, height=125)
    frameTwo.config(bd=4)
    frameTwo.config(relief="sunken")
    labelGD = Label(font=('Helvetica', 10, 'bold'), text=f"¡Bienvenido {userPC}!").place(x= 240, y= 100)
    labelLog = Label(font=('Helvetica', 8), text=f"* RECORDATORIOS").place(x= 25, y= 130)
    recordatorio_1 = Label(font=('Helvetica', 9), text=f"- Los SKU deben estar separados por comas.").place(x= 25, y= 160)
    recordatorio_2 = Label(font=('Helvetica', 9), text=f"- El listado no debe contener saltos de linea").place(x= 25, y= 180)
    # imgCorp = tkinter.PhotoImage(file='icons\peruIMG.png', height= 2, width=4)
    # lblImg = tkinter.Label(frameTwo, image= imgCorp)
    # lblImg.pack()
    frameTwo.place(x=5, y=86)



menu = Menu(root)
root.config(menu=menu)
Country = Menu(menu, tearoff=0)
menu.add_cascade(label = "País", menu = Country)
Country.add_command(label = "Chile", command = Chile)
Country.add_command(label = "Perú", command = Peru)
Chile()
root.mainloop()

