from random import randint

def card_deck():
    card_value = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
    card_type = ['Hearts','Spades','Clubs','Diamonds']
    return [f'{j} of {i}' for i in card_type for j in card_value]

def card_value(card):
    if card[:1] in ('J','Q','K','1'):
        return 10
    elif card[:1] in ('2','3','4','5','6','7','8','9'):
        return int(card[:1])
    elif card[:1] == 'A':
        num = input(f"\n{card}\nDo you want this to be 1 or 11?\n> ")
        while num not in ('1', '11'):
            num = input("Do you want this to be 1 or 11?\n> ")
        return int(num)

def new_card(deck):
    return deck.pop(randint(0, len(deck) - 1))

while True:
    new_deck = card_deck()
    card1, card2 = new_card(new_deck), new_card(new_deck)
    valu1, valu2 = card_value(card1), card_value(card2)
    total = valu1 + valu2
    dealer_card1, dealer_card2 = new_card(new_deck), new_card(new_deck)
    dealer_value1, dealer_value2 = card_value(dealer_card1), card_value(dealer_card2)
    dealer_total = dealer_value1 + dealer_value2

    print(f"\n\n\n\n{card1} and {card2} with a total of {total}")
    print(f"The Dealer smiles as he looks at you and deals one card up and one card face down")
    print(f"First a {dealer_card1} and face down card.")

    if total == 21:
        print("Blackjack!")
    else:
        while total < 21:
            answer = input("Would you like to hit or stand?\n> ")
            if answer.lower() == 'hit':
                more_card = new_card(new_deck)
                more_value = card_value(more_card)
                total += more_value
                print(f"{more_card} for a new total of {total}")
                if total > 21:
                    print("You LOSE!")
                    break
                elif total == 21:
                    print("You WIN BIG WIN WOOHOO")
                    break
            elif answer.lower() == 'stand':
                print(f"The dealer nods and reveals his other card to be a {dealer_card2} for a total of {dealer_total}")
                while dealer_total < 17:
                    dealer_more = new_card(new_deck)
                    more_dealer_value = card_value(dealer_more)
                    print(f"The card is a {dealer_more}")
                    dealer_total += more_dealer_value
                    if dealer_total > 21 and total <=21:
                        print("Dealer Bust! You win!")
                        break
                else:
                    if dealer_total == total:
                        print("Equal Deals, no winner")
                    elif dealer_total < total:
                        print("You win!")
                    else:
                        print("You Lose!")
                break

    play_again = input("\nWould you like to continue? EXIT to leave\n")
    if play_again.lower() == 'exit':
        break

print("Thank you for Playing")