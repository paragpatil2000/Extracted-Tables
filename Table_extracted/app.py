import spacy
from spacy_layout import spaCyLayout
import pandas as pd
import json
import os

# Create a spaCy NLP object
nlp = spacy.blank("en")

# Initialize spaCyLayout
layout = spaCyLayout(nlp)

# Path to your PDF file
pdf_path = 'C:/Users/admin/Downloads/Account.pdf'

# Create output directory if it doesn't exist
output_dir = 'output_tables'
os.makedirs(output_dir, exist_ok=True)

# Process a document and create a spaCy Doc object
try:
    doc = layout(pdf_path)
except FileNotFoundError:
    print(f"The file '{pdf_path}' was not found.")
    exit()

# Tables in the document and their extracted data
tables_json = []
for i, table in enumerate(doc._.tables):
    # Token position and bounding box
    print(table.start, table.end, table._.layout)
    # pandas.DataFrame of contents
    table_data = table._.data
    print(table_data)
    # Convert DataFrame to JSON
    table_json = table_data.to_json(orient='split')
    tables_json.append(json.loads(table_json))
    
    # Save DataFrame to CSV
    csv_filename = os.path.join(output_dir, f'table_{i+1}.csv')
    table_data.to_csv(csv_filename, index=False)
    print(f"CSV file saved to: {csv_filename}")
    
    # Save DataFrame to Excel
    excel_filename = os.path.join(output_dir, f'table_{i+1}.xlsx')
    table_data.to_excel(excel_filename, index=False)
    print(f"Excel file saved to: {excel_filename}")

# Save all tables JSON to a file
json_filename = os.path.join(output_dir, 'tables.json')
with open(json_filename, 'w') as json_file:
    json.dump(tables_json, json_file, indent=4)
print(f"JSON file saved to: {json_filename}")

# Print the JSON output
print(json.dumps(tables_json, indent=4))

# Define a display function for tables
def display_table(df: pd.DataFrame) -> str:
    return f"Table with columns: {', '.join(df.columns.tolist())}"

# Reinitialize spaCyLayout with the display function
layout = spaCyLayout(nlp, display_table=display_table)