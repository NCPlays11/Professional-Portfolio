import tkinter as tk
from tkinter import messagebox
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sample_text = (
            "The quick brown fox jumps over the lazy dog. "
            "Typing fast requires practice and focus. "
            "Measure your typing speed with this test."
        )

        self.create_widgets()

        self.start_time = None
        self.is_typing_started = False

    def create_widgets(self):
        self.label = tk.Label(
            self.root,
            text="Type the text below as fast as you can:",
            font=("Helvetica", 14),
        )
        self.label.pack(pady=10)

        self.sample_text_label = tk.Label(
            self.root,
            text=self.sample_text,
            wraplength=500,
            font=("Helvetica", 12),
            justify="left",
        )
        self.sample_text_label.pack(pady=10)

        self.text_area = tk.Text(self.root, height=10, width=60, font=("Helvetica", 12))
        self.text_area.bind('<Control-v>', lambda _:'break')
        self.text_area.bind('<Control-c>', lambda _:'break')
        self.text_area.pack(pady=10)

        self.submit_button = tk.Button(
            self.root, text="Submit", command=self.calculate_speed
        )
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.text_area.bind("<KeyPress>", self.start_typing)

    def start_typing(self, event):
        if not self.is_typing_started:
            self.start_time = time.time()
            self.is_typing_started = True

    def calculate_speed(self):
        end_time = time.time()

        typed_text = self.text_area.get("1.0", "end-1c")

        time_taken = end_time - self.start_time

        typed_words = typed_text.split()
        sample_words = self.sample_text.split()

        correct_words = 0
        for i in range(min(len(typed_words), len(sample_words))):
            if typed_words[i] == sample_words[i]:
                correct_words += 1

        wpm = (correct_words / time_taken) * 60

        result_message = f"Typing Speed: {wpm:.2f} WPM\nCorrect Words: {correct_words}/{len(sample_words)}"
        self.result_label.config(text=result_message)

        messagebox.showinfo("Typing Test Results", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()