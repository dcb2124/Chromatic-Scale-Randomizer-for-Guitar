import random

chromaticSharp = "C C♯ D D♯ E F F♯ G G♯ A A♯ B"
chromaticFlat = "C D♭ D E♭ E F G♭ G A♭ A B♭ B"
strings = "E A D G B e"

string = strings.split()
sharps = chromaticSharp.split()
flats = chromaticFlat.split()

for x in range(6):
  random.shuffle(sharps)
  random.shuffle(flats)
  print(string[x] + " string sharps: " + str(sharps))
  print(string[x] + " string flats: " + str(flats))