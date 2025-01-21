import os
from langdetect import detect
from moviepy import AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import subprocess

def detect_language_from_video(video_file, output_folder):
    """
    Détecte la langue parlée dans une vidéo et enregistre les résultats dans un fichier texte
    dans un dossier spécifié.
    """
    # Vérifier si le fichier vidéo existe
    if not os.path.exists(video_file):
        print(f"Le fichier vidéo {video_file} n'existe pas.")
        return

    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Nom du fichier texte pour enregistrer la langue détectée
    output_file = os.path.join(output_folder, f"{os.path.basename(video_file)}_langue.txt")

    # Extraire les 30 premières secondes d'audio avec subprocess
    audio_file = os.path.splitext(video_file)[0] + ".wav"
    try:
        # Utilisation de ffmpeg via subprocess pour extraire les 30 premières secondes de l'audio
        subprocess.run([
            "ffmpeg",
            "-i", video_file,
            "-vn",  # Ignore la vidéo
            "-acodec", "pcm_s16le",  # Format audio WAV
            "-ar", "44100",  # Fréquence d'échantillonnage
            "-ac", "2",  # Stéréo
            "-t", "30",  # Limiter la durée à 30 secondes
            audio_file
        ], check=True)

        print(f"✅ Audio extrait avec succès (30 premières secondes).")

    except subprocess.CalledProcessError as e:
        print(f"⚠️ Erreur lors de l'extraction de l'audio : {e}")
        return

    try:
        # Charger l'audio extrait
        with AudioFileClip(audio_file) as audio_clip:
            # Exemple de texte d'audio extrait (remplacer par transcription réelle)
            audio_text = "Exemple de texte extrait de l'audio"

            # Détection de la langue
            detected_language = detect(audio_text)

            # Enregistrer la langue détectée dans un fichier texte
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"Langue détectée pour {os.path.basename(video_file)}: {detected_language}\n")

            print(f"✅ Langue détectée : {detected_language}, enregistrée dans {output_file}.")

    except Exception as e:
        print(f"⚠️ Erreur lors de l'analyse de l'audio : {e}")

    finally:
        # Nettoyer les fichiers temporaires
        if os.path.exists(audio_file):
            os.remove(audio_file)

# Exemple d'utilisation
# dossier_videos = os.path.join(os.getcwd(), "../data")
# dossier_langues = os.path.join(os.getcwd(), "../data/languages_detected")

dossier_videos = "/project/data"
dossier_langues = "/project/data/languages_detected"

# Lister les vidéos dans le dossier
videos = [f for f in os.listdir(dossier_videos) if f.endswith(('.mp4', '.avi', '.mkv'))]

if not videos:
    print("Aucune vidéo trouvée dans le dossier compressé.")
else:
    for video in videos:
        video_to_analyze = os.path.join(dossier_videos, video)
        detect_language_from_video(video_to_analyze, dossier_langues)
