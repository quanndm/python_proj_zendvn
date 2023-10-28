import tkinter as tk
from speedtest import Speedtest
import threading


def run_test(check_button: tk.Button, download_result: tk.Label, upload_result: tk.Label):
    check_button.config(
        text="Checking...",
        state=tk.DISABLED
    )

    def run():
        speed_test = Speedtest()
        speed_test.get_best_server()

        download_speed = speed_test.download() / 1024 / 1024
        upload_speed = speed_test.upload() / 1024 / 1024

        download_result.config(text=f"{download_speed:.2f} Mbps")
        upload_result.config(text=f"{upload_speed:.2f} Mbps")

        check_button.config(state=tk.ACTIVE, text="Check")

    thread = threading.Thread(target=run)
    thread.start()


root = tk.Tk()

root.title("Speed Test")
root.config(
    bg="green"
)

window_width = 400
window_height = 450
x_position =  (root.winfo_screenwidth() - window_width) // 2
y_position = (root.winfo_screenheight() - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

frame = tk.Frame(root, bg="green")
frame.pack(padx=50, pady=50)

label_style = {"font": ("Arial", 14),
               "bg": "green",
               "fg": "white",
               "width": 40,
               "height": 2,
               "highlightthickness": 1}

button_style = {"font": ("Arial", 14),
                "bg": "white",
                "fg": "green",
                "width": 40,
                "height": 2}

download_label = tk.Label(
    frame,
    text="Download speed: ",
    **label_style
)
download_label.pack(pady=7)

download_result = tk.Label(
    frame,
    text="0 Mbps",
    **label_style
)
download_result.pack(pady=7)

upload_label = tk.Label(
    frame,
    text="Upload speed: ",
    **label_style
)
upload_label.pack(pady=7)

upload_result = tk.Label(
    frame,
    text="0 Mbps",
    **label_style
)
upload_result.pack(pady=7)

check_button = tk.Button(
    frame,
    text="Check",
    command=lambda: run_test(check_button, download_result, upload_result),
    **button_style
)
check_button.pack(pady=7)


copyright_label = tk.Label(
    root,
    text="quanndm",
    font=("Arial", 8),
    bg="green",
    fg="white",
    width=40,
    height=2
)
copyright_label.pack(pady=7)

root.mainloop()
