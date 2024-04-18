import tkinter as tk
from tkinter import ttk
import pyttsx3
import wave

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text to Speech Converter")

        # Text input field
        self.text_entry = tk.Text(self.master, height=10, width=50)
        self.text_entry.pack()

        # Language selection dropdown
        self.language_var = tk.StringVar()
        self.language_dropdown = ttk.Combobox(self.master, textvariable=self.language_var)
        self.language_dropdown['values'] = ['English', 'French', 'Spanish']
        self.language_dropdown.pack()

        # Voice selection dropdown
        self.voice_var = tk.StringVar()
        self.voice_dropdown = ttk.Combobox(self.master, textvariable=self.voice_var)
        self.voice_dropdown['values'] = ['Male', 'Female']
        self.voice_dropdown.pack()

        # Speech parameter sliders
        self.rate_label = tk.Label(self.master, text="Speech Rate:")
        self.rate_label.pack()
        self.rate_scale = tk.Scale(self.master, from_=50, to=300, orient=tk.HORIZONTAL)
        self.rate_scale.set(150)
        self.rate_scale.pack()

        self.pitch_label = tk.Label(self.master, text="Speech Pitch:")
        self.pitch_label.pack()
        self.pitch_scale = tk.Scale(self.master, from_=0, to=200, orient=tk.HORIZONTAL)
        self.pitch_scale.set(100)
        self.pitch_scale.pack()

        self.volume_label = tk.Label(self.master, text="Speech Volume:")
        self.volume_label.pack()
        self.volume_scale = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL)
        self.volume_scale.set(50)
        self.volume_scale.pack()

        # Playback controls
        self.play_button = tk.Button(self.master, text="Play", command=self.play_text)
        self.play_button.pack(side=tk.LEFT, padx=5)
        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_text)
        self.pause_button.pack(side=tk.LEFT, padx=5)
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_text)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.replay_button = tk.Button(self.master, text="Replay", command=self.replay_text)
        self.replay_button.pack(side=tk.LEFT, padx=5)

        # Save audio button
        self.save_button = tk.Button(self.master, text="Save Audio", command=self.save_audio)
        self.save_button.pack()

        # Text-to-speech engine initialization
        self.engine = pyttsx3.init()

    def play_text(self):
        text = self.text_entry.get("1.0", "end-1c")
        self.engine.setProperty('rate', self.rate_scale.get())
        self.engine.setProperty('pitch', self.pitch_scale.get() / 100)
        self.engine.setProperty('volume', self.volume_scale.get() / 100)
        self.engine.setProperty('voice', self.voice_dropdown.get())
        self.engine.say(text)
        self.engine.runAndWait()

    def pause_text(self):
        self.engine.pause()

    def stop_text(self):
        self.engine.stop()

    def replay_text(self):
        self.engine.stop()
        self.play_text()

    def save_audio(self):
        text = self.text_entry.get("1.0", "end-1c")
        filename = "output.wav"
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()

def main():
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
