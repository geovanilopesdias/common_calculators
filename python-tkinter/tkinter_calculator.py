import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#Root window configuration
root.title('Gheowin Calculator')
style = ttk.Style()
root.geometry('300x270')  # configura dimensões e posicionamento
root.resizable(False, False)  # torna a janela impossível de redimensionar
display_padding = 10

# Grid configuration: 4 columns x 7 rows:
calc_label = ttk.Label(root,
                        text='Basic Calculator',
                        font=("Courier", 12))
calc_label.grid(column=0, row = 0, columnspan=4, padx=display_padding, pady=display_padding)

calc_display = tk.Text(root, height="1", width="12", font=("Courier", 16), state='disabled')
calc_display.tag_configure("right", justify='right')
calc_display.grid(column=0, row = 1, columnspan=3, sticky='EW', padx=display_padding, pady=display_padding)

# Global variables
decimal_precision = 6
display_content = "0"
display_memory = float()
last_input = float()
last_operation = str()
next_operation = str()
is_first_operation = True
calc_display.insert(1.0, "0.0")
calc_display['state'] = 'disabled'


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


def prepare_display():
    global display_content
    global display_memory
    
    display_content = "0"
    calc_display.delete(1.0, "end")
    calc_display.insert(1.0, str(round(display_memory, decimal_precision)))
    calc_display['state'] = 'disabled'


def clear_display():
    global display_content
    global display_memory
    global is_first_operation

    calc_display['state'] = 'normal'
    display_memory = 0
    last_input = 0
    last_operation = str()
    is_first_operation = True
    display_content = "0"
    calc_display.delete(1.0, "end")
    calc_display.insert(1.0, display_content)
    calc_display['state'] = 'disabled'


def begin_calculation_for(operation):
    global display_content
    global display_memory
    global is_first_operation
    global last_operation

    calc_display['state'] = 'normal'
    last_operation = operation
    display_memory = float(display_content)
    is_first_operation = False
    display_content = "0"
    calc_display.delete(1.0, "end")
    calc_display.insert(1.0, str(round(display_memory, decimal_precision)))
    calc_display['state'] = 'disabled'


def finish_calculation_to_begin(next_operation):
    global last_operation
    global display_content

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

    last_operation = next_operation

    if next_operation in ("+", "-"):
        display_content = "0"
    else:
        display_content = "1"
    

def show_not_allowed_operation_msg():
    calc_display['state'] = 'normal'
    calc_display.delete(1.0, "end")
    calc_display.insert(1.0, "Not allowed")
    calc_display['state'] = 'disabled'


def sum_up():
    global display_content
    global display_memory
    global is_first_operation
    global last_operation
    global last_input

    if is_first_operation:
        begin_calculation_for("+")

    else:
        if last_operation != "+":
            finish_calculation_to_begin("+")

        calc_display['state'] = 'normal'
        last_operation = "+"
        last_input = float(display_content)
        display_memory += float(display_content)
        prepare_display()


def subtract():
    global display_content
    global display_memory
    global is_first_operation
    global last_operation
    global last_input

    if is_first_operation:
        begin_calculation_for("-")
        
    else:
        if last_operation != "-":
            finish_calculation_to_begin("-")

        calc_display['state'] = 'normal'
        last_operation = "-"
        last_input = float(display_content)
        display_memory -= float(display_content)
        prepare_display()


def multiply():
    global display_content
    global display_memory
    global is_first_operation
    global last_operation
    global last_input

    if is_first_operation:
        begin_calculation_for("*")

    else:
        if last_operation != "*":
            finish_calculation_to_begin("*")
                        
        calc_display['state'] = 'normal'
        last_operation = "*"
        last_input = float(display_content)
        display_memory *= float(display_content)
        prepare_display()


def divide():
    global display_content
    global display_memory
    global is_first_operation
    global last_operation
    global last_input

    if is_first_operation:
        begin_calculation_for("/")

    else:
        if last_operation != "/":
            finish_calculation_to_begin("/")
                        
        try:
            calc_display['state'] = 'normal'            
            last_operation = "/"
            last_input = float(display_content)
            display_memory /= float(display_content)
            prepare_display()
        except ZeroDivisionError:
            show_not_allowed_operation_msg()


def percentage():
    global display_content
    global display_memory
    global last_operation

    calc_display['state'] = 'normal'
    if last_operation == "+":
        display_memory *= (1+float(display_content)/100)
    elif last_operation == "-":
        display_memory *= (1-float(display_content)/100)
    else:
        pass
    
    prepare_display()


