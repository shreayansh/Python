import textwrap


def wrap(string, max_width):
    return ('\n'.join(string[i * max_width:i * max_width + max_width]
                      for i in range(len(string) - max_width)))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)