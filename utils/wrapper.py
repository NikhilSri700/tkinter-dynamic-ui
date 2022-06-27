from tkinter import *
import json
import os

current_directory = os.getcwd()
os.chdir('..')
current_directory = os.path.join(current_directory, 'config')
sample_ui = os.path.join(current_directory, 'config_ui.json')


def default_command_for_button():
    print("Button Pressed")


class Wrapper:
    def __init__(self, window):
        with open(sample_ui, "r") as config_file:
            self.config_data = json.load(config_file)
        self.window = window
        self.button = []
        self.textbox = []

    def create_ui(self):
        self.window.geometry('500x500')
        for key, data in self.config_data.items():
            if key == 'AppName':
                self.window.title(data)
            elif key == 'elements':
                row = 0
                for element in data:
                    if element['type'] == 'TextBox':
                        label = element['Label']
                        text_box = self._create_textbox(row, label)
                        self.textbox.append(text_box)
                    elif element['type'] == 'Button':
                        text = element['Text']
                        command = default_command_for_button if element['Command'] == "" else element['Command']
                        button = self._create_button(text, command)
                        button.grid(row=row, column=0)
                        self.button.append(button)
                    row += 1

    def _create_button(self, *args):
        return Button(self.window, text=args[0], command=args[1])

    def _create_textbox(self, *args):
        row = args[0]
        text = args[1]
        label = Label(self.window, text=text)
        label.grid(row=row, column=0)
        entry = Entry(self.window)
        entry.grid(row=row, column=1)
        return entry
