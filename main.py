import products
import store
import promotions

# setup initial stock of inventory
product_list = [
  products.Product("MacBook Air M2", price=1450, quantity=100),
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

best_buy = store.Store(product_list)

def show_all_products(store):
    print("All products in store:\n")
    for i, product in enumerate(store.get_all_products(), 1):
        # Get promotion info
        promotion = product.promotion
        promotion_text = promotion.name if promotion else "None"
        
        # Handle quantity display based on product type
        if isinstance(product, products.NonStockedProduct):
            quantity_text = "Unlimited"
        elif isinstance(product, products.LimitedProduct):
            quantity_text = f"Limited to {product.maximum} per order!"
        else:
            quantity_text = f"Quantity: {product.quantity}"
            
        print(f"{i}. {product.name}, Price: ${product.price}, {quantity_text}, Promotion: {promotion_text}")

def start(store):
    while True:
        print("Store Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit\n")        
        user_input = input("Enter your choice: ")
        if user_input == "1":
            show_all_products(store)
        elif user_input == "2":
            print(f"Total of {store.get_total_quantity()} items in store\n")
        elif user_input == "3":
            shopping_list = []
            while True:
                show_all_products(store)
                wantedProduct = input("Which product # do you want? (0 to finish)\n")
                
                if wantedProduct == "0":
                    if shopping_list:
                        total = store.order(shopping_list)
                        print(f"\nOrder made! Total payment: ${total}\n")
                    break
                    
                if not wantedProduct.isdigit():
                    print("\nProduct number must be a number\n")
                    continue
                    
                wanted_amt = input("What amount do you want? ")
                if not wanted_amt.isdigit():
                    print("Amount must be a number\n") 
                    continue
                
                product_idx = int(wantedProduct) - 1
                quantity = int(wanted_amt)
                
                try:
                    product = store.get_all_products()[product_idx]
                    # Validate quantity before adding to cart
                    if quantity > product.quantity:
                        print(f"Error: {product.name} has only {product.quantity} items in stock\n")
                        continue
                    if quantity <= 0:
                        print("Error: Amount must be greater than 0\n")
                        continue
                    
                    shopping_list.append((product, quantity))
                    print("Product added to cart!\n")
                except IndexError:
                    print("Error: Invalid product number\n")
                    continue
                
        elif user_input == "4":
            print("Thank you for shopping with us!\n")
            break

if __name__ == "__main__":
    start(best_buy)
