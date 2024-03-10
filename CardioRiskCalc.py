import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

def calculate_points_SA(SA):
    if SA <= 19:
        return 1
    elif SA <= 3:
        return 2
    else:
        return 3

def calculate_points_IAAK(IAAK):
    if IAAK < 2:
        return 1
    elif IAAK <= 5:
        return 2
    else:
        return 3

def calculate_points_VT(VT):
    if VT <= 8:
        return 1
    elif VT <= 10:
        return 2
    else:
        return 3

def calculate_points_FG(FG):
    if FG == "2С19*17":
        return 1
    elif FG == "2С19*1":
        return 2
    else:
        return 3

def calculate_points_IAADF5(IAADF5):
    if IAADF5 < 15:
        return 1
    elif IAADF5 <= 60:
        return 2
    else:
        return 3

def calculate_risk():
    try:
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
        result_display.config(state=tk.NORMAL)
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, result_text)
        result_display.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите числовые значения в поля для ввода")

root = tk.Tk()
root.title("CardioRiskCalc")
# root.iconbitmap("ico.ico")
# Получаем размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Задаем размеры и координаты для окна программы
window_width = 630
window_height = 480
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Устанавливаем размеры и координаты
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font="Arial 12", foreground="#383838")
style.configure('TEntry', font="Arial 12")
style.configure('TButton', font="Arial 12", background="#0078D7", foreground="#ffffff")
style.configure('TCombobox', font="Arial 12")
style.map('TButton', background=[('active', '#0053a6')])

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(row=0, column=0, sticky="nsew")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

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
combo_FG.set("2С19*17")

ttk.Label(mainframe, text="ИАадф5 (агрегация с АДФ 50 мкмоль) в %:").grid(row=4, column=0, sticky="w")
entry_IAADF5 = ttk.Entry(mainframe)
entry_IAADF5.grid(row=4, column=1, sticky="ew")

calculate_btn = ttk.Button(mainframe, text='Рассчитать', command=calculate_risk)
calculate_btn.grid(row=5, column=0, columnspan=2, pady=10)

result_display = ScrolledText(mainframe, wrap=tk.WORD, height=14, font="Arial 10")
result_display.grid(row=7, column=0, columnspan=2, sticky="nsew", pady=10)
result_display.config(state=tk.DISABLED)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
