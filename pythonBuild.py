from os import path
import sys

if(path.exists('input.txt')):
 sys.stdin = open("input.txt","r")
 sys.stdout = open("output.txt","w")



n = int(input())
arr = [int(x) for x in input().split()]

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
