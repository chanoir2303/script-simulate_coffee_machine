# data
actions = ['buy', 'fill', 'take', 'remaining', 'exit']
recipes = ['espresso', 'latte', 'cappuccino']
stock = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'price': 550}
espresso_recipe = {'water': 250, 'milk': 0, 'beans': 16, 'cups': 1, 'price': 4}
latte_recipe = {'water': 350, 'milk': 75, 'beans': 20, 'cups': 1, 'price': 74}
cappuccino_recipe = {'water': 200, 'milk': 100, 'beans': 12, 'cups': 1, 'price': 6}
final_stock = {'water': 0, 'milk': 0, 'beans': 0, 'cups': 0, 'price': 0}


def buy():
    # choice between 3 types of coffee
    coffee_choice = input(f'\nWhat do you want to buy? 1 - {recipes[0]}, 2- {recipes[1]}, 3 - {recipes[2]} \n')

    # calculate stock - recipe for each ingredients
    if coffee_choice == '1':
        final_stock = {
            'water': stock['water'] - espresso_recipe['water'],
            'milk': stock['milk'] - espresso_recipe['milk'],
            'beans': stock['beans'] - espresso_recipe['beans'],
            'cups': stock['cups'] - espresso_recipe['cups'],
            'price': stock['price'] + espresso_recipe['price']
        }
        print(f'\nThe coffee machine has:\n'
              f'{final_stock["water"]} of water\n'
              f'{final_stock["milk"]} of milk\n'
              f'{final_stock["beans"]} of coffee beans\n'
              f'{final_stock["cups"]} of disposable cups\n'
              f'{final_stock["price"]} of money')
    elif coffee_choice == '2':
        final_stock = {
            'water': stock['water'] - latte_recipe['water'],
            'milk': stock['milk'] - latte_recipe['milk'],
            'beans': stock['beans'] - latte_recipe['beans'],
            'cups': stock['cups'] - latte_recipe['cups'],
            'price': stock['price'] + latte_recipe['price']
        }
        print(f'\nThe coffee machine has:\n'
              f'{final_stock["water"]} of water\n'
              f'{final_stock["milk"]} of milk\n'
              f'{final_stock["beans"]} of coffee beans\n'
              f'{final_stock["cups"]} of disposable cups\n'
              f'{final_stock["price"]} of money')
    elif coffee_choice == '3':
        final_stock = {
            'water': stock['water'] - cappuccino_recipe['water'],
            'milk': stock['milk'] - cappuccino_recipe['milk'],
            'beans': stock['beans'] - cappuccino_recipe['beans'],
            'cups': stock['cups'] - cappuccino_recipe['cups'],
            'price': stock['price'] + cappuccino_recipe['price']
        }
        print(f'\nThe coffee machine has:\n'
              f'{final_stock["water"]} of water\n'
              f'{final_stock["milk"]} of milk\n'
              f'{final_stock["beans"]} of coffee beans\n'
              f'{final_stock["cups"]} of disposable cups\n'
              f'{final_stock["price"]} of money')


def fill():
    # ask amount of each ingredients to add
    fill_water = input('Write how many ml of water you want to add:\n')
    fill_milk = input('Write how many ml of milk you want to add\n')
    fill_beans = input('Write how many grams of coffee beans you want to add:\n')
    fill_cups = input('Write how many disposable coffee cups you want to add:\n')

    # calculate stock + fill
    final_stock = {
        'water': stock['water'] + int(fill_water),
        'milk': stock['milk'] + int(fill_milk),
        'beans': stock['beans'] + int(fill_beans),
        'cups': stock['cups'] + int(fill_cups),
        'price': stock['price']
    }
    print(f'\nThe coffee machine has:\n'
          f'{final_stock["water"]} of water\n'
          f'{final_stock["milk"]} of milk\n'
          f'{final_stock["beans"]} of coffee beans\n'
          f'{final_stock["cups"]} of disposable cups\n'
          f'{final_stock["price"]} of money')


def take():
    print(f'\nI gave you ${stock["price"]}\n')

    # calculate stock - stock['price']
    final_stock = {
        'water': stock['water'],
        'milk': stock['milk'],
        'beans': stock['beans'],
        'cups': stock['cups'],
        'price': stock['price'] - stock['price']
    }
    print(f'\nThe coffee machine has:\n'
          f'{final_stock["water"]} of water\n'
          f'{final_stock["milk"]} of milk\n'
          f'{final_stock["beans"]} of coffee beans\n'
          f'{final_stock["cups"]} of disposable cups\n'
          f'{final_stock["price"]} of money')


def remaining():
    # display stock
    print(f'\nThe coffee machine has:\n'
          f'{stock["water"]} of water\n'
          f'{stock["milk"]} of milk\n'
          f'{stock["beans"]} of coffee beans\n'
          f'{stock["cups"]} of disposable cups\n'
          f'{stock["price"]} of money')


# read user input for choice
choice_action = input(f'\nWrite action ({actions[0]}, {actions[1]}, {actions[2]}, {actions[3]}, {actions[4]})\n')

while choice_action != 'exit':
    if choice_action == actions[0]:
        buy()
        # read user input for choice
        choice_action = input(f'\nWrite action ({actions[0]}, {actions[1]}, {actions[2]}, {actions[3]}, {actions[4]})\n')
    elif choice_action == actions[1]:
        fill()
        # read user input for choice
        choice_action = input(f'\nWrite action ({actions[0]}, {actions[1]}, {actions[2]}, {actions[3]}, {actions[4]})\n')
    elif choice_action == actions[2]:
        take()
        # read user input for choice
        choice_action = input(f'\nWrite action ({actions[0]}, {actions[1]}, {actions[2]}, {actions[3]}, {actions[4]})\n')
    elif choice_action == actions[3]:
        remaining()
        # read user input for choice
        choice_action = input(f'\nWrite action ({actions[0]}, {actions[1]}, {actions[2]}, {actions[3]}, {actions[4]})\n')
    elif choice_action == actions[4]:
        break
