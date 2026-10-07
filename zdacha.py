def razpoznavane(chislo):
    for znak in chislo:
        if znak >= 'A' and znak <= 'F':
            return 16
    for znak in chislo:
        if znak >= '8' and znak <= '9':
            return 10
    for znak in chislo:
        if znak >= '2' and znak <= '7':
            return 8
    return 2
def v_desetichna(chislo, sistema):
    rezultat = 0
    for znak in chislo:
        if znak >= '0' and znak <= '9':
            cifra = ord(znak) - ord('0')
        else:
            cifra = ord(znak) - ord('A') + 10
        rezultat = rezultat * sistema + cifra
    return rezultat
def ot_desetichna(chislo, sistema):
    znaci = "0123456789ABCDEF"
    rezultat = ""
    while chislo > 0:
        ostatuk = chislo % sistema
        rezultat = znaci[ostatuk] + rezultat
        chislo = chislo // sistema
    return rezultat
chislo = input("Въведи число: ")
nova_sistema = int(input("Въведи системата, в която да го превърна: "))
stara_sistema = razpoznavane(chislo)
desetichno = v_desetichna(chislo, stara_sistema)
rezultat = ot_desetichna(desetichno, nova_sistema)
print("Начална система:", stara_sistema)
print("Резултат:", rezultat)