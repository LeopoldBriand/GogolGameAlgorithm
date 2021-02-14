#The Gogole Algorithm
from random import shuffle
from draw import draw
import json
from random import randrange

templates = None
with open('./utils/templates.json') as f:
  templates = json.load(f)

#List of symbols used in the game Gogole
symbols = ["Kendama","Clope-shit","oreiller memoire de forme","saxo","casque chevalier","wax main",
  "appareil photo rose","clio 2 bleue","206 grise","brouette","canapé violet", "retroprojecteur", 
  "nesquick", "vinyl", "86", "chapeau", "skull king", "malette de gangster", "champignon", "boîte d'allumette", 
  "sangria", "chemise wax", "pétanque", "palet", "twingo", "civilisation", "minecraft", "petit boudin", "robe de chambre", 
  "shrakithler", "cernunos", "freud", "briquet lama", "ponpon vert", "faucille marteau", "roi du zizi", "faucon millenium", 
  "moustache", "crete de punk", "veste dain", "pistoportail", "kenney", "george abidbol", "panneau roahzon", "o brother", 
  "hamac", "tartine frigo", "quai des bulles", "rennes 2", "plug anal en bois", "boucle d'oreille", "capsule", "botte à paillette", 
  "chaussette flamme", "susu", "sombrero", "ruche"]
    
#The number of symbols on a card has to be a prime number + 1
numberOfSymbolsOnCard = 8   #(7 + 1)
shuffleSymbolsOnCard = True

cards = []

#Work out the prime number
n = numberOfSymbolsOnCard - 1

#Total number of cards that can be generated following the gogole rules
numberOfCards = n**2 + n + 1  #e.g. 7^2 + 7 + 1 = 57


#Add first set of n+1 cards (e.g. 8 cards)
for i in range(n+1):  
  #Add new card with first symbol
  cards.append([1])
  #Add n+1 symbols on the card (e.g. 8 symbols)
  for j in range(n):
    cards[i].append((j+1)+(i*n)+1)

#Add n sets of n cards 
for i in range(0,n):
  for j in range(0,n):
    #Append a new card with 1 symbol
    cards.append([i+2])
     #Add n symbols on the card (e.g. 7 symbols)
    for k in range(0,n):
      val  = (n+1 + n*k + (i*k+j)%n)+1
      cards[len(cards)-1].append(val)

#Shuffle symbols on each card
if shuffleSymbolsOnCard :
  for card in cards:
    shuffle(card)
      
#Output all cards

i = 0
for card in cards:
  i+=1
  line = str(i) + " - ["
  for number in card:
    line = line + symbols[number-1] + ", "
  line = line[:-2] + "]"
  draw(card,templates[randrange(6)])