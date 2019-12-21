import random

chromaticSharp = "C C♯ D D♯ E F F♯ G G♯ A A♯ B"
chromaticFlat = "C D♭ D E♭ E F G♭ G A♭ A B♭ B"
strings = "E A D G B e"

string = strings.split()
sharps = chromaticSharp.split()
flats = chromaticFlat.split()

print("sharps and flats separate")
for x in range(6):
  random.shuffle(sharps)
  random.shuffle(flats)
  print(string[x] + " string sharps: " + str(sharps))
  print(string[x] + " string flats:  " + str(flats))

print("")
print("random choice of sharps and flats")


notes = [
  ["C"],
  ["C#", "D♭"],
  ["D"],
  ["E"],
  ["F"],
  ["G"],
  ["A"],
  ["B"],
  ["D♯", "E♭"],
  ["F♯", "Gb"],
  ["G♯","A♭"],
  ["A♯","B♭"], 
]

for x in range(6):
  random.shuffle(notes)
  melody = []
  for y in range(len(notes)):
    melody.append(random.choice(notes[y]))
  print(string[x] + " string: " + str(melody))
