This is a challenge we have to impement:

Part 1:
New product types
After using the program for a few months, the store owner says that some products are not supported by the program design.
Luckily, Inheritance and Polymorphism allows us to create new classes that behave differently, without having to change the rest of the code to support them. That’s the magic of OOP! 🏛️
Ready to start?
♾️ Non stocked products
Some products in the store are not physical, so we don’t need to keep track of their quantity. for example - a Microsoft Windows license. On these products, the quantity should be set to zero and always stay that way.
📦 Limited products
Some products can only be purchased X times in an order. For example - a shipping fee can only be added once. If an order is attempted with quantity larger than the maximum one, it should be refused with an exception.
Task
In the file products.py, create two new classes to support the new product types.
But hey, don’t create entirely new classes! Use inheritance to extend the original Product type, and make only the minimal changes necessary.
Make sure you override the show method in each class, to show the user the special characteristics of the products.
Hint: Use the super() function to avoid code repetition.
Test your code
Here’s a new initialization code for you to test:

# setup initial stock of inventory

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
products.Product("Google Pixel 7", price=500, quantity=250),
products.NonStockedProduct("Windows License", price=125),
products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]
best_buy = store.Store(product_list)

Part 2:

The Best Buy Store manager wants to apply discounts and promotions for certain products. The promotions you should implement are:
Percentage discount (i.e. 20% off)
Second item at half price
Buy 2, get 1 free
Assumptions
Single-Product Promotion
Promotions are applied on a single product only, no mixing. For example, if the promotion “Second item at half price” is applied on the Product Mac, then for every two Mac items that I bought I get one for free.
Single Promotion for each Product
Products can have only one promotion at a given time.
Bonus: support multiple promotions for a single item.
Implementation
We want to be able to add promotions to a product instance and remove them. We also want to be able to add the same promotion to multiple products without repeating code.
We want to create a Promotion class that will expose a simple interface. It will have an instance variable (member) for name, and only one method:
apply_promotion(product, quantity) -> float
This method gets 2 parameters - a product instance and a quantity, and returns the discounted price after promotion was applied.
Abstract class
Is there such thing as a general promotion? Can a store manager tell an employee to add a promotion to a product, without specifying which kind?
If you answered no, then it might be wise to make the Promotion class an abstract class.
❓ Don’t remember? Go back to the lesson about Abstract Classes.
Task
Create the promotions classes
Create the abstract class Promotion and three deriving classes for each of the promotions.
Update the Product class to support promotions
Add an instance variable (member) called promotion (it’s type is the Promotion class). Add a getter and setter methods for that variable.
Update the show method to also show the current promotion, if exists.
Update the buy method. If a promotion exists, it should determine the price using the promotion method apply_promotion.
Test your code
Here’s a new initialization code for you to test:

# setup initial stock of inventory

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
products.Product("Google Pixel 7", price=500, quantity=250),
products.NonStockedProduct("Windows License", price=125),
products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Create promotion catalog

second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products

product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)
