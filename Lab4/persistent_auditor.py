print("***********************************")
print("Welcome to Start Inventory Auditor")
print("***********************************")

INVENTORY_FILE = "inventory.txt"

def get_valid_input():
    """
    Prompts the user for a stock quantity.
    Input:  None
    Output: - an integer (valid quantity), or
            - the string 'quit' (exit signal), or
            - None (invalid/rejected entry)
    """
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
 
    if user_input.lower() == 'quit':
        return 'quit'
    elif user_input.startswith('-') and user_input[1:].isdigit():
        print("Error: Negative stock values are not allowed.")
        return None
    elif not user_input.isdigit():
        print("Error: Invalid entry. Please enter a positive whole number.")
        return None
    else:
        return int(user_input)
 
 
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
 
 
def load_inventory(filename):
    """
    Reads previously saved state from disk.
    Input:  filename (str)
    Output: (total, history) tuple
            total   -> int, the saved running total (0 if no file / empty file)
            history -> list of int, every past transaction amount ([] if none)
    Never raises an error if the file is missing - starts fresh instead.
    """
    try:
        with open(filename, "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return 0, []
 
    if not lines:
        return 0, []
 
    total = int(lines[0])
    history = [int(line) for line in lines[1:] if line.strip() != ""]
    return total, history
 
 
def save_inventory(filename, total, history):
    """
    Writes the current total and transaction history to disk.
    Input:  filename (str), total (int), history (list of int)
    Output: None
    File format: first line = total, each following line = one past transaction.
    """
    with open(filename, "w") as f:
        f.write(f"{total}\n")
        for amount in history:
            f.write(f"{amount}\n")
 
 
def generate_report(total_units, deliveries_processed, failed_attempts, total_tax, history):
    """
    Input:  total_units, deliveries_processed, failed_attempts, total_tax, history
    Output: None (prints the final summary)
    """
    print("\n--- Inventory Audit Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Total Deliveries Processed (this session): {deliveries_processed}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    print(f"Total Tax Collected (this session): {total_tax:.2f}")
    print(f"Full Transaction History: {history}")
 
 
def main():
    # Load whatever was saved from a previous run (or start empty)
    total_inventory, transaction_history = load_inventory(INVENTORY_FILE)
 
    if transaction_history:
        print(f"Loaded existing inventory: {total_inventory} units, "
              f"{len(transaction_history)} past transaction(s).")
    else:
        print("No existing inventory found. Starting fresh.")
 
    rejected_count = 0
    deliveries_processed = 0
    total_tax_collected = 0
 
    while True:
        result = get_valid_input()
 
        # Exit condition
        if result == 'quit':
            break
 
        # Invalid entry - message already printed inside get_valid_input()
        elif result is None:
            rejected_count += 1
            continue
 
        # Valid integer input processing
        else:
            quantity = result
            tax = calculate_tax(quantity)
            total_inventory = process_delivery(total_inventory, quantity)
            transaction_history.append(quantity)
            total_tax_collected += tax
            deliveries_processed += 1
 
            # Check for overstock capacity
            if total_inventory > 500:
                print("ALERT: Overstock threshold exceeded (> 500 units)! Process halted.")
                break
            else:
                print(f"Accepted {quantity} units (Tax: {tax:.2f}). Current Total: {total_inventory}")
 
    # Write-back: persist total + full history so the next run can resume
    save_inventory(INVENTORY_FILE, total_inventory, transaction_history)
    print(f"\nInventory saved to {INVENTORY_FILE}.")
 
    generate_report(total_inventory, deliveries_processed, rejected_count,
                     total_tax_collected, transaction_history)
 
 
if __name__ == "__main__":
    main()