import random
import math


class Stack:
    def __init__(self,size = 1):
        self.size = size
        self.arr = [None]*size
        self.top = -1
    
    
    def push(self,data):
        if self.size == self.top+1:
            self.resize()
        if self.isFull():
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = data
        
    def resize(self):
        self.size *= 2
        newArray = [None]*self.size
        if newArray is None:
            print("bit is small")
            return
        for i in range(0,self.top+1):
            newArray[i] = self.arr[i]
        
        self.arr = newArray
        
    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return
        temp = self.arr[self.top]
        self.top -= 1
        if self.top < self.size//2:
            print("Reducing size")
            self.size //= 2
            newArray = [None]*self.size
            for i in range(0,self.top+1):
                newArray[i] = self.arr[i]
            self.arr = newArray
    
    def peek(self):
        if self.top == -1:
            print("Stack empty")
            return
        return self.arr[self.top]
    
    def  isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.size == self.top+1
    
    

if __name__ == '__main__':
    st = Stack()
    for i in range(10):
        st.push(i)
    
    while st.isEmpty() == False:
        print(i)
        st.pop()
        
        
        
