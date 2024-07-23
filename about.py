import tkinter as tk
import ui  # Import inside the function to avoid circular import
import home  # Import inside the function to avoid circular import

class AboutPage:
    def __init__(self, root):
        self.root = root
        self.root.title("About Page")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f8ff')

        self.create_widgets()

    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#008C95', pady=10)
        header_frame.pack(fill='x')

        tk.Label(header_frame, text="About", font=("Arial", 24, "bold"), bg='#008C95', fg='white').pack()

        # Navigation
        nav_frame = tk.Frame(self.root, bg='#f0f8ff')
        nav_frame.pack(pady=20)

        tk.Button(nav_frame, text="Home", command=self.show_home).pack(side='left', padx=10)
        tk.Button(nav_frame, text="Diagnosis Page", command=self.go_to_diagnosis).pack(side='left', padx=10)
        tk.Button(nav_frame, text="About", command=self.show_about).pack(side='left', padx=10)

        # About Information
        about_frame = tk.Frame(self.root, bg='#f0f8ff')
        about_frame.pack(pady=20)

        tk.Label(about_frame, text="About the Diabetes Diagnosis Expert System", font=("Arial", 22, "bold"), bg='#f0f8ff').pack()
        
        tk.Label(
            about_frame,
            text="This Diabetes Diagnosis Expert System is a final year project developed by [Your Name], a Computer Science student. The project aims to provide a comprehensive and user-friendly tool for diagnosing diabetes based on various user inputs and diagnostic test results. The system leverages advanced algorithms to analyze data and offer recommendations for further action.",
            font=("Arial", 14),
            bg='#f0f8ff',
            wraplength=750
        ).pack(pady=10)

        tk.Label(
            about_frame,
            text="Key Features of the Project:\n"
                 "- User-friendly interface for easy data entry\n"
                 "- Integration of various diagnostic criteria and symptoms\n"
                 "- Personalized treatment recommendations\n"
                 "- Interactive and responsive design\n"
                 "- Implementation of modern UI/UX principles\n\n"
                 "This project showcases proficiency in Python programming, Tkinter for GUI development, and an understanding of diabetes diagnosis and management. It demonstrates the ability to develop a real-world application that combines technical skills with practical knowledge.",
            font=("Arial", 12),
            bg='#f0f8ff',
            wraplength=750
        ).pack(pady=10)

    def show_home(self):
        self.root.destroy()
        root = tk.Tk()
        home.HomePage(root)
        root.mainloop()

    def go_to_diagnosis(self):
        self.root.destroy()
        import ui  # Import inside the function to avoid circular import
        ui.main()

    def show_about(self):
        # Already on the About page
        pass

if __name__ == "__main__":
    root = tk.Tk()
    AboutPage(root)
    root.mainloop()
