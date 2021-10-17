# -*- coding: utf-8 -*-
import random

#where should I use RNG?
# y e s

# seriously this code is more dada than anything it could generate

def dada(text, s, v, w):
	text = text.split()

	poem = ""

	# variables for rhyme generating, ignore them
	# but also don't do anything to them, they're important
	rhymeref = random.randint(0,3)
	rhymeapply = rhymeref + random.randint(1,4)
	counter = 0
	rhymeword = ""

	#generates some fancy name
	name = ''
	for i in range (random.randint(1,3)):
		name += text[random.randint(0,len(text))] + " "
	name += '\n'
	print(name.upper())

	#getting some random numbers for the number of verses 
	#definitely not too complicated
	versenum = []
	for i in range (v+random.randint(0, int(v/2))):
		for j in range (random.randint(1,v+2)):
			versenum.append(i+1)
			
	stanzanum = random.randint(s-1,s+2)		# determining the number of stanzas randomly bcs why not

	for i in range (stanzanum): 	# loop for every stanza
		numofverses = versenum[random.randint(0,len(versenum)-1)] 	# determining the number of verses of current stanza
		stanza = []		# array for verses' string
		for a in range(numofverses):
			stanza.append("") 	#adds an empty string for each verse

		for j in range (numofverses): 	# generates words for each verse
			numofwords = random.randint(1, w+2)		# determines the number of words in a verse

			if counter == rhymeref and numofverses > 1: 	# runs if the verse is the first line of a rhyme
				for k in range (numofwords-1): 	# adding the words
					stanza[j] = stanza[j]+text[random.randint(0,len(text)-1)]+" "
				rhymeword = text[random.randint(0,len(text))]
				stanza[j] += rhymeword
				stanza[j] += "\n"
				rhymeapply = rhymeref + random.randint(1,2)
				counter += 1

			elif counter == rhymeapply: 	# runs if the verse is the second line of a rhyme
				for k in range (numofwords-1): 	# adding the words
					stanza[j] = stanza[j]+text[random.randint(0,len(text))]+" "
				rhymes = []

				for l in range (len(text)-1): 	# the second line of a rhyme
					if text[l][-2:] == rhymeword[-2:] and text[l] != rhymeword:
						rhymes.append(text[l])

				if len(rhymes) > 0:
					stanza[j] += rhymes[random.randint(0,len(rhymes)-1)]
				else:
					stanza[j] += text[random.randint(0,len(text))]
				stanza[j] += "\n"
				rhymeref = rhymeapply + random.randint(1,3)
				counter += 1

			else:		# normal verses without rhymes. meh, normies.
				for k in range (numofwords): 	# adding the words
					stanza[j] = stanza[j]+text[random.randint(0,len(text))]+" "
				stanza[j] += "\n"
				counter += 1

		for j in range (len(stanza)):
			poem = poem + stanza[j]
		poem += "\n"

	poem = poem.lower()		# ofc it's in lowercase, it's fucking art
	return poem

# gets the data from the txt doc
# dont touch, go touch the document instead
# or grass
with open('dadadata.txt', encoding='utf-8') as f:
	text = f.read()


print("Hey, answer these questions. Your answers will be almost irrelevant but...  y'know. Just do it.")
print("Write integers only pls, don't hurt the program\n")
print("How many stanzas you want in your high quality piece of art?")
s = int(input())
print("And how many verses should be in one stanza? Approximately??")
v = int(input())
print("And the number of words in one line?")
w = int(input())
print('\n\n')
print(dada(text, s,v,w))

print("\n\n\n // press enter to end")
input()


