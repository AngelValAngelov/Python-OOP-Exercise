def start_playing(instrument):
    return instrument.play()


class Guitar:
    def play(self):
        print("playing the guitar")


guitar = Guitar()
start_playing(guitar)


class Piano:
    def play(self):
        print("playing the piano")


piano = Piano()
start_playing(piano)
