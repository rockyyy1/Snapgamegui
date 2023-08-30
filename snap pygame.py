import pygame
import pygame.font
import random
import time
from DeckOfCards import Player

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Snap by Rocky Trang")
clock = pygame.time.Clock()
font_file = "Graphics/disko_ot.otf"

def load_permanent_surfaces():
    """Load background, images and text surfaces"""
    
    global green_background_surface, python_playing_cards_surface, text_SNAP, button_SNAP, text_you, font_hover, text_hover
    
    #permanent surfaces
    green_background_surface = pygame.image.load("Graphics/green_background.png")
    python_playing_cards_surface = pygame.image.load("Graphics/pythonplayingcards.png")
    python_playing_cards_surface = pygame.transform.scale(python_playing_cards_surface, (python_playing_cards_surface.get_width() // 4, python_playing_cards_surface.get_height() //4))
    screen.blit(green_background_surface, (0, 0))

    #snap button
    font_SNAP = pygame.font.Font(font_file, 100)
    text_SNAP = font_SNAP.render("SNAP", True, (0,0,0))
    button_SNAP = text_SNAP.get_rect(topleft=(190,300))

    #texts
    font_you = pygame.font.Font(font_file, 30)
    text_you = font_you.render("you", True, (0,0,0))
    font_hover = pygame.font.Font(font_file, 25)
    text_hover = font_hover.render("(click below!/spacebar)", True, (0,0,0))
    screen.blit(text_hover, (175,280))
    
    
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
    
def load_playing_card_image(card):
    """Loads an image from file containing playing card images

    Args:
        card (str): The name of the card e.g "Ace of Spades"

    Returns:
        playing_card_image: an image file of the argument 
    """
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

def isHandEmpty(hand):
    """Checks if the number of cards in hand is 0

    Args:
        hand (list): The player's hand

    Returns:
        True if list is empty
        False if list is not empty
    """
    cards_in_hand = len(hand)
    if cards_in_hand == 0:
        return True
    else:
        return False

def update_card_position(x, y, target_x, target_y, step):
    """Moves card position each frame by a step if not at target destination

    Args:
        x (int): the current x position
        y (int): the current y position
        target_x (int): final x position
        target_y (int): final y position
        step (int): how much card (pixels) move each frame

    Returns:
        x,y (int): next card position
    """
    if x < target_x:
        x += step
    elif x > target_x:
        x -= step
    if y < target_y:
        y += step
    elif y > target_y:
        y -= step
    return x, y

def cards_animation(current_player):
    """Draws the moving playing back card and card played faced up

    Args:
        current_player (int): The player turning over a card (1-4)
    """
    global p1_card_x_pos, p1_card_y_pos, p2_card_x_pos, p2_card_y_pos, p3_card_x_pos, p3_card_y_pos, p4_card_y_pos, p4_card_x_pos 
    global firstTurn
    backcard = pygame.image.load("Graphics/Vector Playing Cards/backcard.png")
    backcard = pygame.transform.scale(backcard, (85,115))
        
    #Player 1
    if current_player == 1:
        if len(central_pile) >= 2:
            if not firstTurn:
                if len(central_pile) > 2:
                    screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (260, 160))
                screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (280, 160))    
            elif firstTurn:
                if len(central_pile) > 2:
                    screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (260, 160))
            screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (280, 160))
        screen.blit(load_playing_card_image(("backcard.png")), (p1_card_x_pos, p1_card_y_pos))
        if p1_card_x_pos == 260 and p1_card_y_pos == 160:
            screen.blit(load_playing_card_image(str(central_pile[-1]) + ".png"), (260, 160))            
            
    #Player 2
    if current_player == 2:
        if len(central_pile) >= 2:
            if not firstTurn:
                if len(central_pile) > 2:
                    screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (280, 160))
                screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (260, 160))
            elif firstTurn:
                if len(central_pile) > 2:
                    screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (280, 160))
            screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (260, 160))
        screen.blit(load_playing_card_image(("backcard.png")), (p2_card_x_pos, p2_card_y_pos))
        if p2_card_x_pos == 280 and p2_card_y_pos == 160:
            screen.blit(load_playing_card_image(str(central_pile[-1]) + ".png"), (280, 160))
            
    #Player 3
    elif current_player == 3:
        if len(central_pile) >= 2:
            if not firstTurn:
                if len(central_pile) > 2:
                    screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (260, 160))
                screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (280, 160))    
            elif firstTurn:
                if len(central_pile) > 2:
                  screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (260, 160))
            screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (280, 160))
        screen.blit(load_playing_card_image(("backcard.png")), (p3_card_x_pos, p3_card_y_pos))
        if p3_card_x_pos == 260 and p3_card_y_pos == 160:
            screen.blit(load_playing_card_image(str(central_pile[-1]) + ".png"), (260, 160))
            
    #Player 4
    elif current_player == 4:
        if len(central_pile) >= 2:
            if not firstTurn:
                if len(central_pile) > 2 :
                    screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (280, 160))
                screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (260, 160))
            elif firstTurn:
                if len(central_pile) > 2:
                    screen.blit(load_playing_card_image(str(central_pile[-3]) + ".png"), (280, 160))
            screen.blit(load_playing_card_image(str(central_pile[-2]) + ".png"), (260, 160))
        screen.blit(load_playing_card_image(("backcard.png")), (p4_card_x_pos, p4_card_y_pos))
        if p4_card_x_pos == 280 and p4_card_y_pos == 160:
            screen.blit(load_playing_card_image(str(central_pile[-1]) + ".png"), (280, 160))

