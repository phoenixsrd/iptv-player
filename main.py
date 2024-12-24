import tkinter as tk
from tkinter import messagebox
import vlc

class IPTVPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("IPTV Player")

        self.url_label = tk.Label(root, text="Stream URL:https://412waf3tbbmrag5m.public.blob.vercel-storage.com/IPTV.M3U8")
        self.url_label.pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play_stream)
        self.play_button.pack()

        self.video_frame = tk.Frame(root, bg="black")
        self.video_frame.pack(fill=tk.BOTH, expand=1)

        self.vlc_instance = vlc.Instance()
        self.player = self.vlc_instance.media_player_new()

    def play_stream(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Erro", "Por Favor, Insira A URL Do Stream.")
            return

        media = self.vlc_instance.media_new(url)
        self.player.set_media(media)

        self.player.set_hwnd(self.video_frame.winfo_id())
      
        self.player.play()

if __name__ == "__main__":
    root = tk.Tk()
    app = IPTVPlayer(root)
    root.mainloop()
