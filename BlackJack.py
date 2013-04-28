import random
class BlackJack:
    '''

    Kody Alan Kantor
    4-22-13
    First Python program

    This class is a BlackJack game. 

    Class variables:
        cards list: Holds a list of all of the values of the cards. Jack/Queen/King are
        represented as 10's.

        For ease of implementation, the Ace is only worth 1.

    Methods:
        ask_the_user(self, prompt):
            Asks the user a question (y/n).
            This method is passed a string, which is the question being asked,
            and returns a boolean
        draw(self):
            Draws the card from the 'top' of the 'deck,' returns it, and deletes the entry
            in the list
        reset(self):
            Redefines the deck, and shuffles it.

    Mod History:
    4-22-13: Original Compilation
            
    '''
    cards  = [1,2,3,4,5,6,7,8,9,10,10,10,10,
              1,2,3,4,5,6,7,8,9,10,10,10,10,
              1,2,3,4,5,6,7,8,9,10,10,10,10,
              1,2,3,4,5,6,7,8,9,10,10,10,10]
        #end class variable cards

    
    def ask_the_user(self, prompt):
        fromUser    =   input(prompt)
        if fromUser is "y":
            return True
        return False #this depends on the previous statement not executing
        #end ask the user y/n question

    def draw(self):
        result = BlackJack.cards[0]
        BlackJack.cards.remove(BlackJack.cards[0])        
        return result
        #end draw and remove a card
    
    def reset(self):
        BlackJack.cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,
                           1,2,3,4,5,6,7,8,9,10,10,10,10,
                           1,2,3,4,5,6,7,8,9,10,10,10,10,
                           1,2,3,4,5,6,7,8,9,10,10,10,10]
        random.shuffle(BlackJack.cards)
        #end reset deck and shuffle

#create the blackjack game
game            =       BlackJack()
while game.ask_the_user("Wanna play blackjack? (y/n) "):
    a           =       game.draw()#dealer card 1
    b           =       game.draw()#dealer card 2
    x           =       game.draw()#player card 1
    y           =       game.draw()#player card 2
    print ("Cards drawn were", x, "and", y, "\n")
    y           =       x + y
    print ("Your total is:", y)
    print ("Dealer has:", a, "and a hidden card\n")
    while y < 21:
        if game.ask_the_user("Hit? "):
            x   =       game.draw()
            print ("You drew a", x)
            y   =       x + y
            print ("Your total is:", y, "\n")
        else:
            break
            #breaks from the '< 21' loop
    if y > 21:
        print ("Bust! \n")
    elif y == 21:
        print ("Yay! 21! \n")
    else:
        print ("Your hand was", y, "\n")
    #end player hand
        
    print("Dealer has:", a, "and", b)
    b = a + b
    print("Dealer's total is:", b, "\n")
    
    while b < 17:
        a       =       game.draw()
        print("Dealer drew a", a)
        b       =       a + b
        print("Dealer's hand is:", b, "\n")
    #end while the dealer's hand is < 17
        
    if b == 21:
        print ("Dealer got 21!")
        print ("You got", y)
    elif b < 21:
        print ("Dealer got", b)
        print ("You got", y)
    else:
        print ("Dealer busts")
        print ("You got", y, "\n")
    #end dealer hand, and game
        
    game.reset()
    #resets the deck (shuffles)
#end while the user wants to play blackjack
