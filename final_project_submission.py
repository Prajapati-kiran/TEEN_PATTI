''' Here is a program of teen patti game 
---> This is played between AI and user
---> Each player is given 3 cards randomly from a deck of cards
---> the order decides the winner if both of them gets same cards with different colours its a draw'''
# Winner is decide on the following bases
'''
    1. TRIAL
    #color doesn,t matter 
    [♠A,♣A,♦A] , [♣K,♠K,♥K] , [♦Q,♥Q,♠Q] ....... [♣2,♦2,♥2]

    2. PURE SEQUENCE
    #color matters , it maybe any color but 3 cards should have the same color
    [♠A,♠K,♠Q] , [♠A,♠2,♠3] , [♠K,♠Q,♠J] ....... [♠4,♠3,♠2]

    3. SEQUENCE
    [♠A,♥K,♣Q] , [♣A,♥2,♦3] , [♣K,♦Q,♦J] ....... [♥4,♦3,♠2]

    4. COLOR
    # if color of 3 cards is same and it is not a sequence
    [♣A,♣K,♣J] , [♣A,♣K,♣10] , [♣A,♣K,♣9] ....... [♣5,♣3,♣2]

    5. PAIR
    #any two cards are same 
    [♠A,♥A,♣K] , [♣A,♥A,♦Q] , [♣A,♦A,♦J] ....... [♥2,♦2,♠3]

    6. HIGH CARDS
    # we know that { A > K > J > Q > 10 > 9 ..... > 2 }
    [♠A,♥K,♣J] , [♣A,♥K,♦10] , [♣A,♦K,♦9] ....... [♥5,♦3,♠2]
    
    TRIAL > PURE SEQUENCE > SEQUENCE > COLOR > PAIR > HIGH CARDS ''' 

import random

#Here is the deck of cards
deck_of_cards = ['♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K','♠A',\
    '♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K','♥A',\
    '♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K','♦A',\
    '♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K','♣A']

#Deck of cards corresponing values such Ace=14, king=13, Queen=12 ........so on 
deck_of_values = [2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,\
            2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14 ] 

#Dummy values these will be replaced after the cards chosen
value1 =[1,2,3] 
value2 =[1,2,3] 

def main():
    # Prints welcome message 
    print_welcome_message()

    # Generate 3 cards to player 1
    cards_of_plyr1 = [0,0,0]  #3 dummy cards
    for i in range(3):
        # A random card is drawn from the deck
        value1[i] = random.randint(0,len(deck_of_cards)-1)
        # We should get a duplicate card in the sets of players cards
        # so we are poping that card from deck
        cards_of_plyr1[i] = deck_of_cards.pop(value1[i])
        # Assigning the corresponding value of that card
        value1[i] = set_value(cards_of_plyr1[i])
        
    # Generate 3 cards to player 2
    cards_of_plyr2 = [0,0,0]  #3 dummy cards
    for i in range(3):
        value2[i] = random.randint(0,len(deck_of_cards)-1)
        cards_of_plyr2[i] = deck_of_cards.pop(value2[i])
        value2[i] = set_value(cards_of_plyr2[i])
    print("")
    print(" AI cards of are: ",cards_of_plyr1)
    print(" Your cards of are: ",cards_of_plyr2)
    print("")
    #Find the winner
    decide_winner(cards_of_plyr1,cards_of_plyr2)

'''Finding the winner'''
def decide_winner(cards_of_plyr1,cards_of_plyr2):
    # test for trial 
    if check_for_trial(cards_of_plyr1,cards_of_plyr2):
        print_end_message()
    # test for pure sequence
    elif check_for_pure_seq(cards_of_plyr1,cards_of_plyr2):
        print_end_message()
    # test for sequence
    elif check_for_seq(cards_of_plyr1,cards_of_plyr2):
        print_end_message()
    # test for color 
    elif check_for_color(cards_of_plyr1,cards_of_plyr2):
        print_end_message()
    # test for double cards
    elif check_for_double(cards_of_plyr1,cards_of_plyr2):
        print_end_message()
    # test for high cards
    elif check_for_high_cards(cards_of_plyr1,cards_of_plyr2):
        print_end_message()
    # this will never be evaluated 
    # so i just say pass
    else:
        pass

