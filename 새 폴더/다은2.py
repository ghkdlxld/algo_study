def trump_tweet(text):
    Hashtag = []
    Mention = []
    ect = []

    sentence = text.split()

    for s in sentence:
        if s.startswith('@'):
            Mention.append(s[1:])
        elif s.startswith('#'):
            Hashtag.append(s[1:])
        else:
            ect.append(s)

    print('hash list : {}'.format(Hashtag))
    print('mention list : {}'.format(Mention))
    print('text list : {}'.format(ect))



t = input()
trump_tweet(t)