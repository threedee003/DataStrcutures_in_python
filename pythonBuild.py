from os import path
import sys

if(path.exists('input.txt')):
 sys.stdin = open("input.txt","r")
 sys.stdout = open("output.txt","w")


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def get_string():
    return sys.stdin.readline().strip()

 #----------------------------------------------------------------------------------------------------------------
 
 
n = int(input())
arr = get_ints()


def main():
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum)


main()



'''


6
1 5 6 4 7 8


31

'''
