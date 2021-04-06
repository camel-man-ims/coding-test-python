
def recursive(data):
    if data<0 :
        pass
    else:
        print(data)
        recursive(data-1)

print(recursive(10))