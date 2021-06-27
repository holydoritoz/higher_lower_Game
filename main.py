import replit
from art import logo,vslogo
import random
from data import data
from replit import clear

score =0
game=True ##Flag

print(logo)


while game:
    generator=random.choices(data,k=2)
    list1=generator[0]
    list2=generator[1]

    ##Comparando seguidores de la lista generada.
    followers_a = list1['follower_count']
    followers_b = list2['follower_count']


    def cleaner(randomList):
        """" Take the random list and clean to be printed """
        name=randomList['name']
        profession=randomList['description']
        ubication=randomList['country']
        print(f'Compare: {name}, a {profession}, from {ubication}.')

    def compareA(followers_a,followers_b):
        global score
        global game
        if followers_a > followers_b:
            score +=100
            print(f'You are right!, score:{score} points!')
        else:
            print('You are Wrong! Game Over!')
            game=False

    def compareB(followers_a,followers_b):
        global score
        global game
        if followers_b > followers_a:
            score +=100
            print(f'You are right!, score:{score} points!')
        else:
            print('You are Wrong! Game Over!')
            game=False

    ##Dashboard
    cleaner(list1)
    print(vslogo)
    cleaner(list2)

    guess=input('Guess who has more followers, Type "A" or "B": ').lower()
    if guess == 'a':
        compareA(followers_a ,followers_b )
    elif guess== 'b':
        compareB(followers_a,followers_b)
        
    clear()
else:
    game=False







