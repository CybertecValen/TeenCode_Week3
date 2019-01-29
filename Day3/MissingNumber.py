
def MissingNumber (val):
    Missing = list()
    sorting = sorted(val)
    lower = sorting[0]
    upper = sorting[-1]

    for x in range(lower,upper):
        if x not in val:
             Missing.append(x)
    return Missing

val = [1,24]
print(MissingNumber(val))