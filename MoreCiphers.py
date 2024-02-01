import numpy as np

def playfair_key_matrix(key):

    J = ord("j") - ord("a")
    I = ord("i") - ord("a")

    key = key.lower()
    
    # Forming key matrix
    key = [ord(k) - ord("a") for k in key]
    for _ in range(26):
        if _ not in key:
            key += [_]
    while J in key:
        key[key.index(J)] = I
    KEY_MATRIX = []
    for k in key:
        if k not in KEY_MATRIX:
            KEY_MATRIX += [k]
    KEY_MATRIX = np.array(KEY_MATRIX)
    KEY_MATRIX = np.reshape(KEY_MATRIX, (5,5))

    return KEY_MATRIX

def playfair_cipher(value, key):

    J = ord("j") - ord("a")
    I = ord("i") - ord("a")

    X = ord("x") - ord("a")

    KEY_MATRIX = playfair_key_matrix(key)


    value = value.lower()
    # Form couplets
    value = [ord(v) - ord("a") for v in value]
    for _ in range(0,len(value)-1,2):
        if value[_] == value[_+1]:
            value = value[:_+1] + [X] + value[_+1:]

    if len(value)%2 != 0:
        value += [ord("z") - ord("a")]

    


    value = np.reshape(np.array(value), (-1,2))


    for v in range(len(value)):
        if value[v][0] == value[v][1]:
            value[v][1] = ord("x") - ord("a")
        if value[v][0] == J:
            value[v][0] = I
        if value[v][1] == J:
            value[v][1] = I

        char0 = np.where(KEY_MATRIX == value[v][0])
        char0 = (char0[0][0], char0[1][0])
        char1 = np.where(KEY_MATRIX == value[v][1])
        char1 = (char1[0][0], char1[1][0])

        # Same row
        if char0[0] == char1[0]:
            value[v][0] = KEY_MATRIX[char0[0]][(char0[1] + 1) % 5]
            value[v][1] = KEY_MATRIX[char1[0]][(char1[1] + 1) % 5]

        # same column
        elif char0[1] == char1[1]:
            value[v][0] = KEY_MATRIX[(char0[0] + 1) % 5][char0[1]]
            value[v][1] = KEY_MATRIX[(char1[0] + 1) % 5][char1[1]]

        # standard case
        else:
            value[v][0] = KEY_MATRIX[char0[0]][char1[1]]
            value[v][1] = KEY_MATRIX[char1[0]][char0[1]]

    value = np.reshape(value, (-1))

    value = "".join([chr(ord("a") + v) for v in value])

    return value

def playfair_decipher(value, key):

    KEY_MATRIX = playfair_key_matrix(key)

    # Form couplets
    value = [ord(v) - ord("a") for v in value]

    value = np.reshape(np.array(value), (-1,2))
    for v in range(len(value)):

        char0 = np.where(KEY_MATRIX == value[v][0])
        char0 = (char0[0][0], char0[1][0])
        char1 = np.where(KEY_MATRIX == value[v][1])
        char1 = (char1[0][0], char1[1][0])

        # Same row
        if char0[0] == char1[0]:
            value[v][0] = KEY_MATRIX[char0[0]][(char0[1] - 1) % 5]
            value[v][1] = KEY_MATRIX[char1[0]][(char1[1] - 1) % 5]

        # same column
        elif char0[1] == char1[1]:
            value[v][0] = KEY_MATRIX[(char0[0] - 1) % 5][char0[1]]
            value[v][1] = KEY_MATRIX[(char1[0] - 1) % 5][char1[1]]

        # standard case
        else:
            value[v][0] = KEY_MATRIX[char0[0]][char1[1]]
            value[v][1] = KEY_MATRIX[char1[0]][char0[1]]

    value = np.reshape(value, (-1))

    value = "".join([chr(ord("a") + v) for v in value])

    

    return value


