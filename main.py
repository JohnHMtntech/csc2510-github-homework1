# Main.py 
# Originally created by Brandon Vandergriff
# Ruined by: John Miller

import time
import urllib.request

def fightClub(): 
    print("Guys, we're supposed to talk about this. ")

#Code borrowed from Sibo on Github
def updateProgressBarJohnMiller(percent):
  bar_length = 25  # should be less than 100
  print('\r', end="", flush=True)
  print("Downloading Bee Movie Script: [{:{}}] {:>3}%".format('■'*int(percent/(100.0/bar_length)), bar_length, int(percent)), end="", flush=True)

def funcJohnHMiller():
  data =  urllib.request.urlopen("https://git.lysator.liu.se/catears/beemovie/-/raw/master/beemovie.txt")
  with open("beeMovieScript.txt", 'w') as writeFile:
    total = 4563  # total line count
    currentLine = 1    
    for line in data:
      lineText = str(line)
      lineText = lineText[2:len(lineText)-3]+"\n"
      writeFile.write(lineText)

      updateProgressBarJohnMiller(100.0*currentLine/total)
      currentLine = currentLine + 1
      
      time.sleep(0.002)
    updateProgressBarJohnMiller(100.0)
  print("\nScript sucessfully downloaded")
  


if __name__ == "__main__":
    fightClub()
    funcJohnHMiller()