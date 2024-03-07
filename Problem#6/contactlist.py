def process_user_contacts(user_input):
    
    user_contacts = user_input.split(' ')
    
 
    newlist = {}

   

    # Put word pairs into a dictionary
    for contact in user_contacts:
        if ',' in contact:
            name, phone_number = contact.split(',')
            newlist[name] = phone_number
        
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    
    print(newlist.get(contact_name, "Contact not found"))
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
