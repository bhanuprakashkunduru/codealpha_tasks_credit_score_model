# Credit Score Classification Model

## Project Overview

This machine learning project predicts an individual's credit score category based on their financial history and credit-related information.

The objective is to classify customers into different credit score categories using supervised machine learning algorithms and evaluate their performance using multiple classification metrics.

---

## Problem Statement

Financial institutions use credit scoring systems to assess the creditworthiness of customers before approving loans, credit cards, or other financial services.

This project builds a classification model that predicts a customer's credit score using financial indicators such as income, debt, credit utilization, payment behavior, and credit history.

---

## Dataset Information

The dataset contains customer financial and credit-related information, including:

- Annual Income
- Monthly Inhand Salary
- Number of Bank Accounts
- Number of Credit Cards
- Interest Rate
- Number of Loans
- Delay from Due Date
- Number of Delayed Payments
- Credit Mix
- Outstanding Debt
- Credit Utilization Ratio
- Credit History Age
- Payment Behaviour
- Monthly Balance
- Credit Score (Target Variable)

### Dataset Size

- Records: 100,000
- Features: 28

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Jupyter Notebook

---

## Data Preprocessing

The following preprocessing steps were performed:

- Data loading and inspection
- Feature selection
- Label Encoding of categorical variables
- Train-Test Split
- Feature Scaling using StandardScaler (for Logistic Regression)

---

## Machine Learning Models Implemented

### 1. Decision Tree Classifier

A Decision Tree model was trained using:

- Criterion: Gini Index
- Maximum Depth: 3

### 2. Random Forest Classifier

An ensemble learning model using multiple decision trees to improve prediction performance.

### 3. Logistic Regression

A linear classification model trained after feature scaling.

---

## Evaluation Metrics

The models were evaluated using:

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score

These metrics help measure classification performance and prediction quality.

---

## Project Workflow

1. Import Required Libraries
2. Load Dataset
3. Data Cleaning & Preprocessing
4. Encode Categorical Features
5. Select Important Features
6. Split Data into Training and Testing Sets
7. Train Machine Learning Models
8. Evaluate Model Performance
9. Compare Results

---

## Key Features

- Creditworthiness Prediction
- Financial Data Analysis
- Multiple Classification Algorithms
- Feature Engineering
- Performance Comparison

---

## Repository Structure

```
Credit-Score-Classification/
│
├── task_1.ipynb
├── credit_score_dataset.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/credit-score-classification.git
```

Move into the project directory:

```bash
cd credit-score-classification
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Open Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
task_1.ipynb
```

Run all cells to reproduce the results.

---

## Future Improvements

- Hyperparameter Tuning
- Feature Selection Optimization
- Cross Validation
- XGBoost Implementation
- LightGBM Implementation
- Model Deployment using Flask/Streamlit

---

## Learning Outcomes

Through this project, the following concepts were practiced:

- Data Preprocessing
- Label Encoding
- Feature Scaling
- Classification Algorithms
- Model Evaluation
- Credit Risk Analysis

---

## Author

Bhanu Prakash

Machine Learning Enthusiast | Data Science Learner