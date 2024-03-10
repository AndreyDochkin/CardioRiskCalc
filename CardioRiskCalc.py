import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from docx import Document
import os

def calculate_points_SA(SA):
    if SA <= 19: return 1
    elif SA <= 3: return 2
    else: return 3

def calculate_points_IAAK(IAAK):
    if IAAK < 2: return 1
    elif IAAK <= 5: return 2
    else: return 3

def calculate_points_VT(VT):
    if VT <= 8: return 1
    elif VT <= 10: return 2
    else: return 3

def calculate_points_FG(FG):
    if FG == "2С19*17": return 1
    elif FG == "2С19*1": return 2
    else: return 3

def calculate_points_IAADF5(IAADF5):
    if IAADF5 < 15: return 1
    elif IAADF5 <= 60: return 2
    else: return 3

def calculate_risk():
    SA = float(entry_SA.get())
    IAAK = float(entry_IAAK.get())
    VT = float(entry_VT.get())
    FG = combo_FG.get()
    IAADF5 = float(entry_IAADF5.get())
    
    points = 0
    points += calculate_points_SA(SA)
    points += calculate_points_IAAK(IAAK)
    points += calculate_points_VT(VT)
    points += calculate_points_FG(FG)
    points += calculate_points_IAADF5(IAADF5)
    
    Krs = points / 5
    
    result_text = f'Крс: {Krs:.1f}\n'
    
    if Krs < 2:
        recommendation = "Целевая гипоагрегация достигнута. Коррекция терапии не требуется. Риск повторных сосудистых событий низкий."
    elif Krs <= 2.8:
        recommendation = "Целевая гипоагрегация не достигнута! Требуется коррекция терапии. Рекомендован переход на ДАТТ с применением комбинации препаратов: Ацетилсалициловая кислота 75 мг + Тикагрелор 90 мг х 2 раза в день. Риск повторных сосудистых событий высокий."
    else:
        recommendation = "Целевая гипоагрегация не достигнута! Требуется срочная коррекция терапии. Рекомендован переход на ДАТТ с применением комбинации препаратов: Ацетилсалициловая кислота 75 мг + Тикагрелор 90 мг х 2 раза в день. Риск повторных сосудистых событий крайне высокий. Повторное исследование в динамике."
    
    result_text += recommendation
    result_display.config(state=tk.NORMAL)  # Разрешить редактирование текста
    result_display.delete(1.0, tk.END)  # Очистить существующий текст
    result_display.insert(tk.END, result_text)  # Вставить новый текст
    result_display.config(state=tk.DISABLED)  # Запретить редактирование текста

root = tk.Tk()
root.title("CardioRiskCalc")
root.geometry("640x480") # Немного увеличим размер окна для лучшего размещения элементов

# Определение и применение стилей для элементов интерфейса
style = ttk.Style()
style.theme_use('clam') # Использование темы 'clam' для более современного вида

# Определение цветовой схемы
style.configure('TLabel', padding=5, font="Arial 12", background="#f3f4f6", foreground="#383838")
style.configure('TEntry', padding=5, font="Arial 12", fieldbackground="#ffffff", foreground="#383838")
style.configure('TButton', padding=5, font="Arial 12", background="#0078D7", foreground="#ffffff")
style.configure('TCombobox', padding=5, font="Arial 12", fieldbackground="#ffffff", foreground="#383838")
style.map('TButton', background=[('active', '#0053a6')])

# Добавление отступов к главному окну для элементов
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky="nsew")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Элементы интерфейса...
ttk.Label(mainframe, text="Спонтанная агрегация (СА) в %:").grid(row=0, column=0, sticky="w")
entry_SA = ttk.Entry(mainframe)
entry_SA.grid(row=0, column=1, sticky="ew")

ttk.Label(mainframe, text="ИАак (арахидоновая кислота) в %:").grid(row=1, column=0, sticky="w")
entry_IAAK = ttk.Entry(mainframe)
entry_IAAK.grid(row=1, column=1, sticky="ew")

ttk.Label(mainframe, text="ВТ (средний размер тромбоцитов, фл/тромбоцит):").grid(row=2, column=0, sticky="w")
entry_VT = ttk.Entry(mainframe)
entry_VT.grid(row=2, column=1, sticky="ew")

ttk.Label(mainframe, text="ФГ (фармакогенетическое тестирование):").grid(row=3, column=0, sticky="w")
combo_FG = ttk.Combobox(mainframe, values=["2С19*17", "2С19*1", "2С19*2/2С19*3"], state="readonly")
combo_FG.grid(row=3, column=1, sticky="ew")
combo_FG.set("2С19*17") # Значение по умолчанию

ttk.Label(mainframe, text="ИАадф5 (агрегация с АДФ 50 мкмоль) в %:").grid(row=4, column=0, sticky="w")
entry_IAADF5 = ttk.Entry(mainframe)
entry_IAADF5.grid(row=4, column=1, sticky="ew")

calculate_btn = ttk.Button(mainframe, text='Рассчитать', command=calculate_risk)
calculate_btn.grid(row=5, column=0, columnspan=2, pady=10)

result_display = ScrolledText(mainframe, wrap=tk.WORD, height=10, font="Arial 10")
result_display.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=10)
result_display.config(state=tk.DISABLED)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5) # Добавляем отступы к элементам

root.mainloop()