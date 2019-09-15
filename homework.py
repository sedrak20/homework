#variables
price_vodka = 5
vodka_txt = 'Vodka'
price_wiskey = 8
wiskey_txt = 'Wiskey'
price_beer = 3
beer_txt = 'Beer'
price_limon_juice = 3
lemon_txt = 'Lemon Juice'
price_orange_juice = 3,5
orange_txt = 'Orange Juice'
checker_sportsman = True
checker_driver = False
# main codes
total_alcohol = price_wiskey + price_vodka
total_fresh = str(price_orange_juice) + str(price_limon_juice)
print('You bought: ' + wiskey_txt +', '+ vodka_txt )
print('The total is: ' + str(total_alcohol) + "$")
print('for driver:' + str(checker_driver) + ",because he drunk alcohol " )