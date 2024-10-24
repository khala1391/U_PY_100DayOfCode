def calculate_total(prices, discount):
    total = 0
    for price in prices:
        total += price
    total = apply_discount(total, discount)  # Apply discount
    return total

def apply_discount(total, discount):
    # Ensure discount is between 0 and 1
    if discount < 0 or discount > 1:
        raise ValueError("Discount must be between 0 and 1")
    return total * (1 - discount)

def main():
    items = ['apple', 'banana', 'orange']  # Correct item prices
    prices = [1.0, 0.5, 1.2]               # Prices of items in order
    discount = 0.2                         # Discount rate (20%)

    # Print item names and prices
    for i in range(len(items)):
        print(f"{items[i]}: ${prices[i]}")

    # Intentionally introduce a bug: calculate_total expects a list of numbers, not strings
    total = calculate_total(prices, discount)

    print(f"Total after {discount*100}% discount: ${total:.2f}")

# Run the main function
if __name__ == "__main__":
    main()
