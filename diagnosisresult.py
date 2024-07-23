import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from fpdf import FPDF
from diagnosis import diagnose
from treatment import get_treatment_recommendations

class DiagnosisResult:
    def __init__(self, root, diagnosis, user_info, tests, symptoms):
        self.root = root
        self.diagnosis = diagnosis
        self.user_info = user_info
        self.tests = tests
        self.symptoms = symptoms

        self.create_widgets()

    def create_widgets(self):
        # Create the result window
        self.result_window = tk.Toplevel(self.root)
        self.result_window.title("Diagnosis Result")
        self.result_window.geometry("800x600")
        self.result_window.configure(bg='#f0f8ff')

        # Create a canvas and scrollbar for scrolling
        self.canvas = tk.Canvas(self.result_window, bg='#f0f8ff')
        self.scrollbar = tk.Scrollbar(self.result_window, orient="vertical", command=self.canvas.yview)

        # Create a frame to contain the widgets
        self.frame = tk.Frame(self.canvas, bg='#f0f8ff')

        # Create a window on the canvas to hold the frame
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Configure the frame's width to match the canvas width
        self.frame.bind("<Configure>", self.on_frame_configure)

        # Create widgets
        self.create_content()

    def create_content(self):
        # Title
        title_label = tk.Label(self.frame, text="Diagnosis Result", font=("Arial", 22, "bold"), bg='#f0f8ff', fg='#008C95')
        title_label.pack(pady=10)

        # Summary Frame
        summary_frame = tk.LabelFrame(self.frame, text="Summary", font=("Arial", 16), bg='#f0f8ff', fg='#008C95', padx=20, pady=20)
        summary_frame.pack(fill='both', expand=True, padx=20, pady=10)

        # Add input summary
        summary_text = self.generate_summary()
        tk.Label(summary_frame, text=summary_text, font=("Arial", 12), bg='#f0f8ff', justify='left').pack(anchor='w')

        # Diagnosis Result
        result_frame = tk.LabelFrame(self.frame, text="Diagnosis", font=("Arial", 16), bg='#f0f8ff', fg='#008C95', padx=20, pady=20)
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)

        tk.Label(result_frame, text=f"Diagnosis: {self.diagnosis}", font=("Arial", 12), bg='#f0f8ff').pack(anchor='w')

        # Treatment Recommendations
        treatment_frame = tk.LabelFrame(self.frame, text="Treatment Recommendations", font=("Arial", 16), bg='#f0f8ff', fg='#008C95', padx=20, pady=20)
        treatment_frame.pack(fill='both', expand=True, padx=20, pady=10)

        tk.Label(treatment_frame, text=f"Recommendations: {self.get_treatment_recommendations()}", font=("Arial", 12), bg='#f0f8ff').pack(anchor='w')

        # Buttons
        button_frame = tk.Frame(self.frame, bg='#f0f8ff')
        button_frame.pack(pady=20)

        # Print button (default styling)
        print_button = tk.Button(button_frame, text="Print", command=self.print_pdf)
        print_button.pack(side='left', padx=10)

        # Close button (default styling)
        close_button = tk.Button(button_frame, text="Close", command=self.result_window.destroy)
        close_button.pack(side='left', padx=10)

    def on_frame_configure(self, event):
        # Update the scroll region of the canvas to encompass the entire frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def generate_summary(self):
        summary = "User Information:\n"
        for key, value in self.user_info.items():
            summary += f"{key.replace('_', ' ').title()}: {value}\n"
        summary += "\nDiagnostic Tests Results:\n"
        for key, value in self.tests.items():
            summary += f"{key.replace('_', ' ').title()}: {value}\n"
        summary += "\nSymptoms:\n"
        for symptom, var in self.symptoms.items():
            summary += f"{symptom}: {'Yes' if var.get() else 'No'}\n"
        return summary

    def get_treatment_recommendations(self):
        # Dummy treatment recommendation function
        # Replace with your actual implementation
        return "Consult with a healthcare provider for a comprehensive treatment plan."

    def print_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Diagnosis Result", ln=True, align='C')

        # Add summary
        pdf.multi_cell(0, 10, txt=self.generate_summary())

        # Add diagnosis result
        pdf.cell(200, 10, txt=f"Diagnosis: {self.diagnosis}", ln=True)

        # Add treatment recommendations
        pdf.cell(200, 10, txt=f"Treatment Recommendations: {self.get_treatment_recommendations()}", ln=True)

        # Save the PDF
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            pdf.output(file_path)
            messagebox.showinfo("Print", "PDF saved successfully.")
