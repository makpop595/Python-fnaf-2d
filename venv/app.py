import random
import time
from enum import Enum
from sys import exit

import pygame

pygame.init()
screen = pygame.display.set_mode((1800, 900), pygame.RESIZABLE)
pygame.display.set_caption("fnaf BETA bild")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)

# numbers states
power_percentage = 100
time1 = 1
distance = 2
night_Bonnie_AI_value = 18
bonnie_movement_timer = 0

# doors state
left_door_y = 200
wemt_door_y = 199
right_door_y = 200

# boolean states
right_door_open = True
middle_went_open = True
left_door_open = True
Vent_seen_last = False

class ActiveMode(Enum):
    NORMAL = 0
    GAME_OVER = 1
    GAME_WON = 2
    CAMERAS = 3
    Vent_cameras = 4


# main state, stage
active_mode = ActiveMode.NORMAL


class CameraMode(Enum):
    CAM1 = 1
    CAM2 = 2
    CAM3 = 3
    CAM4 = 4
    CAM5 = 5
    CAM6 = 6


# camera states
camera_mode = CameraMode.CAM1



def power():
    global power_percentage
    power_percentage_rounded = int(round(power_percentage, 0))
    power_text = font.render(f"{power_percentage_rounded}% Power", True, "Black")
    screen.blit(power_text, (0, 40))


def time_display():
    global time1
    time1_rounded = int(round(time1, 0))
    time_text = font.render(f"{time1_rounded}AM", True, "Black")
    screen.blit(time_text, (0, 0))
    time1 += 0.001


def d(message, pos):
    debug_text = font.render(f"Debug: {message}", True, "Magenta")
    screen.blit(debug_text, (200, pos * 50))


def move_bonnie():
    global distance, active_mode, bonnie_movement_timer
    current_time = pygame.time.get_ticks()

    if distance == 0 and left_door_open:
        if current_time - bonnie_movement_timer >= 3000:
            if distance == 0 and left_door_open:
                # Reset the movement timer
                bonnie_movement_timer = current_time
                # Set active mode to death screen if distance reaches 0 or goes negative and the left door is open
                active_mode = ActiveMode.GAME_OVER
            else: return



    else:
        # Check if it's time to change Bonnie's movement
        if current_time - bonnie_movement_timer >= 5000:  # 5000 milliseconds = 5 seconds
            # Reset the movement timer
            bonnie_movement_timer = current_time

            # Simulate Bonnie's movement every frame
            # Adjust distance and active_mode based on AI behavior and game state
            m_op = random.randint(1, 20)  # Random number for AI behavior
            if m_op < night_Bonnie_AI_value:
                distance -= 1  # Reduce distance if the AI decides to move closer

        elif distance == -1:
            distance = 6


def reducePowerIfDoorsClosed():
    global power_percentage, left_door_open, middle_went_open, right_door_open
    if not left_door_open:
        power_percentage -= 0.003
    elif not middle_went_open:
        power_percentage -= 0.006
    elif not right_door_open:
        power_percentage -= 0.003




left_door_surface = pygame.image.load("grafigs/door.png").convert_alpha()

right_door_surface = pygame.image.load("grafigs/door.png").convert_alpha()

went_door_surfase = pygame.image.load("grafigs/went door .png").convert_alpha()

schoker = pygame.image.load("grafigs/schoker.png")

wal_surface = pygame.Surface((50, 900)).convert_alpha()
wal_surface.fill("#6D798C")

wal_surface1 = pygame.Surface((50, 900)).convert_alpha()
wal_surface1.fill("#6D798C")

wal_surface2 = pygame.Surface((1800, 200)).convert_alpha()
wal_surface2.fill("#6D798C")

wal_surface3 = pygame.Surface((350, 151)).convert_alpha()
wal_surface3.fill("#6D798C")

wal_surface4 = pygame.Surface((300, 701)).convert_alpha()
wal_surface4.fill("#6D798C")

wal_surface5 = pygame.Surface((285, 701)).convert_alpha()
wal_surface5.fill("#6D798C")

middle_HalvayDark = pygame.Surface((350, 600))

left_door_dark = pygame.Surface((390, 700)).convert_alpha()


went_dark = pygame.Surface((350, 199)).convert_alpha()

right_door_dark = pygame.Surface((390, 700)).convert_alpha()

