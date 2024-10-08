import random
import time
from enum import Enum
from sys import exit

import pygame

pygame.init()
screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption("fnaf BETA bild")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)

# numbers states
power_percentage = 100
time1 = 1
bonnie_distance = 2
night_Bonnie_AI_value = 18
bonnie_movement_timer = 0

Chica_distance = 2
night_Chica_AI_value = 18
Chica_movement_timer = 7000

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
    Control_panel = 5


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
    time1 += 0.0003


def d(message, pos):
    debug_text = font.render(f"Debug: {message}", True, "Magenta")
    screen.blit(debug_text, (200, pos * 50))


def move_bonnie():
    global bonnie_distance, active_mode, bonnie_movement_timer
    current_time = pygame.time.get_ticks()

    if bonnie_distance == 0 and left_door_open:
        if current_time - bonnie_movement_timer >= 3000:
            if bonnie_distance == 0 and left_door_open:
                # Reset the movement timer
                bonnie_movement_timer = current_time
                # Set active mode to death screen if distance reaches 0 or goes negative and the left door is open
                active_mode = ActiveMode.GAME_OVER
            else:
                return



    else:
        # Check if it's time to change Bonnie's movement
        if current_time - bonnie_movement_timer >= 5000:  # 5000 milliseconds = 5 seconds
            # Reset the movement timer
            bonnie_movement_timer = current_time

            # Simulate Bonnie's movement every frame
            # Adjust distance and active_mode based on AI behavior and game state
            m_op = random.randint(1, 20)  # Random number for AI behavior
            if m_op < night_Bonnie_AI_value:
                bonnie_distance -= 1  # Reduce distance if the AI decides to move closer

        elif bonnie_distance == -1:
            bonnie_distance = 6


def move_Chica():
    global Chica_distance, active_mode, Chica_movement_timer
    current_time = pygame.time.get_ticks()

    if Chica_distance == 0 and right_door_open:
        if current_time - Chica_movement_timer >= 3000:
            if Chica_distance == 0 and right_door_open:
                # Reset the movement timer
                Chica_movement_timer = current_time
                # Set active mode to death screen if distance reaches 0 or goes negative and the left door is open
                active_mode = ActiveMode.GAME_OVER
            else:
                return



    else:
        # Check if it's time to change Bonnie's movement
        if current_time - Chica_movement_timer >= 5000:  # 5000 milliseconds = 5 seconds
            # Reset the movement timer
            Chica_movement_timer = current_time


            # Simulate Bonnie's movement every frame
            # Adjust distance and active_mode based on AI behavior and game state
            m_op = random.randint(1, 20)  # Random number for AI behavior
            if m_op < night_Chica_AI_value:
                Chica_distance -= 1  # Reduce distance if the AI decides to move closer

        elif Chica_distance == -1:
            Chica_distance = 6


def reducePowerIfDoorsClosed():
    global power_percentage, left_door_open, middle_went_open, right_door_open
    if not left_door_open:
        power_percentage -= 0.006
    elif not middle_went_open:
        power_percentage -= 0.009
    elif not right_door_open:
        power_percentage -= 0.006


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

#control panel
slider = pygame.image.load("grafigs/Slider.png").convert_alpha()
slider_scaled = pygame.transform.scale(slider, (300, 600))
button = pygame.image.load("grafigs/Button.png").convert_alpha()
button_scaled = pygame.transform.scale(button, (200, 100))
arrow = pygame.image.load("grafigs/PixelArtIcons-20-512.png").convert_alpha()
arrow_scaled = pygame.transform.scale(arrow, (100, 100))
slider_position_1 = 1
button_x_1 = 150
slider_position_2 = 1
button_x_2 = 150
slider_position_3 = 1
button_x_3 = 150
slider_position_4 = 1
button_x_4 = 150
slider_position_5 = 1
button_x_6 = 150

