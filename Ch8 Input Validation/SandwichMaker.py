import pyinputplus as pyip

total = 0
prices = {
    "wheat" : 1.00,
    "white" : 1.10,
    "sourdough" : 1.25,
    "chicken" : 2.00,
    "turkey" : 1.95,
    "ham" : 2.15,
    "tofu" : 2.25,
    "cheddar" : 0.25,
    "swiss" : 0.35,
    "mozzarella" : 0.30,
    "mayo": 0.05,
    "mustard" : 0.05,
    "lettuce" : 0.50,
    "tomato" : 0.45,
}

print("Which type of bread would you like?")
bread = pyip.inputMenu(["wheat","white","sourdough"])
print("Which type of protein would you like")
protein = pyip.inputMenu(["chicken","turkey","ham","tofu"])
cheese = pyip.inputYesNo("Would you like cheese?")
if cheese == "yes":
    cheeseType = pyip.inputMenu(["cheddar","swiss","mozzarella"])
else: cheeseType = "none"

mayo = pyip.inputYesNo("Would you like mayo?")
mustard = pyip.inputYesNo("Would you like mustard?")
lettuce = pyip.inputYesNo("Would you like lettuce?")
tomato = pyip.inputYesNo("Would you like tomato?")
quantity = pyip.inputInt("How many sandwiches would you like?", min=1)

total = (prices[bread] + prices[protein])
if cheese == "yes":
    total += prices[cheeseType]
if mayo == "yes":
    total += prices["mayo"]
if mustard == "yes":
    total += prices["mustard"]
if lettuce == "yes":
    total += prices["lettuce"]
if tomato == "yes":
    total += prices["tomato"]

total = total * quantity

print("Your total is $"+ "{:.2f}".format(total))
