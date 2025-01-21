import subprocess
import os

# input_video = "./../videos/input.mp4"
# output_360p = "./../data/output_360p.mp4"
# output_240p = "./../data/output_240p.mp4"

input_video = "/project/videos/input.mp4"
output_360p = "/project/data/output_360p.mp4"
output_240p = "/project/data/output_240p.mp4"


# Vérifier si le fichier vidéo existe
if not os.path.exists(input_video):
    print(f"⚠️ Le fichier {input_video} n'existe pas.")
else:
    # Downscale en 360p (ajuster la largeur pour être divisible par 2)
    subprocess.run([
        "ffmpeg", "-i", input_video, "-vf", "scale=-1:360,setsar=1", "-c:v", "libx264", "-preset", "slow", "-crf", "23", output_360p
    ])

    # Downscale en 240p (ajuster la largeur pour être divisible par 2)
    subprocess.run([
        "ffmpeg", "-i", input_video, "-vf", "scale=-2:240,setsar=1", "-c:v", "libx264", "-preset", "slow", "-crf", "23", output_240p
    ])

    print("✅ Vidéos downscalées avec succès.")
