number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # Nowy blok zaczyna się tutaj
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # Nowy blok kończy się tutaj
elif guess < number:
    # Następny blok
    print('No, it is a little higher than that')
    # Możesz tu robić co zechcesz
else:
    print('No, it is a little lower than that')
    # musisz mieć guessed > number aby być tutaj

print('Done')
# Ostatnia instrukcja jest zawsze wykonywana
# po ukończeniu bloku if
