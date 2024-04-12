import tkinter as tk
import subprocess
from tkinter import filedialog

class SubfinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Subfinder GUI")
        self.root.geometry("400x400")

        # Initialize variables for checkboxes and output folder
        self.use_all_sources = tk.IntVar()
        self.output_folder = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Create a label for domain name
        self.label_domain = tk.Label(self.root, text="Enter domain name:")
        self.label_domain.pack(pady=5)

        # Create an entry field for domain name
        self.domain_entry = tk.Entry(self.root)
        self.domain_entry.pack()

        # Create a label for file selection
        self.label_file = tk.Label(self.root, text="Select a file:")
        self.label_file.pack(pady=5)

        # Create a button to browse and select a file
        self.file_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.file_button.pack()

        # Create a label for output folder selection
        self.label_output_folder = tk.Label(self.root, text="Select output folder:")
        self.label_output_folder.pack(pady=5)

        # Create an entry field for output folder
        self.output_folder_entry = tk.Entry(self.root, textvariable=self.output_folder)
        self.output_folder_entry.pack()

        # Create a button to choose output folder
        self.folder_button = tk.Button(self.root, text="Choose Folder", command=self.choose_folder)
        self.folder_button.pack()

        # Create a checkbox for using all sources
        self.checkbox_all_sources = tk.Checkbutton(self.root, text="Use all sources for enumeration", variable=self.use_all_sources)
        self.checkbox_all_sources.pack(anchor="w")

        # Create a button to start subdomain search
        self.search_button = tk.Button(self.root, text="Search", command=self.start_search)
        self.search_button.pack(pady=10)

        # Create a button to update Subfinder
        self.update_button = tk.Button(self.root, text="Update Subfinder", command=self.update_subfinder)
        self.update_button.pack(pady=10)

    def select_file(self):
        self.selected_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        # Update label to display the selected file name
        if self.selected_file:
            self.label_file.config(text="Selected file: " + self.selected_file)

    def choose_folder(self):
        self.output_folder.set(filedialog.askdirectory())

    def start_search(self):
        command = ["./subfinder"]

        if self.selected_file:
            command.extend(["-dL", self.selected_file])
        else:
            domain = self.domain_entry.get()
            command.extend(["-d", domain])

        if self.use_all_sources.get():
            command.append("--all")

        output_folder = self.output_folder.get()
        if output_folder:
            command.extend(["-o", output_folder])

        # Execute Subfinder command
        subprocess.run(command)

    def update_subfinder(self):
        # Execute Subfinder update command
        subprocess.run(["subfinder", "-up"])

if __name__ == "__main__":
    root = tk.Tk()
    app = SubfinderApp(root)
    root.mainloop()
