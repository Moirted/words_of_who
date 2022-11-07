def wow_cheat(s_in):
    inp = set(s_in.lower().split(' '))
    s_in = s_in.lower().replace(" ", "")

    for i in range(len(s_in) - 1):
        for j in range(i + 1, len(s_in) - 1):
            if s_in[i] == s_in[j]:
                inp.add(s_in[i].upper())

    result = []
    help_pos = 0
    for i in inp:
        for j in inp:
            if i != j:
                result.append(i + j)
                help_pos += 1

    for it in range(len(inp) - 2):
        len_res = len(result)
        start_i = len_res - help_pos
        help_pos = 0
        for i in inp:
            for j in range(start_i, len_res):
                if i not in result[j]:
                    help_pos += 1
                    result.append(result[j] + i)
    result = [x.lower() for x in result]

    rus_dict = open("russian_nouns.txt", 'r', encoding='utf8')
    words = []
    while True:
        s = rus_dict.readline().rstrip()
        if not s:
            break
        if (s in result) and (len(s) > 2):
            words.append(s)
    rus_dict.close()

    words.sort(key=len)
    return words
