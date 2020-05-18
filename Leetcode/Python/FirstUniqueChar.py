def firstUniqChar(s):
    # Store the chars and their existance in dict
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) +1
    
    for char, count in counts.items():
        # We get first appearance of '1 time'
        if count == 1:
            for i in range(len(s)):
                if s[i] == char:
                    return i
    # If there was no unique letter:
    return -1



if __name__ == '__main__':

    print(firstUniqChar('loveleetcode'))