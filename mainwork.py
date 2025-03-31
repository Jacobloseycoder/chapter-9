def main():
  #main should call all other functions to build the entire program
  #main should call all other functions to build the entire program
  shift = get_shift()
  message = get_message()
  chooce = choose_option()
  key = create_key(shift)
  if chooce == True:
      encode(message, key)
  else:
      decode(message, key)
def get_shift():
  #get_shift should prompt the user for the shift value and return the value as a string 
  #Validate for integers 1-25, inclusive
  shift = int(input('enter how many you want to shift'))
    while shift < 0 or shift > 26:
        shift = int(input('enter how many you want to shift'))
    return shift
def choose_option():
    #choose_option should prompt the user to choose to encode or decode. 
    #It should return True if the user chooses encode and False if the user chooses decode.
    #Validate to only accept the appropriate prompts for encode and decode.
    chooce = input('do you want to encode or decode: ')
    while chooce != 'encode' and chooce != 'decode':
        chooce = input('please only select encode or decode')
    if chooce == 'encode':
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
    #create_key should accept the shift value from get_shift.
    #It should create the caesar cipher according to the shift value and store the key in a dictionary and return the dictionary as the key
    
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
        
        # translate if the old letter goes over z
        while old_letter >= 26:
            old_letter = old_letter - 26
    
        old_letter = num_to_letter[old_letter]
        
        # add to key
        key[old_letter] = letter
    
    # return the key
    return key
  
def encode(message, key):
    #encode should accept message as a string and key as a dictionary.
    #It should encode the message using the key and return the encoded message as a string
    pass
def decode(message, key):
    #decode should accept message as a string and key as a dictionary.
    #It should decode the message using the key and return the decoded message as a string
    
    # initialize variables
    new_message = ""
    
    # read each letter and convert it
    for letter in message:
        # go if it isnt a space, if it is add a space.
        if letter != " ":
            # check if its uppercase
            if letter.isupper() == True:
                capital = True
                # set it to lower to translate
                letter = letter.lower()
                
            # set the new letter
            new_letter = key[letter]
            
            # if it was uppercase, change it to uppercase and reset capital variable
            if capital == True:
                new_letter = new_letter.upper()
                capital = False
            # add the new letter to the new message
            new_message += new_letter
        else:
            # add the new message with a space
            new_message += " "
    
    # return the new message
    return new_message
