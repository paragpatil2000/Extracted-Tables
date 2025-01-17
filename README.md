#Table Extracted any pdf 


## Overview
This application is a PDF extraction service that allows users to upload PDF files, extract text and tables, and save the results in Excel, CSV, and JSON formats. It leverages Optical Character Recognition (OCR) and table extraction techniques to provide an easy-to-use interface for data extraction from PDFs.

## Features
- Upload PDF files for extraction.
- Save extracted data in multiple formats (Excel, CSV, JSON).
- Simple web interface for easy interaction.


### Software Requirements
- **Python Version**: 3.10 

### Create virtual environment
python -m nenv nenv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### Libraries
The following Python libraries are required to run this application:
- pandas
- numpy
- Scipy
- spacy
- spacy_layout

#### Using the Application
Upload a PDF: Use the web interface to upload a PDF file.
Data Extraction: The app will extract text and tables from the uploaded file.
Download Results: After processing, download the extracted data in Excel, CSV, or JSON format.
