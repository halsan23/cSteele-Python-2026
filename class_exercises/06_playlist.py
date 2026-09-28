# Combining list's and Dictionary's to create a playlist file
# Colt Steele Python Class
# badDoggy | 9/28/26
##############################################################


# Clear Screen
import subprocess
import os

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


# create the base dictionary
# actual song data will be stored in a list that is part of the dictionary
playlist = {
    "title": "My Playlist",
    "author": "badDoggy",
    "songs": [
        {"title": "song1", "artist": ["blue"], "duration": 2.53},
        {"title": "song2", "artist": ["kitty", "djcat"], "duration": 5.25},
        {"title": "song3", "artist": ["garfield"], "duration": 3.75},
    ],
}


# now that we have our playlist, let's pull some data out
# print the title and author
print(playlist["title"])
print(f"Author: {playlist['author']}\n")


# print the songs list
print("- Songs -")
for song in playlist["songs"]:
    print(f'{song["title"]} by {song['artist']}: length {song['duration']}')


# print playlist total time
total_time = 0
for song in playlist["songs"]:
    total_time += song["duration"]

print(f"\nTotal Time: {total_time}")


print()
print()
print("- - End of Line - -")
