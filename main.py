import random
import pygame

pygame.init()

WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blackjack')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND = (53, 101, 77)
CARD_BACK = (16, 60, 122)
CARD_RED = (199, 27, 28)
CARD_BLACK = (22, 20, 20)

CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['[', ']', '{', '}'] # diamonds, clubs, hearts, spades

CARD_WIDTH = 125
CARD_HEIGHT = 175
CARD_RADIUS = CARD_WIDTH / 10

# creates a shuffled deck that can be used for the code
def shuffle(): 
    new_deck = []
    
    for card in CARDS:
        for suit in SUITS:
            new_deck.append(card + suit)
            
    random.shuffle(new_deck)
    
    return new_deck

# converts a code deck to a readable deck
def readable_deck(deck):
    new_deck = []
    
    for card in deck:
        cardnum = card[0]
        suit = card[-1]
        
        if cardnum == 'A':
            cardnum = 'ace'
        elif cardnum == '1':
            cardnum = '10'
        elif cardnum == 'J':
            cardnum = 'jack'
        elif cardnum == 'Q':
            cardnum = 'queen'
        elif cardnum == 'K':
            cardnum = 'king'
            
        if suit == '[':
            suit = 'diamonds'
        elif suit == ']':
            suit = 'clubs'
        elif suit == '{':
            suit = 'hearts'
        elif suit == '}':
            suit = 'spades'
            
        new_deck.append(f'{cardnum} of {suit}')
        
    return new_deck

# converts a code deck to the blackjack values
def values_deck(deck):
    new_deck = []
    
    for card in deck:
        cardnum = card[0]
        
        if cardnum == 'A':
            cardnum = 1
        elif cardnum == '2':
            cardnum = 2
        elif cardnum == '3':
            cardnum = 3
        elif cardnum == '4':
            cardnum = 4
        elif cardnum == '5':
            cardnum = 5
        elif cardnum == '6':
            cardnum = 6
        elif cardnum == '7':
            cardnum = 7
        elif cardnum == '8':
            cardnum = 8
        elif cardnum == '9':
            cardnum = 9
        elif cardnum == '1':
            cardnum = 10
        elif cardnum == 'J':
            cardnum = 10
        elif cardnum == 'Q':
            cardnum = 10
        elif cardnum == 'K':
            cardnum = 10
            
        new_deck.append(cardnum)
        
    return new_deck

def draw_rounded_rect(color, rect, radius):
    x, y, w, h = rect
    pygame.draw.circle(SCREEN, color, (x + radius, y + radius), radius)
    pygame.draw.circle(SCREEN, color, (x + w - radius, y + radius), radius)
    pygame.draw.circle(SCREEN, color, (x + radius, y + h - radius), radius)
    pygame.draw.circle(SCREEN, color, (x + w - radius, y + h - radius), radius)
    pygame.draw.rect(SCREEN, color, (x, y + radius, w, h - 2 * radius))
    pygame.draw.rect(SCREEN, color, (x + radius, y, w - 2 * radius, h))

def draw_text(text, color, x, y, font_size, flip=False):
    font = pygame.freetype.SysFont('Card Characters', font_size)
    text_surface, _ = font.render(text, color)
    text_surface = pygame.transform.flip(text_surface, flip, flip)
    SCREEN.blit(text_surface, (x, y))

def draw_card(x, y, card):
    center_card = CARD_WIDTH / 2
    padding = 10
    anchor_adjust_x = 35
    anchor_adjust_y = 20
    
    # card background
    draw_rounded_rect(WHITE, (x - center_card, y, CARD_WIDTH, CARD_HEIGHT), CARD_RADIUS)
    
    # number and suit
    if card[-1] == '[' or card[-1] == '{': # change color based on suit
        draw_text(card, CARD_RED, x - center_card + padding, y + padding, 24) # top left
        if card[0] == '1': # position needs to be slightly left for 10
            draw_text(card, CARD_RED, x + CARD_WIDTH - center_card - padding - anchor_adjust_x - 15, y + CARD_HEIGHT - padding - anchor_adjust_y, 24, True) # bottom right
        else:
            draw_text(card, CARD_RED, x + CARD_WIDTH - center_card - padding - anchor_adjust_x, y + CARD_HEIGHT - padding - anchor_adjust_y, 24, True) # bottom right
    else:
        draw_text(card, CARD_BLACK, x - center_card + padding, y + padding, 24) # top left 
        if card[0] == '1': # position needs to be slightly left for 10
            draw_text(card, CARD_BLACK, x + CARD_WIDTH - center_card - padding - anchor_adjust_x - 15, y + CARD_HEIGHT - padding - anchor_adjust_y, 24, True) # bottom right
        else:
            draw_text(card, CARD_BLACK, x + CARD_WIDTH - center_card - padding - anchor_adjust_x, y + CARD_HEIGHT - padding - anchor_adjust_y, 24, True) # bottom right

def main():
    deck = shuffle()
    deck_readable = readable_deck(deck)
    deck_values = values_deck(deck)
    
    while True:
        SCREEN.fill(BACKGROUND)
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        
        # dealer's cards
        draw_card(875, 100, deck[0])
        draw_card(725, 100, deck[1])
        
        # player's cards
        draw_card(875, 600, deck[2])
        draw_card(725, 600, deck[3])
        
        pygame.display.flip()
     
main()