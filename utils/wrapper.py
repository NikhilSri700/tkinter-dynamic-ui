from tkinter import *
from tkinter import filedialog
import json
import os

current_directory = os.getcwd()
config_directory = os.path.join(current_directory, 'config')
script_directory = os.path.join(current_directory, 'scripts')

script = os.path.join(script_directory, 'run.py')
s3_config = os.path.join(config_directory, 's3_config_ui.json')
ec2_config = os.path.join(config_directory, 'ec2_config_ui.json')


def default_command_for_button(entries, file):
    parameters = " "
    entries_text = []
    for entry in entries:
        entries_text.append(f'"{entry.get()}"')
    result = parameters.join(entries_text)
    os.system(f'python "{script}" {result}')


class Wrapper:
    def __init__(self, window):
        with open(s3_config, "r") as s3_config_file:
            self.s3_config_data = json.load(s3_config_file)
        with open(ec2_config, "r") as ec2_config_file:
            self.ec2_config_data = json.load(ec2_config_file)
        self.window = window
        self.primary_color = '#839CF0'
        self.secondary_color = '#FFE5C5'
        self.child_window_color = 'powder blue'
        self.window['bg'] = self.primary_color
        self.s3_textbox = []
        self.ec2_textbox = []
        self.s3_file_location = None
        self.top_frame = Frame(self.window, width=1300, height=50, bg=self.primary_color)
        self.middle_frame = Frame(self.window, width=1300, height=600, bg=self.primary_color)
        self.bottom_frame = Frame(self.window, width=1300, height=50, bg=self.primary_color)

    def create_ui(self):
        self.window.geometry('1300x700+0+0')
        self.window.title('AWS Management')
        self.window.state('zoomed')
        self._create_top(context=self.top_frame, text="AWS Management", bg_color=self.primary_color,
                         fg_color=self.secondary_color)
        self.middle_frame.pack(pady=40)

        s3_button = self._create_button(context=self.middle_frame, font_size=25, border=10, text='AWS S3', width=10,
                                        command=self._create_s3_ui)
        s3_button.pack(anchor='center', pady=40)
        s3_button = self._create_button(context=self.middle_frame, font_size=25, border=10, text='AWS EC2', width=10,
                                        command=self._create_ec2_ui)
        s3_button.pack(anchor='center', pady=40)

    def open_file(self):
        self.s3_file_location = filedialog.askopenfilename()

    def _create_s3_ui(self):
        window = Tk()
        window['bg'] = self.child_window_color
        window.geometry('1100x600')
        s3_top_frame = Frame(window, width=1100, height=50, bg=self.child_window_color)
        s3_middle_frame = Frame(window, width=1100, height=500, bg=self.child_window_color)
        s3_bottom_frame = Frame(window, width=1100, height=50, bg=self.child_window_color)
        self._create_top(context=s3_top_frame, text='S3 Management', bg_color=self.child_window_color,
                         fg_color='#b5651d')
        s3_middle_frame.pack(pady=40)
        s3_bottom_frame.pack(side=BOTTOM, pady=40)

        row = 1
        for key, data in self.s3_config_data.items():
            if key == 'AppName':
                window.title(data)
            elif key == 'elements':
                for element in data:
                    if element['type'] == 'TextBox':
                        label = element['Label']
                        text_box = self._create_textbox(context=s3_middle_frame, row=row, text=label,
                                                        bg_color=self.child_window_color, fg_color='orange')
                        self.s3_textbox.append(text_box)
                    elif element['type'] == 'Open':
                        label = element['Label']
                        self._create_open_file(context=s3_middle_frame, text=label, fg_color='orange',
                                               bg_color=self.child_window_color, row=row)
                    elif element['type'] == 'Button':
                        text = element['Text']
                        button = self._create_button(context=s3_bottom_frame, font_size=16, width=10, border=5,
                                                     text=text)
                        button.pack(anchor='center')
                    row += 2

        window.mainloop()

    def _create_ec2_ui(self):
        window = Tk()
        window['bg'] = self.child_window_color
        window.geometry('1100x600')
        ec2_top_frame = Frame(window, width=1100, height=50, bg=self.child_window_color)
        ec2_middle_frame = Frame(window, width=1100, height=500, bg=self.child_window_color)
        ec2_bottom_frame = Frame(window, width=1100, height=50, bg=self.child_window_color)
        self._create_top(context=ec2_top_frame, text='EC2 Management', bg_color=self.child_window_color,
                         fg_color='#b5651d')
        ec2_middle_frame.pack(pady=40)
        ec2_bottom_frame.pack(side=BOTTOM, pady=40)

        row = 1
        for key, data in self.ec2_config_data.items():
            if key == 'AppName':
                window.title(data)
            elif key == 'elements':
                for element in data:
                    if element['type'] == 'TextBox':
                        label = element['Label']
                        text_box = self._create_textbox(context=ec2_middle_frame, row=row, text=label,
                                                        bg_color=self.child_window_color, fg_color='orange')
                        self.ec2_textbox.append(text_box)
                    elif element['type'] == 'Button':
                        text = element['Text']
                        button = self._create_button(context=ec2_bottom_frame, font_size=16, width=15, border=5,
                                                     text=text)
                        button.pack(anchor='center')
                    row += 2

        window.mainloop()

    @staticmethod
    def _create_top(**kwargs):
        kwargs['context'].pack(side=TOP, pady=20)
        label = Label(kwargs['context'], font=('aria', 30, 'bold'), bg=kwargs['bg_color'], fg=kwargs['fg_color'],
                      text=kwargs['text'], bd='10', anchor='center', padx=50)
        label.grid(row=0, column=0, padx=50)

    def _create_button(self, **kwargs):
        button = Button(kwargs['context'], font=('aria', kwargs['font_size'], 'bold'), width=kwargs['width'],
                        bg='steel blue', fg='white', bd=kwargs['border'], text=kwargs['text'],
                        activebackground=self.secondary_color, activeforeground='steel blue',
                        command=lambda: kwargs['command']())
        return button

    def _create_open_file(self, **kwargs):
        label = Label(kwargs['context'], font=('aria', 16, 'bold'), fg=kwargs['fg_color'], text=kwargs['text'],
                      bg=kwargs['bg_color'], bd=10, padx=30)
        label.grid(row=kwargs['row'], column=0, sticky='w')
        button = Button(kwargs['context'], font=('aria', 16, 'bold'), bg=self.primary_color, fg='white', width=10, bd=2,
                        text='Choose File', command=self.open_file)
        button.grid(row=kwargs['row'], column=1)

    def _create_textbox(self, **kwargs):
        label = Label(kwargs['context'], font=('aria', 16, 'bold'), fg=kwargs['fg_color'], text=kwargs['text'],
                      bg=kwargs['bg_color'], bd=10, padx=30)
        label.grid(row=kwargs['row'], column=0, sticky='w')
        entry = Entry(kwargs['context'], font=('aria', 16, 'bold'), bg=self.secondary_color, bd=2, insertwidth=4,
                      fg='#6a6b00')
        entry.grid(row=kwargs['row'], column=1)
        return entry
