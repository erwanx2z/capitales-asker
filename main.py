from random import *

global totalQuestions
global currentQuestions
global pointsNumber

global tabPays
global alreadyDonePays
global dico

#
# @author Erwan
# Github: github.com/erwanx2z
#
def main():
    global totalQuestions
    totalQuestions = input("Combien de questions voulez-vous au total ?")
    global currentQuestions
    currentQuestions = 0
    global pointsNumber
    pointsNumber = 0

    global tabPays
    tabPays = []
    global alreadyDonePays
    alreadyDonePays = []

    fd = open("capitales.csv", "r")
    global dico
    tabPays = []
    dico = {}
    i = 0
    for ligne in fd.readlines():
        pos1 = ligne.find(',')
        cap = ligne[pos1 + 1:].split("\n")
        dico[ligne[:pos1]] = cap
        tabPays.append(ligne[:pos1])
        i += 1

    fd.close()

    askQuestion()


def endGame():
    global pointsNumber
    global totalQuestions

    print("----------------")
    print("")
    print(" Fin de la partie !")
    print("")
    print("Vous avez ", pointsNumber, " réponses justes sur ", totalQuestions, " questions !")
    print("Réessayez ce quizz afin d'augmenter votre score :o")
    print("")
    print("----------------")


def questionRight():
    print("Félicitations, cette réponse est juste !")
    global pointsNumber
    pointsNumber = pointsNumber + 1

    askQuestion()


def questionFalse():
    print("Malheureusement, cette réponse est fausse !")
    askQuestion()


def askQuestion():
    global currentQuestions
    global totalQuestions

    if currentQuestions == int(totalQuestions):
        endGame()
    else:
        currentQuestions += 1

        global tabPays
        numPays = randint(1, len(tabPays))
        global dico

        print("")
        print("Question ", currentQuestions, "/", totalQuestions)
        print(dico[tabPays[numPays]][0])

        capitale = input("Quelle est la capitale de {} ? :".format(tabPays[numPays]))
        if capitale == dico[tabPays[numPays]][0]:
            tabPays.remove(tabPays[numPays])
            questionRight()
        else:
            tabPays.remove(tabPays[numPays])
            questionFalse()


main()
