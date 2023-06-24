import pygame
import random

pygame.init()
win_dimention=(700,700)
window=pygame.display.set_mode(win_dimention)
pygame.display.set_caption('Number Guessing Game')
window2=pygame.display.set_mode(win_dimention)
clock=pygame.time.Clock()
clock2=pygame.time.Clock()

def main_game(username):

# properties of Font related to unser input number, guess text and user name as well
    number_font=pygame.font.SysFont('Calibri',15,True)
    enter_number= number_font.render('Enter Number',True,(0,0,0))
    guess=pygame.font.SysFont('aerialblack',30,True)
    guess_font= guess.render('Enter',True,(0,0,0))
    guessednumber_font = pygame.font.SysFont('aerialblack', 35)
    user=pygame.font.SysFont('Calibri',40,True)
    username_font= user.render(f'Hello {username.rstrip(username[-1])}',True,(0,0,0))

# To store user input number and random_number for storing random number between 1 to 100 and for counting total attempts
    number_input = ''     
    random_number= random.randint(1,100)
    remaining_attempts = 10

# create rectangle so to use them to click on by mouse
    input_rect = pygame.Rect(305, 300, 100, 30)
    guess_rect=pygame.Rect(305,340,100,30)
    yes_rect=pygame.Rect(50,530,70,30)
    no_rect=pygame.Rect(610,530,70,30)

#  color_active is for the color of textbox when I haven't click on it and color_passive is juct opposite of that
    color_active = pygame.Color('purple')
    color_passive = pygame.Color('blue')
    color = color_passive
    
    active=False # used to change the color of the text box 
    game_started = False # used to stop game during win,loose and game over

    #  used for establishing condition to print statement like you loose,win, greater number,lower number and game over
    display_won = False
    display_game_over = False
    display_higher = False
    display_lower = False
    display_error = False

    # This function stores the all the information of text like play again,yes, no, information such as font,colors,position and rectangle box
    def yes_no():
        playagain=pygame.font.SysFont('aerialblack',25,True)
        playagain_font= playagain.render(f"Do You want to play again?",True,(0,0,0))
        window2.blit(playagain_font,(50,460))
        pygame.draw.rect(window2,(0,0,255),yes_rect)
        pygame.draw.rect(window2,(255,0,0),no_rect)
        yes=pygame.font.SysFont('calibri',25,True)
        yes_font= yes.render(f"Yes",True,(0,0,0))
        no=pygame.font.SysFont('calibri',25,True)
        no_font= no.render(f"No",True,(0,0,0))
        window2.blit(yes_font,(60,535))
        window2.blit(no_font,(630,535))

    # used to display text related to won
    def won():
        window2.fill((153,204,255)) # to change color of game window on winning
        won=pygame.font.SysFont('aerialblack',25,True)
        won_font= won.render(f"Congratulations! You guessed the correct number: {random_number}",True,(0,0,0))
        window2.blit(won_font,(100,390))

    # used to display text related to gameover
    def game_over():
        window2.fill((255,153,153)) # to change color of game window on winning
        gameover=pygame.font.SysFont('aerialblack',25,True)
        gameover_font= gameover.render(f"Game Over! You ran out of attempts. The number was {random_number}",True,(0,0,0))
        window2.blit(gameover_font,(100,390))

    # used to display text if we enter higher number then random number
    def higher():
        higher=pygame.font.SysFont('aerialblack',25,True)
        higher_font= higher.render(f"Try again! The number is higher. Remaining attempts: {remaining_attempts}",True,(0,0,0))
        window2.blit(higher_font,(100,400))

    # used to display text if we enter lower number then random number
    def lower():

        lower=pygame.font.SysFont('aerialblack',25,True)
        lower_font= lower.render(f"Try again! The number is lower. Remaining attempts: {remaining_attempts}",True,(0,0,0))
        window2.blit(lower_font,(100,410))
    # used to display text related to invalid input like string
    def error():
        error=pygame.font.SysFont('aerialblack',25,True)
        error_font= error.render("Invalid input. Please enter an integer.",True,(0,0,0))
        window2.blit(error_font,(200,420))

    flag2=True
    while flag2:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                flag2=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active and not game_started:
                    # used to delate character of string number on pressing backspace
                    if event.key == pygame.K_BACKSPACE:
                        number_input = number_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        #  this expection aries if players enters a string or any othr data type except interger
                        try:
                            user_guess = int(number_input)
                            remaining_attempts -= 1 
                            if user_guess == random_number:
                                display_won=True
                                # except display_ won all the condition becomes true so that other statement does not appers with this statement
                                game_started = False
                                display_game_over = False
                                display_higher = False
                                display_lower = False
                                display_error = False    
                            elif remaining_attempts == 0:
                                display_game_over=True
                                # except display_ game_over all the condition becomes true so that other statement does not appers with this statement
                                game_started = False
                                display_won = False
                                display_higher = False
                                display_lower = False
                                display_error = False
                            elif user_guess > random_number:
                                display_higher=True
                                # except display_ higher all the condition becomes true so that other statement does not appers with this statement
                                display_won = False
                                display_game_over = False
                                display_lower = False
                                display_error = False
                            else:
                                display_lower=True
                                # except display_ lower all the condition becomes true so that other statement does not appers with this statement
                                display_won = False
                                display_game_over = False
                                display_higher = False
                                display_error = False
                        except ValueError:
                            display_error=True
                            # except display_ error all the condition becomes true so that other statement does not appers with this statement
                            display_won = False
                            display_game_over = False
                            display_higher = False
                            display_lower = False
                            
                        if remaining_attempts > 0:
                            number_input= ''
                        else:
                            display_game_over=True
                            # except display_ game_over all the condition becomes true so that other statement does not appers with this statement
                            game_started = False
                            display_won = False
                            display_higher = False
                            display_lower = False
                            display_error = False

                    else:
                        number_input += event.unicode  # Joins characters to make a string
        
        window2.fill((255,153,255))   
        if active:
            color = color_active
        else:
            color = color_passive
            window.blit(enter_number,(310,305))

        #  Calling all the display statement according to condition
        if display_won:
            won()
            yes_no()
        #  By clicking on yes block of game window the game will restart and all the remaining_attempts becomes 10
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_rect.collidepoint(event.pos):
                    remaining_attempts=10
                    display_won=False
        elif display_game_over:
            game_over()
            yes_no()
            # By clicking on no block of game window the game will becomes cancle
            if event.type == pygame.MOUSEBUTTONDOWN:
                if no_rect.collidepoint(event.pos):
                    flag2=False
        elif display_error:
            error()
        elif display_higher:
            higher()
        elif display_lower:
            lower()


        pygame.draw.rect(window2, color, input_rect, 3)
        user_text = guessednumber_font.render(number_input, True, (0,0,0))
        pygame.draw.rect(window2,(255,0,0),guess_rect) 
        window2.blit(guess_font,(320,345)) 
        window2.blit(user_text, (340,303))
        window2.blit(username_font,(270,190))
        input_rect.w = max(100, user_text.get_width()+10)
        clock2.tick(45)
        pygame.display.update()
    pygame.quit()
    quit()  # Here function over

