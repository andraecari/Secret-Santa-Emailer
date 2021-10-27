'''
Andrae Cari
October 19 2021

PROBLEM: 
My group of friend's and I have been doing Secret Santa every year since Grade 
9. We usually draw each Secret Santa by putting names in an envelope and have
everyone pick out of it blindly. This year, mostly everyone has moved out for 
University and are usual way of drawing names is no longer possible.

SOLUTION:
In the perspective of a game master, use Python to draw these names autonomously.
In the future, I want this program to actually send emails to each of the Secret
Santa's, informing them who they have rolled. For now, it will just be collecting
everyone's data and will show who will get who with their data shown.
'''

#test comment

import random
import data
import smtplib
from email.message import EmailMessage

def randomize(numPeople):
    """
    Takes in the number of people, and generates a new list of random and unique indexes of the size of people.
    """
    # Create list
    names = []
    # Assign first receiver
    names.append(random.randint(1,numPeople-1)) 

    # Populate List
    for i in range(1,numPeople):
        while True:
            # Generate random number
            num = random.randint(0, numPeople - 1) 
            #if the generated number is not already in the list
            if num not in names:
                # If that number is not its own index(meaning the same person) and not the last index, add num to list.
                if num != i and i < numPeople - 1: 
                    names.append(num)
                    break
                # If that its the last in the list, add num to the list.
                elif i == numPeople - 1: 
                    names.append(num)
                    # If the last index rolls itself, swap value with a random index in names[].
                    if num == i: 
                        swap = random.randint(0, numPeople - 2)
                        temp = names[swap]
                        names[swap] = i
                        names[i] = temp
                    break
    return names

def showList(names, emails, addresses):
    """
    Takes in the list of names, emails, and addresses, and prints them.
    """
    # Prints header.
    print('~' * 80)
    print(f'{"Name:":20}{"Email:":30}{"Address:"}')
    print('~' * 80)
    # Prints each element in the names, emails, and addresses lists.
    for i in range(len(names)):
        print(f'{names[i]:20}{emails[i]:30}{addresses[i]}')
    print()

def send(names, emails, addresses, receivers):
    """
    Takes in the list of names, emails, addresses, and the new indexes to
    format the final sending output as for who gets who.
    """
    # Prints header.
    print('~' * 95)
    print(f'{"Secret Santa":20}{"Email of Santa":35}{"Receiver":20}{"Address of Receiver"}')
    print('~' * 95)
    i = 0
    # Properly formats and prints wanted output.
    for element in receivers:
        print(f'{names[i]:20}{emails[i]:25}{"--->":10}{names[element]:20}{addresses[element]}')
        i += 1
    print('~' * 95)

def email(names, emails, receivers):
    i = 0
    for element in receivers:
        msg = EmailMessage()
        msg['Subject'] = f'Secret Santa for: {names[i]}'
        msg['From'] = data.SENDER_EMAIL
        msg['To'] = f'{emails[element]}'
        msg.set_content(f'SECRET SANTA! {names[i]} you have gotten...')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(data.SENDER_EMAIL, data.SENDER_PASSWORD)
            smtp.send_message(msg)
            
        i += 1


if __name__ == "__main__":
    # Lists to hold the 3 types of data (names, emails, and addresses).
    names = []
    emails = []
    addresses = []
    print("Welcome to Andrae's Secret Santa program:")

    while True:
        # Print empty line for spacing/readability.
        print()
        # Selects a certain mode for the program.
        if not names:
            mode = "start"
        else:
            mode = input('Please enter a mode (add, remove, show list, send, exit): ')
            
        # If start was selected, populate the lists accordingly to how many people specified.
        if mode == "start":
            # Receive input for how many people are to be added.
            num = int(input('Please enter the amount of people: '))
            # Add to each list num times.
            for i in range(num):
                names.append(input(f'Name {i + 1}: '))
                emails.append(input(f'Email {i + 1}: '))
                addresses.append(input(f'Address {i + 1}: '))
        # If add was selected, add to the lists accordingly to how many people specified.
        elif mode == "add":
            # Receive input for how many people are to be added.
            num = int(input('How many people would you like to add? '))
            # Add to each list num times.
            for i in range(num):
                names.append(input(f'Name {len(names) + 1}: '))
                emails.append(input(f'Email {len(emails) + 1}: '))
                addresses.append(input(f'Address {len(addresses) + 1}: '))
        # If remove was selected, remove index specified from all lists.
        elif mode == "remove":
            # Receive input for who would be removed.
            name = input('Who would you like to remove? ')
            # Find the index of that person.
            index = names.index(name)
            # Remove that index for all three lists.
            names.pop(index)
            emails.pop(index)
            addresses.pop(index)
            print(f'{name} has been removed.')
        # If show list was selected, call the showList() function.
        elif mode == "show list":
            showList(names, emails, addresses)
        # If send was selected, call the randomize() and send() function and print out who gets who.
        elif mode == "send":
            # New list of new indexes using randomize() function.
            receivers = randomize(len(names))
            # Prints the output using send() function.
            send(names, emails, addresses, receivers)
            break
        # If exit was selected, force exit out of the program.
        elif mode == "exit":
            break

    print("Merry Christmas! Have Fun!")
    print('~' * 26)