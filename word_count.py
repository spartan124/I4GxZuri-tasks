from itertools import count


#word counter
word = input("Please Enter your Own String : ")
count = 1

for i in range(len(word)):
    if(word[i] == ' ' or word == '\n' or word == '\t'):
        count = count + 1

print("Total Number of Words in this String = ", count)