# Fibonacci sequence
# X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
# 1,1,2,3,5,8,13,21,34,55 

# Write a for loop, while loop, or function (or all three!) to create a
# list of the first 10 numbers of the fibonacci sequence

def fibonacci(n):
    x_1=1
    x_2=1
    l = [x_1, x_2]
    for m in range(n-2):
        #print(m)
        l.append(l[m]+l[(m+1)])
        #print(l[m]+l[(m+1)])
        
    return(l)

fibonacci(10)

"""return true if there is no e in 'word', else false"""
def has_no_e(word):


"""return true if there is e in 'word', else false"""
def has_e(word):


"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):


"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):


"""true/false is the word in alphabetical order?"""
# Hint: check the methods for lists
def is_abecedarian(word):