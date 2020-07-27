def blackjack(a,b,c):
    if sum((a,b,c)) <= 21 :
        return sum((a,b,c))
    elif sum((a,b,c)) > 21 and (a==11 or b==11 or c == 1):
        return sum((a,b,c)) - 10
    else :
        return 'BUST'
