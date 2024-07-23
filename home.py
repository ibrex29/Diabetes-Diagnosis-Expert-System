import tkinter as tk

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Home Page")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f8ff')

        self.create_widgets()

    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#008C95', pady=10)
        header_frame.pack(fill='x')

        tk.Label(header_frame, text="Diabetes Expert System", font=("Arial", 24, "bold"), bg='#008C95', fg='white').pack()

        # Navigation
        nav_frame = tk.Frame(self.root, bg='#f0f8ff')
        nav_frame.pack(pady=20)

        tk.Button(nav_frame, text="Home", command=self.show_home).pack(side='left', padx=10)
        tk.Button(nav_frame, text="Diagnosis Page", command=self.go_to_diagnosis).pack(side='left', padx=10)
        tk.Button(nav_frame, text="About", command=self.show_about).pack(side='left', padx=10)

        # Introduction
        intro_frame = tk.Frame(self.root, bg='#f0f8ff')
        intro_frame.pack(pady=20)

        tk.Label(intro_frame, text="Welcome to the Diabetes Expert System", font=("Arial", 22, "bold"), bg='#f0f8ff').pack()
        tk.Label(intro_frame, text="This system helps in diagnosing diabetes based on various user inputs and diagnostic tests.", font=("Arial", 14), bg='#f0f8ff').pack(pady=10)

        # Navigate to UI page
        tk.Button(intro_frame, text="Go to Diagnosis Page", command=self.go_to_diagnosis).pack(pady=20)

    def show_home(self):
        self.root.destroy()
        root = tk.Tk()
        HomePage(root)
        root.mainloop()

    def go_to_diagnosis(self):
        self.root.destroy()
        import ui  # Import inside the function to avoid circular import
        ui.main()

    def show_about(self):
        self.root.destroy()
        import about  # Import inside the function to avoid circular import
        root = tk.Tk()
        about.AboutPage(root)
        root.mainloop()


# Create the application
def main():
    root = tk.Tk()
    app =    HomePage(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
