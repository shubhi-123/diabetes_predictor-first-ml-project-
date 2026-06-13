# diabetes_predictor-first-ml-project-

[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)

## Overview

This repository contains a machine learning project for predicting diabetes using Python and Jupyter Notebook. The project includes model training, data preprocessing (scaling), model persistence with serialized `.pkl` files, and a Python script to provide a simple frontend interface for predictions. It serves as an end-to-end demonstration of building, saving, and deploying a machine learning model for diabetes prediction.

## Tech Stack

- **Languages:**  
  - Python
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
├── diabetes_predictor.ipynb          # Main Jupyter Notebook (EDA, model training)
├── frontend_diabetes_predictor.py    # Python script for user interaction with the model
├── model.pkl                         # Serialized trained model
├── model1.pkl                        # Alternate/updated model version
├── requirements.txt                  # List of Python dependencies
├── scaler.pkl                        # Saved scaler for input data preprocessing
└── .ipynb_checkpoints/
    └── diabetes_predictor-checkpoint.ipynb  # Notebook checkpoint (auto-saved)
```

## License

No license has been specified for this project. Please contact the repository owner for usage permissions.

---
[![README powered by ReadmeAI](https://img.shields.io/badge/README-powered%20by%20ReadmeAI-4c9be8?style=flat-square&logo=markdown)](https://www.readmeai.in)
