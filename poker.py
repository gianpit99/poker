import numpy as np
import multiprocessing as mp
#import pygame

number_starting_players = 9

#declare array of cards
deck = ["ah", "as", "ad", "ac",
        "2h", "2s", "2d", "2c",
        "3h", "3s", "3d", "3c",
        "4h", "4s", "4d", "4c",
        "5h", "5s", "5d", "5c",
        "6h", "6s", "6d", "6c",
        "7h", "7s", "7d", "7c",
        "8h", "8s", "8d", "8c",
        "9h", "9s", "9d", "9c",
        "th", "ts", "td", "tc",
        "jh", "js", "jd", "jc",
        "qh", "qs", "qd", "qc",
        "kh", "ks", "kd", "kc"]

#face dictionary
face = {
        "a":0,
        "2":1,
        "3":2,
        "4":3,
        "5":4,
        "6":5,
        "7":6,
        "8":7,
        "9":8,
        "t":9,
        "j":10,
        "q":11,
        "k":12
        }
#suit dictionary
suit = {
        "h":0,
        "s":1,
        "d":2,
        "c":3,
}


#keep track of the index of played cards
index_of_played = []

#initally declare no players at table
p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = None
table = [None, None, None, None, None]

players = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

for i in range(number_starting_players):
    players[i] = ["",""]
    print(i)

def shuffle_and_deal_hands(deck, players, index_of_played, number_starting_players):
    #deal 2 cards to each player
    for x in range(2):
        for y in range(number_starting_players):
            #Take random card
            random_index = np.random.randint(0, 52)

            #Check if card is already taken from deck
            while random_index in index_of_played:
                random_index = np.random.randint(0, 52)

            #Give player the card
            players[y][x] = deck[random_index]

            #Keep track of cards that were taken
            index_of_played.append(random_index)

def deal_flop(index_of_played, table):
    for i in range(3):
        #Take random card
        random_index = np.random.randint(0, 52)

        #Check if card is already taken from deck
        while random_index in index_of_played:
            random_index = np.random.randint(0, 52)

        #set the flop to the random index
        table[i] = deck[random_index]

        #Keep track of cards that were taken
        index_of_played.append(random_index)

def deal_turn(index_of_played, table):
    #Take random card
    random_index = np.random.randint(0, 52)

    #Check if card is already taken from deck
    while random_index in index_of_played:
        random_index = np.random.randint(0, 52)

    #set the turn to the random index
    table[3] = deck[random_index]

    #Keep track of cards that were taken
    index_of_played.append(random_index)

def deal_river(index_of_played, table):
    #Take random card
    random_index = np.random.randint(0, 52)

    #Check if card is already taken from deck
    while random_index in index_of_played:
        random_index = np.random.randint(0, 52)

    #set the river to the random index
    table[4] = deck[random_index]

    #Keep track of cards that were taken
    index_of_played.append(random_index)



#def what_is_the_nuts():
#def what_can_i_hit():
#def what_do_i_have():
#def blind_chance_of_losing():
#def best_hand_right_now():
#def player_odds():


