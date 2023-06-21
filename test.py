import json

def create_nft_json(example_file, output_file, num_items):
    with open(example_file) as f:
        data = json.load(f)

    # Get the example item
    example_item = data[0]

    # Create a list of items with different names
    items = []
    for i in range(num_items):
        item = example_item.copy()
        item['name'] = f"Your Collection #{i+1}"
        items.append(item)

    # Update the data array with the new items
    data = items

    # Write the updated data to the output file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

# Usage example
example_file = 'example.json'
output_file = 'new_collection.json'
num_items = 10010

create_nft_json(example_file, output_file, num_items)
