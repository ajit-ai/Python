def DFA(transitions, start, final, string):

    num = len(string)
    num_final = len(final)
    cur = start

    for i in range(num):

        if transitions[cur][string[i]] is None:
            return False
        else:
            cur = transitions[cur][string[i]]

    for i in range(num_final):
        if cur == final[i]:
            return True
    return False


# find the string in the given dfa

if __name__ == '__main__':
    print(DFA({0: {'a': 1, 'b': None}, 1: {'a': 1, 'b': 2}, 2: {'a': None, 'b': None}}, 0, [2], 'a'))