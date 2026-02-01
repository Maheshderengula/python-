"""
text ="hello python"
print(type(text)) #<class 'str'>

text = "python"
print(len(text)) # 6

#indexing:

text ="python"
print(text[0]) #p
print(text[-1]) #n
#slicing:
text ="python progarmming"
print(text[0:7]) # python
print(text[3:92]) #programming

#commmon string methods(veryy important )
#convert case :
text = "hello world"
print(text.upper()) #hello world
print(text.lower()) #hello world
print(text.title()) #hello world

# remove spaces:
text = "python"
print(text.strip()) #python

#replace text
text = "I love java" 
print(text.replace("java","python"))

#split text
text = "python is easy"
print(text.split()) #['python','is','easy']

#jion text 
words = ['python','is','fun']
print("".join(words))

# checking text (validation)
text = "python123"
print(text.isalpha()) #flase
print(text.isdigit()) #flase
print(text.isalnum()) #flase

#searching in text 
text ="learning python is fun"
print("python"in text)     #true
print(text.find("python")) #9
print(text.count("i"))     #count of i



# reading & writing text file
#read text file 
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
#write text file 
file = open ("data.txt","w")
file.write("hello python\nwelcome")
file.close()

#Best practice(with)
with open("data.txt","r") as file:
    print(file.read())

"""
# simple mini example (text processing)

# count words in text
text = "python is easy and python is powerful"
words = text.split()
print("total words:",len(words))

# count each word 
text = "python java python sql python"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)








