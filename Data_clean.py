# -*- coding: utf-8 -*-
"""Data_clean.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19H_XCb2OKOtii_zW6zVjh26UUnJieZj2
"""

import pandas as pd
import re

# Load the CSV file
df = pd.read_csv('Fashion_clothing.csv')

# Clean and preprocess the data
def clean_text(text):
    # Remove special characters except alphabets, numbers, and spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Convert text to lowercase
    text = text.lower()
    # Address inconsistencies or specific cleaning requirements
    # Add your specific cleaning logic here if needed
    return text

# Apply cleaning to selected columns
columns_to_clean = ['ProductName', 'ProductBrand', 'Description', 'Gender']
for column in columns_to_clean:
    df[column] = df[column].apply(clean_text)


# Save the cleaned data to a new CSV file
df.to_csv('cleaned_dataset.csv', index=False)

print("Cleaned data saved to 'cleaned_dataset.csv'.")