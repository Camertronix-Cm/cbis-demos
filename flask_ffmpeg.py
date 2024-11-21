import os
import subprocess
from flask import Flask, render_template

app = Flask(__name__)

# Répertoire des vidéos pour chaque catégorie
FOLDERS = {
    "default": {"input_dir": "input_videos", "static_dir": "static/default"},
    "set1": {"input_dir": "input_videos1", "static_dir": "static/set1"},
    "set2": {"input_dir": "input_videos2", "static_dir": "static/set2"},
    "set3": {"input_dir": "input_videos3", "static_dir": "static/set3"},
    "set4": {"input_dir": "input_videos4", "static_dir": "static/set4"},
    "set5": {"input_dir": "input_videos5", "static_dir": "static/set5"},
    "set6": {"input_dir": "input_videos6", "static_dir": "static/set6"},
}

TITLES = {
    "default": ["Video 1", "Video 2"],
    "set1": ["Set1 Video 1", "Set1 Video 2"],
    "set2": ["Result"],
}
# Vidéos source et leur sortie (mêmes noms dans chaque catégorie)
VIDEOS = [
    {"input": "camera1.mp4", "output": "video1.mp4"},
    {"input": "camera2.mp4", "output": "video2.mp4"},
    {"input": "output_video1.mp4", "output": "output_result.mp4"},
]

# Fonction de conversion des vidéos avec FFmpeg
"""def convert_videos(input_dir, static_dir):
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    for video in VIDEOS:
        input_path = os.path.join(input_dir, video["input"])
        output_path = os.path.join(static_dir, video["output"])
        
        # Skip conversion if output file already exists
        if os.path.exists(output_path):
            print(f"Fichier déjà converti : {output_path}. Ignoré.")
            continue
        
        if not os.path.exists(input_path):
            print(f"Erreur : fichier {input_path} introuvable.")
            continue
        
        try:
            print(f"Conversion de {input_path} en {output_path}...")
            subprocess.run(
                [
                    "ffmpeg", "-i", input_path,
                    "-vcodec", "libx264", "-preset", "fast", "-crf", "23",
                    "-acodec", "aac", "-strict", "experimental", output_path
                ],
                check=True
            )
            print(f"Conversion réussie : {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la conversion de {input_path}: {e}")

# Conversion des vidéos pour tous les répertoires spécifiés dans FOLDERS
for folder_key, paths in FOLDERS.items():
    print(f"Traitement du répertoire : {folder_key}")
    convert_videos(paths["input_dir"], paths["static_dir"])"""
# Routes for each video set
@app.route("/")
def index():
    video_paths = [os.path.join(FOLDERS["default"]["static_dir"], video["output"]) for video in VIDEOS]
    print("Default dataset video paths:", video_paths)
    return render_template(
        "index.html",
        videos=[video["output"] for video in VIDEOS],
        static_folder=FOLDERS["default"]["static_dir"],
        active="default",
        title="Dataset"
    )

@app.route("/set1")
def set1():
    return render_template(
        "index.html",
        videos=[video["output"] for video in VIDEOS],
        static_folder=FOLDERS["set1"]["static_dir"],
        active="set1",
        title="Dataset1"
    )

@app.route("/set2")
def set2():
    return render_template(
        "index.html",
        videos=[video["output"] for video in VIDEOS],
        static_folder=FOLDERS["set2"]["static_dir"],
        active="set2",
        title="Dataset2"
    )

@app.route("/set3")
def set3():
    return render_template(
        "index.html",
        videos=[video["output"] for video in VIDEOS],
        static_folder=FOLDERS["set3"]["static_dir"],
        active="set3",
        title="Dataset3"
    )

@app.route("/set4")
def set4():
    return render_template(
        "index.html",
        videos=[video["output"] for video in VIDEOS],
        static_folder=FOLDERS["set4"]["static_dir"],
        active="set4",
        title="Dataset4"
    )

@app.route("/set5")
def set5():
    return render_template(
        "index.html",
        videos=[video["output"] for video in VIDEOS],
        static_folder=FOLDERS["set5"]["static_dir"],
        active="set5",
        title="Dataset5"
    )

@app.route("/set6")
def set6():
    return render_template(
        "index.html",
        videos=[video["output"] for video in VIDEOS],
        static_folder=FOLDERS["set6"]["static_dir"],
        active="set6",
        title="Dataset6"
    )

if __name__ == "__main__":
    app.run(debug=True)
