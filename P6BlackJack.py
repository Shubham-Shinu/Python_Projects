# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
ab=False
score = 0
tr=0
vp=0
vd=0
deck=[]
q=0
msg=""
cdpos=cppos=0
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        if pos[0]==20 and pos[1]==200:
            #canvas.draw_image(card_back, (35.5, 48), (71, 96), (55.5, 248), (71, 96))
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0]+CARD_BACK_CENTER[0],pos[1]+CARD_BACK_CENTER[1]],CARD_BACK_SIZE)
        else:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

        
# define hand class
class Hand:
    def __init__(self):
        self.h=""
        self.hand=[]

    def __str__(self):
        return "Hand contains "+str(self.h)

    def add_card(self, card):
        self.h += str(card)
        self.hand.append(card)
        

    def get_value(self):
        v=0
        if len(self.h)>0:
            for l in range(1,len(self.h),2):
                    v+=VALUES[self.h[l]]
            for l in range(1,len(self.h),2):
                if self.h[l]=='A' and v<=11:
                    v+=10
            return v

    def draw(self, canvas, pos):
        global player
        for l in range(0,len(self.hand)):
            self.hand[l].draw(canvas,pos)
            pos[0]+=75
        #if flip==1:
        if in_play==False and flip==1:
            dealer.hand[0].draw(canvas,(19,200))

            pass	# draw a hand on the canvas, use the draw method for cards
        

# define deck class 
class Deck:
    def __init__(self):
        #self.d=[]
        global deck
        deck=[]
        for S in SUITS:
            for R in RANKS:
                c=Card(S,R)
                deck.append(c)

    def shuffle(self):
        random.shuffle(deck)
        # shuffle the deck 

    def deal_card(self):
        global q
        new=deck[q]
        q+=1
        deck.remove(new)
        return new
    
    def __str__(self):
        st="Deck contains "
        for i in range(52):
            st=st+str(deck[i])+" "
        return st


#define event handlers for buttons
def deal():
    global outcome,in_play,deck,q,player,dealer,vp,vd,D,msg,cdpos,cppos,flip,score,ab,tr
    if in_play:
        msg="Abandon! You lost !"
        score -= 1
        ab=True
        in_play=False

    if in_play==False:
        cdpos=cppos=10
        if ab:
            msg="Abandon.You lose! Click Hit/Stand(new)"
            ab=False
        else:
            msg="Click Hit or Stand"
        in_play = True
        q=0
        vp=0
        vd=0
        D=Deck()
        D.shuffle()
        #print Deck()
        flip=0
        player=Hand()
        dealer=Hand()

        player.add_card(Deck.deal_card(D))
        dealer.add_card(Deck.deal_card(D))
        player.add_card(Deck.deal_card(D))
        dealer.add_card(Deck.deal_card(D))
        vp=player.get_value()
        vd=dealer.get_value()

        tr += 1
        #print "Player",player,"    Dealer",dealer
        #print vp,vd

    
def hit():
    global vp,vd,in_play,score,msg,flip,deck
    if in_play:
        player.add_card(Deck.deal_card(D))
        flip=1
        vp=player.get_value()
        #print vp,vd
        if vp>21:
            score -= 1
            msg="Your game busted. NEW DEAL ?"
            #print len(deck)
            #print "Player's game busted. Player loses ! "+str(score)
            in_play=False
        elif vp>vd:
            in_play=False
            score += 1
            msg="You win ! NEW DEAL ?"
            #print len(deck)
            #print "Player Wins ! "+str(score)
        if vp==vd:
            in_play=False
            score -= 1
            msg="You lose ! NEW DEAL"
            #print len(deck)
            #print "Dealer Wins ! "+str(score)
            
    pass	# replace with your code below
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global vp,vd,in_play,score,msg,flip
    if in_play:
        dealer.add_card(Deck.deal_card(D))
        flip=1
        vd=dealer.get_value()
        #print vp,vd
        if vd>17:
            in_play=False
            score += 1
            #print len(deck)
            msg="Dealer's game busted. You win ! Click DEAL"
        if vp==vd:
            in_play=False
            score -= 1
            #print len(deck)
            msg="You lose ! NEW DEAL"

            #print "Dealer's game busted. Player wins ! "+str(score)

    pass	# replace with your code below
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global score,msg,player,dealer,ab
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Game: "+str(tr), [500,60], 25, "Yellow")
    canvas.draw_text("BlackJack", [210,70], 48, "Aqua")
    canvas.draw_text("Score: "+str(score), [250,100], 32, "White")
    canvas.draw_text("Dealer", [20,170], 36, "White")
    canvas.draw_text("Player", [20,380], 36, "White")
    canvas.draw_text(msg, [160,380], 24, "Red")
    player.draw(canvas,[20,400])
    dealer.draw(canvas,[20,200])



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()

    
frame.start()
# remember to review the gradic rubric
