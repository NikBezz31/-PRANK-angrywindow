import tkinter as tk
import random
import threading
import keyboard  # pip install keyboard
import time

root = tk.Tk()
root.title("Безумное окно")
root.geometry("300x200+500+300")

magnitude = 15  # амплитуда тряски
chase_speed = 5  # скорость гонки за мышкой

def shake_window():
    """Постоянная тряска окна"""
    x = root.winfo_x()
    y = root.winfo_y()
    offset_x = random.randint(-magnitude, magnitude)
    offset_y = random.randint(-magnitude, magnitude)
    root.geometry(f"+{x + offset_x}+{y + offset_y}")
    root.after(10, shake_window)

def runaway_close():
    """Убегаем от крестика"""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    new_x = random.randint(0, screen_width - 300)
    new_y = random.randint(0, screen_height - 200)
    root.geometry(f"+{new_x}+{new_y}")

def mouse_hover(event):
    """Телепорт при наведении мыши"""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    new_x = random.randint(0, screen_width - 300)
    new_y = random.randint(0, screen_height - 200)
    root.geometry(f"+{new_x}+{new_y}")

def chase_mouse():
    """Гонка за курсором"""
    while True:
        try:
            mx, my = root.winfo_pointerxy()
            x = root.winfo_x()
            y = root.winfo_y()
            # сдвигаем окно ближе к курсору
            dx = chase_speed if mx > x else -chase_speed
            dy = chase_speed if my > y else -chase_speed
            root.geometry(f"+{x + dx}+{y + dy}")
            time.sleep(0.01)
        except tk.TclError:
            break  # окно закрылось

def listen_alt_f4():
    """Закрытие только через Alt+F4"""
    keyboard.wait('alt+f4')
    root.destroy()

# Запускаем функции
shake_window()
root.protocol("WM_DELETE_WINDOW", runaway_close)
root.bind("<Enter>", mouse_hover)

threading.Thread(target=chase_mouse, daemon=True).start()
threading.Thread(target=listen_alt_f4, daemon=True).start()

root.mainloop()
