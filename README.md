# ⚡ EV Adoption Prediction — VoltWise

A machine learning-powered web application that predicts whether a customer is likely to adopt an Electric Vehicle (EV) based on their demographic profile, commuting behavior, charging infrastructure availability, income, and environmental awareness.

The project combines data preprocessing, machine learning classification, model evaluation, and an interactive Streamlit interface to make EV adoption predictions more accessible and understandable.

## 🌐 Project Overview

Electric vehicle adoption depends on several factors, including affordability, daily commuting distance, access to charging infrastructure, living environment, and environmental awareness.

**VoltWise** uses machine learning to analyze these factors and estimate a customer's likelihood of purchasing an electric vehicle.

The application is designed to provide a simple, human-friendly interface instead of requiring users to interact directly with a machine learning model.

## ✨ Features

- Predict EV purchase/adoption likelihood
- Interactive and user-friendly Streamlit interface
- Customer demographic analysis
- Income and daily commute-based inputs
- Charging infrastructure availability analysis
- Environmental awareness consideration
- Categorical feature encoding
- Numerical feature scaling
- Multiple machine learning model experimentation
- Prediction confidence/probability visualization

## 🧠 Machine Learning Workflow

The project follows a typical machine learning pipeline:

1. **Data Loading** — Load the EV adoption dataset.
2. **Data Cleaning** — Handle missing values and remove irrelevant features.
3. **Feature Selection** — Select relevant demographic, commuting, and infrastructure features.
4. **Encoding** — Apply One-Hot Encoding to categorical variables.
5. **Scaling** — Standardize numerical features using StandardScaler.
6. **Model Training** — Train and evaluate multiple classification algorithms.
7. **Model Evaluation** — Compare model performance using evaluation metrics.
8. **Model Serialization** — Save the preprocessing object and trained model using Joblib.
9. **Deployment Interface** — Integrate the trained model into a Streamlit application.

## 🤖 Models Explored

The following classification algorithms were experimented with:

- Logistic Regression
- Support Vector Classifier (SVC)
- Random Forest Classifier
- Decision Tree Classifier
- XGBoost Classifier

## 📊 Features Used

### Categorical Features

- Gender
- City Type
- Current Car Type
- Home Charging Possible
- Subsidy Available

### Numerical Features

- Age
- Annual Income (USD)
- Daily Commute Distance (km)
- Number of Cars Owned
- Charging Stations Near Home
- Charging Stations Near Work
- Environmental Concern Level

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Preprocessing and machine learning |
| XGBoost | Gradient boosting classification |
| Joblib | Model serialization |
| Streamlit | Web application |

## 📁 Project Structure

```text
ev-adoption-prediction/
│
├── app.py
├── requirements.txt
├── model.pkl
├── preprocessor.pkl
├── label_encoder.pkl
│
├── notebooks/
│   └── EV_Adoption_Analysis.ipynb
│
├── data/
│   └── EV_Adoption_and_Range_Anxiety_Dataset.csv
│
└── README.md
```

*The exact folder structure may differ depending on the files included in the repository.*

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ev-adoption-prediction.git
```

### 2. Navigate to the project directory

```bash
cd ev-adoption-prediction
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the virtual environment

**Windows:**

```powershell
env\Scripts\activate
```

**macOS/Linux:**

```bash
source env/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 📦 Model Files

The application uses serialized machine learning artifacts:

- `model.pkl` — Trained classification model
- `preprocessor.pkl` — Preprocessing pipeline for input features
- `label_encoder.pkl` — Target label encoder (if required by the application)

These files must be available for the application to load and generate predictions.

## 🎯 Objective

The primary objective of this project is to explore how machine learning can help understand potential electric vehicle adoption behavior using customer characteristics and charging-related factors.

This project is an educational and analytical prediction tool. Predictions should not be interpreted as guaranteed purchasing decisions.

## 🔮 Future Improvements

- Hyperparameter optimization
- Cross-validation
- Improved model comparison
- Probability calibration
- Feature importance visualization
- SHAP-based explainability
- Deployment on Streamlit Community Cloud
- Better handling of model uncertainty

## 👨‍💻 Author

**Sanyam Jain**

B.Tech — Artificial Intelligence & Machine Learning

---

⭐ If you find this project interesting, feel free to star the repository!
