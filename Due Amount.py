def dueAmount(b, g):
    if g > b:
        return f"Change to be returned: {g - b}"
    
    elif g < b:
        needed_amount = b - g
        days_to_work = needed_amount / 100
        
        return f"More money needed: {needed_amount}. " \
               f"You need to work for {days_to_work:.2f} days in the kitchen."
    
    else:
        return "Exact amount given, no change needed."


bill = float(input("Enter amount of Bill: "))
given = float(input("Given amount: "))

res = dueAmount(bill, given)
print(res)