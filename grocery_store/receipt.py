import csv
import os

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    dictionary = {}
    
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        
        for row in reader:
            if len(row) != 0:  # Skip empty rows
                key = row[key_column_index]
                dictionary[key] = row
                
    return dictionary

def main():
    try:
        # Read the products dictionary
        products_dict = read_dictionary("products.csv", 0)
        
        print("All Products")
        print(products_dict)
        print()
        
        print("Requested Items")
        
        # Open the request file and process each row
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            
            for row in reader:
                if len(row) != 0:  # Skip empty rows
                    product_number = row[0]
                    quantity = int(row[1])
                    
                    # Get the product info from the dictionary
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    price = float(product_info[2])
                    
                    # Print the product details
                    print(f"{product_name}: {quantity} @ {price:.2f}")
    
    except FileNotFoundError as error:
        print("Error: missing file")
        print(error)
    except PermissionError as error:
        print("Error: permission denied")
        print(error)
    except KeyError as error:
        print("Error: unknown product ID in the request.csv file")
        print(error)

if __name__ == "__main__":
    main()