from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox
#operador
operator = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94]

def click_button(num):
    global operator
    operator = operator + num
    visor_calc.delete(0,END)
    visor_calc.insert(END,operator)

def borrar():
    global operator
    operator = ''
    visor_calc.delete(0,END)

def resultado():
    try:
        result = str(eval(operator))
    except SyntaxError:
        result = "Error: Invalid expression"
    visor_calc.delete(0, END)
    visor_calc.insert(0, result)

def revisar_check():
    x = 0
    for _ in cards_food:
        if variable_food[x].get() == 1:
            cards_food[x].config(state=NORMAL)
            if cards_food[x].get() == '0':
                cards_food[x].delete(0,END)
            cards_food[x].focus()
        else:
            cards_food[x].config(state = DISABLED)
            text_food[x].set('0')
        x += 1
    x = 0
    for _ in cards_drink:
        if variable_drink[x].get() == 1:
            cards_drink[x].config(state=NORMAL)
            if cards_drink[x].get() == '0':
                cards_drink[x].delete(0,END)
            cards_drink[x].focus()
        else:
            cards_drink[x].config(state = DISABLED)
            text_drink[x].set('0')
        x += 1
    x = 0
    for _ in cards_dessert:
        if variable_dessert[x].get() == 1:
            cards_dessert[x].config(state=NORMAL)
            if cards_dessert[x].get() == '0':
                cards_dessert[x].delete(0,END)
            cards_dessert[x].focus()
        else:
            cards_dessert[x].config(state = DISABLED)
            text_dessert[x].set('0')
        x += 1
def total():
    sub_total_comida = 0
    p = 0
    for entry in cards_food:
        cantidad = entry.get()
        sub_total_comida = sub_total_comida + (float(cantidad) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for entry in cards_drink:
        cantidad = entry.get()
        sub_total_bebida = sub_total_bebida + (float(cantidad) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for entry in cards_dessert:
        cantidad = entry.get()
        sub_total_postres = sub_total_postres + (float(cantidad) * precios_postres[p])
        p += 1
    
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.16
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida,2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida,2)}')
    var_costo_postre.set(f'$ {round(sub_total_postres,2)}') 
    var_subtotal.set(f'$ {round(sub_total,2)}')
    var_IVA.set(f'$ {round(impuestos,2)}') 
    var_total.set(f'$ {round(total,2)}')

def recibo():
    # Clear the text_recibo widget
    text_recibo.delete(1.0, END)

    # Generate a random receipt number
    num_recibo = f'N# - {random.randint(1000,9999)}'

    # Get the current date and time
    fecha = datetime.datetime.now()
    date_recibo = f'{fecha.day} - {fecha.month} - {fecha.year} - {fecha.hour}:{fecha.minute}'

    # Insert the receipt details into the text_recibo widget
    text_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{date_recibo}\n')
    text_recibo.insert(END, f'*'*63+'\n')
    text_recibo.insert(END, f'Items \t\t Cant.\t  Costo Items \n')
    text_recibo.insert(END, f'-'*75 + '\n')

    x = 0
    for comida in cards_food:  
        if comida.get() != '0':
            cantidad = comida.get()
            if cantidad != '':
                text_recibo.insert(END, f'{list_foods[x]}\t | \t{comida.get()}\t|\t$ {round((float(cantidad)*precios_comida[x]),2)}\n')
        x += 1

    x = 0
    for bebida in cards_drink:  
        if bebida.get() != '0':
            cantidad = bebida.get()
            if cantidad != '':
                text_recibo.insert(END, f'{list_foods[x]}\t | \t{bebida.get()}\t|\t$ {round((float(cantidad)*precios_bebida[x]),2)}\n')
        x += 1

    x = 0
    for postre in cards_dessert:  
        if postre.get() != '0':
            cantidad = postre.get()
            if cantidad != '':
                text_recibo.insert(END, f'{list_foods[x]}\t | \t{postre.get()}\t|\t$ {round((float(cantidad)*precios_postres[x]),2)}\n')
        x += 1

    text_recibo.insert(END, f'-'*75 + '\n')
    text_recibo.insert(END, f'Costo Comida: {var_costo_comida.get()}\n')
    text_recibo.insert(END, f'Costo Bebida: {var_costo_bebida.get()}\n')
    text_recibo.insert(END, f'Costo Postres: {var_costo_postre.get()}\n')
    text_recibo.insert(END, f'-'*75 + '\n')
    text_recibo.insert(END, f'Sub-Total: {var_subtotal.get()}\n')
    text_recibo.insert(END, f'IVA: {var_IVA.get()}\n')
    text_recibo.insert(END, f'Total: {var_total.get()}\n')
    text_recibo.insert(END, f'*'*63+'\n')
    text_recibo.insert(END, f'Lo esperamos pronto')

