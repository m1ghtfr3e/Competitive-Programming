# We have 25, 50 and 100 bills
# Ticket costs 25

## Not really correct!
def tickets(people):
    acceptable = [25, 50, 100]

    tf, ff, hn = 0, 0, 0        # representing 25, 50, 100
    
    price = 25
    mychange = 0
    change = 0

    for n in people:
        
        if n == price:
            mychange += n
            change += n -price
            tf += 1      
        if n != price:
            change = n - price
            mychange -= change
            if change > mychange:
                try:
                    if change//tf not in acceptable:
                        return 'NO'
                except ZeroDivisionError:
                    return 'NO'
            else:
                return 'YES'

    return 'YES'


def tickets1(people):

    tf = 0
    ff = 0
    hn = 0
    price = 25
    win = 0

    for n in people:
        if n == price:
            tf += 1
            win += n
        else:
            if n == 50:
                ff += 1
                win += n - price
                # Change is always 25
                if tf <= 0:          # If we don't have a 25 bill, no change
                    return 'NO'
                else:
                    return 'YES'
            elif n == 100:
                hn += 1
                win += n - price
                # Change is always 75
                if ff <= 0:        
                    if tf < 3:
                        return 'NO'
                if ff > 0 and tf <= 0:
                    return 'NO'
                else:
                    return 'YES'
    if win == (tf + ff + hn) * price:
        return 'YES'
    else:
        return 'NO'           
                







if __name__ == '__main__':

    print(tickets1([25, 25, 25, 100]))
    print(tickets1([25, 100]))
    #print(tickets1([25, 25, 50]))
    #print(tickets1([25, 25, 25, 25, 25, 25, 25, 25, 25, 25]))
    #print(tickets1([50, 50, 50, 50, 50, 50, 50, 50, 50, 50]))