# 2. Write a program to input any alphabet and check whether it is vowel or consonant.
alpha = input("Enter any  single alphabet: ")
vowel="aeiou"
if alpha.lower() in vowel :
    print("its vowel")
else:
    print("Its consonants")    