def guardar():
    info_recibo = text_recibo.get(1.0,END)
    archivo = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información',"Su recibo ha sido guardado")

def resetear():
    text_recibo.delete(0.1, END)
    for entry in cards_food:
        entry.delete(0, END)
    for entry in cards_drink:
        entry.delete(0, END)
    for entry in cards_dessert:
        entry.delete(0, END)

    for cuadro in cards_food:
        cuadro.config(state=DISABLED)
    for cuadro in cards_drink    :
        cuadro.config(state=DISABLED)
    for cuadro in cards_dessert:
        cuadro.config(state=DISABLED)

    for v in variable_food:
        v.set(0)
    for v in variable_drink:
        v.set(0)
    for v in variable_dessert:
        v.set(0)
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_IVA.set('')
    var_total.set('')
# Iniciar TKINTER
app = Tk()

# configuracion ventana

app.geometry('1400x720')
app.resizable(0,0)
app.title('Mi Restaurante - Sistema de facturacion')
app.config(bg='#4F0EE8')

# Panel superior

panel_superior = Frame(app, bd = 1, relief=FLAT)
panel_superior.pack(side=TOP)
#Etiqueta titulo

etiqueta_titulo = Label(panel_superior, 
                        text='Sistema de facturación', 
                        fg='#F9F2FF',
                        font=('Dosis',58),
                        bg="#8445F5", width=25)
etiqueta_titulo.grid(row=0, column=0)

#Panel izquierdo

panel_izquierdo = Frame(app, bd=2, relief=FLAT)

panel_izquierdo.pack(side=LEFT)

#Panel Costos

panel_costos =  Frame(panel_izquierdo, bd=2, relief=FLAT, bg='#3005B8', padx=40, pady=30)
panel_costos.pack(side=BOTTOM)

#Panel de Comidas

panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Nunito Sans',19,'bold'),
                           bd=2, relief=FLAT, fg='#DAB9FF')
panel_comidas.pack(side=LEFT)

#Panel de Bebidas

panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Nunito Sans',19,'bold'),
                           bd=2, relief=FLAT, fg='#DAB9FF')
panel_bebidas.pack(side=LEFT)

#Panel de Postres

panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Nunito Sans',19,'bold'),
                           bd=2, relief=FLAT, fg='#DAB9FF')
panel_postres.pack(side=LEFT)

#Panel derecha

panel_derecha = Frame(app, bd=2, relief=FLAT)

panel_derecha.pack(side=RIGHT)

#Panel calculadora

panel_calculadora = Frame(panel_derecha, bd=2,relief=FLAT, bg='#4F0EE8')
panel_calculadora.pack()

#Panel recibo

panel_recibo = Frame(panel_derecha, bd=2,relief=FLAT, bg='#4F0EE8')
panel_recibo.pack()

#Panel botones

panel_botones = Frame(panel_derecha, bd=2,relief=FLAT, bg='#4F0EE8')
panel_botones.pack()

# lista de productos
list_foods = ['pollo', 'salmon','albondigas','Pizza','nuggets','milanesa','tacos']
list_drinks = ['Refresco1', 'Agua1', 'Agua2', 'Cerveza', 'Tequila','Agua3','Refresco2']
list_desserts = ['helado', 'crepas', 'pastel1', 'pie2', 'brownie', 'flan', 'mousse']

# Cargar nombres de comida dentro de los paneles
variable_food = []
cards_food = []
text_food = []

