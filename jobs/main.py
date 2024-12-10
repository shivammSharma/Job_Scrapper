import os
import pandas as pd
import glob 
from proto.spiders.simplyReact import SimplyReactSpider
from proto.spiders.simplyJava import simplyJavaSpider
from proto.spiders.simplyAndroid import SimplyAndroidSpider
from proto.spiders.simplyCloud import simplyCloudSpider
from proto.spiders.simplyFrontEnd import simplyFrontSpider
from proto.spiders.internAndroid import InternshipAndroidSpider
from proto.spiders.internFrontEnd import InternshipFrontEndSpider
from proto.spiders.internJava import InternshipJavaSpider
from proto.spiders.internloud import InternshipCloudSpider
from proto.spiders.internWebDev import InternshipWebSpider
from proto.spiders.web3FullStack import Web3FullSpider
from proto.spiders.web3Js import Web3JsSpider
from proto.spiders.web3Solana import Web3SolanaSpider
from proto.spiders.web3Solidity import Web3SoliditySpider

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def crawl_data():
    """Run all the spiders to scrape data."""
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    # Add all the spiders to the process
    process.crawl(simplyJavaSpider)
    process.crawl(SimplyReactSpider)
    process.crawl(SimplyAndroidSpider)
    process.crawl(simplyCloudSpider)
    process.crawl(simplyFrontSpider)
    process.crawl(InternshipAndroidSpider)
    process.crawl(InternshipJavaSpider)
    process.crawl(InternshipCloudSpider)
    process.crawl(InternshipFrontEndSpider)
    process.crawl(InternshipWebSpider)
    process.crawl(Web3SoliditySpider)
    process.crawl(Web3FullSpider)
    process.crawl(Web3SolanaSpider)
    process.crawl(Web3JsSpider)

    process.start()

def merge_csv_files():

    folder_path = "data"

    # Get all CSV files in the folder
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

    # List to store DataFrames
    dataframes = []

    # Loop through each CSV file
    for file in csv_files:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file)
        
        # Inspect the first few rows to check structure (for debugging purposes)
        print(f"Inspecting {file}:")
        print(df.head())  # Check the first few rows to ensure the structure

        # Filter out rows based on the second column (assuming it's named 'experience' or similar)
        if df.shape[1] > 1:  # Ensure there are at least two columns
            # Assuming the second column (index 1) contains the '1y' and '2y' data
            df['experience'] = df.iloc[:, 1].astype(str).str.strip()  # Convert second column to string

            # Remove rows where the second column contains '1y' or '2y'
            df = df[~df['experience'].str.contains(r'1\s?y|1\s?years?|2\s?y|2\s?years?', na=False, case=False)]
        
        # Remove duplicate URLs (assuming URLs are in the last column)
        if 'url' in df.columns:  # If there is a column named 'url'
            df = df.drop_duplicates(subset=['url'], keep='first')  # Keep only the first occurrence of each URL

        # Append the cleaned DataFrame to the list
        dataframes.append(df)

    # Merge all DataFrames into one
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Shuffle the merged DataFrame (optional)
    merged_df = merged_df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Save the merged DataFrame to a new CSV file
    output_file = os.path.join(folder_path, "merged_output_no_duplicates_1y_2y_removed.csv")
    merged_df.to_csv(output_file, index=False)

    print(f"Files have been merged, duplicates and 1y/2y removed, and saved to {output_file}")

if __name__ == "__main__":
    # Step 1: Crawl data
    crawl_data()

    # Step 2: Merge all CSV files in 'data' folder
    # merge_csv_files()
