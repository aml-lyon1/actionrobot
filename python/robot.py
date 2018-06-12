#!/usr/bin/env python3

import ev3dev
import ev3dev.ev3 as ev3

import math

class Robot:
    def __init__(self):
        # config
        # à changer selon l'état de fatigue du robot
        self.ratio_moteur_roue = 0.415
        self.turn_speed = 150
        self.line_speed = 200
        
        self.tile_size = 40 # en cm

        # variables
        self.ratio_taco_cm = 0.11

        # motors
        self.left_motor = ev3.LargeMotor('outA')
        self.right_motor = ev3.LargeMotor('outB')
        self.motors = [self.left_motor, self.right_motor]
        for motor in self.motors:
            motor.stop_action = 'hold'

        # sensors



    # Quand le programme termine, relacher la tension sur les moteurs
    def __del__(self):
        for motor in self.motors:
            motor.reset()


    def deplacer(self, nb_cases=1):
        count_per_rot = self.right_motor.count_per_rot
        self.right_motor.run_to_rel_pos(position_sp=nb_cases * self.tile_size * self.ratio_taco_cm * count_per_rot * self.ratio_moteur_roue,
                                        speed_sp=self.line_speed)
        self.left_motor.run_to_rel_pos(position_sp=nb_cases * self.tile_size * self.ratio_taco_cm * count_per_rot * self.ratio_moteur_roue,
                                       speed_sp=self.line_speed)
        self.left_motor.wait_until_not_moving(10000)

    def avancer(self):
        self.deplacer(1)
    
    def reculer(self):
        self.deplacer(-1)

    # valeurs correctes pour rotation : -1 (sens horaire), 1 (sens trigo)
    # Vous pouvez aussi donner 2 ou -2 pour faire un demi-tour, ou 4 pour faire joyeusement un tour sur vous-même
    def tourner(self, rotation=1):
        count_per_rot = self.right_motor.count_per_rot
        self.right_motor.run_to_rel_pos(position_sp=rotation * count_per_rot * self.ratio_moteur_roue,
                                        speed_sp=self.turn_speed)
        self.left_motor.run_to_rel_pos(position_sp=-rotation * count_per_rot * self.ratio_moteur_roue,
                                       speed_sp=self.turn_speed)

        self.left_motor.wait_until_not_moving(10000)

    def tournerDroite(self):
        self.tourner(1)
    
    def tournerGauche(self):
        self.tourner(-1)
  