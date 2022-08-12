## 1. write the following functions
## 2. write a unittest class to test each of these functions once
## 3. Run it in this script

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    try:        
	    txt_shout = txt.upper()
    	return txt_shout



shout("hola")


## reverse all characters in string
def reverse(txt):
    return txt[::-1]

reverse("hola")

## reverse word order in string
def reversewords(txt):
    return txt.split()[::-1]
    
reversewords("hola como estas")
    

## reverses letters in each word
def reversewordletters(txt):
    return reversewords(reverse(txt))

reversewordletters("hola como estas")

## optional -- change text to piglatin.. google it!
def piglatin(txt):

## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]


		
			
			
			
			
			
			

