def mutate_string(string, position, character):
    string=list(string)
    string.pop(position)
    string.insert(position, character)
    a=""
    return (a.join(string))
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)