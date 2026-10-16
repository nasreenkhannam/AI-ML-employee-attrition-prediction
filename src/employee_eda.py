from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

csv_files = list(DATA_DIR.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError(
        "No CSV file found in the data folder. "
        "Download the employee attrition dataset "
        "and place it inside data/."
    )

DATA_PATH = csv_files[0]

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully.")
print("Dataset file:", DATA_PATH.name)

print("\nFirst five rows:")
print(df.head())

print("\nDataset dimensions:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types and non-null values:")
df.info()

print("\nMissing values by column:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())






# STEP 2: Analyze the Attrition column

print("\n========== ATTRITION ANALYSIS ==========")

# Count employees who left and stayed
attrition_counts = df["Attrition"].value_counts()

print("\nEmployee counts:")
print(attrition_counts)

# Calculate percentages
attrition_percentages = (
    df["Attrition"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nEmployee percentages:")
print(attrition_percentages)

# Show the total number of records
print("\nTotal employees:", len(df))

# Calculate the number of employees who left
employees_left = (df["Attrition"] == "Yes").sum()

print("Employees who left:", employees_left)



# Chart 1: Employee Attrition Distribution

import matplotlib.pyplot as plt

attrition_counts = df["Attrition"].value_counts().reindex(
    ["No", "Yes"], fill_value=0
)

plt.figure(figsize=(7, 5))

bars = plt.bar(
    attrition_counts.index,
    attrition_counts.values
)

plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

# Display the actual count above each bar
plt.bar_label(bars, fmt="%d", padding=3)

plt.tight_layout()

# Save the chart
plt.savefig(
    "images/01_attrition_distribution.png",
    dpi=150
)

plt.show()
plt.close()

print("Chart saved to images/01_attrition_distribution.png")





# STEP 3: Analyze attrition by department

print("\n========== DEPARTMENT VS ATTRITION ==========")

department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"]
)

print("\nEmployee counts by department and attrition:")
print(department_attrition)

# Calculate attrition percentage within each department
department_attrition_percent = (
    pd.crosstab(
        df["Department"],
        df["Attrition"],
        normalize="index"
    ) * 100
).round(2)

print("\nAttrition percentage within each department:")
print(department_attrition_percent)

# Create a stacked bar chart
department_attrition.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 5)
)

plt.title("Employee Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.legend(title="Attrition")
plt.tight_layout()

plt.savefig(
    "images/02_department_attrition.png",
    dpi=150
)

plt.show()
plt.close()

print("Chart saved to images/02_department_attrition.png")






# STEP 4: Analyze overtime and attrition

print("\n========== OVERTIME VS ATTRITION ==========")

# Count employees by overtime status and attrition
overtime_counts = pd.crosstab(
    df["OverTime"],
    df["Attrition"]
)

print("\nEmployee counts:")
print(overtime_counts)

# Calculate attrition percentages within each overtime group
overtime_percentages = (
    pd.crosstab(
        df["OverTime"],
        df["Attrition"],
        normalize="index"
    ) * 100
).round(2)

print("\nAttrition percentages within each overtime group:")
print(overtime_percentages)

# Plot the employee counts
overtime_counts.plot(
    kind="bar",
    stacked=True,
    figsize=(8, 5)
)

plt.title("Employee Attrition by Overtime Status")
plt.xlabel("Works Overtime")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.legend(title="Attrition")
plt.tight_layout()

plt.savefig(
    "images/03_overtime_attrition.png",
    dpi=150
)

plt.show()
plt.close()

print("Chart saved to images/03_overtime_attrition.png")







# STEP 5: Analyze job satisfaction and attrition

print("\n========== JOB SATISFACTION VS ATTRITION ==========")

# Count employees by satisfaction rating and attrition
satisfaction_counts = pd.crosstab(
    df["JobSatisfaction"],
    df["Attrition"]
)

print("\nEmployee counts:")
print(satisfaction_counts)

# Calculate attrition percentages within each satisfaction rating
satisfaction_percentages = (
    pd.crosstab(
        df["JobSatisfaction"],
        df["Attrition"],
        normalize="index"
    ) * 100
).round(2)

print("\nAttrition percentages by job satisfaction:")
print(satisfaction_percentages)

# Create a stacked bar chart
satisfaction_counts.plot(
    kind="bar",
    stacked=True,
    figsize=(8, 5)
)

plt.title("Employee Attrition by Job Satisfaction")
plt.xlabel("Job Satisfaction Rating (1 = Low, 4 = Very High)")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.legend(title="Attrition")
plt.tight_layout()

plt.savefig(
    "images/04_job_satisfaction_attrition.png",
    dpi=150
)

plt.show()
plt.close()

print("Chart saved to images/04_job_satisfaction_attrition.png")







# STEP 6: Analyze age groups and attrition

print("\n========== AGE GROUP VS ATTRITION ==========")

# Create age groups
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 100],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56+"
    ]
)

# Count employees by age group and attrition
age_counts = pd.crosstab(
    df["AgeGroup"],
    df["Attrition"]
)

print("\nEmployee counts by age group:")
print(age_counts)

# Calculate attrition percentage within each age group
age_percentages = (
    pd.crosstab(
        df["AgeGroup"],
        df["Attrition"],
        normalize="index"
    ) * 100
).round(2)

print("\nAttrition percentages by age group:")
print(age_percentages)

# Create a stacked bar chart
age_counts.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 5)
)

plt.title("Employee Attrition by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.legend(title="Attrition")
plt.tight_layout()

plt.savefig(
    "images/05_age_group_attrition.png",
    dpi=150
)

plt.show()
plt.close()

print("Chart saved to images/05_age_group_attrition.png")
