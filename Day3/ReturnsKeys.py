def listContaining(keylists):

    even = []
    odd = []
    characters = []
    Valen_Dic = dict()

    for x in keylists:

        if isinstance(x, int):
            if x % 2 == 0:
                even.append(x)

            else:
                odd.append(x)

        elif isinstance(x, str):
            characters.append(x)

    Valen_Dic['even1'] = sorted(even)
    Valen_Dic['odd1'] = sorted(odd)
    Valen_Dic['character1'] = sorted(characters)
    return Valen_Dic


print(listContaining([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14, 'a', 'b'
                      ,'c','d','e','f','g','h']))