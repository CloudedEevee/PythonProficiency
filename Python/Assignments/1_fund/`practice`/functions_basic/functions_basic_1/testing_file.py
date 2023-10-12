# The file to test each code block individually



def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
# Prediction: 1
# Prediction: 3
# Prediction: 5
print(y)