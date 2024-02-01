# %%
def encrypt_caesar(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

# %%
def decrypt_caesar(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

# %%
def encrypt_vignere(text, key):
    result = ""
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        if (text[i].isupper()):
            x += ord('A')
        else:
            x += ord('a')
        result += chr(x)
    return result

# %%
def decrypt_vignere(text, key):
    result = ""
    for i in range(len(text)):
        x = (ord(text[i]) - ord(key[i]) + 26) % 26
        if (text[i].isupper()):
            x += ord('A')
        else:
            x += ord('a')
        result += chr(x)
    return result

# %%
def columnar_encrypt(text, key):
    chunks, chunk_size = len(text), len(key)
    L = [text[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    new_L = ['' for i in range(len(key))]
    for i in range(len(L)):
        for j in range(len(L[i])):
            new_L[j] += L[i][j]
    print(L)
    print(new_L)
    D = {}
    for i in range(len(key)):
        D[key[i]] = new_L[i]
    result = ''
    for j in sorted(key):
        result+= D[j]
    return result

# %%
def columnar_decrypt(text, key):
    

# %%
def encrypt_rail(text, key):
    rail = [['' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row,col = 0, 0
    for i in range(len(text)):
        if ((row == 0) or (row == key-1)):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col+=1
        if dir_down:
            row+=1
        else:
            row-=1
    result = ''
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '':
                result+=rail[i][j]
    return result

# %%
def decrypt_rail(text, key):
    rail = [['' for i in range(len(text))] for j in range(key)]
    dir_down=False
    row,col=0,0
    for i in range(len(text)):
        if (row==0) or (row==key-1):
            dir_down=not dir_down
        rail[row][col] = "*"
        col+=1
        if dir_down:
            row+=1
        else:
            row-=1
    index = 0
    for i in range(key):
        for j in range(len(text)):
            if (rail[i][j] == '*') and (index < len(text)):
                rail[i][j] = text[index]
                index+=1
    dir_down = False
    result = ''
    row,col = 0,0
    for i in range(len(text)):
        if (row==0) or (row==key-1):
            dir_down=not dir_down
        result+=rail[row][col]
        col+=1
        if dir_down:
            row+=1
        else:
            row-=1
    return result


# %%
text = "MAMANAARMAMIYAAR"
for i in range(len())

# %%
[t]

# %%



