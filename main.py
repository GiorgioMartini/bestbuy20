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
    print("All products in store:")
    for i, product in enumerate(store.get_all_products(), 1):
        print(f"{i}. {product.name}")

def start(store):
    while True:
        print("Store Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")        
        user_input = input("Enter your choice: ")
        if user_input == "1":
            show_all_products(store)
        elif user_input == "2":
            print(f"Total of {store.get_total_quantity()} items in store")
        elif user_input == "3":
            show_all_products(store)
            while True:
                wantedProduct = input("Which product # do you want? ")
                if not wantedProduct.isdigit():
                    print("Product number must be a number")
                    break
                wanted_amt = input("What amount do you want? ")
                if not wanted_amt.isdigit():
                    print("Amount must be a number") 
                    break
                
                product_idx = int(wantedProduct) - 1  # Subtract 1 because indices start at 0
                quantity = int(wanted_amt)
                
                product = store.get_all_products()[product_idx]
                
                shopping_list = [(product, quantity)]
                total = store.order(shopping_list)
                print(f"Order made! Total payment: ${total}")
                break
        elif user_input == "4":
            print("Thank you for shopping with us!")
            break

if __name__ == "__main__":
    start(best_buy)
