from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage

window = Tk(className="Rachel Ai")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("images")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def gui(arg):
    global window

    window.geometry("400x400")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=400,
        width=400,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    canvas.create_rectangle(
        0.0,
        0.0,
        400.0,
        386.0,
        fill="#000000",
        outline=""
    )

    # Load the image and store it in a global variable
    image_image_1 = PhotoImage(file=relative_to_assets("icon.png"))
    canvas.image = image_image_1

    canvas.create_image(
        200.0,
        220.0,
        image=image_image_1
    )

    canvas.create_text(
        72.0,
        0.0,
        anchor="nw",
        text="Rachel Ai",
        fill="#0084FF",
        font=("MontserratRoman SemiBold", 64 * -1)
    )
    window.resizable(False, False)

