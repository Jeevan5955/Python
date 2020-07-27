def palindrome(s):
    reverse = s[::-1]
    normal = s
    for word in range(0, len(s)-1):
        if reverse[word] == normal[word]:
            return True
        else:
            return False


# can be done using .replace() also
#def palindrome(s):
    
    #s = s.replace(' ','') 
    #return s == s[::-1]
