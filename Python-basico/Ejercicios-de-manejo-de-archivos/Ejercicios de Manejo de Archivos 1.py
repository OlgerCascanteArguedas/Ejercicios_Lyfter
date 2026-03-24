def sort_songs(input_file, output_file):
    with open(input_file, "r") as file:
        songs = file.readlines()
    songs = [song.strip() for song in songs]
    songs.sort()
    with open(output_file, "w") as file:
        for song in songs:
            file.write(song + "\n")
if __name__ == "__main__":
    sort_songs("songs.txt", "sorted_songs.txt")
    print("Songs sorted successfully!")

    
