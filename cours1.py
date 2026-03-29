def prenom(ma_liste):

    prenom_valide = []

    for prenom in ma_liste:
        if len(prenom) >= 5:
            prenom_valide.append(prenom)
    return prenom_valide



def ma_fonction(mon_dict):

    return f"{mon_dict['nom']} est {mon_dict['metier']} à {mon_dict['ville']}"

mon_dict = {"nom": "Dupont", "metier": "developpeur", "ville": "paris"}
print(ma_fonction(mon_dict))

def ma_fonction(dictionnaire):

    try:
        return f"{dictionnaire['age']} ans"


    except:
        return "age non trouvé"
dictionnaire = {"nom": "Dupont"}
print(ma_fonction(dictionnaire))