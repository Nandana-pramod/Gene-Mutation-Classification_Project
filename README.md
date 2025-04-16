🧬 Gene Mutation Classification using Machine Learning
This project focuses on classifying gene mutations such as Missense, Nonsense, and Silent mutations using a Random Forest Classifier. It automates the classification process using genomic data, which is crucial for medical research and diagnosis support.

📌 Project Overview
Problem: Classify genetic mutations based on features like chromosome, variant type, allele, and annotation.

Goal: Build an ML model that predicts the mutation type to assist in genetics and biomedical research.

Model: Random Forest Classifier

Deployment: Flask-based web application

📊 Dataset Details
Source: 	https://depmap.org/portal/download/all/?file=CCLE_mutations.csv&r elease=DepMap+Public+22Q2  

Size: 1.2 million rows, 32 columns

Target Variable: Variant_Classification

Input Features:

Chromosome

Start and End Position

Strand

Variant_Type

Reference and Alternate Allele

COSMIC and TCGA features

Variant Annotation

🔧 Project Workflow
Data Preprocessing

Handled missing values using mean and mode

Label encoding and one-hot encoding for categorical features

Feature scaling (if required)

Model Building

Random Forest Classifier

Hyperparameter tuning using GridSearchCV

Evaluation Metrics

Accuracy, Precision, Recall, F1-score

Deployment

Flask web app

User-friendly interface for mutation input and prediction

✅ Model Evaluation

Metric	Value
Accuracy	97.55%
Precision	97.52%
Recall	97.55%
F1-Score	97.53%
🖥️ Technologies Used
Python

Scikit-learn

Pandas, NumPy

Flask

HTML/CSS

Pickle

🚀 How to Run Locally
bash
Copy
Edit
# Clone the repo
git clone https://github.com/yourusername/gene-mutation-classifier.git
cd gene-mutation-classifier

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
Then open http://127.0.0.1:5000/ in your browser.

🌱 Future Enhancements
Integrate Deep Learning models (e.g., CNNs for DNA sequences)

Expand to disease diagnosis

Build a mobile-friendly interface

Improve handling of rare mutation types

📚 References
DepMap Portal

Scikit-learn

Flask Documentation

ChatGPT (for assistance and explanation)

