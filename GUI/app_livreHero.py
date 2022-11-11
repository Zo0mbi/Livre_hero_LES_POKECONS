import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importer la classe Ui_MainWindow du fichier GUI.py
from GUI import Ui_MainWindow

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="Livre_hero"
)
def convertTuple(tup):
    pass

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)
        # On connecter un événement sur le line edit

    # insertion du joueur dans la BD
    def insertionJoueur(self):
        mycursor = mydb.cursor()
        nom = self.lineEditNom.text()
        sql ="INSERT INTO joueur_sauvegarde (nom, chapitre_pogression, point_de_vie, combat, endurance) VALUES (%s, %s, %s, %s, %s)"
        val = (nom, 0, 100, 25, 25)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted")
        
    
    # Select du premier chapitre du livre
    def selectChapitre1(self):
        mycursor= mydb.cursor()
        mycursor.execute("SELECT texte FROM chapitre WHERE no_chapitre = 0")
        chapitre = 'Avertir le roi'
        monResultat = mycursor.fetchall()
        texte = ""
        for x in monResultat:
            for y in x:
                texte = y
        
        self.labelTexte.setText(texte)
        print(texte)
        self.labelChapitre.setText(chapitre)

    
    def selectPartieSauvegarde(self):
        # Get la partie du joueur
        # Après ça select le texte du chapitre
        # affiche moe ça dans gros texte box
        pass
    
    def updateChapitreJoueur(self):
        # faire un update sur la table joueur_sauvegarde
        # avec le chapitre du joueur est rendu ou
        pass
    
    def updateStats(self):
        # update des stats dans la table joueur_sauvegarde
        pass

    def selectTexte(self):
        # juste un select pour afficher le texte du chapitre
        pass
    def selectChapitre(self):
        # un select du texte pour le prochain chapitre
        pass
    def updateChapitre(self):
        # update le chapitre la bien simple
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
