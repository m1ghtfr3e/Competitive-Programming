'''
  Let P be the Principal = 1000.00      
  Let I be the Interest Rate = 0.05      
  Let T be the Tax Rate = 0.18      
  Let D be the Desired Sum = 1100.00
'''

def calculate_years(principal, interest, tax, desired):

    if principal == desired:
        return 0

    notdesired = True
    count = 0
    while notdesired:
        payint = (principal * interest)             # Interest to pay
        paytax = payint * tax                       # Tax to pay
        tmp = payint - paytax                       # Increase
        principal += tmp 
        count += 1
        if principal >= desired:
            notdesired = False

    return count


if __name__ == '__main__':

    print(calculate_years(1000, 0.05, 0.18, 2000))