from typing import List


def split(data: str, sep=' ', maxsplit=-1):
    result_collection = []
    new_word = ''
    split_usage = 0
    start_char_trigger = False

    if len(data) > 0:
        for elem in data:
            if sep.__contains__(elem) and split_usage < maxsplit and maxsplit > 0:
                split_usage += 1
            elif split_usage < maxsplit and maxsplit!= -1:
                new_word += elem
                continue
            else:
                if start_char_trigger == True:
                    new_word += elem
                elif sep.__contains__(elem):
                    continue
                else:
                    new_word += elem
                    start_char_trigger = True
                    continue
                continue

            result_collection.append(new_word)
            new_word = ""

        result_collection.append(new_word)

    return result_collection



if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']


