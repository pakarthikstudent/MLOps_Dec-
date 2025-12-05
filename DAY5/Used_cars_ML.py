# ==============================
#  Car Price Prediction Model
# ==============================

# 1️ Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# 2️ Load Data
df = pd.read_csv("cleaned_used_cars.csv")
print(" Data loaded:", df.shape)

# 3️ Define Features (X) and Target (y)
X = df.drop(columns=['Price'])
y = df['Price']

# 4️ Split Data into Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5️ Identify Column Types
numeric_features = ['Year', 'Kilometers_Driven', 'Mileage', 'Engine', 'Power']
categorical_features = ['Location', 'Fuel_Type', 'Transmission']

# 6️ Preprocessing
numeric_transformer = 'passthrough'
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# 7️ Build Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# 8️ Train Model
model.fit(X_train, y_train)

# 9️ Evaluate Model
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f" R² Score: {r2:.3f}")
#print(f" Mean Absolute Error: {mae:.3f}")

# 10 Example Prediction
sample = X_test.iloc[0:1]
predicted_price = model.predict(sample)[0]
print("\n Sample Car:")
print(sample)
print(f"\n Predicted Price: {predicted_price:.2f} Lakh")
