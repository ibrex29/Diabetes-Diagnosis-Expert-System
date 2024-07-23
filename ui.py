import tkinter as tk
from diagnosis import diagnose
from treatment import get_treatment_recommendations
from diagnosisresult import DiagnosisResult

class DiabetesExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Diabetes Diagnosis Expert System")
        self.root.geometry("1000x800")
        self.root.configure(bg='#f0f8ff')

        self.create_widgets()

    def create_widgets(self):
        # Create a canvas for the main content with a scrollbar
        self.canvas = tk.Canvas(self.root, bg='#f0f8ff')
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.main_frame = tk.Frame(self.canvas, bg='#f0f8ff')

        # Bind the canvas and scrollbar
        self.main_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Create a window in the canvas
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Title Frame
        title_frame = tk.Frame(self.main_frame, bg='#008C95', pady=20)
        title_frame.pack(fill='x')

        # Create title label
        tk.Label(title_frame, text="Diabetes Diagnosis Expert System", font=("Arial", 22, "bold"), bg='#008C95', fg='white').pack()

        # User Information Frame
        user_info_frame = tk.LabelFrame(self.main_frame, text="User Information", font=("Arial", 16), bg='#f0f8ff', fg='#008C95', padx=20, pady=20)
        user_info_frame.pack(fill='x', pady=10)

        self.user_info = {
            "age": tk.IntVar(),
            "BMI": tk.DoubleVar(),
            "family_history": tk.BooleanVar(),
            "ethnicity": tk.StringVar(),
            "gestational_diabetes": tk.BooleanVar(),
            "PCOS": tk.BooleanVar(),
            "blood_pressure": tk.DoubleVar(),
            "HDL_cholesterol": tk.DoubleVar(),
            "triglycerides": tk.DoubleVar(),
            "physical_inactivity": tk.BooleanVar(),
            "smoking": tk.BooleanVar(),
            "heart_disease": tk.BooleanVar(),
            "kidney_disease": tk.BooleanVar(),
        }

        # User Info Widgets
        self.create_label_entry(user_info_frame, "Age:", self.user_info["age"])
        self.create_label_entry(user_info_frame, "BMI:", self.user_info["BMI"])
        self.create_checkbutton(user_info_frame, "Family history of diabetes", self.user_info["family_history"])
        self.create_label_entry(user_info_frame, "Ethnicity:", self.user_info["ethnicity"])
        self.create_checkbutton(user_info_frame, "History of gestational diabetes", self.user_info["gestational_diabetes"])
        self.create_checkbutton(user_info_frame, "Polycystic ovary syndrome (PCOS)", self.user_info["PCOS"])
        self.create_label_entry(user_info_frame, "Blood Pressure (mmHg):", self.user_info["blood_pressure"])
        self.create_label_entry(user_info_frame, "HDL Cholesterol (mg/dL):", self.user_info["HDL_cholesterol"])
        self.create_label_entry(user_info_frame, "Triglycerides (mg/dL):", self.user_info["triglycerides"])
        self.create_checkbutton(user_info_frame, "Physical inactivity", self.user_info["physical_inactivity"])
        self.create_checkbutton(user_info_frame, "Smoking", self.user_info["smoking"])
        self.create_checkbutton(user_info_frame, "Heart disease", self.user_info["heart_disease"])
        self.create_checkbutton(user_info_frame, "Kidney disease", self.user_info["kidney_disease"])

        # Create a canvas for the Symptoms Frame with a scrollbar
        self.symptoms_canvas = tk.Canvas(self.main_frame, bg='#f0f8ff')
        self.symptoms_scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=self.symptoms_canvas.yview)
        self.symptoms_frame = tk.Frame(self.symptoms_canvas, bg='#f0f8ff')

        # Bind the canvas and scrollbar
        self.symptoms_frame.bind(
            "<Configure>",
            lambda e: self.symptoms_canvas.configure(scrollregion=self.symptoms_canvas.bbox("all"))
        )

        # Create a window in the canvas
        self.symptoms_canvas.create_window((0, 0), window=self.symptoms_frame, anchor="nw")
        self.symptoms_canvas.pack(side="left", fill="both", expand=True)
        self.symptoms_scrollbar.pack(side="right", fill="y")
        self.symptoms_canvas.configure(yscrollcommand=self.symptoms_scrollbar.set)

        # Symptoms Frame
        symptoms_frame = tk.LabelFrame(self.symptoms_frame, text="Symptoms", font=("Arial", 16), bg='#f0f8ff', fg='#008C95', padx=20, pady=20)
        symptoms_frame.pack(fill='x', pady=10)

        self.symptoms = {
            "Frequent urination": tk.BooleanVar(),
            "Excessive thirst": tk.BooleanVar(),
            "Extreme hunger": tk.BooleanVar(),
            "Unexplained weight loss": tk.BooleanVar(),
            "Fatigue": tk.BooleanVar(),
            "Blurred vision": tk.BooleanVar(),
        }

        for symptom, var in self.symptoms.items():
            tk.Checkbutton(symptoms_frame, text=symptom, variable=var, font=("Arial", 12), bg='#f0f8ff').pack(anchor='w', pady=2)

        # Diagnostic Tests Frame
        tests_frame = tk.LabelFrame(self.main_frame, text="Diagnostic Test Results", font=("Arial", 16), bg='#f0f8ff', fg='#008C95', padx=20, pady=20)
        tests_frame.pack(fill='x', pady=10)

        self.tests = {
            "fasting_glucose": tk.DoubleVar(),
            "HbA1c": tk.DoubleVar(),
            "OGTT": tk.DoubleVar(),
            "random_glucose": tk.DoubleVar(),
        }

        self.create_label_entry(tests_frame, "Fasting Blood Glucose (mg/dL):", self.tests["fasting_glucose"])
        self.create_label_entry(tests_frame, "HbA1c (%):", self.tests["HbA1c"])
        self.create_label_entry(tests_frame, "OGTT 2-hour Blood Glucose (mg/dL):", self.tests["OGTT"])
        self.create_label_entry(tests_frame, "Random Blood Glucose (mg/dL):", self.tests["random_glucose"])

        # Diagnose Button
        self.create_button(
            self.main_frame,
            "Diagnose",
            self.diagnose
        )

        

    def create_label_entry(self, parent, label_text, variable):
        tk.Label(parent, text=label_text, font=("Arial", 12), bg='#f0f8ff').pack(anchor='w', pady=5)
        tk.Entry(parent, textvariable=variable, font=("Arial", 12), width=30).pack(fill='x', pady=5)

    def create_checkbutton(self, parent, text, variable):
        tk.Checkbutton(parent, text=text, variable=variable, font=("Arial", 12), bg='#f0f8ff').pack(anchor='w', pady=5)

    def create_button(self, parent, text, command):
        tk.Button(
            parent,
            text=text,
            command=command
        ).pack(pady=10)

    def diagnose(self):
        # Collect symptoms
        selected_symptoms = {symptom: var for symptom, var in self.symptoms.items() if var.get()}
        user_info = {key: var.get() for key, var in self.user_info.items()}
        tests = {key: var.get() for key, var in self.tests.items()}

        # Get diagnosis result
        diagnosis = diagnose(selected_symptoms, user_info, tests)
        treatment = get_treatment_recommendations(diagnosis, user_info)

        # Show diagnosis result in the new window
        DiagnosisResult(self.root, diagnosis, user_info, tests, self.symptoms)

  
# Create the application
def main():
    root = tk.Tk()
    app = DiabetesExpertSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
