import re
import string
import random

class Email:
    def __init__(self):
        self.pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,20}$"

    def valider(self, email):
        return bool(re.match(self.pattern, email))

    def generer(self, longueur = 16):
        if longueur < 8:
            raise ValueError("La longueur de l'email doit être d'au moins 8 caractères.")
    
        # Generate username part
        username_length = random.randint(6, longueur -7)
        username = ''.join(random.choice(string.ascii_letters + string.digits + r"._%+-") for _ in range(username_length))
    
        # Common domain names
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', "ofppt-edu-.ma"]
        domain = random.choice(domains)
    
        # Combine parts
        email = f"{username}@{domain}"
        return email

class Password:
    def __init__(self):
        self.pattern = (
            r"(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*[\d])"
            r"(?=.*[@$!%*?&])"
            r"([a-zA-Z\d@$!%*?&]{8,16})"
        )

    def valider(self, mot_de_passe):
        return bool(re.match(self.pattern, mot_de_passe))
    
    def force(self, mo_de_passe):
        if len(mo_de_passe) < 8:
            return "faible"
        elif len(mo_de_passe) >= 8 and len(mo_de_passe) <= 12:
            return "moyen"
        else:
            return "fort"
        
    def generer(self, longueur = 16):
        if longueur < 8:
            raise "La longueur du mot de passe doit être d'au moins 8 caractères."
        
        caracteres = string.ascii_letters + string.digits + string.punctuation
        mot_de_passe = "".join(random.choice(caracteres) for _ in range(longueur)) 

        if not self.valider(mot_de_passe):
            return self.generer(longueur)
        else:
            return mot_de_passe

# Création d'un objet Email

adresse_email = Email()
email = adresse_email.generer()
print()
print("Email généré:", email)
is_valid = adresse_email.valider(email)
print("Est valide:", is_valid)
print()

# Création d'un objet Password
password = Password()
mot_de_passe = password.generer()
print("Mot de passe généré :", mot_de_passe)
is_valid = password.valider(mot_de_passe)
print("Est valide:", is_valid)
print()