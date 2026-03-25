import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from PIL import ImageDraw, ImageFont


class WaterMark:
    def __init__(self, root):
        self.root = root
        self.root.title("WaterMark Image App")
        self.root.geometry("600x500")

        self.original_image = None
        self.processed_image = None
        self.file_path = None
        self.tk_preview = None

        self.setup_ui()


    def setup_ui(self):
        self.preview_label = tk.Label(self.root, text="No Image Selected", height=20, width=60, bg="green")
        self.preview_label.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        self.upload_btn = tk.Button(button_frame, text="Upload Image", command=self.upload_image, width=15)
        self.upload_btn.grid(row=0, column=0, padx=10)

        self.watermark_btn = tk.Button(button_frame, text="Add Watermark", command=self.apply_watermark, width=15,
                                       state=tk.DISABLED)
        self.watermark_btn.grid(row=0, column=1, padx=10)

    def apply_watermark(self):
        if self.original_image:
            img = self.original_image.copy().convert("RGBA")
            draw = ImageDraw.Draw(img)

            text = "Watermark"
            try:
                font = ImageFont.truetype("arial.ttf", 40)
            except:
                font = ImageFont.load_default()

            width, height = img.size
            x, y = width - 250, height - 80

            draw.text(
                (x, y),
                text,
                fill=(255, 255, 255, 255),
                font=font,
                stroke_width=2,
                stroke_fill=(0, 0, 0, 255)
            )

            self.processed_image = img.convert("RGB")
            preview_copy = self.processed_image.copy()
            preview_copy.thumbnail((400, 400))
            self.tk_preview = ImageTk.PhotoImage(preview_copy)
            self.preview_label.config(image=self.tk_preview)



    def upload_image(self):
        file_types = [("Image files", "*.png;*.jpg;*.jpeg")]

        self.file_path = filedialog.askopenfilename(filetypes=file_types)

        if self.file_path:
            self.original_image = Image.open(self.file_path)
            preview_image = self.original_image.copy()
            preview_image.thumbnail((400, 400))

            self.tk_preview = ImageTk.PhotoImage(preview_image)
            self.preview_label.config(image=self.tk_preview, text="")

            self.watermark_btn.config(state=tk.NORMAL)
            messagebox.showinfo("Success", "Image Uploaded Successfully")
        else:
            messagebox.showerror("Something went wrong. File not uploaded")



