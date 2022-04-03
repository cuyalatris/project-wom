# project-wom
Architecture Microservices - Projet de fin de module 

Pour lancer le projet :
- aller dans le dossier fastapi-mongo
- ouvrez un terminal
- lancez la commande suivante : docker-compose up --build

Ensuite, pour importer la base de données
- ouvrez MongoDB Compass (si besoin l'installer)
- une fois les dockers build, connectez vous au docker de mongo avec la commande suivante : mongodb://localhost:27017
- puis importer la collection "movies_collection" dans la database movies