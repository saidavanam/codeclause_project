import os
import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame
pygame.init()

# Create the main window
root = tk.Tk()
root.title("Colorful Music Player")

# Set the background color
root.configure(bg='#3E3E3E')

# Set the directory where your music files are stored
music_dir = 'C:/Users/ASUS/Downloads/music'

# Create a list of music files in the directory
music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]

# Initialize the mixer for audio playback
pygame.mixer.init()

# Create a function to play music
def play_music():
    selected_file = listbox.get(tk.ACTIVE)
    pygame.mixer.music.load(os.path.join(music_dir, selected_file))
    pygame.mixer.music.play()

# Create a function to open a file dialog and add songs to the listbox
def add_songs():
    files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
    for file in files:
        filename = os.path.basename(file)
        listbox.insert(tk.END, filename)

# Create a listbox to display available songs with custom styling
listbox = tk.Listbox(root, bg='#222', fg='#FFF', selectbackground='#FFC107', selectforeground='#222', selectmode=tk.SINGLE, height=10)
for file in music_files:
    listbox.insert(tk.END, file)

# Create buttons to play and add songs with custom styling
play_button = tk.Button(root, text="Play", command=play_music, bg='#FFC107', fg='#222', relief=tk.RAISED)
add_button = tk.Button(root, text="Add Songs", command=add_songs, bg='#FFC107', fg='#222', relief=tk.RAISED)

# Place widgets in the window
listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
play_button.pack(pady=5, padx=10)
add_button.pack(pady=5, padx=10)

# Start the GUI event loop
root.mainloop()

# Quit pygame
pygame.quit()
