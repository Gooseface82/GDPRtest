import boto3
import pandas as pd
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
import json
import os
import io

# Initialize S3 client
s3 = boto3.client('s3')

def load_s3_file_info(export_dir):
    """
    Loads the S3 file info (bucket name and file path) from the JSON file.
    """
    file_path = os.path.join(export_dir, 's3_file_info.json')
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist")
        return None, None

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return data.get("bucket_name"), data.get("s3_file_path")

def convert_df_to_bytestream(df):
    """
    Converts a DataFrame to a bytestream.
    """
    bytestream = io.BytesIO()
    df.to_csv(bytestream, index=False)
    bytestream.seek(0)  # Reset the pointer to the beginning of the stream
    return bytestream

def read_csv_from_s3(bucket_name, s3_file_path):
    """
    Reads a CSV file from the specified S3 bucket and path.
    Converts the DataFrame to a bytestream.
    """
    try:
        # Get the object from S3
        response = s3.get_object(Bucket=bucket_name, Key=s3_file_path)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(response['Body'])
        
        # Convert DataFrame to bytestream
        bytestream = convert_df_to_bytestream(df)
        
        return bytestream
    except s3.exceptions.NoSuchKey:
        print(f"The file {s3_file_path} does not exist in the bucket {bucket_name}")
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except ClientError as e:
        print(f"An S3 client error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

# Example usage
if __name__ == '__main__':
    # Directory where JSON file is stored
    export_dir = 'output/s3_files'
    
    # Load bucket name and s3_file_path from JSON
    bucket_name, s3_file_path = load_s3_file_info(export_dir)

    if bucket_name and s3_file_path:
        # Read the CSV from S3 and convert to bytestream
        bytestream = read_csv_from_s3(bucket_name, s3_file_path)

        # Print DataFrame if it was successfully loaded
        if bytestream is not None:
            # Read bytestream into DataFrame to display
            df = pd.read_csv(bytestream)
            print('***************data frame***************')
            print(df)
            print('***************bytestream***************') 
            print (bytestream.getvalue().decode('utf-8'))
        else:
            print("Failed to load bytestream, try uploading some data 1st.")
    else:
        print("Failed to retrieve bucket name or S3 file path. Try uploading data first using upload.py")


