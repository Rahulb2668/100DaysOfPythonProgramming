import tkinter as tk
window = tk.Tk()
window.title("The most dangerous writing app")
window.geometry("800x600")
window.configure(bg="black")


timer_id = None

def start_timer(event):
    global timer_id

    if timer_id is not None:
        window.after_cancel(timer_id)
        
    timer_id = window.after(5000, clear_text)

def clear_text():
    text_area.delete("1.0", tk.END)

text_area = tk.Text(window, font=("Arial", 12), bg="black", fg="white", wrap="word")
text_area.pack(expand=True, fill="both")


text_area.bind("<KeyRelease>", start_timer)


window.mainloop()
