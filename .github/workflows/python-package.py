import pandas as pd

# Load dataset
df = pd.read_csv('/mnt/data/Medical Appointment No Shows.csv')

# Display basic info
print("Initial shape:", df.shape)
print(df.info())

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Handle missing values
# Check missing values
print(df.isnull().sum())

# Fill or drop missing values
df = df.dropna()   # OR use fillna() if needed

# 3. Standardize column names (lowercase, remove spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 4. Convert date columns to datetime
if 'scheduledday' in df.columns:
    df['scheduledday'] = pd.to_datetime(df['scheduledday'])

if 'appointmentday' in df.columns:
    df['appointmentday'] = pd.to_datetime(df['appointmentday'])

# 5. Fix inconsistent data (example: gender)
if 'gender' in df.columns:
    df['gender'] = df['gender'].str.upper()

# 6. Remove invalid ages
if 'age' in df.columns:
    df = df[df['age'] >= 0]

# 7. Convert categorical values (No-show column)
if 'no-show' in df.columns:
    df['no-show'] = df['no-show'].map({'No': 0, 'Yes': 1})

# 8. Reset index after cleaning
df = df.reset_index(drop=True)

# Final output
print("Cleaned shape:", df.shape)
print(df.head())

# Save cleaned dataset
df.to_csv('/mnt/data/cleaned_medical_data.csv', index=False)

print("Cleaned dataset saved successfully!")
    
