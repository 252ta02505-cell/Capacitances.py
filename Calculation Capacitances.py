# Capacitances.py

def series_capacitance(capacitances):
    """Calculate equivalent capacitance for capacitors in series."""
    return 1 / sum(1 / c for c in capacitances)


def parallel_capacitance(capacitances):
    """Calculate equivalent capacitance for capacitors in parallel."""
    return sum(capacitances)


print("Capacitance Calculator")
print("1. Series")
print("2. Parallel")

choice = input("Enter your choice (1/2): ")

values = input("Enter capacitance values in farads, separated by spaces: ")
capacitances = [float(c) for c in values.split()]

if choice == "1":
    result = series_capacitance(capacitances)
    print(f"Equivalent capacitance = {result:.6g} F")

elif choice == "2":
    result = parallel_capacitance(capacitances)
    print(f"Equivalent capacitance = {result:.6g} F")

else:
    print("Invalid choice.")
