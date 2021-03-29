import random
# Your main() method accepts one argument.  The value of the argument is stored in a variable called "balance" (See line 9)
def main(balance):
  a=int(input(f'Your balance is {balance}. How much would you like to wager?'))
  print(f'Your are betting {a}')
  slot1=random.randint(0,9)
  slot2=random.randint(0,9)
  slot3=random.randint(0,9)
  print(f'You spun >>{slot1}<< >>{slot2}<< >>{slot3}<<')
  if slot1==slot2==slot3:
    amount=(a*1)
    total_won=balance+amount
    print(f'You won {amount}!')
    c=input(f'Your balance is {total_won}. Enter Y to play again: ')
  elif slot1==slot2:
    amount=a*1.5
    total_won=balance+amount
    print(f'You won {amount}!')
    c=input(f'Your balance is {total_won}. Enter Y to play again: ')
  elif slot1==slot3:
    amount=a*1.5
    total_won=balance+amount
    print(f'You won {amount}!')
    c=input(f'Your balance is {total_won}. Enter Y to play again: ')
  elif slot2==slot3:
    amount=a*1.5
    total_won=balance+amount
    print(f'You won {amount}!')
    c=input(f'Your balance is {total_won}. Enter Y to play again: ')
  else: 
    total_won=balance-a
    print(f'Your lost {a}!')
    c=input(f'Your balance is {total_won}. Enter Y to play again: ')
    if c== "Y":
      main(total_won)
    
  
  
        

# Start your program with the main() method
# Set the initial balance for the user to 10000
if __name__=="__main__":
  main(10000)