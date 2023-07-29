from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage

window = Tk(className="Rachel Ai")
RESPONSE = "RESPONSE:"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("images")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def gui(arg):
    global window

    window.geometry("784x650")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 650,
        width = 784,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        784.0,
        650.0,
        fill="#00FFD1",
        outline="")

    # Load the image and store it in a global variable
    image_image_1 = PhotoImage(file=relative_to_assets("icon.png"))
    canvas.image = image_image_1

    canvas.create_image(
    392.0,
    345.0,
    image=image_image_1
    )

    canvas.create_text(
    238.0,
    39.0,
    anchor="nw",
    text="Rachel Ai",
    fill="#0084FF",
    font=("MontserratRoman SemiBold", 64 * -1)
)

    canvas.create_text(
        142.0,
        516.0,
        anchor="nw",
        text=RESPONSE,
        fill="#000000",
        font=("MontserratRoman SemiBold",16 * -1)
    )
    window.resizable(False, False)


gui(22)
window.mainloop()
