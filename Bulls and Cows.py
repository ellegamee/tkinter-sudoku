#Bulls and Cows
import random
code = []
player = []
output = ['_','_','_','_']
guess = 0
guesses = 0
maxvalue = 9
minvalue = 0
bulls = 0
cows = 0
goats = 0
for i in range (0,4) :
  code.append(random.randint(0,9))

while guesses < 11 :
  player = []
  for i in range(0,4) :
    while True :
      try :
        guess = int(input('Skriv in ett tal mellan {} och {}: '.format(minvalue,maxvalue)))

      except :
        print('Skriv in ett tal mellan {} och {}\n '.format(minvalue,maxvalue))
        continue


      if guess < minvalue or guess > maxvalue :
        print('Skriv in ett tal mellan {} och {}\n '.format(minvalue,maxvalue))
        continue

      else :
        player.append(guess)
        break
  print(code)
  print(player)
  bulls = 0
  cows = 0
  goats = 0
  for j in range(0,len(player)) :
    if player[j] == code[j] :
      output.pop(j)
      output.insert(j,'B')
      bulls += 1
   
    else :
      for k in range(0,len(player)) :
        if player[k] == code[j] :
          print(player[k],code[j])
          #output.pop(j)
          output.insert(j,'C')
          cows += 1
        else : 
          print(player[k],code[j])
          #output.pop(j)
          output.insert(j,'G')
          goats += 1
  print(output,'\nAntal Bulls {}, Antal Cows {}, Antal Goats {}\n'.format(bulls,cows,goats))
  guesses += 1