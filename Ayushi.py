# Import libraries
import pandas as pd

# Load CSV file
df = pd.read_csv("Medical Appointment No Shows.csv")

# View first 5 rows
print(df.head())

# Check basic info
print(df.info())

# -----------------------------
# DATA CLEANING STARTS HERE
# -----------------------------

# 1. Handle missing values
print(df.isnull().sum())  # check missing
df = df.dropna()          # remove missing rows (or use fillna)

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. Standardize text (example: gender)
df['Gender'] = df['Gender'].str.lower()

# 4. Convert date format
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# 5. Rename columns (clean format)
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 6. Fix data types
df['age'] = df['age'].astype(int)

# Final cleaned data preview
print(df.head())

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)
