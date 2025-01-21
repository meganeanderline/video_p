# Utiliser une image de base avec Python 3.10 sur Alpine
FROM python:3.10.16-alpine3.20

# Mettre à jour le système et installer les dépendances nécessaires
RUN apk add --no-cache \
    ffmpeg \
    flac \
    wget \
    ca-certificates

# Définir une variable pour le chemin d'installation de SpeechRecognition
ENV FLAC_PATH="/usr/local/lib/python3.10/site-packages/speech_recognition/flac-linux-x86_64"

# Télécharger le fichier FLAC
RUN wget -q --no-check-certificate -O $FLAC_PATH \
    https://raw.githubusercontent.com/Uberi/speech_recognition/master/speech_recognition/flac-linux-x86_64 \
    && chmod +x $FLAC_PATH \
    || echo "Erreur lors du téléchargement de FLAC, vérifier le lien ou la connexion réseau."

# Installer les dépendances Python nécessaires
RUN pip install --no-cache-dir \
    moviepy \
    speechrecognition \
    langdetect

# Définir le répertoire de travail
WORKDIR /project