def isSnap(central_pile):
    """Checks the two latest cards in Pile if they match in value

    Args:
        central_pile (list): The Pile where cards are being discarded into

    Returns:
        True if two cards match
        False if they do not match
    """
    if len(central_pile) > 1:
        if central_pile[-1].value == central_pile[-2].value:
            return True
    return False

def snap_call():
    """Chooses a random player (not player 1) to call snap and collect the central pile
    """
    random_player = random.randint(2,4)
    
    if random_player == 2:
        for i in central_pile:
            player_2_hand.append(i)
        print("player 2 called SNAP")
        
    elif random_player == 3:
        for i in central_pile:
            player_3_hand.append(i)
        print("player 3 called SNAP")
        
    elif random_player == 4:
        for i in central_pile:
            player_4_hand.append(i)
        print("player 4 called SNAP")

    central_pile.clear()
    pygame.display.update()

def displayWinner():
    """Checks to see which player has the most cards and declares the winner
    """
    card_counts = []
    for hands in players_hands:
        card_counts.append(len(hands))
    winner = 0
    most_cards = 0
    for i in range(len(card_counts)):
        if card_counts[i] > most_cards:
            most_cards = card_counts[i]
            winner = i + 1
    print("GAME OVER")
    print(f"Player {winner} has won the game with {most_cards} cards!")
    
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
p1_card_x_pos = 98
p1_card_y_pos = 298    
p2_card_x_pos = 40
p2_card_y_pos = 56    
p3_card_x_pos = 452
p3_card_y_pos = 52   
p4_card_x_pos = 442
p4_card_y_pos = 280

