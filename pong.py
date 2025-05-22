import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BALL_RADIUS = 10
PAD_WIDTH, PAD_HEIGHT = 8, 100
HALF_PAD_WIDTH, HALF_PAD_HEIGHT = PAD_WIDTH // 2, PAD_HEIGHT // 2
INITIAL_BALL_VEL = 6

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Ball and paddle initialization
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [INITIAL_BALL_VEL, -INITIAL_BALL_VEL]

paddle1_pos = [HALF_PAD_WIDTH - 1, HEIGHT // 2]
paddle2_pos = [WIDTH + 1 - HALF_PAD_WIDTH, HEIGHT // 2]
paddle1_vel = 0
paddle2_vel = 0

# Scores
score1 = 0
score2 = 0

# Helper function to reset ball position and velocity
def ball_init(right):
    global ball_pos, ball_vel
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    horz = random.randrange(2, 4)
    vert = random.randrange(1, 3)
    if right:
        ball_vel = [horz, -vert]
    else:
        ball_vel = [-horz, -vert]

    # Increase initial speed
    ball_vel[0] *= 1.5
    ball_vel[1] *= 1.5
    
    # Add delay of 2 seconds before the ball starts moving
    pygame.time.delay(2000)  # 2000 milliseconds = 2 seconds

# Key handlers
def keydown(event):
    global paddle1_vel, paddle2_vel
    if event.key == pygame.K_w:
        paddle1_vel = -6
    elif event.key == pygame.K_s:
        paddle1_vel = 6
    elif event.key == pygame.K_UP:
        paddle2_vel = -6
    elif event.key == pygame.K_DOWN:
        paddle2_vel = 6
    elif event.key == pygame.K_q:
        pygame.quit()
        exit()

def keyup(event):
    global paddle1_vel, paddle2_vel
    if event.key in (pygame.K_w, pygame.K_s):
        paddle1_vel = 0
    elif event.key in (pygame.K_UP, pygame.K_DOWN):
        paddle2_vel = 0

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keydown(event)
        elif event.type == pygame.KEYUP:
            keyup(event)
    
    # Update paddle positions
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    
    # Keep paddles on the screen
    if paddle1_pos[1] < HALF_PAD_HEIGHT:
        paddle1_pos[1] = HALF_PAD_HEIGHT
    if paddle1_pos[1] > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    if paddle2_pos[1] < HALF_PAD_HEIGHT:
        paddle2_pos[1] = HALF_PAD_HEIGHT
    if paddle2_pos[1] > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Ball collision with top and bottom
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # Ball collision with paddles
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if paddle1_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            # Increase ball velocity
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            score2 += 1
            ball_init(True)
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if paddle2_pos[1] - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos[1] + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            # Increase ball velocity
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            score1 += 1
            ball_init(False)
    
    # Draw everything
    screen.fill(BLACK)
    pygame.draw.line(screen, RED, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 1)
    pygame.draw.line(screen, RED, [PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(screen, RED, [WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(screen, RED, [WIDTH // 2, HEIGHT // 2], 70, 1)
    
    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, (paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT, PAD_WIDTH, PAD_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT, PAD_WIDTH, PAD_HEIGHT))
    
    # Draw scores
    font = pygame.font.SysFont("Comic Sans MS", 20)
    score1_surf = font.render(str(score1), True, WHITE)
    score2_surf = font.render(str(score2), True, WHITE)
    screen.blit(score1_surf, (WIDTH // 4, 20))
    screen.blit(score2_surf, (WIDTH * 3 // 4, 20))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
