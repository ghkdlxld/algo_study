

def filter_by_text(text):
    corpus = []
    result = []
    # text 로 시작하는 단어 corpus에 저장
    with open('corpus.txt') as file:
        for line in file:
            words = tuple(line.strip('\n').split('/'))
            word = (words[0], int(words[1]))
            corpus.append(word)
            if word[0].startswith(text):
                result.append(word)


    # start_text 빈도수 대로 내림차순 정렬
    for i in range(len(result)-1):
        for j in range(len(result)-1-i):
            if result[j][1] < result[j+1][1]:
                result[j], result[j+1] = result[j+1], result[j]

    # 상위 20개 출력
    if len(result) < 20:
        return print(result)
    else:
        return print(result[:20])


t = input()
filter_by_text(t)