# sum of the nth term series
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

def series_sum(n):
   
    if n <= 1:
        return '%.2f' %n

    div = 4
    s = 1
    for _ in range(n-1):
        s += 1/div
        div += 3

    return '%.2f' %s


if __name__ == '__main__':

    print(series_sum(0))