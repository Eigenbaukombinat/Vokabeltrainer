import flask
import csv
import random
x=0


app=flask.Flask("Vokabeltrainer")


Vokabel= list(csv.reader(open("Vokabeln.csv"),delimiter=";"))
#Vokabel=[["ich","moi"],["du","tu"],["Computer","ordinateur"]]

richtig=[]

@app.route("/")
def index():
    global x
    global richtig
    x=0
    richtig=[]
    return flask.render_template("index.html")

@app.route("/lernen/")
def lernen():
    global x
    result=""
    msg=""
    antwort=flask.request.args.get("antwort")
    if antwort:
        x=x+1
        antwort_id=flask.request.args.get("antwort_id")
        if antwort==Vokabel[int(antwort_id)][1]:
            result="richtig"
            richtig.append(int(antwort_id))
            msg="Ja,das ist richtig!"
        else:
            result="falsch"
            msg="Nein das ist falsch! Geh lernen!"
    status="Du hast "+str(len(richtig))+" Vokabeln gelernt.Du hast "+str(x)+" Versuche gebraucht."
    if len (richtig)==len(Vokabel):
        return flask.render_template("fertig.html",status=status)
    r=random.randint(0,len(Vokabel)-1)
    while r in richtig:
        r=random.randint(0,len(Vokabel)-1)
    auswahl=Vokabel[r][0]
    return flask.render_template("lernen.html",frage=auswahl,id=r,msg=msg,result=result,status=status)



