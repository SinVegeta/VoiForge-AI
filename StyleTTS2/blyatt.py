import time
import sys

# 🎵 Step 1: Define lyrics with timestamps (in seconds)
lyrics_with_timestamps = [
    (1, "jo tere khatir tadpe ..."),
    (2, "pehele se he..."),
    (3, "kya usee tadpana🥀..."),
    (4, "O Zalimaa..."),
    (9, "O Zalimaaaaaa😭..."),
    (12, "jo tere ishk me beheka🥰..."),
    (13, "pehele se he..."),
    (14, "kya usee behekana..."),
    (15, "O Zalimaaaaaa😩..."),
    (20, "O Zalimaa🙅🏻‍♂️...")
]

# 🎵 Step 2: Function to print lyrics letter by letter
def play_lyrics(lyrics, delay_per_char=0.1):
    start_time = time.time()
    for timestamp, line in lyrics:
        # Wait until it's time for this line
        while time.time() - start_time < timestamp:
            time.sleep(0.05)
        # Print each character with delay
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay_per_char)
        print()  # move to next line after full lyric

if __name__ == "__main__":
    print("🎶 Starting karaoke...\n")
    play_lyrics(lyrics_with_timestamps)