def square_root():
    from math import sqrt
    global display_content
    global display_memory
    global is_first_operation

    if display_memory < 0:    
        show_not_allowed_operation_msg()

    if is_first_operation:
        display_memory = sqrt(float(display_content))
        is_first_operation = False
    else:
        display_memory = sqrt(display_memory)

    calc_display['state'] = 'normal'
    prepare_display()


def alter_sign():
    global display_content
    global display_memory
    global is_first_operation

    calc_display['state'] = 'normal'

    if is_first_operation:
        display_memory = (-1)*float(display_content)
        is_first_operation = False
    else:
        display_memory *= (-1)
        
    calc_display.delete(1.0, "end")
    calc_display.insert(1.0, str(round(display_memory, decimal_precision)))
    calc_display['state'] = 'disabled'


def iterate_last_operation():
    global display_content
    global display_memory
    global last_input
    global is_first_operation
    
    if last_input != 0 and not is_first_operation:
        try:
            calc_display['state'] = 'normal'
            if last_operation == "+":
                display_memory += last_input
            elif last_operation == "-":
                display_memory -= last_input
            elif last_operation == "*":
                display_memory *= last_input
            elif last_operation == "/":
                display_memory /= last_input

            prepare_display()

        except ZeroDivisionError:
            show_not_allowed_operation_msg()


def show_result():
    finish_calculation_to_begin(last_operation)
    


# Construção dos botões:
num_btn_cfg = {'bg': 'white', 'width': 4}
ope_btn_cfg = {'bg': 'blue', 'fg': 'white', 'width': 4}

zer_btn = tk.Button(root, text='0', command=lambda: set_display(0), **num_btn_cfg)
zer_btn.grid(column=1, row=6)

one_btn = tk.Button(root, text='1', command=lambda: set_display(1), **num_btn_cfg)
one_btn.grid(column=0, row=5)

two_btn = tk.Button(root, text='2', command=lambda: set_display(2), **num_btn_cfg)
two_btn.grid(column=1, row=5)

two_btn = tk.Button(root, text='3', command=lambda: set_display(3), **num_btn_cfg)
two_btn.grid(column=2, row=5)

fou_btn = tk.Button(root, text='4', command=lambda: set_display(4), **num_btn_cfg)
fou_btn.grid(column=0, row=4)

fiv_btn = tk.Button(root, text='5', command=lambda: set_display(5), **num_btn_cfg)
fiv_btn.grid(column=1, row=4)

six_btn = tk.Button(root, text='6', command=lambda: set_display(6), **num_btn_cfg)
six_btn.grid(column=2, row=4)

sev_btn = tk.Button(root, text='7', command=lambda: set_display(7), **num_btn_cfg)
sev_btn.grid(column=0, row=3)

eig_btn = tk.Button(root, text='8', command=lambda: set_display(8), **num_btn_cfg)
eig_btn.grid(column=1, row=3)

nin_btn = tk.Button(root, text='9', command=lambda: set_display(9), **num_btn_cfg)
nin_btn.grid(column=2, row=3)

dot_btn = tk.Button(root, text='.', command=lambda: set_display("."), **num_btn_cfg)
dot_btn.grid(column=0, row=6)

plu_btn = tk.Button(root, text='+', command=sum_up, **ope_btn_cfg)
plu_btn.grid(column=3, row=2)

min_btn = tk.Button(root, text='-', command=subtract, **ope_btn_cfg)
min_btn.grid(column=3, row=3)

mul_btn = tk.Button(root, text='x', command=multiply, **ope_btn_cfg)
mul_btn.grid(column=3, row=4)

div_btn = tk.Button(root, text='\u00F7', command=divide, **ope_btn_cfg)
div_btn.grid(column=3, row=5)

per_btn = tk.Button(root, text='%', command=percentage, **ope_btn_cfg)
per_btn.grid(column=1, row=2)

sqr_btn = tk.Button(root, text='\u221A', command=square_root, **ope_btn_cfg)
sqr_btn.grid(column=2, row=2)

sgn_btn = tk.Button(root, text='+/\u23BC', command=alter_sign, bg='grey', fg = '#ffffff', width=4)
sgn_btn.grid(column=2, row=6)

ans_btn = tk.Button(root, text='=', command=show_result, bg='black', fg = '#ffffff', width=4)
ans_btn.grid(column=3, row=6)

ite_btn = tk.Button(root, text='\u2B6F', command=iterate_last_operation, bg='yellow', width=4)
ite_btn.grid(column=3, row=1)

cle_btn = tk.Button(root, text='C', command=clear_display, bg='#800000', fg = '#ffffff', width=4)
cle_btn.grid(column=0, row=2)


root.mainloop()
