str = 'АСКЕТ КЕЛЬТ СЕКТА ЖИЛЕТ СЕТКА СТЕКА ТЕСАК КЕЛЬТ ПУЛЬТ ТОРТ СЛИВ СОРТ СЛОВ ТОРС ТРОС';

set1 = set(str.split(' '))
totalList = []

for word1 in set1:
    listAnagram = []
    for word2 in set1:
        if set(word1) == set(word2):
            listAnagram.append(word2)

    if len(listAnagram) > 1 and totalList.count(listAnagram) < 1:
        totalList.append(listAnagram)
        print("Anagram List: ", listAnagram)

input("Press Enter for exit")
