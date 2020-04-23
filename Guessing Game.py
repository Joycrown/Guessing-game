import random
name = input('Enter your name: \n')
print(name+', You Are Welcome On Board!')
diffculty = input("Pls, Enter 1 For Easy, 2 For Medium, 3 For Hard: \n")
def start_again():
    start= input('Do You Wish To Start Again? Enter yes or no: \n').lower()
    if start == 'yes':
        game_level()
    elif start=='no':
        print(name + ' Thank You For Your Time, Have A Good Life!')
    else:
         print("Pls Enter 'Yes' Or 'No' ")
         start_again()

def game_level():
         print('Level 1, Choose A Number Between 1-10 '
               'NOTE! You Have 6 Trails ')
         secret_number= random.randint(1,10)
         guess_taken= 0
         limit=6
         try:
             while guess_taken<=5:
                 guess =int(input('Guess Number: \n'))
                 limit-=1
                 guess_taken+=1
                 if guess == secret_number:
                    print(name + ', You Won!')
                    diffculty_level = int(input('Press 2 To Unlock level 2 \n'))
                    print(diffculty_level)
                    if diffculty_level==2:
                        game_level2()
                    else:
                        print('INVALID! Try Again!')
                        print(diffculty_level)
                    break
                 else:
                    print('WRONG Try Again!' + ' You Have ' +  str(limit)  + 'chance(s) left')
                    if guess_taken ==6:
                        print('Number = ' + str(secret_number))

             else:
                 print('GAME OVER!')
                 start= input('Do You Wish To Start Again? Enter yes or no: \n').lower()
                 if start == 'yes':
                       game_level()
                 elif start=='no':
                     print(name + ' Thank You For Your Time, Have A Good Life!')
                 else:
                     print("Pls Enter 'Yes' Or 'No' ")
                     start_again()

         except ValueError:
             print('INVALID, Only Numbers Are Allowed. Try Again')
             game_level()

def game_level2():
     print('Level 2 Unlocked! Choose A Number Between 1-20 '
           'NOTE! You Have 4 trails')
     limit=4
     guess_taken=0
     secret_number2= random.randint(1,20)
     try:
         while guess_taken<=3:
             guess2 =int(input('Guess Number: \n'))
             limit-=1
             guess_taken+=1
             if guess2==secret_number2:
                 print(name + ', You Won!')
                 diffculty_level = int(input('Press 3 To Unlock level 3 \n'))
                 print(diffculty_level)
                 if diffculty_level==3:
                     game_level3()
                 else:
                      print('INVALID! Try Again!')
                      print(diffculty_level)
                 break
             else:
                 print('WRONG Try Again!' + ' You Have ' +  str(limit)  + 'chance(s) left')
                 if guess_taken ==4:
                        print('Number = ' + str(secret_number2))
         else:
             print('GAME OVER! ')
             start= input('Do You Wish To Start Again? Enter yes or no: \n').lower()
             if start== 'yes':
                 game_level2()
             elif start=='no':
                 print(name + ' Thank You For Your Time, Have A Good Life!')
             else:
                 print("Pls Enter 'Yes' Or 'No' ")
                 start_again()
     except ValueError:
             print('INVALID, Only Numbers Are Allowed. Try Again')
             game_level2()

def game_level3():
    print('Level 3 Unlocked! Choose A Number Between 1 - 50 '
          'NOTE: You Have 3 Trails')
    limit=3
    guess_taken=0
    secret_number3=random.randint(1,50)
    try:
        while guess_taken<=2:
            guess3=int(input('Guess Number: \n'))
            limit-=1
            guess_taken+=1
            if guess3==secret_number3:
                print(name + ', You Won!')
                break
            else:
                print('WRONG Try Again!' + ' You Have ' +  str(limit)  + 'chance(s) left')
                if guess_taken ==3:
                        print('Number = ' + str(secret_number3))
        else:
            print('GAME OVER! ')
            start= input('Do You Wish To Start Again? Enter yes or no: \n').lower()
            if start == 'yes':
                 game_level3()
            elif start=='no':
                print(name + ' Thank You For Your Time, Have A Good Life!')
            else:
                print("Pls Enter 'Yes' Or 'No' ")
                start_again()
    except ValueError:
         print('INVALID, Only Numbers Are Allowed. Try Again')
         game_level3()
def user_error():
    diffculty = input("Pls, Enter 1 For Easy, 2 For Medium, 3 For Hard: \n")
    if diffculty == '1':
        game_level()
        game_level2()
        game_level3()
    elif diffculty =='2':
        game_level2()
        game_level3()
    elif diffculty =='3':
        game_level3()
    else:
        print('ooops! Command Not Regonised ')
        user_error()





if diffculty == '1':
    game_level()
elif diffculty =='2':
    game_level2()
elif diffculty =='3':
    game_level3()
else:
    print('ooops! Command Not Recognised ')
    diffculty = input("Pls, Enter 1 For Easy, 2 For Medium, 3 For Hard: \n")
    user_error()




















