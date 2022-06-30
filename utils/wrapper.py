from tkinter import *
import json
import os

current_directory = os.getcwd()
config_directory = os.path.join(current_directory, 'config')
script_directory = os.path.join(current_directory, 'scripts')

script = os.path.join(script_directory, 'run.py')
sample_ui = os.path.join(config_directory, 'config_ui.json')


def default_command_for_button(entries):
    parameters = " "
    entries_text = []
    for entry in entries:
        entries_text.append(f'"{entry.get()}"')
    result = parameters.join(entries_text)
    os.system(f'python "{script}" {result}')


class Wrapper:
    def __init__(self, window):
        with open(sample_ui, "r") as config_file:
            self.config_data = json.load(config_file)
        self.window = window
        self.primary_color = '#839CF0'
        self.secondary_color = '#FFE5C5'
        self.window['bg'] = self.primary_color
        self.button = []
        self.textbox = []
        self.frames = []
        self.label = []
        self.top_frame = Frame(self.window, width=1300, height=50, bg=self.primary_color)
        self.middle_frame = Frame(self.window, width=1300, height=600, bg=self.primary_color)
        self.bottom_frame = Frame(self.window, width=1300, height=50, bg=self.primary_color)

    def create_ui(self):
        self.window.geometry('1300x700+0+0')
        self._create_top()
        self.middle_frame.pack(pady=40)
        self.bottom_frame.pack(side=BOTTOM, pady=40)
        row = 1
        for key, data in self.config_data.items():
            if key == 'AppName':
                self.window.title(data)
            elif key == 'elements':
                for element in data:
                    if element['type'] == 'TextBox':
                        label = element['Label']
                        text_box = self._create_textbox(row, label)
                        self.textbox.append(text_box)
                    elif element['type'] == 'Button':
                        text = element['Text']
                        button = self._create_button(text)
                        button.pack(anchor='center')
                        self.button.append(button)
                    row += 2

    def _create_top(self):
        self.top_frame.pack(side=TOP, pady=20)
        label = Label(self.top_frame, font=('aria', 30, 'bold'), bg=self.primary_color, fg=self.secondary_color,
                      text="Sample Form", bd='10', anchor='center', padx=50)
        label.grid(row=0, column=0, padx=50)

    def _create_button(self, *args):
        return Button(self.bottom_frame, font=('aria', 20, 'bold'), width=10, bg='steel blue', fg='white', bd=6,
                      text=args[0], activebackground=self.secondary_color, activeforeground='steel blue',
                      command=lambda: default_command_for_button(self.textbox))

    def _create_label(self, *args):
        text = args[0]
        label = Label(self.window, text=text, bg=self.primary_color, font='bold')
        self.label.append(label)
        return label

    def _create_textbox(self, *args):
        row = args[0]
        text = args[1]
        label = Label(self.middle_frame, font=('aria', 16, 'bold'), fg='white', text=text, bg=self.primary_color,
                      bd=10, padx=30)
        label.grid(row=row, column=0, sticky='w')
        entry = Entry(self.middle_frame, font=('aria', 16, 'bold'), bg=self.secondary_color, bd=2, insertwidth=4,
                      fg='#6a6b00')
        entry.grid(row=row, column=1)
        return entry
