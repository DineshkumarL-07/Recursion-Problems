def reverse(s,ind):

    if ind == len(s)//2:
        return
    s[ind], s[len(s)-ind-1] = s[len(s)-ind-1], s[ind]
    reverse(s,ind + 1)

arr = [1,2,3,4,5,6]
reverse(arr,0)
print(arr) 