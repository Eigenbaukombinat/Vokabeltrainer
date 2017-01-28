import csv
import random

Vokabel= list(csv.reader(open("Vokabeln.csv"),delimiter=";"))
Vokabel=[["ich","moi"],["du","tu"],["Computer","ordinateur"]]

richtig=[]
x=0
while len(richtig)<len(Vokabel):        
    r=random.randint(0,len(Vokabel)-1)
    if r in richtig:
        continue
    antwort=input(Vokabel[r][0]+" ")
    x=x+1
    
    if antwort==Vokabel[r][1]:
        richtig.append(r)
        print("Ja,das ist richtig!")
    else:
        print("Nein das ist falsch! Geh lernen!")

print("Herzlichen Glückwunsch. Du hasst es geschafft. Jetzt kannst du deinen Frusst abbauen.:D")
print("Du hast "+str(len(richtig))+" Vokabeln gelernt.")
print("Du hast "+str(x)+" Versuche gebraucht.")
