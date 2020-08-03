# tee ratkaisu tänne
def joulukuusi(numero):
    print("joulukuusi!")
    apuri = 1
    tyhja = numero -1
    tyhja2 = numero -1
    apuri2 = 0
    while apuri <= numero:
        print(" " * tyhja +"*"*apuri+"*"*apuri2)
        apuri = apuri +1
        tyhja = tyhja -1
        apuri2 = apuri2 +1
    print(" " *tyhja2 + "*")

joulukuusi(5)