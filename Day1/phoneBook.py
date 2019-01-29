
# A python phonebook code #

Phonebook = {"name": "Mukisa" ,"email": "val@gmail.com", "number": "757735793"}
all_contacts =[]
all_contacts.append(Phonebook)

name = input("Enter name: ")
email = input("Enter email: ")
number = int(input("Enter number: "))

new_person = {"name": name, "email": email, "number": number}
all_contacts.append(new_person)
