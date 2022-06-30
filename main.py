from tkinter import *
from utils.wrapper import Wrapper

if __name__ == '__main__':
    window = Tk()
    app = Wrapper(window)
    app.create_ui()

    window.mainloop()