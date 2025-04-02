def main():
    message = 'aaa'
    shift = 2
    key = create_key(shift)
    message = encode(message, key)
    decode(message, key)
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
    print(new_message)