def hill_cipher(value, key):

    size = len(key)
    value = np.array([ord(v) - ord("a") for v in value.lower()]).reshape(size,-1)

    value = np.dot(key, value) % 26

    value = np.reshape(value, (-1))


    return "".join([chr(ord("a") + v) for v in value])

def hill_decipher(value, key):
    
    size = len(key)
    key = np.linalg.inv(key)
    value = np.array([ord(v) - ord("a") for v in value.lower()]).reshape(size,-1)

    value = np.dot(key, value) % 26

    value = np.reshape(value, (-1))


    return "".join([chr(ord("a") + v) for v in value])


def ceasar_cipher(value, key):

    value = [(ord(v) - ord("a") + key) % 26 for v in value.lower()]

    return "".join([chr(v + ord("a")) for v in value])

def ceasar_decipher(value, key):

    value = [(ord(v) - ord("a") - key) % 26 for v in value.lower()]

    return "".join([chr(v + ord("a")) for v in value])


def onepad_cipher(value, key):

    value = [ord(v) - ord("a") for v in value.lower()]
    key = [ord(k) - ord("a") for k in key]

    for _ in range(len(value)):
        value[_] = (value[_] + key[_%len(key)]) % 26

    return "".join([chr(v + ord("a")) for v in value])

def onepad_decipher(value, key):
    value = [ord(v) - ord("a") for v in value.lower()]
    key = [ord(k) - ord("a") for k in key]

    for _ in range(len(value)):
        value[_] = (value[_] - key[_%len(key)]) % 26

    return "".join([chr(v + ord("a")) for v in value])


def railwaygate_cipher(value, key):

    INC = 1
    DEC = -1

    counter = 0
    col = []

    for i in range(len(value)):
        if counter == key:
            flag = DEC
        if counter == 0:
            flag = INC
        
        col += [counter]
        counter += flag

    indexes = np.argsort(col)

    values = np.array(list(value))[indexes]

    return "".join(values)

def railwaygate_decipher(value, key):
    INC = 1
    DEC = -1

    counter = 0
    col = []

    for i in range(len(value)):
        if counter == key:
            flag = DEC
        if counter == 0:
            flag = INC
        
        col += [counter]
        counter += flag

    indexes = np.argsort(col)

    empty = np.zeros(len(value), dtype = np.int64)

    for _ in range(len(indexes)):
        empty[indexes[_]] = _

    values = np.array(list(value))[empty]

    return "".join(values)

    return empty

    
def columnar_cipher(value, key):

    key = np.array([ord(k) - ord("a") for k in key])
    order = key.argsort()
    ranks = list(order.argsort())
    mapping = (ranks * ((len(value) //len(key)) + 1))[:len(value)]

    indices = np.argsort(mapping)

    values = np.array(list(value))[indices]

    return "".join(values)

def columnar_decipher(value, key):

    key = np.array([ord(k) - ord("a") for k in key])
    order = key.argsort()
    ranks = list(order.argsort())
    mapping = (ranks * ((len(value) //len(key)) + 1))[:len(value)]
    indices = np.argsort(mapping)

    temp = np.zeros(len(value), dtype = np.int64)

    for _ in range(len(value)):
        temp[indices[_]] = _
    
    values = np.array(list(value))[temp]

    return "".join(values)


def vernam_cipher(value, key):

    value = [ord(v) - ord("a") for v in value]
    key = [ord(k) - ord("a") for k in key]

    key = (key * ((len(value) // len(key)) + 1))[:len(value)]

    value = np.array(value)
    key = np.array(key)

    value = (value + key) % 26

    return "".join([chr(v + ord("a")) for v in value])

def vernam_decipher(value, key):

    value = [ord(v) - ord("a") for v in value]
    key = [ord(k) - ord("a") for k in key]

    key = (key * ((len(value) // len(key)) + 1))[:len(value)]


    value = np.array(value)
    key = np.array(key)

    value = (value - key) % 26

    return "".join([chr(v + ord("a")) for v in value])
