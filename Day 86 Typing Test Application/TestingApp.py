import tkinter as tk


class TestingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Test")
        self.root.geometry("600x500")

        self.score = 0
        self.time_left = 60
        self.running = False

        self.setup_ui()

    def setup_ui(self):
        self.score_label = tk.Label(
            self.root,
            text=f"Score (WPM): {self.score}",
            font=('Helvetica', 16, "bold")
        )
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(
            self.root,
            text=f"Time: {self.time_left}s",
            font=('Helvetica', 16, "bold")
        )
        self.timer_label.pack(pady=10)

        # Changed to self.text_box so we can read the input
        self.text_box = tk.Text(self.root, height=10, width=50, font=("Helvetica", 12))
        self.text_box.pack(pady=20)

        self.start_btn = tk.Button(self.root, text="Start Test", command=self.start_test)
        self.start_btn.pack(pady=20)

    def start_test(self):
        self.time_left = 60
        self.score = 0

        self.timer_label.config(text=f"Time: {self.time_left}s")
        self.score_label.config(text="Score (WPM): 0")
        self.text_box.delete("1.0", tk.END)
        self.text_box.focus_set()

        if not self.running:
            self.running = True
            self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.running = False
            self.calculate_score()

    def calculate_score(self):

        input_text = self.text_box.get("1.0", "end-1c")

        char_count = len(input_text)
        wpm = char_count / 5

        self.score_label.config(text=f"Score (WPM): {int(wpm)}")
        print(f"Total Characters: {char_count}")