count = 0
for food in list_foods:

    #crear checkbuttons
    variable_food.append('')
    text_food.append('')
    text_food[count] = StringVar()
    text_food[count].set('0')
    variable_food[count] = IntVar()
    food = Checkbutton(panel_comidas, 
                        text=food.title(),
                        font=('Nunito Sans', 19, 'bold'),
                        onvalue=1, offvalue=0,
                        variable=variable_food[count],
                        command=revisar_check)
    food.grid(row=count, column=0, sticky=W)

    #cards of input
    cards_food.append('')
    text_food.append('')
    cards_food[count] = Entry(panel_comidas,
                              font=('Nunito Sans', 19,'bold'), 
                              bd=2, width=7,
                              state=DISABLED,
                              textvariable=text_food[count])

    cards_food[count].grid(row=count, column=1)
    count+= 1

# Cargar nombres de bebidas dentro de los paneles
variable_drink= []
cards_drink = []
text_drink = []
count = 0

for drink in list_drinks:
    variable_drink.append('')
    text_drink.append('')
    text_drink[count] = StringVar()
    text_drink[count].set('0')
    variable_drink[count] = IntVar()
    drink = Checkbutton(panel_bebidas,
                        text=drink.title(), 
                        font=('Nunito Sans', 19, 'bold'),
                        onvalue=1, offvalue=0,
                        variable=variable_drink[count],
                        command=revisar_check)
    drink.grid(row=count, column=0, sticky=W)
    
    #cards of input
    cards_drink.append('')
    text_drink.append('')
    cards_drink[count] = Entry(panel_bebidas,
                            font=('Nunito Sans', 19,'bold'), 
                            bd=2, width=7,
                            state=DISABLED,
                            textvariable=text_drink[count])

    cards_drink[count].grid(row=count, column=1)
    count+= 1

# Cargar nombres de postres dentro de los paneles
variable_dessert = []
cards_dessert = []
text_dessert = []
count = 0

for dessert in list_desserts:
    variable_dessert.append('')
    text_dessert.append('')
    text_dessert[count] = StringVar()
    text_dessert[count].set('0')
    variable_dessert[count] = IntVar()
    dessert = Checkbutton(panel_postres,
                        text=dessert.title(),
                        font=('Nunito Sans', 19, 'bold'),
                        onvalue=1, offvalue=0,
                        variable=variable_dessert[count],
                        command=revisar_check)
    dessert.grid(row=count, column=0, sticky=W)
        #cards of input
    cards_dessert.append('')
    text_dessert.append('')
    cards_dessert[count] = Entry(panel_postres,
                            font=('Nunito Sans', 19,'bold'), 
                            bd=2, width=7,
                            state=DISABLED,
                            textvariable=text_dessert[count])

    cards_dessert[count].grid(row=count, column=1)
    
    count+= 1


#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_IVA = StringVar()
var_total = StringVar()
# etiquetas de costo y campos de entrada
etiquetas_costo_comida = Label(panel_costos,
                            text='Costo comida',
                            font=('Nunito Sans',19,'bold'),
                            bg='#8445F5',
                            fg='white')
etiquetas_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                        font=('Nunito Sans',12,'bold'),
                        bd=2,
                        width=10,
                        state='readonly',
                        textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1)

# etiquetas de costo y campos de entrada
etiquetas_costo_bebida = Label(panel_costos,
                            text='Costo bebida',
                            font=('Nunito Sans',19,'bold'),
                            bg='#8445F5',
                            fg='white')
etiquetas_costo_bebida.grid(row=0, column=2)

texto_costo_bebida = Entry(panel_costos,
                        font=('Nunito Sans',12,'bold'),
                        bd=2,
                        width=10,
                        state='readonly',
                        textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=0, column=3)

# etiquetas de costo y campos de entrada
etiquetas_costo_postre = Label(panel_costos,
                            text='Costo postre',
                            font=('Nunito Sans',19,'bold'),
                            bg='#8445F5',
                            fg='white')
etiquetas_costo_postre.grid(row=0, column=4)