# properties of Font related to unser input name,text, welcome and enter as well
wel=pygame.font.SysFont('arialblack',40,False)
welcome=wel.render('Welcome',True,(0,0,0))
inst=pygame.font.SysFont('Agency FB',40,True)
instruction=inst.render('Instructions :',True,(45,15,243))
text=pygame.font.SysFont('Calibri',30,False)
textinstruct= text.render('1.You have to guass the number in between 1 and 100.',True,(225,225,225))
text1=pygame.font.SysFont('Calibri',30,False)
textinstruct1= text1.render('2.You have 10 attenmpts to guess the number.',True,(225,225,225))
text2=pygame.font.SysFont('Calibri',30,False)
textinstruct2= text2.render('3.If you guass correct number, you win.',True,(225,225,225)) 
enter_text=pygame.font.SysFont('Agency FB',20,True)
enter=enter_text.render('Press ENTER to start',True,(255,255,255))
name=pygame.font.SysFont('Calibri',15,True)
enter_name= name.render('Enter name',True,(225,225,225)) 
input_font = pygame.font.SysFont('Calibri', 30)
input_rect = pygame.Rect(305, 300, 300, 30)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False
flag= True
user_input = ''
while flag:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            flag=False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        # used to delate character of string on pressing backspace
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
                    key= pygame.key.get_pressed()
                    #  by pressing enter call the main game window
                    if key[pygame.K_RETURN]:
                        main_game(user_input)
    window.fill((255,51,51))  
    if active:
        color = color_active
    else:
        color = color_passive
        window.blit(enter_name,(310,305))

    pygame.draw.rect(window, color, input_rect, 3)
    user_text = input_font.render(user_input, True, (0,0,0))
    window.blit(user_text, (310,300))
    input_rect.w = max(100, user_text.get_width()+10)
    window.blit(welcome,(250,240))
    window.blit(instruction,(5,380))
    window.blit(enter,(270,340))
    window.blit(textinstruct,(10,430))
    window.blit(textinstruct1,(10,460))
    window.blit(textinstruct2,(10,490))
    clock.tick(45)
    pygame.display.update()
pygame.quit()
quit()