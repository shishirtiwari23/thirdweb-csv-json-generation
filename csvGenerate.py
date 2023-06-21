import csv

def create_nft_csv_from_csv(csv_file, output_file, start_token, end_token):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Create a new CSV file with the desired data
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(start_token, end_token + 1):
            item = {
                "name": f"Token {i} Name",
                "description": f"Token {i} Description",
                "external_url": rows[0]["external_url"],  # Assuming it's the same for all rows
                "background_color": rows[0]["background_color"],  # Assuming it's the same for all rows
                "youtube_url": rows[0]["youtube_url"],  # Assuming it's the same for all rows
                "additional": rows[0]["additional"],  # Assuming it's the same for all rows
                "properties": rows[0]["properties"],  # Assuming it's the same for all rows
                "can be": rows[0]["can be"],  # Assuming it's the same for all rows
                "added": rows[0]["added"]  # Assuming it's the same for all rows
            }
            writer.writerow(item)

# Usage example
csv_file = 'example.csv'
output_file = 'new_collection.csv'
start_token = 0
end_token = 10009

create_nft_csv_from_csv(csv_file, output_file, start_token, end_token)
