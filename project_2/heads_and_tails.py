from enum import Enum
import random
import tkinter as tk
from PIL import Image, ImageTk
import time

FlipSelection = Enum('FlipSelection', ["HEAD", "TAIL"])


def get_photo(url: str, resize: tuple[int, int]) -> ImageTk.PhotoImage:
    image = Image.open(url)
    image = image.resize(resize, Image.LANCZOS)
    return ImageTk.PhotoImage(image)


def show_photo(photo: ImageTk.PhotoImage, time_sleep: float):
    image_label.config(image=photo)
    root.update()

    time.sleep(time_sleep)


def shake_animation(time_shake: int | float, head_photo: ImageTk.PhotoImage, tail_photo: ImageTk.PhotoImage):
    time_start = time.time()

    while time.time() - time_start < time_shake:
        show_photo(head_photo, 0.15)
        show_photo(tail_photo, 0.15)


def flip_coin(choice: type[FlipSelection], head_photo: ImageTk.PhotoImage, tail_photo: ImageTk.PhotoImage):
    head_button.config(state=tk.DISABLED)
    tail_button.config(state=tk.DISABLED)

    result_label.config(text="Flipping...")
    shake_animation(2, head_photo, tail_photo)

    random_choice = random.choice(list(FlipSelection))
    result_photo = head_photo if random_choice == FlipSelection.HEAD else tail_photo
    result_string = "You win!" if choice == random_choice else "You lose!"

    result_label.config(text=result_string)
    image_label.config(image=result_photo)

    head_button.config(state=tk.ACTIVE)
    tail_button.config(state=tk.ACTIVE)


root = tk.Tk()
root.title("Heads and Tails")

window_width = 400
window_height = 480
x_position = (root.winfo_screenwidth() - window_width) // 2
y_position = (root.winfo_screenheight() - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


result_label = tk.Label(root, text="Choose head or tail",
                        font=("Helvetica", 18, "bold"))
result_label.pack(pady=20)

head_photo = get_photo("images/head.png", (250, 250))
tail_photo = get_photo("images/tail.png", (250, 250))

image_label = tk.Label(root, image=head_photo)
image_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

button_style = {"font": ("Helvetica", 18, "bold"), "bg": "#cfcfcf"}

head_button = tk.Button(button_frame, text="Head", **button_style)
head_button.pack(side=tk.LEFT, padx=10)

tail_button = tk.Button(button_frame, text="Tail", **button_style)
tail_button.pack(side=tk.RIGHT, padx=10)


head_button.config(command=lambda: flip_coin(
    FlipSelection.HEAD, head_photo, tail_photo))
tail_button.config(command=lambda: flip_coin(
    FlipSelection.TAIL,  head_photo, tail_photo))
copyright_label = tk.Label(
    root,
    text="quanndm",
    font=("Arial", 12),
    fg="black",
    width=40,
    height=2
)
copyright_label.pack(pady=7)

root.mainloop()
