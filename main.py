
# Online Python - IDE, Editor, Compiler, Interpreter

mini = 100
arr = [1,4,6,4,3,56,67,5,]

arr2 = []

while (len(arr) > 0) :
    mini = min(arr)
    arr2.append(mini)
    arr.remove(mini)

print(arr2)