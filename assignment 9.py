#Question 1
# Code shows ZeroDivisionError
a=3
if a<4:
    try:
        a=a/(a-3)
    except:
        print("Denominator cannot be zero")
print(a)

#Question 2
# Code shows IndexError
l=[1,2,3]
try:
    print(l[3])
except:
    print("Index above 2 not available")

#Question 3
'''An exception
error'''

#Question 4
'''-5.0
a/b result in 0'''

#Question 5
# ImportError
try:
    import coppyy
except ImportError as msg:
    print('Exception:',msg)
# ValueError
try:
    num=int(input("enter number "))
except ValueError as msg:
    print('Exception:',msg)
# IndexError
a=[4,5,6]
try:
    print(a[4])
except:
    print("index out of range")




