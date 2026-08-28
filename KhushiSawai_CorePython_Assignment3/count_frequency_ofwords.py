# Create a dictionary that counts how many times each word appears in a sentence.
sentence=input("Enter sentence:")
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word]= frequency[word]+1
    else:
        frequency[word]=1
print(frequency)