selected_slider = 1
arrow_y = 196

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                left_door_dark.fill("#000000")

            elif event.key == pygame.K_e:

                right_door_dark.fill("#000000")

        if event.type == pygame.KEYDOWN:
            if active_mode == ActiveMode.Control_panel:

                if event.key == pygame.K_RIGHT:
                    if selected_slider == 1:
                        selected_slider = 2
                    elif selected_slider == 2:
                        selected_slider = 3
                    elif selected_slider == 3:
                        selected_slider = 4
                if event.key == pygame.K_LEFT:
                    if selected_slider == 4:
                        selected_slider = 3
                    elif selected_slider == 3:
                        selected_slider = 2
                    elif selected_slider == 2:
                        selected_slider = 1
                if event.key == pygame.K_DOWN:

                    if selected_slider == 1:
                        if slider_position_1 < 6:
                            slider_position_1 += 1

                    elif selected_slider == 2:
                        if slider_position_2 < 6:
                            slider_position_2 += 1

                    elif selected_slider == 3:
                        if slider_position_3 < 6:
                            slider_position_3 += 1

                    elif selected_slider == 4:
                        if slider_position_4 < 6:
                            slider_position_4 += 1

                if event.key == pygame.K_UP:

                    if selected_slider == 1:
                        if slider_position_1 > 1:
                            slider_position_1 -= 1

                    elif selected_slider == 2:
                        if slider_position_2 > 1:
                            slider_position_2 -= 1

                    elif selected_slider == 3:
                        if slider_position_3 > 1:
                            slider_position_3 -= 1

                    elif selected_slider == 4:
                        if slider_position_4 > 1:
                            slider_position_4 -= 1

            if event.key == pygame.K_c and active_mode == ActiveMode.NORMAL:
                active_mode = ActiveMode.Control_panel

            elif active_mode == ActiveMode.Control_panel and event.key == pygame.K_c:
                active_mode = ActiveMode.NORMAL

            if event.key == pygame.K_e:
                if Chica_distance == 0 or Chica_distance == 1:
                    right_door_dark.fill("#f5e942")
                    power_percentage -= 0.004
                else:
                    right_door_dark.fill("#FFFFFF")
                    power_percentage -= 0.004

            if event.key == pygame.K_q:
                if bonnie_distance == 0 or bonnie_distance == 1:
                    left_door_dark.fill("#4a1d9b")
                    power_percentage -= 0.004
                else:
                    left_door_dark.fill("#FFFFFF")
                    power_percentage -= 0.004

            if active_mode == ActiveMode.CAMERAS or ActiveMode.Vent_cameras:

                if event.key == pygame.K_v and active_mode == ActiveMode.CAMERAS or active_mode == ActiveMode.Vent_cameras:
                    vent_seen_last = True
                    if active_mode == ActiveMode.CAMERAS:
                        active_mode = ActiveMode.Vent_cameras
                    else:
                        active_mode = ActiveMode.CAMERAS

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

            if active_mode == ActiveMode.NORMAL:

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
    move_Chica()

    if active_mode == ActiveMode.Control_panel:
        reducePowerIfDoorsClosed()
        screen.fill("#FFFFFF")
        if selected_slider == 1:
            if slider_position_1 == 1:
                button_x_1 = 150
            elif slider_position_1 == 2:
                button_x_1 = 300
            elif slider_position_1 == 3:
                button_x_1 = 450
            elif slider_position_1 == 4:
                button_x_1 = 550
            elif slider_position_1 == 5:
                button_x_1 = 700

        if selected_slider == 2:
            if slider_position_2 == 1:
                button_x_2 = 150
            elif slider_position_2 == 2:
                button_x_2 = 300
            elif slider_position_2 == 3:
                button_x_2 = 450
            elif slider_position_2 == 4:
                button_x_2 = 550
            elif slider_position_2 == 5:
                button_x_2 = 700

        if selected_slider == 3:
            if slider_position_3 == 1:
                button_x_3 = 150
            elif slider_position_3 == 2:
                button_x_3 = 300
            elif slider_position_3 == 3:
                button_x_3 = 450
            elif slider_position_3 == 4:
                button_x_3 = 550
            elif slider_position_3 == 5:
                button_x_3 = 700

        if selected_slider == 4:
            if slider_position_4 == 1:
                button_x_4 = 150
            elif slider_position_4 == 2:
                button_x_4 = 300
            elif slider_position_4 == 3:
                button_x_4 = 450
            elif slider_position_4 == 4:
                button_x_4 = 550
            elif slider_position_4 == 5:
                button_x_4 = 700

        if selected_slider == 1:
            arrow_y = 196
        if selected_slider == 2:
            arrow_y = 596
        if selected_slider == 3:
            arrow_y = 996
        if selected_slider == 4:
            arrow_y = 1396

        screen.blit(slider_scaled, (100, 150))
        screen.blit(button_scaled, (150, button_x_1))
        screen.blit(slider_scaled, (500, 150))
        screen.blit(button_scaled, (550, button_x_2))
        screen.blit(slider_scaled, (900, 150))
        screen.blit(button_scaled, (950, button_x_3))
        screen.blit(slider_scaled, (1300, 150))
        screen.blit(button_scaled, (1350, button_x_4))
        screen.blit(arrow_scaled, (arrow_y, 750))

    if active_mode == ActiveMode.Vent_cameras:
        reducePowerIfDoorsClosed()
        power_percentage -= 0.003

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
        power_percentage -= 0.003

        if camera_mode == CameraMode.CAM1:
            screen.blit(camera_scrren_cam_1, (0, 0))
            screen.blit(camera_map_floor, (0, 320))

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

            if left_door_y > 200:
                left_door_y = 200

        if middle_went_open:
            wemt_door_y -= 20
            if wemt_door_y < -199:
                wemt_door_y = -199

        else:
            wemt_door_y += 20

            if wemt_door_y > 0:
                wemt_door_y = 0

        if right_door_open:
            right_door_y -= 50
            if right_door_y < -700:
                right_door_y = -700

        else:
            right_door_y += 50

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
        reducePowerIfDoorsClosed()

    d("Active mode: " + str(active_mode), 1)
    d("camera_mode: " + str(camera_mode), 2)
    d("left_door_open: " + str(left_door_open), 3)
    d("midle_vent_open" + str(middle_went_open), 4)
    d("right_door_open: " + str(right_door_open), 5)
    d("Bonnie_distance: " + str(bonnie_distance), 6)
    d("Vent_seen_last: " + str(Vent_seen_last), 7)
    d("Chica_distance: " + str(Chica_distance), 8)
    d("Time_specific: " + str(time1), 9)
    d("selected_slider: " + str(selected_slider), 10)
    d("slider_position_4: " + str(slider_position_4), 11)

    pygame.display.update()
    clock.tick(60)
