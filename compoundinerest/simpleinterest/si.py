def simple_interest(principal, rate, time):
    # Convert annual rate percentage to decimal
    rate = rate / 100
    interest = principal * rate * time
    amount = principal + interest
    return amount, interest


# Taking user inputs
P = float(input("Enter Principal: "))
R = float(input("Enter Rate (%): "))
T = int(input("Enter Time (years): "))

# Calculating simple interest
total, interest = simple_interest(P, R, T)

# Displaying results
print(f"Total Amount: {total:.2f}")
print(f"Simple Interest: {interest:.2f}")