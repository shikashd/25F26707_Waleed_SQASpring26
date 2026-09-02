customer_spending = [1200, 750, 300, 1500, 450]

for spending in customer_spending:
    print("Processing spending value:", spending)

    if spending >= 1000:
        print(spending, "- High-value customer")
    elif spending >= 500:
        print(spending, "- Medium-value customer")
    else:
        print(spending, "- Low-value customer")
