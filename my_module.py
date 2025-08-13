#
'''
pi = 3.14

def summa(a:int, b:float) -> int:
    
    эта функция 
    делает a + b
    
    return a + b


#print("привет из модуля")
if __name__ == '__main__':
    print('самостоятельный запуск')
else:
    print(__name__, 'был импортирован')
'''
import tkinter as tk
from tkinter import messagebox


        
def study_entry():
    window = tk.Toplevel()
    window.title("Поля ввода")
    window.geometry("300x200")
    
    tk.Label(window, text="Имя:").pack(pady=5)
    entry1 = tk.Entry(window)
    entry1.pack(pady=5)
  
    tk.Label(window, text="Пароль:").pack(pady=5)
    entry2 = tk.Entry(window, show="*")
    entry2.pack(pady=5)
    def show_values():
        messagebox.showinfo("Результат", f"Имя: {entry1.get()}\nПароль: {entry2.get()}")
    tk.Button(window, text="Показать", command=show_values).pack(pady=10)
    
 
    
