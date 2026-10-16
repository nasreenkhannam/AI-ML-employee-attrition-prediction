# AI-Based Employee Attrition Prediction System

## Project Overview

This project explores employee attrition data to understand patterns associated with employees leaving an organization. The current stage focuses on data loading, data quality checks, exploratory data analysis (EDA), and visualization.

Predictive model training and evaluation are not included in this EDA stage.

## Objectives

- Load and inspect the employee dataset.
- Check for missing values and duplicate records.
- Analyze the overall employee attrition distribution.
- Explore attrition across departments, overtime status, job satisfaction, and age groups.
- Present findings using tables and charts.

## Dataset

The project uses the IBM HR Analytics Employee Attrition dataset.

- **Records:** 1,470 employees
- **Features:** 35 original columns
- **Missing values:** 0
- **Duplicate rows:** 0

The dataset includes employee demographics, job information, satisfaction ratings, overtime status, and attrition labels.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
AI-ML-INTERNSHIP-employee-attrition-prediction/
├── data/
├── images/
├── notebooks/
│   └── employee_eda.ipynb
├── reports/
│   └── eda_report.md
├── src/
│   └── employee_eda.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Exploratory Data Analysis

The following analyses are included:

1. Overall employee attrition distribution
2. Department vs. attrition
3. Overtime status vs. attrition
4. Job satisfaction vs. attrition
5. Age group vs. attrition

## Initial Findings

- The dataset contains 1,470 employee records.
- 237 employees (16.12%) are labeled as having left the organization.
- 1,233 employees (83.88%) are labeled as having stayed.
- The observed attrition percentage is higher among employees who work overtime than among those who do not.
- Attrition percentages vary across departments, job satisfaction ratings, and age groups.

These are descriptive findings from this dataset and do not establish causation.

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-ML-INTERNSHIP-employee-attrition-prediction
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Add the dataset

Place the CSV file in the `data/` folder using this filename:

`WA_Fn-UseC_-HR-Employee-Attrition.csv`

Follow the dataset's applicable license and usage terms.

### 5. Run the Python script

```powershell
python src/employee_eda.py
```

### 6. Open the Jupyter Notebook

Open `notebooks/employee_eda.ipynb` in VS Code and select your project's Python environment.

## Project Status

**Current stage:** Data inspection and exploratory data analysis.

Predictive model training, model evaluation, and deployment are future stages and should only be marked complete after they are implemented and tested.
