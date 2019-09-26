vowel_set={'a','e','i','o','u'}
word_list=['alligator','penguin','water fowl','giraffe']


for word in word_list:
    count=0
    for letter in word:
        if letter in vowel_set:
            count+=1
    print(f'the word {word} has {count} vowels')
