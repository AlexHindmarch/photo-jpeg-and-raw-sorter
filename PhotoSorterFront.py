import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_photos(source_folder, jpeg_folder, cr2_folder):
    # Create destination folders if they don't exist
    os.makedirs(jpeg_folder, exist_ok=True)
    os.makedirs(cr2_folder, exist_ok=True)

    # Traverse through the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Get the file extension
            _, extension = os.path.splitext(file)

            # Check if the file is a JPG or CR2
            if extension.lower() == '.jpg':
                destination_folder = jpeg_folder
            elif extension.lower() == '.cr2':
                destination_folder = cr2_folder
            else:
                continue  # Skip files with other extensions

            # Build the full paths
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)

            # Check if the file already exists in the destination folder
            if os.path.exists(destination_path):
                print(f"File {file} already exists in {destination_folder}. Skipping.")
            else:
                # Move the file to the appropriate folder
                shutil.move(source_path, destination_path)
                print(f"Moved {file} to {destination_folder}")

def browse_button(entry_var):
    filename = filedialog.askdirectory()
    entry_var.set(filename)

def organize_photos_gui():
    root = tk.Tk()
    root.title("Photo Organizer")

    # Entry widgets for source folder and destination folders
    source_var = tk.StringVar()
    source_entry = tk.Entry(root, textvariable=source_var, width=40)
    source_entry.grid(row=0, column=0, padx=10, pady=10)

    jpeg_var = tk.StringVar()
    jpeg_entry = tk.Entry(root, textvariable=jpeg_var, width=40)
    jpeg_entry.grid(row=1, column=0, padx=10, pady=10)

    cr2_var = tk.StringVar()
    cr2_entry = tk.Entry(root, textvariable=cr2_var, width=40)
    cr2_entry.grid(row=2, column=0, padx=10, pady=10)

    # Browse buttons to select folders
    tk.Button(root, text="Browse Source", command=lambda: browse_button(source_var)).grid(row=0, column=1)
    tk.Button(root, text="Browse jpeg", command=lambda: browse_button(jpeg_var)).grid(row=1, column=1)
    tk.Button(root, text="Browse raw", command=lambda: browse_button(cr2_var)).grid(row=2, column=1)

    # Organize button
    tk.Button(root, text="Organize Photos", command=lambda: organize_photos(source_var.get(), jpeg_var.get(), cr2_var.get())).grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    organize_photos_gui()