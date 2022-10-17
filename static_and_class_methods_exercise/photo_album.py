import math


class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        self.page_number = 0
        self.slot_number = 0
        for page in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(math.ceil(photos_count / 4))

    def add_photo(self, label: str):
        self.slot_number += 1
        if self.slot_number > 4:
            self.page_number += 1
            self.slot_number = 1

        if len(self.photos) > self.page_number:
            self.photos[self.page_number].append(label)
            # return f"{label} photo added successfully on page {self.page_number + 1} slot {self.slot_number}"
            return f"{label} photo added successfully on page {self.page_number + 1} slot {self.slot_number}"
        return "No more free slots"

    def display(self):
        lines = '-' * 11
        result = lines + '\n' + '\n'.join([('[] ' * len(page)).rstrip(' ') + '\n' + lines for page in self.photos])
        return result + '\n'


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
