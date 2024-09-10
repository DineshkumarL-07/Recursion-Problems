def reverse(ind, new):
    if ind == -1:
        return new
    return reverse(ind - 1, new + String1[ind])



String1 = "madamm"
if reverse((len(String1) - 1),"") == String1:
    print(True)
else:
    print(False)