def best_class(face, suit):
    '''
    HIARCHY
    [1] Royal Flush           rf    ~   return 5 cards
    [2] Straight Flush        sf    ~   return 5 cards
    [3] Four of a Kind        4k    ~   return 4 cards and kicker
    [4] Full House            fh    ~   return 5 cards in order
    [5] Flush                 fl    ~   return 5 cards in order
    [6] Straight              st    ~   return 5 cards in order
    [7] Three of a Kind       3k    ~   return 3 cards and two kickers
    [8] Two Pair              2p    ~   return 4 cards in order and kicker
    [9] One Pair              1p    ~   return 2 cards and 3 kickers
    [10] High Card            hk    ~   return 5 highest order
    '''

    #what are my 5 highest cards
    suit_count = [0, 0, 0, 0]
                #hearts spades diamonds clubs
    face_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #             A  2  3  4  5  6  7  8  9  T  J  Q  K  A

    #declare boolean array of cards
    check = [[0, 0, 0, 0],  # ah, as, ad, ac
             [0, 0, 0, 0],  # 2h, 2s, 2d, 2c
             [0, 0, 0, 0],  # 3h, 3s, 3d, 3c
             [0, 0, 0, 0],  # 4h, 4s, 4d, 4c
             [0, 0, 0, 0],  # 5h, 5s, 5d, 5c
             [0, 0, 0, 0],  # 6h, 6s, 6d, 6c
             [0, 0, 0, 0],  # 7h, 7s, 7d, 7c
             [0, 0, 0, 0],  # 8h, 8s, 8d, 8c
             [0, 0, 0, 0],  # 9h, 9s, 9d, 9c
             [0, 0, 0, 0],  # th, ts, td, tc
             [0, 0, 0, 0],  # jh, js, jd, jc
             [0, 0, 0, 0],  # qh, qs, qd, qc
             [0, 0, 0, 0],  # kh, ks, kd, kc
             [0, 0, 0, 0]]  # ah, as, ad, ac

    hand = ["as","th"]
    table = ["ad", "td", "4s", "9s", "5s"]

    check_cards = hand + table
    best_class = None
    best_five = None

    #keep a count of the suits and faces
    for i in range(7):
        card = list(check_cards[i])
        print(card)
        suit_count[suit[card[1]]] += 1
        face_count[int(face[card[0]])] += 1
        check[int(face[card[0]])][suit[card[1]]] = 1
        if card[0] == 'a':
            face_count[int(face[card[0]]) + 13] += 1
            check[int(face[card[0]]) + 13][suit[card[1]]] = 1

    #order highest cards
    sort_done = False
    while(not sort_done):
        sort_done = True
        for i in range(0, 6):
            print(i)
            card1 = list(check_cards[i])
            card2 = list(check_cards[i+1])

            if card1[0] == 'a':
                card1_value = 13
            else:
                card1_value = int(face[card1[0]])
            if card2[0] == 'a':
                card2_value = 13
            else: card2_value = int(face[card2[0]])

            if card1_value < card2_value:
                temp = check_cards[i]
                check_cards[i] = check_cards[i+1]
                check_cards[i+1] = temp
                sort_done = False

    #check royal flush
    for x in range(4):
        for y in range(13, 8, -1):
            print(y)
            if check[y][x] == 0:
                break
            if y == 9:
                print("ROYAL FLUSH")
                best_hand = []
                for z in range(13, 8, -1):
                    best_hand.append(deck[z][x])
                return best_hand, "rf"

    #check straight flush
    for x in range(7):
        #go through all 7 cards
        card = list(check_cards[x])

        #if the card is an ace, scan from the top
        if card[0] == 'a':
            ub = int(face[card[0]]) + 13
        #if the card is not an ace, scan from where the card is
        else:
            ub = int(face[card[0]])

        #if the card is an ace, set the lower limit of the scan to 8
        if card[0] == 'a':
            lb = 8
        #if the card is smaller than 3, a stright flush is impossible
        elif int(face[card[0]]) <= 3:
            continue
        #set the lower limit of the scan to 5 cards less than the upper limit
        else:
            lb = ub - 5

        #scan from the upper limit to the lower limit
        for y in range(ub, lb, -1):
            #check if the card exists of the 7
            if check[y][suit[card[1]]] == 0:
                break
            #if the last card exists, then it is a straight flush
            if y == (lb+1):
                print("STRAIGHT FLUSH")
                best_hand = []
                for z in range(ub, lb, -1):
                    best_hand.append(deck[z][x])
                return best_hand, "sf"

    #check four of a kind
    for i in range(13, 0, -1):
        #check if one of the faces has four cards
        if face_count[i] >= 4:
            print("FOUR OF A KIND")
            best_hand = []
            for x in range(4):
                best_hand.append(deck[i][x])
            return best_hand, '4k'

    #check for a full house
    for x in range(13, 0, -1):
        #check if any of the faces has 3 or more cards
        if face_count[x] >= 3:
            for y in range(13, 0, -1):
                #skip the check if your looking at the triple card face
                if y == x:
                    continue
                #check for doubles in the other faces
                if face_count[y] >= 2:
                    print("FULL HOUSE")
                    best_hand = []
                    for i in range(4):
                        if check[x][i] == 1:
                            best_hand.append(deck[x][i])
                    for i in range(4):
                        if check[y][i] == 1:
                            best_hand.append(deck[y][i])
                        if i >= 2:
                            break
                    return best_hand, "fh"

    #check for a flush
    for i in range(0, 4):
        if suit_count[i] >= 5:
            print("FLUSH")
            best_hand = []
            for x in range(13):
                if check[x][i] == 1:
                    best_hand.append(deck[i][x])
                if x >= 5:
                    break
            return best_hand, "fl"

    #check for a straight
    for x in range(13, 3, -1):
        #go through all face counts
        for y in range(0, 5):
            #if a face card doesnt exist, straight isnt possible with these 5 cards
            if face_count[x-y] == 0:
                break
            #if all 5 cards exist then the stright is made
            if y == 4:
                print("STRAIGHT")
                best_hand = []
                for i in range(x, x-5):
                    for j in range(4):
                        if check[i][j] == 1:
                            best_hand.append(deck[i][j])
                            break
                return best_hand, "st"
                #return statment

    #check for 3 of a kind
    for i in range(13, 0, -1):
        #check to see if any one suit has 3 cards
        if face_count[i] >= 3:
            print("THREE OF A KIND")
            best_hand = []
            for x in range(3):
                if check[i][x] == 1:
                    best_hand.append(deck[i][x])
            added = 0
            for x in range(7):
                if check_cards[x] not in best_hand:
                    best_hand.append(check_cards[x])
                    added += 1
                if added >= 2:
                    break
            return best_hand, "3k"
            #return statment

    #check for two pair
    for x in range(13, 0, -1):
        #check for first pair
        if face_count[x] >= 2:
            #check for second pair
            for y in range(13, 0, -1):
                #skip the first pair so it isnt counted twice
                if x == y:
                    continue
                #return the two pairs
                if face_count[y] >= 2:
                    print("TWO PAIR")
                    best_hand= []
                    for i in range(4):
                        if check[x][i] == 1:
                            print(check[x][i] == 1)
                            print(x, i)
                            print(deck[x][i])
                            best_hand.append(deck[x][i])
                    for i in range(4):
                        if check[y][i] == 1:
                            best_hand.append(deck[y][i])
                    added = 0
                    for i in range(7):
                        if check_cards[i] not in best_hand:
                            best_hand.append(check_cards[i])
                            added += 1
                        if added >= 1:
                            break
                    return best_hand, "2p"
                    #return statment

    #check for single pair
    for i in range(13, 0, -1):
        if face_count[i] >= 2:
            print("SINGLE PAIR")
            best_hand = []
            for x in range(4):
                if check[i][x] == 1:
                    best_hand.append(deck[i][x])
            added = 0
            for x in range(7):
                if check_cards[x] not in best_hand:
                    best_hand.append(check_cards[x])
                    added += 1
                if added >= 3:
                    break
            return best_hand, "1p"

    print("HIGHEST CARD")
    best_hand = []
    for i in range(5):
        best_hand.append(check_cards[i])
    return best_hand, "hc"

print(players)
shuffle_and_deal_hands(deck, players, index_of_played, number_starting_players)
print(players)
print(index_of_played)

print(table)
deal_flop(index_of_played, table)
print(table)
deal_turn(index_of_played, table)
print(table)
deal_river(index_of_played, table)
print(table)

print(" ")
print(best_class(face, suit))
