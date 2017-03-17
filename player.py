#!/usr/bin/env python3

import time

import os

import subprocess

import pyglet

import RPi.GPIO as GPIO

from RPLCD import CharLCD


lcd = CharLCD(cols=20, rows=4,

                pin_rw=None,

                pin_rs=22,

                pin_e=18,

                pins_data=[16,15,13,11],

                numbering_mode=GPIO.BOARD)

artist = "Frank Ocean" #input("What artist?")

album = "Blonde" #input("What album?")

song = "*.mp3" #input("What song?")

lcd.cuursor_pos = (0, 1)

lcd.write_string(artist)

time.sleep (1)

lcd.cursor_pos = (1, 0)

lcd.write_string(album)

time.sleep (1)

lcd.cursor_pos = (3, 0)

lcd.write_string('....................')

#music = "~/Music/" + artist + "/" + album + "/" + song 

command = "mplayer -ao alsa:device=hw=1.0 ~/Music/'" + artist + "'/'" + album + "'/*.mp3 </dev/null >/dev/null 2>&1 &"
#there is better way to do this by creating playlist m3u files when importing the music
os.system(command)

song_prev = song

while 1:

	if song != song_prev:
		
		lcd.cursor_pos = (2, 0)
		
		lcd.write_string("                    ")

		lcd.cursor_pos = (2, 0)

		lcd.write_string(song)

	
	song_prev = song

	os.system("lsof +D /home/pi/Music | fgrep '.mp3' | awk -F'/' '{ print $NF; }' | cut -d'.' -f1 > log.txt")
	
	f = open("log.txt", "r")
		
	song = f.readline()

	f.close()
	
	time.sleep (1)
	
