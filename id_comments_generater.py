import random


ID_LENGHT = 10


def get_all_abled_symb():
    lower = "".join([chr(i) for i in range(ord("a"), ord("z"))])
    upper = lower.upper()
    digits = "012356789"

    return lower + upper + digits


def get_id_comment(numb=1,
                   id_lenght=ID_LENGHT,
                   all_symb=get_all_abled_symb(),
                   without_format="#  use '{}' for search"):
    def get_id():
        return "".join([random.choice(all_symb) for _ in range(id_lenght)])

    return ["#  Use '{}' for search".format(get_id()) for _ in range(numb)]


print(get_id_comment(1)[0])
l = get_id_comment(numb=int(input("input number of rands(for exmaple 1): ")))
print("\n".join(l))
    # {}{}{}_{}{}{}_{}{}{} 
# print(l.__name__)
