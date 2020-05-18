def get_sum(a,b):
    if a == b:
        return a
    else:
        result = 0
        if a < b:
            for i in range(a, b+1):
                result += i
            return result
        if b < a:
            for i in range(b, a+1):
                result += i
            return result


if __name__ == '__main__':

    print(get_sum(0, -3))