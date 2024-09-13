#shipping cost calculator

##input package weight and shipping rate
weight= float(input("enter the package weight in kilograms"))
rate= float(input("enter the shipping rate per kilogram"))

##calculate the shipping cost
shipping_cost= weight*rate

##display the results
print(f"shipping_cost: {shipping_cost} USD")
