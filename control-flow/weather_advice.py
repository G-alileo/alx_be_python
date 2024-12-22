# Prompt User for Weather Input:
condition = input("What's the weather like today? (sunny/rainy/cold):")

#Recommend clothing
if condition == "sunny":
    print("Wear a t-shirt and sunglasses.")

elif condition == "rainy":
    print("Don't forget your umbrella and a raincoat.")

elif condition == "cold":
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("Sorry, I don't have recommendations for this weather")