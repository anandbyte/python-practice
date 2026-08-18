# Q12 — Simple Discount Calculator

amount = float(input("Enter your purchase amount: "))

if amount >= 1000:
    discount = amount * 0.10
    final_amount = amount - discount
    print(f"Your final discounted amount: {final_amount}")

elif amount >= 500:
    discount = amount * 0.05
    final_amount = amount - discount
    print(f"Your final discounted amount: {final_amount}")

else:
    print("No discount")