def check_for_trial(cards_of_plyr1,cards_of_plyr2):
    plyr1_win = False
    plyr2_win = False
    # Testing for 3 same numbers
    if cards_of_plyr1[0][1] == cards_of_plyr1[1][1] == cards_of_plyr1[2][1]:
        plyr1_win = True
    if cards_of_plyr2[0][1] == cards_of_plyr2[1][1] == cards_of_plyr2[2][1]:
        plyr2_win = True
    if plyr1_win == True and plyr2_win == False:
        print("AI won the match")
        return True
    if plyr2_win == True and plyr1_win == False:
        print("You won the match")
        return True
    if plyr1_win == plyr2_win == True:
        if sum(value1)>sum(value2):
            print("AI won the match")
        else:
            print("You won the match")
        return True
    return False
            
def check_for_seq(cards_of_plyr1,cards_of_plyr2):
    plyr1_win = False
    plyr2_win = False
    # Check will check for sequence
    if check(value1):
        plyr1_win = True   
    if check(value2):
        plyr2_win = True 
    if plyr1_win == True and plyr2_win == False:
        print("AI won the match")
        return True
    if plyr2_win == True and plyr1_win == False:
        print("You won the match")
        return True
    if plyr1_win == plyr2_win == True:
        # If both had seq find highest sequence
        case = find_higest_cards(value1,value2)
        if case == 1 :
            print("AI won the match")
        elif case == 2 :
            print("You won the match")
        else:
            print("the match is tie")
        return True    
    return False
    
def check_for_pure_seq(cards_of_plyr1,cards_of_plyr2):
    plyr1_win = False
    plyr2_win = False
    # First check for color followed by seq
    if cards_of_plyr1[0][0] == cards_of_plyr1[1][0] == cards_of_plyr1[2][0]:
        if check_for_seq_with_color(cards_of_plyr1,value1):
            plyr1_win = True 
    if cards_of_plyr2[0][0] == cards_of_plyr2[1][0] == cards_of_plyr2[2][0]:
        if check_for_seq_with_color(cards_of_plyr1,value2):
            plyr2_win = True           
    if plyr1_win == True and plyr2_win == False:
        print("AI won the match")
        return True        
    if plyr2_win == True and plyr1_win == False:
        print("You won the match")
        return True       
    if plyr1_win == plyr2_win == True:
        case = find_higest_cards(value1,value2)
        if case == 1:
            print("AI won the match")
        elif case == 2:
            print("You won the match")
        else:
            print("match is tie")
        return True
    return False

def find_higest_cards(value_1,value_2):
    # here the sequence we have 1st higest seq and then we have 2nd higest A,2,3 so we are 
    # shiffting its value A,K,Q to 40 and A,2,3 to 39 
    if sum(value_1) == 39:
        value_1 = 40
    if sum(value_2) == 39:
        value_2 = 40
    if sum(value_1) == 19:
        value_1 = 39
    if sum(value_2) == 19:
        value_2 = 39
    # find higest cards and returning a value
    if sum(value_1)>sum(value_2):
        return 1
    elif sum(value_1)<sum(value_2):
        return 2
    else:
        return 3
        
def check_for_seq_with_color(cards_of_plyr1,value_1):
    # Check will check for sequence
    if check(value_1):
        return True
    return False

def check(value):
    value.sort()
    if value[0] == 2 and value[1] == 3 and value[2] == 14:
        return True
    if value[0] == value[1]-1 == value[2]-2:
        return True
    return False

def check_for_color(cards_of_plyr1,cards_of_plyr2):
    plyr1_win = False
    plyr2_win = False
    # Check for color
    if cards_of_plyr1[0][0] == cards_of_plyr1[1][0] == cards_of_plyr1[2][0]:
        plyr1_win = True
    if cards_of_plyr2[0][0] == cards_of_plyr2[1][0] == cards_of_plyr2[2][0]:
        plyr2_win = True
    if plyr1_win == True and plyr2_win == False:
        print("AI won the match")
        return True 
    if plyr2_win == True and plyr1_win == False:
        print("You won the match")
        return True
    if plyr1_win == plyr2_win == True:
        # If both gets color test for high cards in color
        color_high_cards(value1,value2)
        return True
    return False
    
