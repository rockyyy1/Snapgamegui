import pygame
import pygame.font
import random
import time
from DeckOfCards import Player, DeckOfCards

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Snap by Rocky Trang")
clock = pygame.time.Clock()
font_file = "Graphics/disko_ot.otf"

def load_permanent_surfaces():
    global green_background_surface, python_playing_cards_surface, text_SNAP, button_SNAP, text_you, font_hover, text_hover
    
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

def load_playing_card_image(card):
    playing_card_image = pygame.image.load("Graphics/Vector Playing Cards/"+ card)
    playing_card_image = pygame.transform.scale(playing_card_image, (85,115))
    
    return playing_card_image

def random_emoji():
    '''Returns a random image file from emoji folder'''
    global player_1_emoji, player_2_emoji, player_3_emoji, player_4_emoji
    
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
    
    images = random.sample(image_filenames, 4)
    images = [pygame.image.load("Graphics/"+image) for image in images]
    images = [pygame.transform.scale(image, (image.get_width() // 40, image.get_height() // 40)) for image in images]
    
    player_1_emoji = images[0] 
    player_2_emoji = images[1] 
    player_3_emoji = images[2]
    player_4_emoji = images[3]
    
    return player_1_emoji, player_2_emoji, player_3_emoji, player_4_emoji

def check_player_card_count(hand):
            cards_in_hand = len(hand)
            if cards_in_hand == 0:
                return False
            else:
                return True

def update_card_position(x, y, target_x, target_y, step):
    if x < target_x:
        x += step
    elif x > target_x:
        x -= step
    if y < target_y:
        y += step
    elif y > target_y:
        y -= step
    return x, y

def draw_game_elements():
    screen.blit(green_background_surface, (0, 0))
    
    # Draw player 1's elements
    screen.blit(player_1_emoji, (0,300)) 
    screen.blit(python_playing_cards_surface,(90,290))
    screen.blit(text_you, (30,280))
    
    # Draw player 2's elements
    screen.blit(player_2_emoji, (0,0)) 
    screen.blit(python_playing_cards_surface,(40,50))

    # Draw player 3's elements
    screen.blit(player_3_emoji, (500,0)) 
    screen.blit(python_playing_cards_surface,(450,50))

    # Draw player 4's elements
    screen.blit(player_4_emoji, (500,300)) 
    screen.blit(python_playing_cards_surface,(440,280))
    
    screen.blit(text_hover, (230,280))
    
def cards_animation(current_player):
    global p1_card_x_pos, p1_card_y_pos, p2_card_x_pos, p2_card_y_pos, p3_card_x_pos, p3_card_y_pos, p4_card_y_pos, p4_card_x_pos 
    global first, card_counter
    backcard = pygame.image.load("Graphics/Vector Playing Cards/backcard.png")
    backcard = pygame.transform.scale(backcard, (85,115))

    #Player 1
    if current_player == 1:
        if first == False:
            screen.blit(load_playing_card_image(str(central_pile[-4]) + ".png"), (260, 160))
            screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (280, 160))
            screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (300, 160))
            screen.blit(load_playing_card_image(str(central_pile[-1]) + ".png"), (320, 160))
        screen.blit(load_playing_card_image(("backcard.png")), (p1_card_x_pos, p1_card_y_pos))
        if p1_card_x_pos == 260 and p1_card_y_pos == 160:
            screen.blit(load_playing_card_image(str(player_1_hand[0]) + ".png"), (260, 160))            
            
    #Player 2
    if current_player == 2:
        if first == False:
            screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (300, 160))
            screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (320, 160))
        screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (260, 160))
        screen.blit(load_playing_card_image(("backcard.png")), (p2_card_x_pos, p2_card_y_pos))
        if p2_card_x_pos == 280 and p2_card_y_pos == 160:
            screen.blit(load_playing_card_image(str(central_pile[-1]) + ".png"), (280, 160))
            

    #Player 3
    elif current_player == 3:
        if first == False:
            screen.blit(load_playing_card_image(str(central_pile[-4]) + ".png"), (320, 160))
        screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (260, 160))
        screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (280, 160))    
        screen.blit(load_playing_card_image(("backcard.png")), (p3_card_x_pos, p3_card_y_pos))
        if p3_card_x_pos == 300 and p3_card_y_pos == 160:
            screen.blit(load_playing_card_image(str(central_pile[-1]) + ".png"), (300, 160))
            

    #Player 4
    elif current_player == 4:
        if first == False:
            screen.blit(load_playing_card_image(str(central_pile[-5]) + ".png"), (320, 160))
        screen.blit(load_playing_card_image(str(central_pile[-4]) + ".png"), (260, 160))
        screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (280, 160))
        screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (300, 160))
        screen.blit(load_playing_card_image(("backcard.png")), (p4_card_x_pos, p4_card_y_pos))
        if p4_card_x_pos == 320 and p4_card_y_pos == 160:
            screen.blit(load_playing_card_image(str(central_pile[-1]) + ".png"), (320, 160))

                
             
                    
