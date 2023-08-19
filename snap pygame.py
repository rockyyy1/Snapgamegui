import pygame
import pygame.font
import random
import time
from DeckOfCards import DeckOfCards, Player

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Snap")
clock = pygame.time.Clock()
#font
font_file = "Graphics/disko_ot.otf"

#permanent surfaces
green_background_surface = pygame.image.load("Graphics/green_background.png")
python_playing_cards_surface = pygame.image.load("Graphics/pythonplayingcards.png")
python_playing_cards_surface = pygame.transform.scale(python_playing_cards_surface, (python_playing_cards_surface.get_width() // 4, python_playing_cards_surface.get_height() //4))

#snap button
font_SNAP = pygame.font.Font(font_file, 100)
text_SNAP = font_SNAP.render("SNAP", True, (0,0,0))
button_SNAP = text_SNAP.get_rect(topleft=(190,300))

#texts
font_you = pygame.font.Font(font_file, 30)
text_you = font_you.render("you", True, (0,0,0))
font_hover = pygame.font.Font(font_file, 25)
text_hover = font_hover.render("(click below!)", True, (0,0,0))

def random_emoji():
    '''Returns a random image file from emoji folder'''
    
    image_filenames = [
    "5241479_face_evil_smiley_angry_devil_grin_smile.png", 
    "5241480_smiley_face_shocked_surprise_shock.png",
    "5241481_face_lol_positive_smiley_laughter_smile.png",
    "5241482_smile_face_positive_smiley.png",
    "5241495_demon_face_evil_angry_devil_emoji_hatred.png",
    "5241485_glasses_face_smile_smiley.png",
    "5241486_misunderstanding_puzzled_surprise_emoji_face.png",
    "5241487_cute_face_smiley_naive_naivety_emoji_smile.png",
    "5241488_embarrassed_be_face_smiley_embarrassment_emoji_smile.png",
    "5241492_speechless_emoji_zipped_lips.png",
    "5241490_emoji_sad_saddened_alarmed_face.png"]
    
    random_number = random.randint(0, 10)
    image = pygame.image.load("Graphics/"+image_filenames[random_number])
    image = pygame.transform.scale(image, (image.get_width() // 40, image.get_height() // 40))

    return image

def check_player_card_count(hand):
            cards_in_hand = len(hand)
            if cards_in_hand == 0:
                return False
            else:
                return True
            
#inititialize the deck of cards
play = Player()
players_hands = play.snap(4)

#give each player a hand
player_1_hand = players_hands[0]
player_2_hand = players_hands[1]
player_3_hand = players_hands[2]
player_4_hand = players_hands[3]
#give each player a random emoji
player_1_emoji =  random_emoji()
player_2_emoji =  random_emoji()
player_3_emoji =  random_emoji()
player_4_emoji =  random_emoji()

#card positions
p1_card_x_pos = 100
p1_card_y_pos = 300    
p2_card_x_pos = 40
p2_card_y_pos = 50    
p3_card_x_pos = 450
p3_card_y_pos = 50   
p4_card_x_pos = 440
p4_card_y_pos = 280   
    
def player_1_flips(card_hand):
    card = card_hand[0]
    player_1_hand.pop(card)
    return card

def load_playing_card_image(card):
    playing_card_image = pygame.image.load("Graphics/Vector Playing Cards/"+ card)
    playing_card_image = pygame.transform.scale(playing_card_image, (80,105))
    
    return playing_card_image

all_players_have_cards = True

while all_players_have_cards:
    for event in pygame.event.get():
        screen.blit(text_SNAP, button_SNAP)
        pygame.draw.rect(screen, (255,0,0), button_SNAP, 2)

        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            if button_SNAP.collidepoint(event.pos):
                font_SNAP = pygame.font.Font(font_file, 110)
                text_SNAP = font_SNAP.render("SNAP", True, (255,0,0))
            else:
                font_SNAP = pygame.font.Font(font_file, 100)
                text_SNAP = font_SNAP.render("SNAP", True, (0,0,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse cursor location:", pygame.mouse.get_pos())
            if button_SNAP.collidepoint(event.pos):
                print("SNAP Button was pressed")
            
    screen.blit(green_background_surface, (0,0))
    
    #bottomleft
    screen.blit(player_1_emoji, (0,300)) 
    screen.blit(python_playing_cards_surface,(90,290))
    screen.blit(text_you, (30,280))
    #animation      

    if p1_card_x_pos< 270: p1_card_x_pos  += 2
    if p1_card_y_pos> 154: p1_card_y_pos += -2
    screen.blit(load_playing_card_image(str(player_1_hand[0])+".png"), (p1_card_x_pos, p1_card_y_pos))

    if p2_card_x_pos< 270: p2_card_x_pos  += 3.2
    if p2_card_y_pos< 154: p2_card_y_pos += 1.5
    screen.blit(load_playing_card_image(str(player_2_hand[0])+".png"), (p2_card_x_pos, p2_card_y_pos))
    
    if p3_card_x_pos> 270: p3_card_x_pos  += -2
    if p3_card_y_pos< 154: p3_card_y_pos += 2
    screen.blit(load_playing_card_image(str(player_3_hand[0])+".png"), (p3_card_x_pos, p3_card_y_pos))

    if p4_card_x_pos> 270: p4_card_x_pos  += -3.2
    if p4_card_y_pos> 154: p4_card_y_pos += -1.5
    screen.blit(load_playing_card_image(str(player_4_hand[0])+".png"), (p4_card_x_pos, p4_card_y_pos))
    
    #topleft
    screen.blit(player_2_emoji, (0,0)) 
    screen.blit(python_playing_cards_surface,(40,50))
    #topright
    screen.blit(player_3_emoji, (500,0)) 
    screen.blit(python_playing_cards_surface,(450,50))
    #bottomright
    screen.blit(player_4_emoji, (500,300)) 
    screen.blit(python_playing_cards_surface,(440,280))

    screen.blit(text_SNAP, (190,300))
    screen.blit(text_hover, (200,280))
            
    pygame.display.update()
    clock.tick(70)

