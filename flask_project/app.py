import os
import pandas as pd
import plotly.express as px
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration du dossier pour les fichiers uploadés
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Fonction pour vérifier l'extension du file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Fonction pour générer des suggestions de visualisation
def suggest_visualization(df):
    suggestions = []
    
    # Histogrammes pour les colonnes numériques
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        suggestions.append({"type": "histogram", "column": col})
    
    # Graphiques en barres pour les col catégoriques
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        suggestions.append({"type": "bar", "column": col})
    
    # Scatter plot pour les paires de col numériques
    if len(num_cols) >= 2:
        suggestions.append({"type": "scatter", "columns": num_cols[:2]})
    
    # Box plots aussi pour les col numériques
    if len(num_cols) > 1:
        suggestions.append({"type": "box", "columns": num_cols})
    
    return suggestions

# route pour page d'acceurl
@app.route("/")
def index():
    return render_template("index.html")

# Route pour upload fichier
@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "Aucun fichier reçu."})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "Nom de fichier invalide."})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Lire le fichier CSV ou Excel
        if filename.endswith('.csv'):
            df = pd.read_csv(filepath)
        else:
            df = pd.read_excel(filepath)
        
        # Générer des suggestions de visualisation
        suggestions = suggest_visualization(df)
        
        return jsonify({"filename": filename, "columns": df.columns.tolist(), "suggestions": suggestions})
    else:
        return jsonify({"error": "Type de fichier non autorisé. Veuillez télécharger un fichier CSV ou Excel."})

# Route pour afficher les graphiques
@app.route("/plot", methods=["POST"])
def plot_graph():
    data = request.json
    filename = data["filename"]
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Vérifier si le fichier existe
    if not os.path.exists(filepath):
        return jsonify({"error": f"Le fichier {filename} n'existe pas."})
    
    # Lire le fichier CSV ou Excel
    if filename.endswith('.csv'):
        df = pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath)
    
    # Création des graphiques selon le type spécifié
    try:
        if data["type"] == "histogram":
            col = data["column"]
            fig = px.histogram(df, x=col, title=f"Histogramme de {col}", color_discrete_sequence=['#FF6347'])
        elif data["type"] == "bar":
            col = data["column"]
            fig = px.bar(df, x=df[col].value_counts().index, y=df[col].value_counts().values, title=f"Graphique en barres de {col}")
        elif data["type"] == "scatter":
            cols = data["columns"]
            fig = px.scatter(df, x=cols[0], y=cols[1], title=f"Scatter Plot entre {cols[0]} et {cols[1]}")
        elif data["type"] == "box":
            cols = data["columns"]
            fig = px.box(df, y=cols, title=f"Diagramme en boîte pour {', '.join(cols)}")
        else:
            return jsonify({"error": "Type de graphique non pris en charge."})
    except Exception as e:
        return jsonify({"error": f"Erreur lors de la génération du graphique : {str(e)}"})
    
    return jsonify(fig.to_json())

if __name__ == "__main__":
    app.run(debug=True)