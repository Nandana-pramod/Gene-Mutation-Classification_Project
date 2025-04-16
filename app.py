from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

# -------------------------------
# Load model, encoders, scaler
# -------------------------------
with open("mutation_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("label_encoders.pkl", "rb") as le_file:
    label_encoders = pickle.load(le_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# ✅ Load class mapping (encoded value → original class label)
with open("class_mapping.pkl", "rb") as mapping_file:
    class_mapping = pickle.load(mapping_file)

# -------------------------------
# Flask App Setup
# -------------------------------
app = Flask(__name__)

# Feature List
FEATURES = ["Chromosome", "Start_position", "End_position", "Strand", "Variant_Type",
            "Reference_Allele", "Alternate_Allele", "isDeleterious", "isTCGAhotspot",
            "isCOSMIChotspot", "COSMIChsCnt", "Variant_annotation"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data from HTML
        input_data = {
            "Chromosome": request.form["chromosome"],
            "Start_position": int(request.form["start_position"]),
            "End_position": int(request.form["end_position"]),
            "Strand": request.form["strand"],
            "Variant_Type": request.form["variant_type"],
            "Reference_Allele": request.form["reference_allele"],
            "Alternate_Allele": request.form["alternate_allele"],
            "isDeleterious": request.form["is_deleterious"] == "True",
            "isTCGAhotspot": request.form["is_tcga_hotspot"] == "True",
            "isCOSMIChotspot": int(request.form["is_cosmic_hotspot"]),
            "COSMIChsCnt": float(request.form["cosmic_hs_cnt"]),
            "Variant_annotation": request.form["variant_annotation"]
        }

        # Label encoding for categorical features
        for feature, encoder in label_encoders.items():
            if feature in input_data:
                input_data[feature] = encoder.transform([input_data[feature]])[0]

        # Create DataFrame and scale
        input_df = pd.DataFrame([input_data])
        input_scaled = scaler.transform(input_df)

        # ✅ Predict encoded label
        prediction_encoded = model.predict(input_scaled)[0]
        prediction_encoded = int(prediction_encoded)  # Ensure it's an int

        # ✅ Convert to original class label
        prediction_label = class_mapping.get(prediction_encoded, "Unknown")

        return render_template("index.html", prediction_text=f"Predicted Variant Classification: {prediction_label}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
