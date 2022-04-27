alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_number):
  cipher_text = "" # creating an empty list to keep the ciphered txt
  for letter in plain_text:# to iterate through the plain txt
    target_position = alphabet.index(letter)# finding out the letters position in the alphabet list
    new_targetPosition = target_position + shift_number#sumin that index position to the shift number
    new_letter = alphabet[new_targetPosition]
    cipher_text += new_letter
    
  print(f"The encoded text is ",cipher_text)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_number):
    deciphered_text = ""#creating an empty list
    for character in cipher_text:#function to loop across the text
      relocalize = alphabet.index(character)#getting the letter's position
      real_position = relocalize - shift_number#moving backwards
      real_letter = alphabet[real_position]#identifying the letters position in the alphabet list
      deciphered_text += real_letter#adds content in the empty list
    print(f'The decoded text is, {deciphered_text}')#prints
  
      

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_number=shift)
 