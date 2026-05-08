import vlc
import time
import os
import sys
import keyboard

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

video_path = os.path.join(base_path, "video.mp4")

if not os.path.exists(video_path):
    sys.exit()

instance = vlc.Instance("--input-repeat=9999", "--no-video-title-show", "--quiet")
player = instance.media_player_new()
media = instance.media_new(video_path)
player.set_media(media)

player.play()

time.sleep(1) 
player.set_fullscreen(True)

try:
    while True:
        state = player.get_state()
        if state == vlc.State.Ended or state == vlc.State.Stopped:
            player.play()
            time.sleep(0.5)
            player.set_fullscreen(True)

        if keyboard.is_pressed('esc'):
            player.stop()
            break
            
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    player.stop()
    sys.exit()