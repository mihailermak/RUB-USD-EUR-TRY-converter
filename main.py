from currency_converter import CurrencyConverter
from tkinter import *

#обозначаем Tkinter за window 
window = Tk()

#обозначаем CurrencyConverter за converter
converter = CurrencyConverter

#задаем заголовок окна
window.title('RUB-USD-EUR-TRY-converter')

#задаем размеры окна
window.geometry('400x300')

#фиксируем значения размера окна
window.resizable(width=False, height=False)

#добавляем цвет фона
window['bg'] = 'white'

