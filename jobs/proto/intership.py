import csv

def clean_company_names(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        # Create a list to store cleaned data
        cleaned_data = []
        
        for row in reader:
            # Remove extra spaces from the company name
            row['company'] = ' '.join(row['company'].split())
            cleaned_data.append(row)

    # Write the cleaned data to a new CSV file
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)

    print(f"Cleaned data has been written to {output_file}")

# Specify the input and output file names
input_file = 'inernshala.csv'  # Change this to your input CSV file name
output_file = 'cleaned_internships.csv'  # Output file name

# Run the cleaning function
clean_company_names(input_file, output_file)