#! /usr/bin/python
#!-*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time
import pygame, sys
import pygame.camera
import time

WEBCAM_DIR = "/home/pi/projeto/foto_webcam"

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (640,480))

gpio.setmode(gpio.BCM)

gpio.setup(17, gpio.IN, pull_up_down = gpio.PUD_DOWN)


while True:
    if(gpio.input(17) == 0):
        ("Botão desligado")
    else:
        print("Botão pressionado")
        cam.start()
        image = cam.get_image()
        cam.stop
        timestamp = time.strftime("%d-%m-%Y_%H-%M-%S", time.localtime())
        filename = "%s/%s.jpg" % (WEBCAM_DIR, timestamp)
 
        # salvando a imagem
        pygame.image.save(image, filename)
 
        print "Salvo"
        
time.sleep(1)
    
gpio.cleanup()
exit()
