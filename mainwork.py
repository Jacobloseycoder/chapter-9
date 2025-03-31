def main():
  #main should call all other functions to build the entire program
  pass
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
  pass
def get_message():
  #get_message should prompt the user to enter a message to encode or decode.  It should return that message
  pass
def create_key():
  #create_key should accept the shift value from get_shift.
  #It should create the caesar cipher according to the shift value and store the key in a dictionary and return the dictionary as the key
  pass
def encode():
  #encode should accept message as a string and key as a dictionary.
  #It should encode the message using the key and return the encoded message as a string
  pass
def decode():
  #decode should accept message as a string and key as a dictionary.
  #It should decode the message using the key and return the decoded message as a string
  pass
