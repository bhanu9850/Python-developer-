import tkinter as tk
from tkinter import filedialog, messagebox
from filehandling import upload_file, download_file

class FileSharingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Sharing App")
        self.geometry("600x400")

        self.upload_button = tk.Button(self, text="Upload File", command=self.upload_file)
        self.upload_button.pack()

        self.download_button = tk.Button(self, text="Download File", command=self.download_file)
        self.download_button.pack()

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                upload_file(file_path, self.server_address.get(), int(self.server_port.get()))
                messagebox.showinfo("Success", "File uploaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error uploading file: {str(e)}")

    def download_file(self):
        file_name = filedialog.asksaveasfilename()
        if file_name:
            try:
                download_file(file_name, self.server_address.get(), int(self.server_port.get()))
                messagebox.showinfo("Success", "File downloaded successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error downloading file: {str(e)}")

if __name__ == "__main__":
    app = FileSharingApp()

    # Add server address and port entry fields
    server_address_label = tk.Label(app, text="Server Address:")
    server_address_label.pack()
    app.server_address = tk.Entry(app)
    app.server_address.pack()

    server_port_label = tk.Label(app, text="Server Port:")
    server_port_label.pack()
    app.server_port = tk.Entry(app)
    app.server_port.pack()

    # Default server address and port
    app.server_address.insert(0, 'localhost')
    app.server_port.insert(0, '45268')

    app.mainloop()
