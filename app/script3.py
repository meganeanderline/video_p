import os
from moviepy import VideoFileClip
from speech_recognition import Recognizer, AudioFile, UnknownValueError, RequestError

def get_language_for_video(lang_folder, video_file):
    """
    Récupère la langue associée à une vidéo à partir du fichier texte dans le dossier langue_détectée.
    """
    video_name_with_extension = os.path.basename(video_file)
    lang_file = os.path.join(lang_folder, f"{video_name_with_extension}_langue.txt")
    
    if not os.path.exists(lang_file):
        raise FileNotFoundError(f"Fichier de langue introuvable pour la vidéo : {video_file}")

    with open(lang_file, "r", encoding="utf-8") as f:
        detected_language = f.read().strip().split(":")[-1].strip()
    return detected_language

def transcribe_video(video_file, language_code, output_folder):
    """
    Transcrit une vidéo en texte et enregistre les sous-titres dans un dossier spécifié.
    """
    if not os.path.exists(video_file):
        print(f"Le fichier vidéo {video_file} n'existe pas.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    subtitles_file = os.path.join(output_folder, os.path.splitext(os.path.basename(video_file))[0] + "_subtitles.txt")

    audio_file = os.path.splitext(video_file)[0] + ".wav"

    try:
        print(f"Extraction de l'audio depuis la vidéo : {video_file}...")
        video = VideoFileClip(video_file)
        video.audio.write_audiofile(audio_file)

        recognizer = Recognizer()

        with AudioFile(audio_file) as source:
            audio_data = recognizer.record(source, duration=60)  # Limiter à 60 secondes

        try:
            # Tentative avec Google (en ligne)
            print("Tentative de transcription avec Google...")
            text = recognizer.recognize_google(audio_data, language=language_code)
        except (RequestError, UnknownValueError):
            # Si la reconnaissance échoue, basculer sur Sphinx (hors ligne)
            print("Transcription avec Google échouée. Tentative avec Sphinx...")
            text = recognizer.recognize_sphinx(audio_data)

        with open(subtitles_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Sous-titres générés et enregistrés dans {subtitles_file}.")

    except Exception as e:
        print(f"Erreur lors de la transcription pour la vidéo {video_file} : {e}")

    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)
        if 'video' in locals():
            video.close()

def main():
    # dossier_videos = os.path.join(os.getcwd(), "./../data")
    # dossier_langues = os.path.join(os.getcwd(), "./../data/languages_detected")
    # dossier_sous_titres = os.path.join(os.getcwd(), "./../data/sous_titres")

    dossier_videos = os.path.join(os.getcwd(), "/project/data")
    dossier_langues = os.path.join(os.getcwd(), "/project/data/languages_detected")
    dossier_sous_titres = os.path.join(os.getcwd(), "/project/data/sous_titres")

    videos = [f for f in os.listdir(dossier_videos) if f.endswith(('.mp4', '.avi', '.mkv'))]

    if not videos:
        print("Aucune vidéo trouvée dans le dossier.")
        return

    for video in videos:
        video_path = os.path.join(dossier_videos, video)

        try:
            detected_language = get_language_for_video(dossier_langues, video)
            print(f"Langue récupérée pour {video} : {detected_language}")

            transcribe_video(video_path, detected_language, dossier_sous_titres)

        except FileNotFoundError as e:
            print(e)

if __name__ == "__main__":
    main()
