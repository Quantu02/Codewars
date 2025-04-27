def is_pangram(st):

    if len(st) < 26: #Checking the length of string
        return False
    else:
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        st = st.lower()
        sentence_letter = set() #Making set of all letter in the string
        for char in st:
            if char.isalpha():#Cheching for alphabet
                sentence_letter.add(char)
        if  sentence_letter >= alphabet:
            return True
        else:
            return False