def color_high_cards(value_1,value_2):
    value_1.sort()
    value_2.sort()
    # To check which player has highest card
    # If they have same highest card check the next lowest card
    # If they have same next highest card check the next lowest card there are same match is draw 
    if value_1[2]==value_2[2] and value_1[1]==value_2[1] and value_1[0]>value_2[0]:
        print("AI won the match")
    elif value_1[2]==value_2[2] and value_1[1]==value_2[1] and value_2[0]>value_1[0]: 
        print("You won the match")
    elif value_1[2]==value_2[2] and value_1[1]>value_2[1]:
        print("AI won the match")
    elif value_1[2]==value_2[2] and value_1[1]<value_2[1]:
        print("You won the match")
    elif value_1[2]>value_2[2]:
        print("AI won the match")
    elif value_1[2]<value_2[2]:
        print("You won the match")
    else:
        print("match is tie")
    
def check_for_double(cards_of_plyr1,cards_of_plyr2):
    plyr1_win = False
    plyr2_win = False
    # Here test will test for double cards and return true or false
    if test(value1):
        plyr1_win = True
    if test(value2):
        plyr2_win = True
    #Player who had double is winner
    if plyr1_win == True and plyr2_win == False:
        print("AI won the match")
        return True  
    if plyr2_win == True and plyr1_win == False:
        print("You won the match")
        return True
    #if both players had double cards check who's double card is higest
    if plyr1_win == plyr2_win == True:
        case1 = sum_of_double_cards(value1)
        case2 = sum_of_double_cards(value2)
        if case1>case2:
            print("AI won the match")
        elif case1<case2:
            print("You won the match")
        else:
            print("match is tie")
        return True
    return False
    
def sum_of_double_cards(value_1):
    # If both got double cards
    # check for the non-double high card  
    if value_1[0]==value_1[1]:
        return value_1[2]+value_1[0]
    if value_1[1]==value_1[2]:
        return value_1[0]+value_1[2]
            
#Test if any player got double cards             
def test(value_1):
    value_1.sort()
    if value_1[0]==value_1[1]==value_1[2]:
        return False
    else:
        if value_1[0]==value_1[1]:
            return True
        if value_1[1]==value_1[2]:
            return True
    
def check_for_high_cards(cards_of_plyr1,cards_of_plyr2):
    get_winner(value1,value2)
    return True
    
def get_winner(value_1,value_2):
    value_1.sort()
    value_2.sort()
    # To check which player has highest card
    # If they have same highest card check the next lowest card
    # If they have same next highest card check the next lowest card there are same match is draw 
    if sum(value_1)>sum(value_2) and value_1[2]>value_2[2]:
        print("AI won the match")
    elif sum(value_2)>sum(value_1) and value_2[2]>value_1[2]:
        print("You won the match")
    elif value_1[2]==value_2[2] and value_1[1]==value_2[1] and value_1[0]>value_2[0]:
        print("AI won the match")
    elif value_1[2]==value_2[2] and value_1[1]==value_2[1] and value_2[0]>value_1[0]: 
        print("You won the match")
    elif value_1[2]==value_2[2] and value_1[1]>value_2[1]:
        print("AI won the match")
    elif value_1[2]==value_2[2] and value_1[1]<value_2[1]:
        print("You won the match")
    elif value_1[2]>value_2[2]:
        print("AI won the match")
    elif value_1[2]<value_2[2]:
        print("You won the match")
    else:
        print("match is tie")

def set_value(val):
    if len(val) == 3:
        return 10
    else:
        if val[1][0] == 'A':
            return 14
        elif val[1][0] == 'K':
            return 13
        elif val[1][0] == 'Q':
            return 12
        elif val[1][0] == 'J':
            return 11
        elif val[1][0] == "10":
            return 10
        else:
            return int(val[1][0])
    
def print_welcome_message():
    print("    ----- welcome to TEEN PATTI game -----") 
    print("") 
    print("Your player 1 and player 2 is AI")

def print_end_message():
    print("")
    print("   -----Thanks for playing this game----")
    
if __name__ == '__main__':
    main()
