import pygame
import pygwidgets
import random
from type_effectiveness import *
from pygame.locals import *

BLACK = (0, 0, 0)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    

class Game:
    def __init__(self):
        self.attacker = None
        self.correct_answer = None
        self.choices = []
        self.feeback_text = ''
        self.feedback_timer = 0
        self.time_limit = 60
        self.timer = self.time_limit
        self.last_tick = pygame.time.get_ticks()
        self.score = 0
        self.game_time = 60
        self.question_display = pygwidgets.DisplayText(screen, (300, 50), "", fontSize=36)

        self.start_time = pygame.time.get_ticks()

        self.game_over = False

        # images downloaded from Ian Skelskey on Itch.io

        self.idle_frames = [pygame.transform.scale(pygame.image.load("professor_images/professor_1.png"), (200, 300)),
                            pygame.transform.scale(pygame.image.load("professor_images/professor_2.png"), (200, 300)),
                            pygame.transform.scale(pygame.image.load("professor_images/professor_3.png"), (200, 300)),
                            pygame.transform.scale(pygame.image.load("professor_images/professor_4.png"), (200, 300))]
        
        self.frame = 0
        self.frame_timer = 0
        self.frame_speed = 500

        self.buttons = [pygwidgets.TextButton(screen,(150,500),'',width=150,height=50),
        pygwidgets.TextButton(screen,(350,500),'',width=150,height=50),
        pygwidgets.TextButton(screen,(550,500),'',width=150,height=50),
        pygwidgets.TextButton(screen,(750,500),'',width=150,height=50)]
        

        self.question_text = ''
        self.new_question()

    def new_question(self):

        self.attacker = random.choice(list(type_effectiveness_chart.keys()))
        self.question_text = f"What is {self.attacker} effective against?"

        correct_list = type_effectiveness_chart[self.attacker]

        self.correct_answers = correct_list

        all_types = list(type_effectiveness_chart.keys())

        wrong_answer_pool = [w for w in all_types if w != self.correct_answer and w != self.attacker]

        if len(wrong_answer_pool) < 3:
            raise ValueError("Not enough wrong answers in dataset")

    # 4. Always pick exactly 3 wrong answers
        wrong_answers = random.sample(wrong_answer_pool, 3)

        self.choices = wrong_answers + self.correct_answers.copy()
        random.shuffle(self.choices)

        for i in range(4):
            rect = self.buttons[i].getRect()
            self.buttons[i] = pygwidgets.TextButton(screen,rect.topleft, self.choices[i],width=150,
        height=50)
            
        
        
    
    def handle_event(self, event):
            if self.game_over:
                return
            
            i = 0
            
            for btn in (self.buttons):
                if btn.handleEvent(event):

                    clicked = self.choices[i]
                    correct = self.correct_answer

                    if clicked in self.correct_answers:
                        self.feedback_text = "Correct!"
                        self.score += 1
                    else:
                        self.feedback_text = "Wrong!"

                    self.feedback_timer = 3000

                    self.new_question()
                    break
                    
                i += 1

    def update_timer(self):
        now = pygame.time.get_ticks()

        if now - self.last_tick >= 1000:
            self.timer -= 1
            self.last_tick = now
        
        if self.timer <= 0:
            self.feedback_text = "Time's Up!"
            self.feedback_timer = 30
            self.new_question()

    def update_animation(self):
        self.frame_timer += 1

        if self.frame_timer >= self.frame_speed:
            self.frame_timer = 0
            self.frame += 1

        if self.frame >= len(self.idle_frames):
            self.frame = 0

    def update_game_timer(self):
        now = pygame.time.get_ticks()
        elapsed = (now - self.start_time) // 1000

        if elapsed >= self.game_time:
            self.game_over = True

    def draw(self, screen, font):
        screen.fill((255, 255, 255))

        if self.game_over:
            end_text = font.render(f"Game Over! Score: {self.score}", True, (0, 0, 0))
            screen.blit(end_text, (350, 250))
            return

        
        self.question_display.setValue(self.question_text)
        self.question_display.draw()

        if self.feedback_timer > 0:
            feedback_surface = font.render(self.feedback_text, True, (0, 0, 0))
            screen.blit(feedback_surface, (475, 450))
            self.feedback_timer -= 1

        for btn in self.buttons:
            btn.draw()
        
        timer_surface = font.render(f"Time: {self.timer}", True, (0, 0, 0))
        screen.blit(timer_surface,(100, 100))
    
        sprite = self.idle_frames[self.frame]
        screen.blit(sprite, (400, 100))

        


game = Game()
font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        game.handle_event(event)
    
    game.update_timer()
    game.update_animation()
    game.update_game_timer()

    game.draw(screen, font)
    pygame.display.flip()
    