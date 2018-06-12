#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ev3dev
import ev3dev.ev3 as ev3

import math
import robot
		
if __name__ == "__main__":
    robot = Robot()
    # avancer d'une case 
    robot.avancer(1)
    # tourner à droite 
    robot.tourner(1)
    # tourner à gauche 
    robot.touner(-1)
    # demi-tour
    robot.tourner(2) 
    # reculer d'une case 
    robot.avancer(-1)
