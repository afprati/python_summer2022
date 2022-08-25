# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 21:44:28 2022

@author: Tita
"""
import random
import time
import matplotlib.pyplot as plt
  
def bubbleSort(lst):
    lenght = len(lst)
  
    # outer for loop list elements
    for i in range(lenght):
  
        # inner for loop from 0 to lenght-1 each time
        for j in range(0, lenght-i-1):

            #swap if the element is greater
            if lst[j] > lst[j+1]:
                elemnt_j = lst[j]
                lst[j]= lst[j+1]
                lst[j+1]  = elemnt_j
           

def piv(lst, low, high):
  
  # choose the right element of the list
  piv = lst[high]
  j = low - 1
  
  for i in range(low, high):
    if lst[i] <= piv:
      #if i element is smaller than pivot then swap
      j = j + 1
  
      (lst[j], lst[i]) = (lst[i], lst[j])
  
  # pivot element with the greater element specified by i
  (lst[j + 1], lst[high]) = (lst[high], lst[j + 1])
  
  # return where the partition was done
  return j + 1

#Using function piv
def quickSort(lst, low, high):
  if low < high:
  
    p = piv(lst, low, high)
  
    quickSort(lst, low, p - 1)
  
    quickSort(lst, p + 1, high)
  
    
         
timeBubble = []
timeQuick = []
randombubble = []
randomquick=[]
n = [100, 200, 500, 1000, 2000, 2500, 3000,3500,4000,4500]

for i in n:

    time_bubble = []
    time_quick= []

    for j in range(200):
        

        n_bubble = random.randint(1,50)
        randombubble.append(n_bubble)
        n_quick = random.randint(1,50)
        randomquick.append(n_quick)

        
        start_bubble = time.time()
        bubbleSort(randombubble)

        
        time_bubble.append(time.time() - start_bubble)
        
        
        start_quick = time.time()
        quickSort(randomquick,0, len(randomquick)-1)

        
        time_quick.append(time.time() - start_quick)
        

    timeBubble.append(time_bubble)
    timeQuick.append(time_quick)




#plotting time
plt.plot(n, timeBubble, label="Bubble Sort")
plt.plot(n, timeQuick, label="Quick Sort")
plt.xlabel("Elements")
plt.ylabel("Time")
plt.grid(False)
plt.legend()
plt.savefig("hw_plot.pdf")
plt.close()