game_ower_screen = pygame.Surface((1800, 900)).convert()
game_ower_screen.fill("RED")

game_woon_screen = pygame.Surface((1800, 900)).convert()
game_woon_screen.fill("Green")

camera_scrren_cam_1 = pygame.image.load("grafigs/camera test/camera.png").convert_alpha()
camera_scrren_cam_2 = pygame.image.load("grafigs/camera test/camera 2 test.png").convert_alpha()
camera_scrren_cam_3 = pygame.image.load("grafigs/camera test/camera 3 .png").convert_alpha()
camera_scrren_cam_4 = pygame.image.load("grafigs/camera test/camera 4 .png").convert_alpha()
camera_scrren_cam_5 = pygame.image.load("grafigs/camera test/camera 5 .png").convert_alpha()
camera_scrren_cam_6 = pygame.image.load("grafigs/camera test/camera 6 .png").convert_alpha()
camera_map_floor = pygame.image.load("grafigs/floor_map.png").convert_alpha()
camera_map_vent = pygame.image.load("grafigs/Camera_Map.png").convert_alpha()



while True:



    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("testttttt")
                if distance == 1 or distance == 2:
                    left_door_dark.fill("#4a1d9b")
                else:
                    left_door_dark.fill("#FFFFFF")
            else:
                left_door_dark.fill("#000000")
                print("test")
            if active_mode == ActiveMode.CAMERAS or ActiveMode.Vent_cameras:

                if event.key == pygame.K_v and active_mode == ActiveMode.CAMERAS or active_mode == ActiveMode.Vent_cameras:
                    vent_seen_last = True
                    if active_mode == ActiveMode.CAMERAS:
                        active_mode = ActiveMode.Vent_cameras
                    else: active_mode = ActiveMode.CAMERAS

                if event.key == pygame.K_1:
                    camera_mode = CameraMode.CAM1
                elif event.key == pygame.K_2:
                    camera_mode = CameraMode.CAM2
                elif event.key == pygame.K_3:
                    camera_mode = CameraMode.CAM3
                elif event.key == pygame.K_4:
                    camera_mode = CameraMode.CAM4
                elif event.key == pygame.K_5:
                    camera_mode = CameraMode.CAM5
                elif event.key == pygame.K_6:
                    camera_mode = CameraMode.CAM6

            if event.key == pygame.K_SPACE:

                if Vent_seen_last:
                    if active_mode == ActiveMode.NORMAL:
                        active_mode = ActiveMode.Vent_cameras


                elif active_mode == ActiveMode.CAMERAS:
                    active_mode = ActiveMode.NORMAL
                    Vent_seen_last = False

                elif not Vent_seen_last and active_mode == ActiveMode.NORMAL:
                    active_mode = ActiveMode.CAMERAS

                elif active_mode == ActiveMode.Vent_cameras:
                    active_mode = ActiveMode.NORMAL
                    Vent_seen_last = True
                    print(Test)







            if event.key == pygame.K_ESCAPE:
                if active_mode == ActiveMode.GAME_OVER:
                    active_mode = ActiveMode.NORMAL
                    power_percentage = 100
                    time1 = 1
                    distance = 2
                    night_Bonnie_AI_value = 18
                    bonnie_movement_timer = 0

                    # doors state
                    left_door_y = 200
                    wemt_door_y = 199
                    right_door_y = 200

                    # boolean states
                    right_door_open = True
                    middle_went_open = True
                    left_door_open = True

            if event.key == pygame.K_d:

                if right_door_open:
                    right_door_open = False

                else:
                    right_door_open = True

            if event.key == pygame.K_s:
                if middle_went_open:
                    middle_went_open = False
                else:
                    middle_went_open = True

            if event.key == pygame.K_a:

                if left_door_open:
                    left_door_open = False
                else:
                    left_door_open = True

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if power_percentage <= 0:
        active_mode = ActiveMode.GAME_OVER

    if time1 >= 7:
        active_mode = ActiveMode.GAME_WON

    move_bonnie()


    if active_mode  == ActiveMode.Vent_cameras:
        reducePowerIfDoorsClosed()

        if camera_mode == CameraMode.CAM1:
            screen.blit(camera_scrren_cam_1, (0, 0))
            screen.blit(camera_map_vent, (0, 320))

        if camera_mode == CameraMode.CAM2:
            screen.blit(camera_scrren_cam_2, (0, 0))
            screen.blit(camera_map_vent, (0, 320))

        if camera_mode == CameraMode.CAM3:
            screen.blit(camera_scrren_cam_3, (0, 0))
            screen.blit(camera_map_vent, (0, 320))

        if camera_mode == CameraMode.CAM4:
            screen.blit(camera_scrren_cam_4, (0, 0))
            screen.blit(camera_map_vent, (0, 320))

        if camera_mode == CameraMode.CAM5:
            screen.blit(camera_scrren_cam_5, (0, 0))
            screen.blit(camera_map_vent, (0, 320))

        if camera_mode == CameraMode.CAM6:
            screen.blit(camera_scrren_cam_6, (0, 0))
            screen.blit(camera_map_vent, (0, 320))

        power()
        time_display()

    if active_mode == ActiveMode.GAME_OVER:
        screen.blit(game_ower_screen, (0, 0))

    elif active_mode == ActiveMode.GAME_WON:
        screen.blit(game_woon_screen, (0, 0))

    elif active_mode == ActiveMode.CAMERAS:
        reducePowerIfDoorsClosed()

        if camera_mode == CameraMode.CAM1:
            screen.blit(camera_scrren_cam_1, (0, 0))
            screen.blit(camera_map_floor,(0,320))

        if camera_mode == CameraMode.CAM2:
            screen.blit(camera_scrren_cam_2, (0, 0))
            screen.blit(camera_map_floor, (0, 320))

        if camera_mode == CameraMode.CAM3:
            screen.blit(camera_scrren_cam_3, (0, 0))
            screen.blit(camera_map_floor, (0, 320))

        if camera_mode == CameraMode.CAM4:
            screen.blit(camera_scrren_cam_4, (0, 0))
            screen.blit(camera_map_floor, (0, 320))

        if camera_mode == CameraMode.CAM5:
            screen.blit(camera_scrren_cam_5, (0, 0))
            screen.blit(camera_map_floor, (0, 320))

        if camera_mode == CameraMode.CAM6:
            screen.blit(camera_scrren_cam_6, (0, 0))
            screen.blit(camera_map_floor, (0, 320))

        power()
        time_display()

    elif active_mode == ActiveMode.NORMAL:

        if left_door_open:
            left_door_y -= 50

            if left_door_y < -700:
                left_door_y = -700

        else:
            left_door_y += 50
            power_percentage -= 0.003
            if left_door_y > 200:
                left_door_y = 200

        if middle_went_open:
            wemt_door_y -= 20
            if wemt_door_y < -199:
                wemt_door_y = -199

        else:
            wemt_door_y += 20
            power_percentage -= 0.006
            if wemt_door_y > 0:
                wemt_door_y = 0

        if right_door_open:
            right_door_y -= 50
            if right_door_y < -700:
                right_door_y = -700

        else:
            right_door_y += 50
            power_percentage -= 0.003
            if right_door_y > 200:
                right_door_y = 200

        screen.blit(right_door_dark, (1360, 200))
        screen.blit(left_door_dark, (50, 200))

        screen.blit(left_door_surface, (50, left_door_y))
        screen.blit(right_door_surface, (1360, right_door_y))

        screen.blit(wal_surface, (0, 0))
        screen.blit(wal_surface1, (1750, 0))
        screen.blit(wal_surface2, (50, 0))
        screen.blit(wal_surface3, (725, 199))
        screen.blit(wal_surface4, (440, 200))
        screen.blit(wal_surface5, (1075, 200))
        screen.blit(went_dark, (725, 0))
        screen.blit(went_door_surfase, (725, wemt_door_y))
        screen.blit(schoker, (550, 600))
        screen.blit(middle_HalvayDark, (740, 300))

        power()
        time_display()

    d("Active mode: " + str(active_mode), 1)
    d("camera_mode: " + str(camera_mode), 2)
    d("left_door_open: " + str(left_door_open), 3)
    d("midle_vent_open" + str(middle_went_open),4)
    d("right_door_open: " + str(right_door_open), 5)
    d("Bonnie_distance: " + str(distance), 6)
    d("Vent_seen_last: " + str(Vent_seen_last), 7)


    pygame.display.update()
    clock.tick(60)
