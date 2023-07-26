def play():
    vides = int(input('BENVINGUT AL PENJAT!\n\nQuantes vides tindreu? '))
    while vides < 3:
        print('Com a mínim hi ha d\'haver 3 vides!')
        vides = int(input('BENVINGUT AL PENJAT!\n\nQuantes vides tindreu? '))
    oculta = input('Jugador 1 - Inserta la paraula oculta: ')
    l = len(oculta)
    print(f'La paraula té {l} lletres!')
    paraula = '_'*l
    winner = False
    while not winner:
        lletra = input('Jugadors, quina lletra escolliu? ')
        aux = paraula
        paraula = canvia(oculta=oculta, actual=paraula, lletra=lletra)
        if paraula == oculta:
            winner = True
            print('Felicitats! Heu encertat')
            print(f'Efectivament, la paraula oculta era "{oculta}"')
            break
        if aux == paraula:
            vides -= 1
            print(f'Heu fallat! -1 vida. Vides actuals = {vides}')
            if vides == 0:
                winner = True
                print('Us heu quedat sense vides! El Jugador 1 ha guanyat.')
                break
        print(f'-- PROGRÉS ACTUAL --\nParaula actual: {paraula}\n Vides restants: {vides}')

        
def canvia(oculta, actual, lletra):
    nova_paraula = ''
    for idx,i in enumerate(oculta):
        if i == lletra:
            nova_paraula += lletra
        else:
            nova_paraula += actual[idx]
    return nova_paraula