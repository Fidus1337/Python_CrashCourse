"""
Dream Vacation: Write a program that polls users about their dream vacation. 
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.
"""
answers_dream_vacation = {}
poll_active = True
while poll_active:
    input_name = input('What is your name? ')
    input_dream_vacation = input('What is your dream vacation? ')
    answers_dream_vacation[input_name] = input_dream_vacation

    continue_pull_question = input('Will we continue poll?(Yes/No)')
    if continue_pull_question.title() == 'Yes':
        poll_active = True
    else:
        poll_active = False

print(answers_dream_vacation)
