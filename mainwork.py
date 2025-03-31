def main():
    #main should call all other functions to build the entire program
    pass
def get_shift():
    #get_shift should prompt the user for the shift value and return the value as a string 
    #Validate for integers 1-25, inclusive
    pass
def choose_option():
    #choose_option should prompt the user to choose to encode or decode. 
    #It should return True if the user chooses encode and False if the user chooses decode.
    #Validate to only accept the appropriate prompts for encode and decode.
    pass
def get_message():
    #get_message should prompt the user to enter a message to encode or decode.  It should return that message
    bad = True
    
    while bad == True:
        message = input("Enter a message to encode/decode: ")
        bad = False
        for letter in message:
            if message.isalpha() or message.isspace():
                pass
            else:
                bad = True
    
    return message

def create_key(shift):
    #create_key should accept the shift value from get_shift.
    #It should create the caesar cipher according to the shift value and store the key in a dictionary and return the dictionary as the key
    
    # import string
    import string
    
    ALPHABET = string.ascii_lowercase
    alpha_to_letter = dict()
    letter_to_alpha = dict()
    key = dict()
    count = 0
    
    for letter in ALPHABET:
        count += 1
        letter_to_alpha[count] = letter
        alpha_to_letter[letter] = count
    
    for letter in ALPHABET:
        new_letter = alpha_to_letter[letter]
        new_letter += shift
        new_letter = letter_to_alpha[new_letter]
        
        key[new_letter] = letter
    print(key)
    
def encode(message, key):
    #encode should accept message as a string and key as a dictionary.
    #It should encode the message using the key and return the encoded message as a string
    pass
def decode(message, key):
    #decode should accept message as a string and key as a dictionary.
    #It should decode the message using the key and return the decoded message as a string
    pass
get_message()
