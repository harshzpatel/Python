""" This program is for encrypting or decrypting a message 
it's just for fun, don't take it seriously..."""


EnOrDe =  input("\nWhat you want to do ? \nEncrypt or decrypt\n(type 'e' or 'd', without quotes)\n").lower()  # asks for what you want to do

alph = ['a','b','c','d','e',  # list of all alphabets
        'f','g','h','i','j',
        'k','l','m','n','o',
        'p','q','r','s','t',
        'u','v','w','x','y',
                'z']

def Encrypt(st):  # function to encrypt the text
    st = ':'+st
    for i in range(26):
        st = st.replace(alph[i],str(i)+':')
    st = st.replace(' ','-:')
    print('\nThis is the encrypted text-\n\n'+st)

def Decrypt(st):  # function to decrypt the text
    for i in range(26):
        st = st.replace(':'+str(i)+':',':'+alph[i]+':')
        for i in range(26):
            st = st.replace(':'+str(i)+':',':'+alph[i]+':')
    st = st.replace('-',' ')
    st = st.replace(':','')
    print('\nThis is the decrypted text-\n\n'+st)
	
if EnOrDe == 'e':
    st = input('\nType the text which you want to encrypt-\n\n').lower()
    Encrypt(st)

elif EnOrDe == 'd':
    st = input('\nType the text which you want to decrypt-\n\n').lower()
    Decrypt(st)

else:
    print('Invalid input')
    exit()
