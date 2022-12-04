if __name__ == "__main__":

    engWords = open('words_alpha.txt', 'r').read().splitlines() # remove newlines from input
    finWords = open('kaikkisanat.txt', 'r').read().splitlines()

    engList = []
    count = 0

    for word in engWords:
        engList.append(word)

    for word in finWords:
        if word in engList:
            count += 1

    print(count)