texto_costo_postre = Entry(panel_costos,
                        font=('Nunito Sans',12,'bold'),
                        bd=2,
                        width=10,
                        state='readonly',
                        textvariable=var_costo_postre)
texto_costo_postre.grid(row=0, column=5)

# etiquetas de costo y campos de entrada
etiquetas_subtotal = Label(panel_costos,
                            text='Subtotal',
                            font=('Nunito Sans',19,'bold'),
                            bg='#8445F5',
                            fg='white')
etiquetas_subtotal.grid(row=1, column=0)

texto_subtotal = Entry(panel_costos,
                        font=('Nunito Sans',12,'bold'),
                        bd=2,
                        width=10,
                        state='readonly',
                        textvariable=var_subtotal)
texto_subtotal.grid(row=1, column=1)

# etiquetas de costo y campos de entrada
etiquetas_IVA = Label(panel_costos,
                            text='IVA',
                            font=('Nunito Sans',19,'bold'),
                            bg='#8445F5',
                            fg='white')
etiquetas_IVA.grid(row=1, column=2)

texto_IVA = Entry(panel_costos,
                        font=('Nunito Sans',12,'bold'),
                        bd=2,
                        width=10,
                        state='readonly',
                        textvariable=var_IVA)
texto_IVA.grid(row=1, column=3)

# etiquetas de costo y campos de entrada
etiquetas_total = Label(panel_costos,
                            text='Total',
                            font=('Nunito Sans',19,'bold'),
                            bg='#8445F5',
                            fg='white')
etiquetas_total.grid(row=1, column=4)

texto_total = Entry(panel_costos,
                        font=('Nunito Sans',12,'bold'),
                        bd=2,
                        width=10,
                        state='readonly',
                        textvariable=var_total)
texto_total.grid(row=1, column=5)

#Botones

botones = ['total', 'recibo','guardar','resetear']
botones_creados = []
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                    text=boton.title(),
                    font=('Nunito Sans',14,'bold'),
                    fg='#DAB9FF',
                    bg='#8445F5',
                    bd=2,
                    width=9)
    botones_creados.append(boton)

    boton.grid(row=0,
                column=columnas)
    columnas+=1
botones_creados[0].config(command = total)
botones_creados[1].config(command = recibo)
botones_creados[2].config(command = guardar)
botones_creados[3].config(command = resetear)
#Area de recibo
text_recibo = Text(panel_recibo,
                    font=('Nunito Sans',12,'bold'),
                    bd=1,
                    width=42,
                    height=15)
text_recibo.grid(row=0,
                column=0)

#Calculadora
visor_calc = Entry(panel_calculadora,
                    font=('Nunito Sans',16,'bold'),
                    width=32,
                    bd=2)
visor_calc.grid(row=0,column=0, columnspan=5)

botones_calculadora = ['7','8','9','+',
                        '4','5','6','-'
                        ,'1','2','3','x'
                        ,'=','Borrar','0','/']
botones_guardados = []
fila= 1
columna= 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                    text=boton.title(),
                    font=('Nunito Sans',16,'bold'),
                    fg='#DAB9FF',
                    bg='#8445F5',
                    bd=2,
                    width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila,
                column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0
botones_guardados[0].config(command=lambda : click_button('7'))
botones_guardados[1].config(command=lambda : click_button('8'))
botones_guardados[2].config(command=lambda : click_button('9'))
botones_guardados[3].config(command=lambda : click_button('+'))
botones_guardados[4].config(command=lambda : click_button('4'))
botones_guardados[5].config(command=lambda : click_button('5'))
botones_guardados[6].config(command=lambda : click_button('6'))
botones_guardados[7].config(command=lambda : click_button('-'))
botones_guardados[8].config(command=lambda : click_button('1'))
botones_guardados[9].config(command=lambda : click_button('2'))
botones_guardados[10].config(command=lambda : click_button('3'))
botones_guardados[11].config(command=lambda : click_button('*'))
botones_guardados[12].config(command=resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_button('0'))
botones_guardados[15].config(command=lambda : click_button('/'))
#Evitar que la patalla se cierre
app.mainloop()
