# diagnosis.py
def diagnose(symptoms, user_info, tests):
    risk_factors = 0

    # General Rules
    if user_info["age"] > 45 and user_info["BMI"] > 25:
        risk_factors += 1
    if user_info["family_history"]:
        risk_factors += 1
    if user_info["ethnicity"] in ["African American", "Hispanic", "Native American", "Asian American", "Pacific Islander"]:
        risk_factors += 1
    if user_info["gestational_diabetes"]:
        risk_factors += 1
    if user_info["PCOS"]:
        risk_factors += 1
    if user_info["blood_pressure"] > 140/90:
        risk_factors += 1
    if user_info["HDL_cholesterol"] < 35:
        risk_factors += 1
    if user_info["triglycerides"] > 250:
        risk_factors += 1
    if user_info["physical_inactivity"]:
        risk_factors += 1
    if user_info["smoking"]:
        risk_factors += 1

    # Symptom-Based Rules
    if len(symptoms) >= 3:
        risk_factors += 1

    # Diagnostic Test Rules
    if 100 <= tests["fasting_glucose"] <= 125:
        return "Prediabetes"
    if tests["fasting_glucose"] >= 126:
        return "Diabetes"
    if 5.7 <= tests["HbA1c"] <= 6.4:
        return "Prediabetes"
    if tests["HbA1c"] >= 6.5:
        return "Diabetes"
    if 140 <= tests["OGTT"] <= 199:
        return "Prediabetes"
    if tests["OGTT"] >= 200:
        return "Diabetes"
    if tests["random_glucose"] >= 200 and len(symptoms) > 0:
        return "Diabetes"

    if risk_factors >= 3:
        return "High risk of diabetes. Please consult a doctor."
    elif 1 <= risk_factors < 3:
        return "Moderate risk of diabetes. Consider consulting a doctor."
    else:
        return "Low risk of diabetes. Maintain a healthy lifestyle."
