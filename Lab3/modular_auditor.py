print("***********************************")
print("Welcome to Start Inventory Auditor")
print("***********************************")

total_inventory = 0
rejected_count = 0


def get_valid_input():
    """
    Prompts the user for a stock quantity.
    Input:  None
    Output: - an integer (valid quantity), or
            - the string 'quit' (exit signal), or
            - None (invalid/rejected entry)
    """
    get_user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
 
    if get_user_input.lower() == 'quit':
        return 'quit'
    elif get_user_input.startswith('-') and get_user_input[1:].isdigit():
        print("Error: Negative stock values are not allowed.")
        return None
    elif not get_user_input.isdigit():
        print("Error: Invalid entry. Please enter a positive whole number. Letters and symbols are not allowed")
        return None
    else:
        return int(get_user_input)

def process_delivery(current_total, new_value):
    """
    Input:  current_total (int), new_value (int)
    Output: the new running total (int)
    """
    return current_total + new_value

def calculate_tax(amount):
    """
    Input:  amount (int/float) - the value of a single delivery
    Output: the tax owed on that delivery (10%)
    """
    return amount * 0.10

def generate_report(total_units, deliveries_processed, failed_attempts, total_tax):
    """
    Input:  total_units, deliveries_processed, failed_attempts, total_tax
    Output: None (prints the final summary)
    """
    print("\n--- Inventory Audit Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    print(f"Total Tax Collected: {total_tax:.2f}")

def main():
    total_inventory = 0
    rejected_count = 0
    deliveries_processed = 0
    total_tax_collected = 0
 
    while True:
        result = get_valid_input()

        # Exit condition
        if result == 'quit':
            break

        elif result is None:
            rejected_count += 1
            continue

        else:
            quantity = result
            tax = calculate_tax(quantity)
            total_inventory = process_delivery(total_inventory, quantity)
            total_tax_collected += tax
            deliveries_processed += 1

# Final Reporting
            if total_inventory > 500:
                print("ALERT: Overstock threshold exceeded (> 500 units)! Process halted.")

                break
            else:
                print(f"Accepted {quantity} units (Tax: {tax:.2f}). Current Total: {total_inventory}")
    generate_report(total_inventory, deliveries_processed, rejected_count, total_tax_collected)
    
if __name__ == "__main__":
    main()