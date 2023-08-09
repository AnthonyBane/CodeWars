def create_phone_number(n):
    return "({}) {}-{}".format(\
                    "".join(str(char) for char in n[0:3]),\
                    "".join(str(char) for char in n[3:6]),\
                    "".join(str(char) for char in n[6:]))