animation_time_start = time.time()
opportunity_start_time = time.time() + 12
current_player = 0
#initialize game states
firstTurn = True
user_snap_detected = False
automatic_snap_triggered = False
player_snap_success = False
all_player_have_cards =  True
user_has_snapped = False
while all_player_have_cards:
    load_permanent_surfaces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            font_SNAP = pygame.font.Font(font_file, 110)
            text_SNAP = font_SNAP.render("SNAP", True, (255, 0, 0))
            screen.blit(text_SNAP, (190,300))        
        if event.type == pygame.MOUSEBUTTONDOWN and button_SNAP.collidepoint(event.pos) or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not user_has_snapped:
                user_has_snapped = True
                user_snap_detected = True
                
                if len(central_pile) >= 2:
                    if isSnap(central_pile) == True:
                        if not automatic_snap_triggered:
                            print("YOU CALLED SNAP!")
                            for i in central_pile:
                                player_1_hand.append(i)
                            player_snap_success = True                      
                    else:
                        print("NOT A SNAP - you lose a card :(")
                        #append last card to start of central pile and pop last card in hand
                        if len(player_1_hand) < 1:
                            displayWinner()
                            all_player_have_cards = False
                        central_pile.insert(0, player_1_hand[-1])
                        player_1_hand.pop()
                        player_snap_success = False
                        automatic_snap_triggered = False
                        user_snap_detected = False

    #update card positions each frame      
    p1_card_x_pos, p1_card_y_pos = update_card_position(p1_card_x_pos, p1_card_y_pos, 260, 160, 6)
    p2_card_x_pos, p2_card_y_pos = update_card_position(p2_card_x_pos, p2_card_y_pos, 280, 160, 8)
    p3_card_x_pos, p3_card_y_pos = update_card_position(p3_card_x_pos, p3_card_y_pos, 260, 160, 6)
    p4_card_x_pos, p4_card_y_pos = update_card_position(p4_card_x_pos, p4_card_y_pos, 280, 160, 6)
    
    #hover over button will make it red    
    pos = pygame.mouse.get_pos()
    if button_SNAP.collidepoint(pos) : 
        font_SNAP = pygame.font.Font(font_file, 110)
        text_SNAP = font_SNAP.render("SNAP", True, (255,0,0))
        screen.blit(text_SNAP, (190,300))
 
    #if animation takes more than 2 seconds, finish animation.
    if((time.time() - animation_time_start) > 2):
        pygame.time.set_timer(pygame.USEREVENT, 3000)
        #print((opportunity_start_time - time.time()))
        if ((opportunity_start_time - time.time()) > 9):
            automatic_snap_triggered = True 
            if not user_snap_detected and len(central_pile) >= 2:
                if isSnap(central_pile):
                #another player calls snap
                    snap_call()
    
    #reset game states after snaps
        if player_snap_success:
            central_pile.clear()
        automatic_snap_triggered = False
        user_snap_detected = False
        player_snap_success = False
        pygame.event.clear()
        pygame.time.delay(1000)
        if current_player < 4:
              current_player += 1
              user_has_snapped = False
        else:
            firstTurn = False
            current_player = 1
        
        match current_player:
            case 1:
                p1_card_x_pos = 98
                p1_card_y_pos = 298
                if len(player_1_hand) == 0:
                    print("Player 1 has run out of cards!")
                    displayWinner()
                    break
                central_pile.append(player_1_hand[0])
                player_1_hand.pop(0)
            case 2:
                p2_card_x_pos = 40
                p2_card_y_pos = 56
                if len(player_2_hand) == 0:
                    print("Player 2 has run out of cards!")
                    displayWinner()
                    break
                central_pile.append(player_2_hand[0])
                player_2_hand.pop(0)
            case 3:
                p3_card_x_pos = 452
                p3_card_y_pos = 52 
                if len(player_3_hand) == 0:
                    print("Player 3 has run out of cards!")
                    displayWinner()
                    break
                central_pile.append(player_3_hand[0])
                player_3_hand.pop(0)
            case 4:
                p4_card_x_pos = 442
                p4_card_y_pos = 280  
                if len(player_4_hand) == 0:
                    print("Player 4 has run out of cards!")
                    displayWinner()
                    break
                central_pile.append(player_4_hand[0])
                player_4_hand.pop(0)

        #reset times
        opportunity_start_time = time.time() + 12
        animation_time_start = time.time()
        
    if current_player > 0:
        cards_animation(current_player)

    pygame.display.update()
    clock.tick(60)

