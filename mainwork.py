def main():
    #main should call all other functions to build the entire program
    #calls all other functions
    shift = get_shift()
    message = get_message()
    chooce = choose_option()
    key = create_key(shift)
    #finds if neds to encode or decode
    if chooce == True:
        print("Here is your encoded message: ")
        message = encode(message, key)
        print(message)
    else:
        print("Here is your decoded message: ")
        message = decode(message, key)
        print(message)
        
def get_shift():
    #get_shift should prompt the user for the shift value and return the value as a string 
    #Validate for integers 1-25, inclusive
    shift = int(input('enter how many you want to shift'))
    #makes sure not more or less then alowed
    while shift < 0 or shift > 26:
        shift = int(input('enter how many you want to shift'))
    return shift

def choose_option():
    #choose_option should prompt the user to choose to encode or decode. 
    #It should return True if the user chooses encode and False if the user chooses decode.
    #Validate to only accept the appropriate prompts for encode and decode.
    chooce = input('do you want to encode or decode: ')
    #make sure you only choose en or decode
    while chooce != 'encode' and chooce != 'decode':
        chooce = input('please only select encode or decode')
    if chooce == 'encode':
        #returns encode or decode
        return True
    else:
        return False
    
def get_message():
    #get_message should prompt the user to enter a message to encode or decode.  It should return that message
    
    # initialize variable
    bad = 2
    
    # loop until the message is good
    while bad > 0:
        message = input("Enter a message to encode/decode: ")
        bad = 0
        for letter in message:
            # check the message is good
            if letter.isalpha() == False and letter.isspace() == False:
                bad += 1
    
    return message

def create_key(shift):
    # create_key should accept the shift value from get_shift.
    # It should create the caesar cipher according to the shift value and store the key in a dictionary and return the dictionary as the key
    
    # import string
    import string
    
    # initialize variables
    ALPHABET = string.ascii_lowercase
    num_to_letter = dict()
    letter_to_num = dict()
    key = dict()
    counter = 0
    
    # create the translating dictionaries
    for letter in ALPHABET:
        letter_to_num[letter] = counter
        num_to_letter[counter] = letter
        counter += 1
    
    # create the key with the old letters translated to new letters
    for letter in ALPHABET:
        old_letter = letter_to_num[letter]
        old_letter += shift
        
        # translate if the old letter goes over 'z'
        while old_letter >= 26:
            old_letter = old_letter - 26
    
        old_letter = num_to_letter[old_letter]
        
        # add to key
        key[letter] = old_letter  # This now stores the encoding mapping
    
    # return the key
    return key

def encode(message, key):
    new_message = ""
    
    # loop through each letter in the message
    for letter in message:
        # check if it's not a space, otherwise just add space to the new message
        if letter != " ":
            # check if it's uppercase
            if letter.isupper():
                capital = True
                # convert to lowercase for translation
                letter = letter.lower()
            else:
                capital = False
            
            # get the encoded letter from the key
            new_letter = key[letter]
            
            # if the original letter was uppercase, convert the new letter to uppercase
            if capital:
                new_letter = new_letter.upper()
            
            # append the new letter to the result
            new_message += new_letter
        else:
            # if it's a space, just add a space to the encoded message
            new_message += " "
    
    # return the final encoded message
    return new_message

def decode(message, key):
    # decode should accept message as a string and key as a dictionary.
    # It should decode the message using the key and return the decoded message as a string
    
    # Create the reverse key for decoding (this will map encoded letters back to the original letters)
    reverse_key = {v: k for k, v in key.items()}
    
    # initialize variables
    new_message = ""
    capital = False
    
    # read each letter and convert it
    for letter in message:
        if letter != " ":
            # check if it's uppercase
            if letter.isupper():
                capital = True
                letter = letter.lower()  # convert to lowercase for decoding
                
            # set the new letter using the reverse key
            new_letter = reverse_key[letter]
            
            # if it was uppercase, change it to uppercase and reset the capital variable
            if capital:
                new_letter = new_letter.upper()
                capital = False
                
            # add the new letter to the new message
            new_message += new_letter
        else:
            # if it's a space, just add a space to the decoded message
            new_message += " "
    
    # print or return the new message
    return new_message
