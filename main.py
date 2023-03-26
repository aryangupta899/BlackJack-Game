import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
l = len(cards)


def deal_card():
    n = random.randint(0, l-1)
    return cards[n]


def win(player_cards):
    if sum_cards(player_cards) == 21:
        return 1
    else:
        return 0


def sum_cards(player_cards):
    sum = 0
    ctr = 0
    for c in player_cards:
        if c == 11:
            ctr += 1
        else:
            sum += c
    while ctr:
        if sum+11 > 21:
            sum = sum+1
        else:
            sum = sum+11
        ctr -= 1

    return sum


def bust(player_cards):
    s = sum_cards(player_cards)
    if s > 21:
        return 1
    return 0


def play_game():
    print(art.logo)
    user_cards = []
    dealer_cards = []
    display_dealer_cards = []
    print("Dealing the initial cards:")
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
    display_dealer_cards.append('*')
    dealer_cards.append(deal_card())
    display_dealer_cards.append(dealer_cards[-1])

    print("Your cards are:", user_cards)
    print("Dealer cards are:", display_dealer_cards)
    print("The sum of your cards is: ", sum_cards(user_cards))

    if win(dealer_cards):
        print("The dealer wins, the sum of his cards is 21")
        print("Dealer's cards are:", dealer_cards)
        return
    if win(user_cards):
        print("You win, the sum of your cards is 21")
        print("Your cards are:", user_cards)
        print("Dealer's cards are:", dealer_cards)
        return
    if bust(user_cards):
        print("You lose, the sum of your cards exceeded 21")
        print("Your cards are:", user_cards)
        print("Dealer's cards are:", dealer_cards)
        return
    if bust(dealer_cards):
        print("You win, the sum of dealer's cards exceeded 21")
        print("Dealer's cards are:", dealer_cards)
        return

    draw = input("Do you want to draw more cards? (Y/N) ")
    while draw == 'Y':
        user_cards.append(deal_card())
        print("Your cards are:", user_cards)
        print("The sum of your cards is: ", sum_cards(user_cards))
        if win(user_cards):
            print("You win, the sum of your cards is 21")
            print("Your cards are:", user_cards)
            print("Dealer's cards are:", dealer_cards)
            return
        if bust(user_cards):
            print("You lose, the sum of your cards exceeded 21")
            print("Your cards are:", user_cards)
            print("Dealer's cards are:", dealer_cards)
            return

        draw = input("Do you want to draw more cards? (Y/N) ")

    print("Now it is the dealer's turn: ")
    while sum_cards(dealer_cards) < 17:
        print("The dealer draws a card")
        dealer_cards.append(deal_card())
        display_dealer_cards.append(dealer_cards[-1])
        print("Dealer cards are:", display_dealer_cards)
        if win(dealer_cards):
            print("The dealer wins, the sum of his cards is 21")
            print("Dealer's cards are:", dealer_cards)
            return
        if bust(dealer_cards):
            print("You win, the sum of dealer's cards exceeded 21")
            print("Dealer's cards are:", dealer_cards)
            return

    if sum_cards(dealer_cards) > sum_cards(user_cards):
        print("The dealer wins, the sum of his cards is more than yours")
        print("Dealer's cards are:", dealer_cards)
        print("Your cards are:", user_cards)
    else:
        print("You win, the sum of your cards is more than the dealer's")
        print("Dealer's cards are:", dealer_cards)
        print("Your cards are:", user_cards)


play = 'Y'

while play == 'Y':
    play_game()
    play = input("Do you want to play again? (Y/N) ")
