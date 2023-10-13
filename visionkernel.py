import argparse
import boto3
import pandas as pd
import os

def upload_file_to_s3(bucket_name, local_file_path, s3_file_name):
    s3 = boto3.client('s3')
    s3.upload_file(local_file_path, bucket_name, s3_file_name)

def convert_text_to_csv_or_excel(input_text, output_file, to_format):
    if to_format.lower() == 'csv':
        # Read the text file into a DataFrame and write it as CSV
        df = pd.read_csv(input_text, sep='\t')  # Adjust the separator if needed
        df.to_csv(output_file, index=False)
    elif to_format.lower() == 'xls':
        # Read the text file into a DataFrame and write it as Excel
        df = pd.read_csv(input_text, sep='\t')  # Adjust the separator if needed
        df.to_excel(output_file, index=False)
    else:
        print("Invalid target format. Supported formats are 'csv' and 'xls'.")

def main():
    parser = argparse.ArgumentParser(description="Upload files to AWS S3 and convert text files to CSV or Excel")
    parser.add_argument("bucket", help="Name of the S3 bucket")
    parser.add_argument("local_file", help="Local file path (text, CSV, or Excel)")
    parser.add_argument("s3_file_name", help="Name for the file on S3")
    parser.add_argument("--convert", help="Convert text file to CSV or Excel and specify the output file format")
    
    args = parser.parse_args()

    if args.convert:
        target_format = args.convert.lower()
        if target_format in ['csv', 'xls']:
            converted_file = args.local_file.replace('.txt', f'.{target_format}')
            convert_text_to_csv_or_excel(args.local_file, converted_file, target_format)
            upload_file_to_s3(args.bucket, converted_file, args.s3_file_name)
            print(f"Text file converted to {target_format}: {converted_file}")
        else:
            print("Invalid target format. Supported formats are 'csv' and 'xls.")
    else:
        upload_file_to_s3(args.bucket, args.local_file, args.s3_file_name)
        print(f"File uploaded to {args.bucket}/{args.s3_file_name}")

if __name__ == "__main__":
    main()