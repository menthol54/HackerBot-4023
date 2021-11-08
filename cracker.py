import itertools
import string

with open('password.txt', 'r') as f:
    real_pass = f.read()


def guess_password(real):
    with open('guess.txt', 'w') as k:
        k.write('')
    chars = string.digits  # + string.ascii_lowercase + string.ascii_uppercase **Uncomment this to add letters**
    attempts = 0
    for password_length in range(1, 13):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return f'password is {guess}. found in {attempts} guesses.'
            with open('guess.txt', 'a') as q:  # prints each guess to a txt file for testing
                q.write(f'{guess} \n')


print(guess_password(real_pass))
