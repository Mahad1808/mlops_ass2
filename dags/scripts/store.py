import pandas as pd
import os


def store_data(preprocessed_data):
    # Sample processed data
   
    
    # Convert processed data to a DataFrame
    df = pd.DataFrame(preprocessed_data)
    
    # Define the directory where you want to save the file
    storage_directory = "processed_data"
    
    # Create the directory if it doesn't exist
    if not os.path.exists(storage_directory):
        os.makedirs(storage_directory)
    
    # Define the path for the CSV file
    storage_path = os.path.join(storage_directory, "preprocessed_data.csv")
    
    # Write the DataFrame to a CSV file
    df.to_csv(storage_path, index=False)


if __name__ == "__main__":
    # Load preprocessed data (replace this with your actual preprocessed data)
    preprocessed_data = [
        {"title": "Preprocessed Title 1", "description": "Preprocessed Description 1", "link": "Preprocessed Link 1"},
        {"title": "Preprocessed Title 2", "description": "Preprocessed Description 2", "link": "Preprocessed Link 2"},
        # Add more preprocessed data here
    ]

    # Store the preprocessed data
    store_data(preprocessed_data)
