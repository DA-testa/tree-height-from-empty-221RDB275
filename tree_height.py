# python3
import sys
import threading
import numpy

def compute_height(n, parents):
    height = numpy.zeros(n, dtype=int)
    for i in range(n):
        if parents[i] == -1:
            start = i
    calculate_height(height, start, parents)
    return numpy.max(height)

def calculate_height(height, poz, parents):
    if height[poz] != 0:
        return height[poz]
    max_height = 0
    for child in numpy.where(parents == poz)[0]:
         branch = calculate_height(height, child, parents)
         max_height = max(max_height, branch)
    height[poz] = max_height
    return height[poz]

def main():
    input_type = input()
    if input_type[0] == 'F':
        file_name = input
        if 'a' in file_name():
           return
        else:   
            with open("./test/" + file_name) as test:
                input_type = test.readlines()
            n = int(input_type[0].replace('\n'))
            parents = input_type[1].replace('\n').split(" ")
            parents = numpy.asarray(parents)
    elif input_type[0] == 'I':
        n = int(input())
        stu = input()
        parents = numpy.asarray(stu.split(" "))
    else:
        return
    height = compute_height(n, parents)
    print(height)
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))