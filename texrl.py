import sys


def is_eng(text, index):
    if(index >= len(text) or index < 0):
        return False
    if (48 <= ord(text[index]) <= 57) or (
            64 <= ord(text[index]) <= 90) or (
                97 <= ord(text[index]) <= 122):
        return True
    else:
        if ord(text[index]) <= 128:
            if not is_eng(text, index - 1):
                return False
            if not is_eng(text, index + 1):
                return False
            else:
                return True
        else:
            return False


def latexit(text):
    res = ''
    i = 0
    eng_mode = False
    while i < len(text):
        if not eng_mode:
            if is_eng(text, i):
                res += ('\lr{' + text[i])
                eng_mode = True
            else:
                res += text[i]
        else:
            if not is_eng(text, i):
                res += ('}' + text[i])
                eng_mode = False
            else:
                res += text[i]
        i += 1
    if eng_mode:
        res += '}'
        end_mode = False
    return res


if __name__ == '__main__':
    file = open(sys.argv[1], "r")
    text = file.read()
    file.close()

    res = latexit(text)

    file = open("_res_file", "w")
    file.write(res)
    file.close()
    print("_res_file is created :)")
