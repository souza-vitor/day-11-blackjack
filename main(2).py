import random
import art
import replit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_game = ''

def deal_card(input_cards):
  random_card = random.choice(cards)

  input_cards.append(random_card)

def calculate_score(cards):
  if len(cards) == 2 and sum(cards) == 21:
    return 0

  if cards.count(11) > 0:
    if sum(cards) > 21:
      cards.remove(11)
      cards.append(1)

  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return 'Tie'
  if user_score == 0:
    return "You've got Blackjack! You win!"
  elif computer_score == 0:
    return "Computer got Blackjack! You lose!"
  elif user_score > 21:
    return "You went over 21! You lose!"
  elif computer_score > 21:
    return "Computer went over 21! You win!"
  else:
    if user_score > computer_score:
      return "You win!"
    else:
      return "You lose!"

def play_game():
  
  user_cards = []
  computer_cards = []
  
  user_score = ''
  computer_score = ''
  
  repeat = ''
  game_over = False
  
  deal_card(user_cards)
  deal_card(user_cards)
  deal_card(computer_cards)
  deal_card(computer_cards)
  
  print(art.logo)
  
  while repeat != 'n':
  
    if repeat == 'y':
      deal_card(user_cards)
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
  
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0:
      if user_score == 0:
        game_over = True
        break
      elif computer_score == 0:
        game_over = True
        break
    elif user_score > 21:
      game_over = True
      break
    else:
      repeat = input("You want to draw another card? (y/n) \n")
      if repeat == 'n':
        game_over = True
        break
  
  while game_over != False:
    while computer_score < 17:
      deal_card(computer_cards)
      computer_score = calculate_score(computer_cards)
    
    break
  
  print(f"Your final hand {user_cards}, final score: {user_score}")
  print(f"Computer's final hand {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  print("")

start_game = input("Do you want to play a game of blackjack? (y/n) \n")

while start_game == 'y':
  replit.clear()
  play_game()
  start_game = input("Do you want to play game of blackjack? (y/n) \n")
  if start_game == 'n':
    print("Thanks for playing!")
    break