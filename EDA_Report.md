# Exploratory Data Analysis (EDA) Report  
## Task 2 – Data Analytics Internship

### Intern Name
[Your Name]

### Organization
ApexPlanet Software Pvt. Ltd.

---

## 1. Introduction
The purpose of this Exploratory Data Analysis (EDA) is to analyze customer purchase behavior and extract meaningful business insights.  
EDA helps in understanding data distributions, identifying patterns, and uncovering relationships between variables that support data-driven decision making.

This report focuses on:
- Understanding customer demographics
- Analyzing purchase trends
- Identifying high-performing categories and cities
- Exploring relationships between age and spending behavior

---

## 2. Dataset Overview
The dataset used for this analysis represents customer purchase transactions and contains the following attributes:

- Customer demographics (Age, Gender, City)
- Product information (Product Category)
- Transaction details (Purchase Amount, Purchase Date)
- Payment information (Payment Method)

Each row represents a single purchase made by a customer.

---

## 3. Data Preparation
Before analysis:
- The dataset was loaded using Python (Pandas)
- The `Purchase_Date` column was converted into a datetime format
- Data types were verified to ensure consistency

No missing or duplicate values were observed in this dataset.

---

## 4. Descriptive Statistics

### Numerical Features
Key numerical attributes analyzed:
- Age
- Purchase Amount

Summary statistics such as mean, minimum, maximum, and standard deviation were calculated to understand the spread and central tendency of the data.

**Observations:**
- Purchase amounts vary significantly across customers
- Higher spending values are observed in certain product categories

---

### Categorical Features
Categorical attributes include:
- Gender
- City
- Product Category
- Payment Method

Frequency distributions were used to identify dominant categories.

---

## 5. Univariate Analysis

### Purchase Amount Distribution
A histogram was used to visualize the distribution of purchase amounts.

**Insights:**
- Most purchases fall within low to mid price ranges
- High-value purchases are fewer but significantly impact revenue

---

### Product Category Analysis
A bar chart was used to visualize purchase frequency by product category.

**Insights:**
- Electronics and Clothing are the most frequently purchased categories
- Furniture and Groceries show lower purchase counts but consistent demand

---

## 6. Business-Oriented Analysis

### Business Questions Addressed

1. **Which product category generates the highest revenue?**  
   - Electronics contributes the highest average purchase value.

2. **Which city contributes the most to total sales?**  
   - Delhi and Bangalore are the top-performing cities.

3. **What payment method is most preferred?**  
   - UPI and Cash are the most commonly used payment methods.

These insights help businesses focus marketing and inventory strategies effectively.

---

## 7. Multivariate Analysis

### Age vs Purchase Amount
A scatter plot was used to analyze the relationship between customer age and purchase amount.

**Insights:**
- Customers aged between 30 and 45 tend to make higher-value purchases
- Younger customers generally spend less per transaction

---

### Correlation Analysis
A correlation heatmap was used for numerical variables.

**Insights:**
- A moderate positive correlation exists between age and purchase amount
- Age can be considered a contributing factor in spending behavior

---

## 8. Key Insights Summary
- Electronics is the highest-value product category
- Delhi and Bangalore lead in total sales contribution
- UPI and Cash dominate payment preferences
- Customers aged 30–45 are high-value buyers
- Spending behavior shows a moderate dependency on age

---

## 9. Proposed Dashboard KPIs
Based on EDA findings, the following KPIs are recommended for a dashboard:
- Total Sales
- Average Purchase Amount
- Top Product Category
- Top City by Sales
- Preferred Payment Method

These KPIs will enable quick performance tracking and strategic planning.

---

## 10. Conclusion
This Exploratory Data Analysis provided a strong understanding of customer purchase behavior and sales patterns.  
The insights derived from this task form the foundation for:
- Interactive dashboard development
- Deep-dive business analysis
- Strategic decision-making in future tasks

---

## 11. Tools & Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook / VS Code

---

**End of Report**
