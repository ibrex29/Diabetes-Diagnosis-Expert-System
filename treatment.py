# treatment.py
def get_treatment_recommendations(diagnosis, user_info):
    if diagnosis == "Diabetes":
        if user_info["heart_disease"]:
            return "Start with lifestyle changes and prefer GLP-1 receptor agonists or SGLT2 inhibitors. Consult a doctor."
        if user_info["kidney_disease"]:
            return "Start with lifestyle changes and avoid certain medications like metformin in advanced stages. Consult a doctor."
        return "Start with lifestyle changes (diet, exercise). If not controlled, consider metformin or other medications. Consult a doctor."
    elif diagnosis == "Prediabetes":
        return "Implement lifestyle changes (diet, exercise). Monitor blood glucose levels regularly."
    elif "High risk" in diagnosis:
        return "Consult a doctor for further evaluation and possible intervention."
    elif "Moderate risk" in diagnosis:
        return "Consider consulting a doctor and monitor symptoms regularly."
    else:
        return "Maintain a healthy lifestyle and regular check-ups."
