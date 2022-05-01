# CMPS 2200 Assignment 5
## Answers

**Name:** Charles Tyndal  
**Name:** Jamie Hartman


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.** I may have a misunderstanding of the question, but the code for the coin algorithm is below.
- 
def findCoins(int N):
  binary = decimalToBinary(N)
  length = len(binary)
  for i, k in enumerate(binary):
    if k == 1:
      temp = 2**length
      print(f'1 {temp} cent coin, ')
    length-1
def decimalToBinary(n):
  return bin(n).replace("0b", "")

This algorithm would not be optimal as it is designed to not use more than 1 of any coin type, but if able to use more than one, you may be able to use less coins.

- **1b.**
  - The work and span of this algorithm would be O(n) and O(n)
    
- **2a.**
  - Greedy algorithms cannot work for this function as by design they are always looking for the largest part that fits within them and then moving top down. In this situation you cannot use this approach as the remainder is not garunteed to be able to be summed from the smaller portions. To do this you would have to not immediately go for the largest part and work down, but rather test all sorts of combinations to see which summed properly. Greedy Algorithms are incapable of seeing the wholistic picture but rather make the "best" decision at that given moment.

- **2b.**
- import sys
- def minCoins(coinList, listSize, N):
  - storage = [0 for i in range(N + 1)]
  - #initializing storage
  - for i in range(0, N + 1):
    - if(i == 0):
      - storage[i] = 0
    - storage[i] = sys.maxsize
  - #check all values from 1 to the total
  - for i in range(1, N + 1):
    - #check all values for each sum with all of the coins smaller than i
    - for j in range(listSize):
      - if(coinList[j] <= i):
        - #collect all data in a another array
        - internalStorage = storage[i - coinList[j]]
        - if(internalStorage) != sys.maxsize and internalStorage + 1 < storage[i]):
          - storage[i] = internalStorage + 1
  - return table[N]

- The work and span of this would be W = O(n^2) and the span would also be S = O(n^2)