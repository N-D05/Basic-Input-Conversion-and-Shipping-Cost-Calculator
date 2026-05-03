#PROblem 2
# #of packages
packages = int(input("Enter # of packages to ship: "))

# shipping type
shipping_type = input("Enter r for regular, e for express: ")

# cost for each type
if shipping_type == "r":
    rate = 10
elif shipping_type == "e":
    rate = 15
else:
    print("Invalid shipping type")
    rate = 0

# total cost
total_cost = packages * rate

# Show cost
print("Total cost: $", total_cost)