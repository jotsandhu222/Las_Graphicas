import pygame
import pyttsx3
import os
import string
import time

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Initialize black screen
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Sign Language Display")
font = pygame.font.SysFont(None, 48)

image_folder = "sign_images"

def speak_and_show(letter):
    print(f"Pressed: {letter.upper()}")
    
    
    engine.say(f"{letter.lower()}")
    engine.runAndWait()

    image_path = os.path.join(image_folder, f"{letter.upper()}.jpg")
    # image available 
    if os.path.exists(image_path):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (400, 400))
        screen.blit(image, (0, 0))
        pygame.display.flip()
    
    # no image available
    else:
        screen.fill((0, 0, 0))
        text = font.render(f"No image for {letter.upper()}", True, (255, 0, 0))
        screen.blit(text, (50, 180))
        pygame.display.flip()

def speak_word(word):
    print(f"speaking full word: {word}")
    engine.say(f"the word is {word}")
    engine.runAndWait()


#main loop
running = True
current_word = ""
word_start_time = None
word_time_limit = 20
print("Press a key (A-Z or 0-9). Press ESC to quit.")


while running:
    current_time = time.time()
    if word_start_time and (current_time - word_start_time > word_time_limit):
        current_word = ""
        word_start_time = None
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            
            if key_name in string.ascii_lowercase + string.digits:
                speak_and_show(key_name)
                current_word += key_name
                if not word_start_time:
                    word_start_time = time.time()
                    
            elif event.key == pygame.K_RETURN:
                if current_word:
                    speak_word(current_word)
                    current_word = ""
                    word_start_time = None
                    
            elif event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
