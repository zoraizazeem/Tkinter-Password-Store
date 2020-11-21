import numpy as np
#inp = input("Please enter a sentence you want to shift: ")
def encryption(sentence):
    part1=[]
    ListInput = []
    for i in sentence:
        ListInput.append(i)
    for i in ListInput:
        k = ord(i) + 3
        part1.append(k)
    part2 = np.exp(np.asarray(part1))
    part3 = part2 / len(ListInput)
    print("encrypted it is: {}".format(part3))
    decryption(part3)
    return part3
def decryption(part3=None):
    part1 = []
    ListInput = []
    for element in part3:
        ListInput.append(float(element))
    print(ListInput)
    ListInput = np.multiply(np.asarray(ListInput), int(len(ListInput)))
    ListInput = np.log(ListInput)
    for i in ListInput:
        k = i - 3
        part1.append(chr(int(round(k))))
    print("decrypted it is: {}".format(part1))
    output = str(part1)
    return output
#encryption(inp)