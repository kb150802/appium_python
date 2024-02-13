def getData():
    return ["kushagra@qaprod.flock.com", "kushagra@123"]



def get_incorrect_data():
    return [
        ["kushagra@titan.email", "abcd@1234"],
        ["abcd@titan.email", "qwerty@12345"],
    ]


def get_invalid_data():
    return [
        ["abcd", "abcd@1234"],
        ["abcd@titan.email","abcd"],
        ["abcd", "abcd"]
    ]