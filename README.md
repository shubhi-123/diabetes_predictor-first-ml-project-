# Diabetes Predictor
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

## Project Overview

This project predicts whether a person is likely to have diabetes using the **Pima Indians Diabetes Dataset** and a **Logistic Regression** model. The prediction is based on medical attributes such as **Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, and Age**. The project follows end-to-end ML workflow for model development, including data preprocessing, exploratory data analysis (EDA), feature scaling, model training, and evaluation. It serves as a beginner-friendly healthcare prediction project that demonstrates the fundamentals of binary classification using Scikit-learn.
<img width="467" height="422" alt="1" src="https://github.com/user-attachments/assets/3286b85f-077a-453e-b3a3-58fad3886ca5" />

<img width="435" height="416" alt="2" src="https://github.com/user-attachments/assets/8cf4c929-4e0f-4294-9a82-1618ea702f9f" />

## Features

- Predicts the likelihood of diabetes based on patient health parameters.
- Performs exploratory data analysis (EDA) to understand data distribution and feature relationships.
- Includes data preprocessing, standardization, and feature scaling for improved model performance.
- Uses Logistic Regression for binary classification.
- Evaluates the model using an 80–20 train-test split.
- Built using Python, Pandas, Matplotlib, and Scikit-learn.

## 📊 Model Performance

| Metric | Value |
|----------|----------|
| **Algorithm** | Logistic Regression |
| **Dataset** | Pima Indians Diabetes Dataset |
| **Dataset Size** | 700+ samples |
| **Train-Test Split** | 80% Training / 20% Testing |
| **Accuracy** | **67.5%** |
| **F1-Score** | **0.61** |

## Tech Stack

- **Languages:**  
  - Python
  - Jupyter Notebook
- **Libraries & Tools:**  
  - scikit-learn (for model training, scaling, and persistence)
  - pandas, numpy (for data manipulation)
  - matplotlib (for visualization)
  - pickle (for model serialization)
  - Additional dependencies as listed in `requirements.txt`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shubhi-123/diabetes_predictor-first-ml-project-.git
   cd diabetes_predictor-first-ml-project-
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

## Usage

1. **Explore and train the model:**
   - Open `diabetes_predictor.ipynb` in Jupyter Notebook.
   - Run the cells to understand data preprocessing, model training, and evaluation.
   - Modify or retrain the model as needed within the notebook.

2. **Interact with the trained model:**
   - Ensure `model.pkl`, `model1.pkl`, and `scaler.pkl` are present in the project directory.
   - Run the frontend script to make predictions:
     ```bash
     python frontend_diabetes_predictor.py
     ```
   - Follow the prompts in the terminal to input data and receive predictions.

3. **Model deployment or integration:**
   - The saved `.pkl` files (`model.pkl`, `model1.pkl`, `scaler.pkl`) can be loaded in other Python scripts for further deployment or integration.

## Project Structure

```
.
├── .gitignore.txt
├── diabetes_predictor.ipynb          # Main Jupyter Notebook 
├── frontend_diabetes_predictor.py    # Python script for user interaction with the model
├── model.pkl                         # Serialized trained model
├── model1.pkl                        # Alternate/updated model version
├── requirements.txt                  # List of Python dependencies
├── scaler.pkl                        # Saved scaler for input data preprocessing
└── .ipynb_checkpoints/
    └── diabetes_predictor-checkpoint.ipynb  # Notebook checkpoint (auto-saved)
```
## Future Improvements

- Experiment with advanced models such as Random Forest, XGBoost, and Support Vector Machines.
- Perform hyperparameter tuning to improve predictive performance.
- Apply feature engineering and feature selection techniques.
- Use cross-validation for more robust model evaluation.
- Deploy the model as an interactive web application using Streamlit or Flask.
- Train the model on a larger and more diverse dataset to improve generalization and accuracy.


---
