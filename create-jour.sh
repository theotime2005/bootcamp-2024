# Ce script sert a générer un fichier .zip avec la journée de bootcamp et le mail de l'élève.
# Se placer à la racine du dossier de Bootcamp et créer un fichier mail.txt avec son mail
# Exécuter le script en indiquant simplement le numéro du jour
# Les dossiers doivent être nommés jour1/jour2/etc
echo "Numéro du jour"
read jour
cd jour$jour
zip ../jour$jour.zip *
cd ../
zip ./jour$jour.zip ./mail.txt