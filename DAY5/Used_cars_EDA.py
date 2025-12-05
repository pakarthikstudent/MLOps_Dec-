# ==============================
#  EDA for Cleaned Used Cars Dataset
# ==============================

# 1️ Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folder for saving plots
os.makedirs("eda_plots", exist_ok=True)

# 2️ Load Data
df = pd.read_csv("cleaned_used_cars.csv")

print(" Data Loaded Successfully")
print("Shape:", df.shape)
print(df.info())

# 3️ Basic Stats
print("\n Basic Statistics:")
print(df.describe(include='all').T)

# 4️ Missing Values
print("\n Missing Value Summary:")
print(df.isnull().sum())

# 5️ Distribution of Key Categorical Columns
categorical_cols = ['Location', 'Fuel_Type', 'Transmission']

for col in categorical_cols:
    plt.figure(figsize=(8, 4))
    sns.countplot(x=col, data=df, palette='viridis')
    plt.title(f"{col} Distribution")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(f"eda_plots/{col}_distribution.png")
    plt.close()

# 6️ Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Price'], bins=30, kde=True, color='teal')
plt.title("Price Distribution")
plt.xlabel("Price (Lakh)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("eda_plots/price_distribution.png")
plt.close()

# 7️ Boxplot to Check Outliers
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Price'], color='salmon')
plt.title("Car Price Outlier Detection")
plt.tight_layout()
plt.savefig("eda_plots/price_boxplot.png")
plt.close()

# 8️ Relationship Analysis (Bivariate)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Year', y='Price', data=df)
plt.title("Price vs Year of Manufacture")
plt.tight_layout()
plt.savefig("eda_plots/price_vs_year.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='Kilometers_Driven', y='Price', data=df)
plt.title("Price vs Kilometers Driven")
plt.tight_layout()
plt.savefig("eda_plots/price_vs_km.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Fuel_Type', y='Price', data=df)
plt.title("Price by Fuel Type")
plt.tight_layout()
plt.savefig("eda_plots/price_by_fuel.png")
plt.close()

# 9️ Correlation Analysis
corr = df[['Year', 'Kilometers_Driven', 'Mileage', 'Engine', 'Power','Price']].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Matrix")
plt.tight_layout()
plt.savefig("eda_plots/correlation_matrix.png")
plt.close()

# 10 Insights Summary
print("\n EDA Completed! All plots saved inside the 'eda_plots/' folder.")
print("""
 Quick Insights:
- Newer cars generally have higher prices.
- More powerful engines (higher BHP) tend to increase price.
- Cars with higher mileage (kmpl) often have smaller engines.
- Automatic cars and diesel variants usually cost more.
""")
