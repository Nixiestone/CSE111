import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip header row
            
            for row in reader:
                if len(row) != 0:
                    key = row[key_column_index]
                    dictionary[key] = row
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Error: missing file\n{error}")
    except PermissionError as error:
        raise PermissionError(f"Error: permission denied\n{error}")
    
    return dictionary

def main():
    try:
        # Store information
        STORE_NAME = "Inkom Emporium"
        TAX_RATE = 0.06
        
        # Read products dictionary
        products_dict = read_dictionary("products.csv", 0)
        
        # Initialize receipt variables
        ordered_items = []
        total_items = 0
        subtotal = 0.0
        
        # Process request.csv
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip header row
            
            for row in reader:
                if len(row) != 0:
                    product_number = row[0]
                    quantity = int(row[1])
                    
                    # Get product info
                    product_info = products_dict[product_number]
                    product_name = product_info[1]
                    price = float(product_info[2])
                    
                    # Calculate item total
                    item_total = quantity * price
                    
                    # Add to receipt lists
                    ordered_items.append({
                        'name': product_name,
                        'quantity': quantity,
                        'price': price,
                        'total': item_total
                    })
                    
                    # Update totals
                    total_items += quantity
                    subtotal += item_total
        
        # Calculate taxes and total
        sales_tax = subtotal * TAX_RATE
        total = subtotal + sales_tax
        
        # Get current date and time
        current_date_and_time = datetime.now()
        
        # Print receipt
        print(STORE_NAME)
        for item in ordered_items:
            print(f"{item['name']}: {item['quantity']} @ {item['price']:.2f}")
        
        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("\nThank you for shopping at the Inkom Emporium.")
        print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))
        
        # EXCEEDING REQUIREMENTS: New Years Sale reminder
        today = datetime.now()
        new_year = datetime(today.year + 1, 1, 1)
        days_until_new_year = (new_year - today).days
        print(f"\nOnly {days_until_new_year} days until our New Years Sale!")
    
    except FileNotFoundError as error:
        print(error)
    except PermissionError as error:
        print(error)
    except KeyError as error:
        print(f"Error: unknown product ID in the request.csv file\n{error}")

if __name__ == "__main__":
    main()