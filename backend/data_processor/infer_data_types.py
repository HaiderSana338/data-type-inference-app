import pandas as pd
from django.core.files.uploadedfile import InMemoryUploadedFile
import os

def load_and_infer(uploaded_file):
    # Check if the uploaded_file is an InMemoryUploadedFile
    if isinstance(uploaded_file, InMemoryUploadedFile):
        # Use the file-like object directly
        file_extension = os.path.splitext(uploaded_file.name)[1]  # Get the file extension
    else:
        raise ValueError("Unsupported file type")

    # Read the uploaded file into a DataFrame
    try:
        if file_extension == '.csv':
            df = pd.read_csv(uploaded_file, low_memory=False)  # Set low_memory to False for better type inference
        elif file_extension in ('.xls', '.xlsx'):
            df = pd.read_excel(uploaded_file)
        else:
            raise ValueError("Unsupported file type")
    except Exception as e:
        return {"error": str(e)}

    inferred_types = {}

    for column in df.columns:
        inferred_type = infer_column_type(df[column])
        inferred_types[column] = inferred_type

    # Convert numpy types to strings for output
    inferred_types = {k: str(v) for k, v in inferred_types.items()}

    return {"inferred_data": inferred_types}

def infer_column_type(series):
    # Check for datetime format
    try:
        converted = pd.to_datetime(series, errors='coerce')
        if not converted.isnull().all():  # If not all values are NaT
            return converted.dtype  # Return the inferred datetime type
    except Exception:
        pass

    # Check for numeric types
    try:
        converted = pd.to_numeric(series, errors='coerce')
        if not converted.isnull().all():  # If not all values are NaN
            if converted.dtype.kind in 'biuf':  # Integer or float
                return converted.dtype  # Return the inferred numeric type
    except Exception:
        pass

    # Check for categorical data
    if series.dtype == 'object':
        # Identify categorical data based on unique value count
        unique_count = series.nunique()
        total_count = len(series)
        if unique_count < total_count * 0.5:  # Arbitrary threshold for categories
            return 'category'
        else:
            return 'object'

    return series.dtype  # Default return of current dtype

# Example usage
if __name__ == "__main__":
    # The following line is for testing. In your Django view, you would replace this with the actual uploaded file.
    uploaded_file = "path/to/your/testfile.csv"  # Change this to an actual InMemoryUploadedFile in your view
    result = load_and_infer(uploaded_file)
    print(result)










