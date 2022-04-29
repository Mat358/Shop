import os


cls = lambda: os.system('cls')

class Products():

    def __init__(self, cost, stock, cart, option):
        self.cost = cost
        self.stock = stock
        self.cart = cart
        self.option = option
   
choice = Products(None, None, None, None)
apple = Products(2.00, 20, 0, None)
carrot = Products(1.50, 50, 0, None)

print('Welcome to FoodMarket, please choose what You want to buy:')


while choice.option !=3:
        try: 
            choice.option = int(input('1.Apple\n2.Carrot\n3.Finalize transaction\nInput number 1-3: '))
            if  choice.option == 1:
                cls()
                apple_qty = int(input(f'You choose an apple, how much do You need?\nCurrent stock is: ' + str(apple.stock) + '\nPlease input qty: '))
                
                if apple_qty <= apple.stock:
                    apple.stock -= apple_qty
                    apple.cart += apple_qty 
                    choice.option
                    cls()
                else:
                    print('Not enought apples in stock.')

            elif  choice.option == 2:
                cls()
                carrot_qty = int(input(f'You choose a carrot, how much do You need?\nCurrent stock is: ' + str(carrot.stock) + '\nPlease input qty: '))
                
                if carrot_qty <= carrot.stock:
                    carrot.stock -= carrot_qty
                    carrot.cart += carrot_qty 
                    cls()
                else:
                    print('Not enought carrots in stock.')

            elif choice.option == 3:
                total_cost = (apple.cost * apple.cart) + (carrot.cost * carrot.cart)
                foramted_total_cost = "{:.2f}".format(total_cost)

                total_cost_vat = (total_cost * 1.23)
                fromated_total_cost_vat = "{:.2f}".format(total_cost_vat)

                print('*' * 50)
                print('You bought:\n' + str(apple.cart) +' Appels\n' + str(carrot.cart) + ' Carrots')
                print('*' * 50)
                print('Total cost will be:\n' + str(foramted_total_cost) + ' zl net\n' + 'It will be:\n' + str(fromated_total_cost_vat) + ' zl including VAT')

        except ValueError:
            cls()
            print('Please input number.')
 


