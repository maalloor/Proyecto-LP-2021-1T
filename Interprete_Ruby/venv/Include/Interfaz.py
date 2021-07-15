import tkinter as tk
import random as rd
from lexer import lex_analyzer
from verificator import verificator
from parser import *

#Manuel: Métodos auxiliares
def evaluation(input, output):
    index = rd.randint(1, 3)
    with open(f'./prueba/prueba{index}.txt', encoding='utf-8') as file:
        ejemplo = ''.join(file.readlines())
        input.delete('1.0', tk.END)
        input.insert(1.0, ejemplo)
        output.config(state = tk.NORMAL)
        output.delete('1.0', tk.END)
        output.insert(1.0, "En este cuadro visualizará el resultado de su análisis.")
        output.config(state = tk.DISABLED)

def verificator_lex():
    text = coding_input.get("1.0", "end-1c")
    output = lex_analyzer(text)
    text_error(output, "Léxico")

def verificator_yacc():
    text = coding_input.get("1.0", "end-1c")
    output = yacc_analyzer(text)
    error = output.data_yacc_error
    evaluation(error, "Sintáctico")

def text_error(output, type):
    coding_output.config(state = tk.NORMAL)
    coding_output.delete('1.0', tk.END)
    if output != '':
        coding_output.insert(1.0, output)
    else:
        coding_output.insert(1.0, f"No existen errores encontrados por el Analizador {type}")
    coding_output.config(state=tk.DISABLED)

#Aporte Manuel Loor
frame = tk.Tk()
frame.geometry("1200x700")
frame.title("Interpréte de Ruby")
frame.resizable(True, True)
frame.config(bg="#000")

title = tk.Label(frame, text='INTÉRPRETE DE RUBY', font="Roboto 30", fg='#2CE8FF', bg="#000",compound=tk.RIGHT)
title.place(x=50, y=20)

background_input_area = tk.Canvas(frame, width=472, height=380, bg="#000", highlightthickness=0)
background_input = tk.PhotoImage(file="./Fondo-azul.png")
background_input_area.create_image(245, 245, image=background_input)
coding_input = tk.Text(frame, height=20, width=55, bg="#FFF", fg="#000", highlightthickness=0, relief='ridge', wrap="word")
coding_input.insert(2.0, 'Ingrese en este casillero el código a analizar')
background_input_area.place(x=600, y=130)
coding_input.place(x=615, y=160)

background_output_area = tk.Canvas(frame, width=472, height=380, bg="#000", highlightthickness=0)
background_output_area.place(x=60, y=130)
background_output = tk.PhotoImage(file="./Fondo-azul.png")
background_output_area.create_image(245, 245, image=background_output)
coding_output = tk.Text(frame, height=20, width=55, bg="#FFF", fg="#000", highlightthickness=0, relief='ridge', wrap="word")
coding_output.insert(2.0, "-> Resultados del análisis realizado")
coding_output.config(state="disabled")
coding_output.place(x=75, y=160)
open_file = tk.Button(frame, text="Abrir Archivo", bg='#FFF', fg='black', padx=10, pady=2, command=lambda: evaluation(coding_input,  coding_output))
lexer = tk.Button(frame, text="Analizador Léxico", bg='#FFF', fg='black', compound=tk.LEFT, padx=10, pady=10, command=verificator_lex)
parser = tk.Button(frame, text="Analizador Sintáctico", bg='#FFF', fg='black', compound=tk.LEFT, padx=10, pady=10, command=verificator_yacc)
open_file.place(x=790, y=550)
lexer.place(x=110, y=550)
parser.place(x=350, y=550)
frame.mainloop()
