import random
import tkinter
TK_SILENCE_DEPRECATION=1


def load_images(card_images):
    suits = ["heart","club","diamond","spade"]
    faces = ["jack","queen","king"]

    extension = 'ppm'

    for suit in suits:
        #numbers
        for card in range(1,11) :
            name = "cards/{}_{}.{}".format(str(card), suit, extension)  
            image = tkinter.PhotoImage(file= name)
            card_images.append((card, image))
        #faces
        for card in faces:
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file= name)
            card_images.append((10, image))

def deal_card(frame):
    #pop the next card off the top of the deck
    next_card = deck.pop(0)
    #add image to a label and display
    tkinter.Label(frame, image=next_card[1], relief = "raised").pack(side="left")
    # now return card's face value
    return next_card

def score_hand(hand):
    #calculate the total score of all cards in the list.
    #only one ace can have value 11, will reduce to 1 if bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check for ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    
    return score

def deal_dealer():
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Baa Baa Boo")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Baa Baa Best")
    elif dealer_score > player_score:
        result_text.set("Baa Baa Boo")
    else:
        result_text.set("Baa Baa Black Sheep Have You Any Wool? Yes Sir Yes Sir Three Bags Full. One For The Master And One For The Dame. One For The Little Boy Who Lives Down The Lane. Baa Baa Black Sheep Have You Any Wool? Yes Sir Yes Sir Three Bags Full.")
def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Baa Baa Boo!")
    # global player_score, player_ace
    
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # #if we would bust, check if there is an ace and subtract 10
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Baa Baa Bust!")

def new_game():
    global deck
    global dealer_hand, player_hand, dealer_card_frame, player_card_frame
    deck = list(cards)
    random.shuffle(deck)
    dealer_hand=[]
    player_hand=[]
    print(dealer_hand,player_hand)
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="#e6ccff")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan = 2)
    
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="#e6ccff")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan = 2)

    deal_player()
    deal_dealer()
    deal_player()
    


mainWindow  = tkinter.Tk()

#set up screen and frames for dealer and player
mainWindow.title("Baa Baa Blackjack")
mainWindow.geometry("640x480")
mainWindow.configure(bg= "#1f7a1f")
result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable= result_text, bg = "#1f7a1f", fg = "red")
result.grid(row = 0, column = 0, columnspan = 3)

card_frame = tkinter.Frame(mainWindow, relief= "sunken", borderwidth= 1, background= "#e6ccff")
card_frame.grid(row = 1, column = 0, sticky = "ew", columnspan = 3, rowspan = 2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text= "Dealer", background= "#e6ccff", fg= "black").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable =dealer_score_label, 
background = "#e6ccff", fg = "black").grid(row=1, column=0)
# embedded frame holds the card images
dealer_card_frame = tkinter.Frame(card_frame, background="#e6ccff")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan = 2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background = "#e6ccff", fg = "black").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable = player_score_label, 
background = "#e6ccff", fg = "black").grid(row=3, column=0)
# embedded frame holds the card images
player_card_frame = tkinter.Frame(card_frame, background="#e6ccff")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan = 2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan = 3, sticky = "w")

dealer_button = tkinter.Button(button_frame, text = "Dealer", command = deal_dealer)
dealer_button.grid(row=0, column = 0)

player_button = tkinter.Button(button_frame, text = "Player", bg = "#e6ccff", fg = "black", command = deal_player)
player_button.grid(row=0, column = 1)

# button for new game
new_button = tkinter.Button(button_frame, text = "New Game", command = new_game)
new_button.grid(row=0, column = 2)

cards = []
load_images(cards)
#create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

#create the list to store the player's and dealer's hands
dealer_hand = []
player_hand = []    
deal_player()
deal_dealer()
deal_player()


mainWindow.mainloop()