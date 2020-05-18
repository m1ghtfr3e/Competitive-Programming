def canConstruct(ransomNote, magazine):
    # Possible combinations;
    comboM = []
    comboR = []

    for i in range(len(magazine)+1):
        for j in range(len(magazine)+1):
            comboM.append(magazine[i:j])

    for i in range(len(ransomNote)+1):
        for j in range(len(ransomNote)+1):
            comboR.append(ransomNote[i:j])
    
    return comboM, comboR
    


if __name__ == '__main__':

    print(canConstruct('aa', 'aab'))
