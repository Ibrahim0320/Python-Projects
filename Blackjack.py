# Blackjack

import random
suits= ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks= ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values= {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11 or 1}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank= rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):

        self.deck= []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)

                self.deck.append(created_card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards= []
        self.value= 0
        self.aces= 0

    def add_card(self, Card):
        self.cards.append(Card)
        self.value += values[Card.rank]
        if Card.rank == 'Ace' and self.value > 21:
            self.value -= 10

    def adjust_for_ace(self):
        if Card.rank == 'Ace':
            ace_value= input('What is you desired Ace value) (11 or 1):')
            if ace_value == '1' or ace_value== '11':
                values[Card.rank] == int(ace_value)
            else:
                print('Invalid value. Ace can only be 11 or 1. Choose again.')


class Chips:
    def __init__(self):
        self.total= 100
        self.bet= 0
    def win_bet(self):
        self.total += self.bet
        print('You won back 2x your bet! You now have {} €.'.format(self.total))
        

    def lose_bet(self):
        self.total -= self.bet
        print('You lost your bet! You have {} € left'.format(self.total))

        


def take_bet(chips):
    
    while True:
        print('\nYour current balance €:', chips.total)
        try:
            bet = int(input('How much would you like to bet?: '))
        except ValueError:
            print('Invalid entry. Pick a bet amount:')
            continue
        if bet == 0:
            print('Thanks for playing.')
            break
        elif bet > chips.total:
            print("Bet exceeds your current balance. Choose a lower amount.")
        else:
            chips.bet = bet
            break


def hits(Deck, Hand):
    
    new_card= Deck.deal()
    Hand.add_card(new_card)
    print(f"You recieved a new card: {new_card}")
    print(f"Your hand: {', '.join(str(card) for card in Hand.cards)}")


def hit_or_stand(deck, player, chips):
    global playing
    while playing:
        choice = input("Would you like to Hit or Stand?: ").lower()
        if choice == 'hit':
            hits(deck, player)
            show_some(player, dealer)
            if player.value > 21:
                player_busts(player, dealer, chips)
                playing = False  # Set playing to False to exit the loop
                break  # Exit the loop immediately after player busts
        elif choice == 'stand':
            print("You have decided to stand.")
            playing = False  # Set playing to False to exit the loop
            break  # Exit the loop immediately after player stands
        else:
            print("Invalid choice. Please enter 'Hit' or 'Stand'.")


        

def show_some(player, dealer):

    
    print("Player has the following cards: {}".format(", ".join(str(card) for card in player.cards)), 
          '\nwith a value of {}'.format(player.value))
    
    # Show only the value of the visible card in the dealer's hand
    print("Dealer has the following cards: {} and one hidden card".format(dealer.cards[0]), 
          '\nwith a value of {}'.format(values[dealer.cards[0].rank]))
    

def show_all(player, dealer):

    print('Player has the following cards: {}'.format(", ".join(str(card) for card in player.cards)), '\nwith a value of {}'.format(player.value))
    print('Dealer has the following cards: {}'.format(", ".join(str(card) for card in dealer.cards)), '\nwith a value of {}'.format(dealer.value))





def player_busts(player_hand, dealer_hand, chips):
    if player_hand.value > 21:
        print("Player's hand is greater than 21. Player loses this round")
        chips.lose_bet()
        global playing  # Add this line
        playing = False  # Set playing to False after player busts


def player_wins(player_hand, dealer_hand, Chips):
    if dealer_hand.value < player_hand.value < 21:
        print("Player's hand is better than dealer's. Player wins this round. ")
        Chips.win_bet()
    if dealer_hand.value > 21 and player_hand.value <= 21:
        print("Dealer's hand exceeds 21. Player wins this round")
        Chips.win_bet()

def dealer_busts(player_hand, dealer_hand, chips):
    print("Dealer's hand is greater than 21. Dealer loses this round.")
    chips.win_bet()




def dealer_wins(player_hand, dealer_hand, chips):
    if player_hand.value < dealer_hand.value < 21:
        print("Dealer's hand is greater than player's. Dealer wins this round")
        chips.lose_bet()
    if player_hand.value > 21 and dealer_hand.value <= 21:
        print("Player's hand exceeds 21. Dealer wins this round")
        chips.lose_bet()



while True:
    print('Welcome to Blackjack!')

    new_deck = Deck()
    new_deck.shuffle()
    player1 = Hand()
    dealer = Hand()

    player1.add_card(new_deck.deal())
    dealer.add_card(new_deck.deal())
    player1.add_card(new_deck.deal())
    dealer.add_card(new_deck.deal())

    chips = Chips()
    take_bet(chips)

    show_some(player1, dealer)

    playing = True

    while playing:
        hit_or_stand(new_deck, player1, chips)

        show_some(player1, dealer)

        if player1.value > 21:
            player_busts(player1, dealer, chips)
            break
        else:
            continue

    if player1.value <= 21:
        while dealer.value < 17:
            hits(new_deck, dealer)

        show_all(player1, dealer)  # Move this line here

        if dealer.value > 21:
            dealer_busts(player1, dealer, chips)
        elif player1.value > dealer.value:
            player_wins(player1, dealer, chips)
        elif dealer.value > player1.value:
            dealer_wins(player1, dealer, chips)
        else:
            print("It's a tie! No one wins.")


    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break







    
        



