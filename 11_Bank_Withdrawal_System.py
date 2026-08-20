#Q11 Bank Withdrawal System

balance = float(input("Enter your balance: ₹"))
withdrawal_amount = float(input("Enter your withdrawal amount: ₹"))

if balance <= 0 or withdrawal_amount <= 0:
    print("Invalid amount")

elif withdrawal_amount > balance:
    print("Insufficient balance")

else:
    remaining_balance = balance - withdrawal_amount

    print("Withdrawal successful")
    print(f"Remaining balance: ₹{remaining_balance:.2f}")
  
