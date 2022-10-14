from spoopify.project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = [s for s in args]

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        song_list = [s for s in self.songs if s.name == song_name]
        if song_list:
            song = song_list[0]
            self.songs.remove(song)
            return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f'Album {self.name}\n'
        result += '\n'.join([f'== {a.get_info()}' for a in self.songs])
        return result + '\n'
