print("***********************************")
print("Welcome to Start Inventory Auditor")
print("***********************************")

total_inventory = 0
rejected_count = 0

while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()
    
    # 1. Exit condition
    if user_input.lower() == 'quit':
        break
    
    # 2. Reject negative numbers
    elif user_input.startswith('-') and user_input[1:].isdigit():
        print("Error: Negative stock values are not allowed.")
        rejected_count += 1
        
    # 3. Reject non-numeric strings (e.g., "ten")
    elif not user_input.isdigit():
        print("Error: Invalid entry. Please enter a positive whole number.")
        rejected_count += 1
        
    # 4. Valid integer input processing
    else:
        quantity = int(user_input)
        total_inventory += quantity
        
        # Check for overstock capacity
        if total_inventory > 500:
            print("ALERT: Overstock threshold exceeded (> 500 units)! Process halted.")
            break
        else:
            print(f"Accepted {quantity} units. Current Total: {total_inventory}")

# Final Reporting
print("\n--- Inventory Audit Report ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {rejected_count}")