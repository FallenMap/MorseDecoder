# Python program to implement Morse Code Translator
from gtts import gTTS
from playsound import playsound
from os import remove
from os import path
import tkinter as tk
from threading import Thread
import time
'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''
# global variable message
ms = ''
i = 0
# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-',           'B':'-...',
                    'C':'-.-.',         'D':'-..',      'E':'.',
                    'F':'..-.',         'G':'--.',      'H':'....',
                    'I':'..',           'J':'.---',     'K':'-.-',
                    'L':'.-..',         'M':'--',       'N':'-.',
                    'O':'---',          'P':'.--.',     'Q':'--.-',
                    'R':'.-.',          'S':'...',      'T':'-',
                    'U':'..-',          'V':'...-',     'W':'.--',
                    'X':'-..-',         'Y':'-.--',     'Z':'--..',
                    '1':'.----',        '2':'..---',    '3':'...--',
                    '4':'....-',        '5':'.....',    '6':'-....',
                    '7':'--...',        '8':'---..',    '9':'----.',
                    '0':'-----',        ', ':'--..--',  '.':'.-.-.-',
                    '?':'..--..',       '/':'-..-.',    '-':'-....-',
                    '(':'-.--.',        ')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':

			# Looks up the dictionary and adds the
			# corresponding morse code
			# along with a space to separate
			# morse codes for different characters
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			# 1 space indicates different characters
			# and 2 indicates different words
			cipher += ' '

	return cipher

# Function to decrypt the string
# from morse to english
def decrypt(message):

	# extra space added at the end to access the
	# last morse code
	message += ' '

	decipher = ''
	citext = ''
	for letter in message:

		# checks for space
		if (letter != ' '):

			# counter to keep track of space
			i = 0

			# storing morse code of a single character
			citext += letter

		# in case of space
		else:
			# if i = 1 that indicates a new character
			i += 1

			# if i = 2 that indicates a new word
			if i == 2 :

				# adding space to separate words
				decipher += ' '
			else:

				# accessing the keys using their values (reverse of encryption)
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(citext)]
				citext = ''

	return decipher

# Hard-coded driver function to run the program
def boton():
        global i, ms
        try:
                result = decrypt(ms)
                print (result)
                s = gTTS(result)
                s.save('sample' + str(i) + '.mp3')
                playsound('sample' + str(i) + '.mp3')
                i += 1
        except:
                print('Morse code not valid. Try again.')
                ms = ''
        ms = ''
    
def insert0():
        global ms
        ms += '.'
        print(ms)

def insert1():
        global ms
        ms += '-'
        print(ms)

def inserte():
        global ms
        ms += ' '
        print(ms)
        
# Executes the main function
if __name__ == '__main__':
        ventana = tk.Tk()
        ventana.title('Morse Decoder')
        ventana.geometry('300x300')
        ventana.resizable(width=0, height=0)
        ventana.configure(background = 'dark gray')
        etiqueta1 = tk.Label(ventana, text = 'Morse Decoder \n Made by: Miguel Puentes     ', bg = 'red', fg= 'white')
        etiqueta1.place(relx=100, rely=10)
        etiqueta1.pack()
        button = tk.Button(ventana, text = 'Point (.)',width=7,height=5, command = insert0)
        button.place(x=40, y=100)
        button1 = tk.Button(ventana, text = 'Line (-)',width=7,height=5, command = insert1)
        button1.place(x=120, y=100)
        button2 = tk.Button(ventana, text = 'Space',width=7,height=5, command = inserte)
        button2.place(x=200, y=100)
        send = tk.Button(ventana, text = 'Convert',width=10,height=5, command = boton)
        send.place(x=110, y=200)
        ventana.mainloop()
        print(ms)
        i -= 1
        while(i != -1):
                remove(path.dirname(__file__) +'\sample' + str(i) + '.mp3')
                i -= 1
 

