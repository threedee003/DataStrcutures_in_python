import random
import os
import math


class Stack:
    def __init__(self,size):
        self.size = size
        self.arr = [None]*size
        self.top = -1
        
    def push(self,data):
        if self.size == self.top+1:
            print("Stack Overflow. Cant be executed")
            return
        self.top += 1
        self.arr[self.top] = data
        
    def pop(self):
        if self.top == -1:
            print("Stack Overflow")
            return
        self.arr[self.top] = None
        self.top -= 1
    
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return
        return self.arr[self.top]
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.size == self.top+1





if __name__ == '__main__':
    st = Stack(100)          #stack of size = 100
    st.push(43)
    print(st.peek())



