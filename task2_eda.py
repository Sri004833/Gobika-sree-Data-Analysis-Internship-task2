import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("customer_purchases_raw.csv")

# Convert date column
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# -----------------------------
# Descriptive Statistics
# -----------------------------
print("Dataset Overview:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nCategorical Summary:")
print(df.describe(include="object"))

# -----------------------------
# Univariate Analysis
# -----------------------------

# Purchase Amount Distribution
plt.figure()
sns.histplot(df["Purchase_Amount"], bins=5, kde=True)
plt.title("Distribution of Purchase Amount")
plt.show()

# Product Category Count
plt.figure()
sns.countplot(x="Product_Category", data=df)
plt.title("Purchases by Product Category")
plt.show()

# -----------------------------
# Business Questions
# -----------------------------

# 1. Average purchase amount by category
avg_category = df.groupby("Product_Category")["Purchase_Amount"].mean()
print("\nAverage Purchase Amount by Category:")
print(avg_category)

# 2. City-wise total sales
city_sales = df.groupby("City")["Purchase_Amount"].sum()
print("\nTotal Sales by City:")
print(city_sales)

# 3. Payment method usage
payment_usage = df["Payment_Method"].value_counts()
print("\nPayment Method Distribution:")
print(payment_usage)

# -----------------------------
# Multivariate Analysis
# -----------------------------

# Age vs Purchase Amount
plt.figure()
sns.scatterplot(x="Age", y="Purchase_Amount", hue="Product_Category", data=df)
plt.title("Age vs Purchase Amount")
plt.show()

# Correlation Heatmap
plt.figure()
sns.heatmap(df[["Age", "Purchase_Amount"]].corr(), annot=True)
plt.title("Correlation Matrix")
plt.show()
