def coffee_bot():
  print('Welcome to the cafe!')
  size = get_size()
  drink_type = get_drink_type()
  print("Alright, that's a",size,drink_type,"!")
  name = input('Can I get your name please?')
  print("Thanks, "+name+"! Your drink will be ready shortly")


def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if(res == 'a'):
    return 'small'
  elif(res == 'b'):
    return 'medium'
  elif(res == 'c'):
    return 'large'
  else:
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    get_size()

def get_drink_type():
  res = input('What type of drink would you like?\n[a] Brewed Coffee\n[b] Mocha\n[c] Latte\n>')
  if(res == 'a'):
    return 'brewed coffee'
  elif(res == 'b'):
    return 'mocha'
  elif(res == 'c'):
    return order_latte()
  else:
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte?\n[a] 2%milk\n[b] Non-fat milk\n[c] Soy milk\n>")
  if(res == 'a'):
    return 'latte'
  elif(res == 'b'):
    return 'non-fat latte'
  elif(res == 'c'):
    return 'soy latte'
  else:
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    order_latte()

# Call coffee_bot()!
coffee_bot()
