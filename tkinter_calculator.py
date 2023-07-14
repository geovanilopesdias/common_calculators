import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#Root window configuration
root.title('Gheowin Calculator')
root.geometry('350x250')  # configura dimensões e posicionamento
root.resizable(False, False)  # torna a janela impossível de redimensionar
display_padding = 10
display_style = ttk.Style(root)
display_style.configure('Display.TEntry', background='#90EE90')


# Grid configuration: 4 columns x 7 rows:
calc_label = ttk.Label(root,
                        text='Basic Calculator',
                        font=("Courier", 12))
calc_label.grid(column=0, row = 0, columnspan=4)

calc_display = tk.Text(root, height="1", width="16", font=("Courier", 20), state='disabled')
calc_display.tag_configure("right", justify='right')
calc_display.grid(column=0, row = 1, columnspan=4, sticky='EW', padx=display_padding, pady=display_padding)

# Global variables
display_content = "0"
display_memory = float()
last_operation = str()
is_first_digit = True


# Definição das funções:
def set_display(value):
    global display_content
    calc_display['state'] = 'normal'
    if display_content == "0" and value != "0":
        display_content = str(value)
        calc_display.delete(1.0, "end")
        calc_display.insert(1.0, display_content)
        calc_display['state'] = 'disabled'
    else:
        display_content += str(value)
        calc_display.delete(1.0, "end")
        calc_display.insert(1.0, display_content)
        calc_display['state'] = 'disabled'


def display_clear():
    global display_content
    global display_memory
    global is_first_digit

    calc_display['state'] = 'normal'
    display_content = "0"
    display_memory = 0
    is_first_digit = True
    calc_display.delete(1.0, "end")
    calc_display.insert(1.0, display_content)
    calc_display['state'] = 'disabled'


def begin_calculation_for(operation):
    global display_content
    global display_memory
    global is_first_digit
    global last_operation

    calc_display['state'] = 'normal'
    last_operation = operation
    display_memory = float(display_content)
    is_first_digit = False
    display_content = ""
    calc_display.delete(1.0, "end")
    calc_display.insert(1.0, str(display_memory))
    calc_display['state'] = 'disabled'
    

def sum_up():
    global display_content
    global display_memory
    global is_first_digit
    global last_operation

    if is_first_digit:
        begin_calculation_for("+")

    else:
        calc_display['state'] = 'normal'
        last_operation = "+"
        display_memory += float(display_content)
        display_content = ""
        calc_display.delete(1.0, "end")
        calc_display.insert(1.0, str(display_memory))
        calc_display['state'] = 'disabled'


def subtract():
    global display_content
    global display_memory
    global is_first_digit
    global last_operation

    if is_first_digit:
        begin_calculation_for("-")

    else:
        calc_display['state'] = 'normal'
        last_operation = "-"
        display_memory -= float(display_content)
        display_content = ""
        calc_display.delete(1.0, "end")
        calc_display.insert(1.0, str(display_memory))
        calc_display['state'] = 'disabled'


def multiply():
    global display_content
    global display_memory
    global is_first_digit
    global last_operation

    if is_first_digit:
        begin_calculation_for("*")

    else:
        calc_display['state'] = 'normal'
        last_operation = "*"
        display_memory *= float(display_content)
        display_content = ""
        calc_display.delete(1.0, "end")
        calc_display.insert(1.0, str(display_memory))
        calc_display['state'] = 'disabled'


def divide():
    global display_content
    global display_memory
    global is_first_digit
    global last_operation

    if is_first_digit:
        begin_calculation_for("/")

    else:
        calc_display['state'] = 'normal'
        last_operation = "/"
        display_memory /= float(display_content)
        display_content = ""
        calc_display.delete(1.0, "end")
        calc_display.insert(1.0, str(display_memory))
        calc_display['state'] = 'disabled'


def show_result():
    global is_first_digit
    global last_operation

    calc_display['state'] = 'normal'
    if last_operation == "+":
        sum_up()
        
    elif last_operation == "-":
        subtract()
        
    elif last_operation == "*":
        multiply()
        
    elif last_operation == "/":
        divide()
        
    else:
        pass

    is_first_digit = True
    last_operation = ""
    calc_display['state'] = 'disabled'


# Construção dos botões:
zer_btn = ttk.Button(root, text='0', command=lambda: set_display(0))
zer_btn.grid(column=1, row=6)

one_btn = ttk.Button(root, text='1', command=lambda: set_display(1))
one_btn.grid(column=0, row=5)

two_btn = ttk.Button(root, text='2', command=lambda: set_display(2))
two_btn.grid(column=1, row=5)

two_btn = ttk.Button(root, text='3', command=lambda: set_display(3))
two_btn.grid(column=2, row=5)

fou_btn = ttk.Button(root, text='4', command=lambda: set_display(4))
fou_btn.grid(column=0, row=4)

fiv_btn = ttk.Button(root, text='5', command=lambda: set_display(5))
fiv_btn.grid(column=1, row=4)

six_btn = ttk.Button(root, text='6', command=lambda: set_display(6))
six_btn.grid(column=2, row=4)

sev_btn = ttk.Button(root, text='7', command=lambda: set_display(7))
sev_btn.grid(column=0, row=3)

eig_btn = ttk.Button(root, text='8', command=lambda: set_display(8))
eig_btn.grid(column=1, row=3)

nin_btn = ttk.Button(root, text='9', command=lambda: set_display(9))
nin_btn.grid(column=2, row=3)

dot_btn = ttk.Button(root, text='.', command=lambda: set_display("."))
dot_btn.grid(column=0, row=6)

plu_btn = ttk.Button(root, text='+', command=sum_up)
plu_btn.grid(column=3, row=2)

min_btn = ttk.Button(root, text='-', command=subtract)
min_btn.grid(column=3, row=3)

mul_btn = ttk.Button(root, text='x', command=multiply)
mul_btn.grid(column=3, row=4)

div_btn = ttk.Button(root, text='/', command=divide)
div_btn.grid(column=3, row=5)

ans_btn = ttk.Button(root, text='=', command=show_result)
ans_btn.grid(column=3, row=6)

cle_btn = ttk.Button(root, text='C', command=display_clear)
cle_btn.grid(column=0, row=2)


root.mainloop()
