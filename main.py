import os
import git
import pyperclip
import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading

class GitPusherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Git Directory Pusher")
        self.geometry("600x400")
        self.iconbitmap('logofinal.ico')
        self.configure(bg='white')
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.title_label = ctk.CTkLabel(self, text="Git Directory Pusher\n(Credits to Germanized)", font=("Segoe UI", 14))
        self.title_label.pack(pady=20)
        self.choose_button = ctk.CTkButton(self, text="Choose Directory", command=self.choose_directory)
        self.choose_button.pack(pady=20)
        self.repo_url_label = ctk.CTkLabel(self, text="Repository URL:", font=("Segoe UI", 12))
        self.repo_url_label.pack(pady=5)
        self.repo_url_entry = ctk.CTkEntry(self, placeholder_text="Enter GitHub Repository URL", font=("Segoe UI", 12))
        self.repo_url_entry.pack(pady=5, padx=20, fill='x')
        self.push_button = ctk.CTkButton(self, text="Push to GitHub", command=self.push_to_github)
        self.push_button.pack(pady=20)
        self.status_label = ctk.CTkLabel(self, text="", font=("Segoe UI", 12))
        self.status_label.pack(pady=10)
        self.directory = ""

    def choose_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            messagebox.showinfo("Selected Directory", f"Directory selected: {self.directory}")

    def push_to_github(self):
        if not self.directory:
            messagebox.showerror("Error", "No directory selected!")
            return
        
        repo_url = self.repo_url_entry.get()
        if not repo_url:
            messagebox.showerror("Error", "Repository URL is required!")
            return

        self.status_label.configure(text="Initializing repository...")
        self.update()
        
        threading.Thread(target=self._push_to_github, args=(self.directory, repo_url)).start()

    def _push_to_github(self, directory, repo_url):
        try:
            repo = git.Repo.init(directory)
            if 'origin' in repo.remotes:
                repo.remotes.origin.set_url(repo_url)
            else:
                repo.create_remote('origin', repo_url)
            repo.remotes.origin.fetch()
            repo.git.merge('origin/main', no_edit=True)
            repo.git.add(A=True)
            repo.index.commit("Automated commit")
            repo.remotes.origin.push('main')
            self.status_label.configure(text="Push successful!")
        except Exception as e:
            error_message = f"Error: {e}"
            self.status_label.configure(text=error_message)
            pyperclip.copy(error_message)

if __name__ == "__main__":
    app = GitPusherApp()
    app.mainloop()
