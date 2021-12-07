<h1 align="center"> Ecommerce API </h1> <br>



* L'administrateur peut créer/mettre à jour/supprimer une catégorie de produit
* L'administrateur peut créer/mettre à jour/supprimer les détails du produit
* Les utilisateurs authentifiés peuvent faire des demandes POST à la catégorie de produit et aux détails du produit
* Les utilisateurs non authentifiés ne peuvent faire des demandes GET qu'à la catégorie de produit et aux détails du produit
* Les utilisateurs peuvent s'inscrire pour être autorisés
* Les utilisateurs autorisés peuvent effectuer des paiements et commander des produits

Installation étape : 
 Sous mac

1. Création environnement virtuel `python3 -m venv venv`
2. Aller dans le directory de l'env `cd projectenv`
3. Activer le Virtual Environment `chmod +x ./venv/bin/activate.csh`
4. Go To Project Directory `cd DRF-Ecommerce-API`
5. Installer les paquets requis `pip3 install -r requirements.txt`
6. Migrate Database `python3 manage.py migrate`
7. Finallement demarrer le Projet `python3 manage.py runserver`


