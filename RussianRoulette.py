from os import system
from random import randint
from os import path
import pygame
import time

pygame.mixer.init(44100, 16, 2, 1024)
Playing = True
RealBullet = True
ShotPlayer = pygame.mixer.Sound(path.join("Assets", "SoundEffect", "Player_died.wav"))
ShotAI = pygame.mixer.Sound(path.join("Assets", "SoundEffect", "Ai_died.wav"))
empty = pygame.mixer.Sound(path.join("Assets", "SoundEffect", "Empty_gun.wav"))

def GiveUp():
    print("Ok...Then you can quit :)")
    wait = input("")  # useless input to make the prompt wait before closing
    global Playing
    Playing = False

def Dead():
    if RealBullet:
        system("shutdown /p")
    else:
        print("In real life you will be dead...")
        while Playing:
            print("Another Game? y/n")
            rep = input("")

            if rep == "y":
                break

            elif rep == "n":
                GiveUp()

def Win():
    system('cls')
    print("You won !! GG")
    while Playing:
        print("Another Game? :p y/n")
        rep = input("")

        if rep == "y":
            break

        elif rep == "n":
            GiveUp()


def RussianRoulettePlay():
    print("Ok then pull the trigger...")
    BulletPlacement = randint(1,6)
    Placement = 0
    Round = 0
    FinalRound =False
    while Playing:
        Round +=1
        system('cls')
        Placement += 1
        print("Round "+str(Round))
        if Placement == 5:
            print("Final Round")
            while True:
                print("Do you pass your turn? y/n")
                rep = input("")

                if rep == "y":
                    print("Ok my turn so...")
                    time.sleep(3)

                    if Placement == BulletPlacement:
                        ShotAI.play()
                        print("PAN!")
                        Win()
                        break
                    else:
                        empty.play()
                        print("I survive...Your turn :)")
                        time.sleep(1)
                        print("AHAHHAHAH")
                        time.sleep(2)
                        print("PAN!")
                        print("your dead")
                        ShotPlayer.play()
                        Dead()
                        break


        time.sleep(3)
        if Placement == BulletPlacement:
            print("PAN!")
            print("your dead")
            ShotPlayer.play()
            Dead()
            break
        else:
            empty.play()
            print("you survive...my turn")
            if Placement == 5:
                print("Goodbye...")
        time.sleep(3)
        Placement += 1

        if Placement == BulletPlacement:
            ShotAI.play()
            print("PAN!")
            Win()
            break
        else:
            empty.play()
            print("I survive...Your turn")
        while Playing:
            print("continue? y/n")
            rep = input("")

            if rep == "y":
                break

            elif rep == "n":
                GiveUp()



while Playing:
    system('cls')
    print("Do you want to play a real russian roulette ? y/n")

    rep = input("")
    if rep == "y" :
        print("with real bullet? y/n")
        rep = input("")
        if rep == "y":
            RussianRoulettePlay()

        elif rep == "n":
            RealBullet = False
            RussianRoulettePlay()

    elif rep == "n" :
        GiveUp()
    else:
        pass





