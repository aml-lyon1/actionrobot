#!/usr/bin/env python3

import ev3dev
import ev3dev.ev3 as ev3

import math

class Robot:
    def __init__(self):
        # config (A CHANGER SI VOUS CHANGEZ LA STRUCTURE DU ROBOT)
        self.turn_speed = 200
        #self.turn_factor = 144
        self.ratio_moteur_roue = 0.5
        self.tile_size = 40 # en cm


        # motors
        self.left_motor = ev3.LargeMotor('outA')
        self.right_motor = ev3.LargeMotor('outD')
        self.motors = [self.left_motor, self.right_motor]
        for motor in self.motors:
            motor.stop_action = 'hold'

        # sensors

        pass

    # Quand le programme termine, relacher la tension sur les moteurs
    def __del__(self):
        for motor in self.motors:
            motor.reset()

    def avancer(self, nb_cases=1):
		self.right_motor.run_timed(time_sp=3000, speed_sp=500)
		self.left_motor.run_timed(time_sp=3000, speed_sp=500)
		
    def reculer(self, nb_cases=1):
        pass

    def demitour(self):
        self.tourner(6)

    # valeurs correctes pour rotation : -1 (sens horaire), 1 (sens trigo)
    # Vous pouvez aussi donner 2 ou -2 pour faire un demi-tour, ou 4 pour faire joyeusement un tour sur vous-même
    def tourner(self, rotation=1):
        sens = math.copysign(1, rotation)
        rotation = math.copysign(rotation, 1)
        count_per_rot = self.right_motor.count_per_rot
        self.right_motor.run_to_abs_pos(position_sp=sens * rotation * count_per_rot * self.ratio_moteur_roue,
                                        speed_sp=self.turn_speed)
        self.left_motor.run_to_abs_pos(position_sp=-sens * rotation * count_per_rot * self.ratio_moteur_roue,
                                       speed_sp=self.turn_speed)
        #factor = self.turn_factor / self.turn_speed
        #self.right_motor.run_timed(time_sp=rotation * factor * 1000,
        #                           speed_sp=sens * self.turn_speed)
        #self.left_motor.run_timed(time_sp=rotation * factor * 1000,
        #                          speed_sp=-sens * self.turn_speed)

        self.left_motor.wait_until_not_moving(10000)
		
if __name__ == "__main__":
    robot = Robot()
	print("hello")
    #for i in range(4):
    robot.avancer(1)
