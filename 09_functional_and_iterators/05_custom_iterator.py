"""05_custom_iterator.py - Make your own object work in a for loop."""


class Countdown:
    """Counts down from a number to 1."""

    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration     # tells the for loop to stop
        value = self.current
        self.current -= 1
        return value


class Playlist:
    def __init__(self, songs: list):
        self.songs = songs

    def __iter__(self):
        return iter(self.songs)     # reuse the list's own iterator

    def __len__(self):
        return len(self.songs)


for number in Countdown(4):
    print(number, end=" ")
print()

playlist = Playlist(["Song A", "Song B", "Song C"])
print("Songs:", len(playlist))
for song in playlist:
    print("Playing", song)
