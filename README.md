# Data Check

**Data Check** est une application développée en Python avec Flask permettant de télécharger des fichiers CSV ou Excel, d'analyser les données qu'ils contiennent et de proposer des visualisations graphiques adaptées. Ce projet est conçu pour aider à l'analyse des données en générant des graphiques utiles et des recommandations sur la meilleure manière de visualiser les informations.


## Aperçu de l'application

![Aperçu de Data Check](demo_dataCheck.jpg)

## Fonctionnalités

- Téléchargement de fichiers CSV ou Excel.
- Analyse des données contenues dans ces fichiers.
- Suggestions automatiques de visualisations graphiques adaptées (histogrammes, graphiques en barres, scatter plots, etc.).
- Affichage dynamique des graphiques via Plotly.

## Prérequis

Avant de commencer, assurez-vous que vous avez installé les éléments suivants :

- **Python 3.x** (recommandé : 3.8 ou plus récent)
- **Pip** (gestionnaire de paquets Python)

## Installation

1. Clonez le dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/Lemar00/data-check.git
Allez dans le répertoire du projet :
cd data-check
Créez un environnement virtuel (facultatif mais recommandé) :
python -m venv venv
Activez l'environnement virtuel :
Sur Windows :
.\venv\Scripts\activate
Sur macOS/Linux :
source venv/bin/activate
Installez les dépendances requises :
pip install -r requirements.txt
Lancer l'application

Une fois les dépendances installées, lancez l'application Flask :
python app.py
Ouvrez un navigateur et accédez à l'application via :
http://127.0.0.1:5000
Utilisation

Téléchargez un fichier CSV ou Excel en utilisant le formulaire sur la page principale.
L'application analysera le fichier et vous proposera des suggestions de visualisation basées sur le contenu du fichier (histogrammes, graphiques en barres, scatter plots, etc.).
Sélectionnez l'une des suggestions pour afficher un graphique interactif.
Technologies utilisées

Flask : Framework web Python pour le backend.
Pandas : Bibliothèque Python pour la manipulation des données.
Plotly : Bibliothèque pour la création de graphiques interactifs.
Werkzeug : Utilisé pour sécuriser les noms de fichiers et gérer les uploads.
Contributions

Les contributions sont les bienvenues ! Si vous avez des idées d'améliorations ou des corrections de bugs, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.