#inititialize the deck of cards
play = Player()
players_hands = play.snap(4)
central_pile = []

#give each player a random emoji
random_emoji()

#give each player a hand
player_1_hand = players_hands[0]
player_2_hand = players_hands[1]
player_3_hand = players_hands[2]
player_4_hand = players_hands[3]

#initial starting card positions
p1_card_x_pos = 100
p1_card_y_pos = 300    
p2_card_x_pos = 40
p2_card_y_pos = 52    
p3_card_x_pos = 452
p3_card_y_pos = 52   
p4_card_x_pos = 440
p4_card_y_pos = 280

first = True
all_players_have_cards = True
animation_time_start = time.time()
counter = 1
card_counter = 0

while all_players_have_cards:
    load_permanent_surfaces()
    for event in pygame.event.get():
        screen.blit(text_SNAP, button_SNAP)
        pygame.draw.rect(screen, (255,0,0), button_SNAP, 2)
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse cursor location:", pygame.mouse.get_pos())
            if button_SNAP.collidepoint(event.pos):
                print("SNAP Button was pressed")
                
    #update card positions each frame      
    p1_card_x_pos, p1_card_y_pos = update_card_position(p1_card_x_pos, p1_card_y_pos, 260, 160, 4)
    p2_card_x_pos, p2_card_y_pos = update_card_position(p2_card_x_pos, p2_card_y_pos, 280, 160, 6)
    p3_card_x_pos, p3_card_y_pos = update_card_position(p3_card_x_pos, p3_card_y_pos, 300, 160, 4)
    p4_card_x_pos, p4_card_y_pos = update_card_position(p4_card_x_pos, p4_card_y_pos, 320, 160, 4)
    
    draw_game_elements()
    pos = pygame.mouse.get_pos()
    if button_SNAP.collidepoint(pos):
        font_SNAP = pygame.font.Font(font_file, 110)
        text_SNAP = font_SNAP.render("SNAP", True, (255,0,0))
        screen.blit(text_SNAP, (190,300))
    else:
        screen.blit(text_SNAP, (190,300))

    #print((animation_time_start - time.time()))
    if((time.time() - animation_time_start) > 2):
        if counter < 4:
            counter += 1
        else:
            counter = 1
            first = False
            if card_counter < (len(player_1_hand) - 1):
                card_counter += 1
                #print(card_counter)
                
        match counter:
            case 1:
                p1_card_x_pos = 100
                p1_card_y_pos = 300
            case 2:
                p2_card_x_pos = 40
                p2_card_y_pos = 52
                central_pile.append(player_1_hand[0])
                player_1_hand.pop(0)
                central_pile.append(player_2_hand[0])                
                player_2_hand.pop(0)
                print(central_pile)
            case 3:
                p3_card_x_pos = 452
                p3_card_y_pos = 52 
                central_pile.append(player_3_hand[0])
                player_3_hand.pop(0)
            case 4:
                p4_card_x_pos = 440
                p4_card_y_pos = 280  
                central_pile.append(player_4_hand[0])
                player_4_hand.pop(0)
        animation_time_start = time.time()

    cards_animation(counter)

    pygame.display.update()
    
    for hand in players_hands:
        check_player_card_count(hand)
        
    clock.tick(60)

print("Game Over")
