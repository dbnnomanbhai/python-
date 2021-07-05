import  random
def guess(x):
    random_number = random.randint(1, x)
    guess = int(input (f'guess number between 1 and (x):'))
    if guess < random_number:
        print("sorry ,try again,its too low")
    elif guess > random_number:
        print("sorry !try agian .its too high")
    print(f"confrats, you have the guess number {random_number}orrectly !!")

def user_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low


        feedback = input(f'its {guess} too high or too low, or correct?:')
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f'the computer guess your number,{guess},correctly')
user_guess(1000)