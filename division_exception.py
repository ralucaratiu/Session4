#faceti cu try si except un program care imparte 2 numere citite
#cu input

try:
    deimpartit = int(input("Impartitorul este: "))
    impartitor = int(input("Deimpartitul este: "))
    rezultatul = deimpartit/impartitor
except ValueError:
    print("introdu valori corecte")
except ZeroDivisionError:
    print("impartitorul nu poate fi zero")
except:
    print("some other error I did not forsee")
else:
    #asta se executa doar daca nu a fost nicio exceptie
    print("Rezultatul este:", rezultatul)
finally:
    #indiferent, asta se executa la final
    print("hasta la vista")