
# a sufficiently long list to take 12 notes out of any note
whole_notes = ['C' , 'C#', 'D', 'D#', 'E', 'F', 'F#' , 'G', 'G#', 'A', 'A#', 'B']*3

def get_notes(key, intervals):
    """Given any key C, C#... B
       and intervals z.B Tone Tone Semitone"""
    root = whole_notes.index(key)
    octave = whole_notes[root:root+12]
    return [octave[i] for i in intervals]

# Now given some intervals
scales = { 
    "major" : [0, 2, 4, 5, 7, 9, 11],
    "minor" : [0, 2 , 3, 5, 7,8, 10,],
    "dorian" : [0,  2,  3,  5,  7,  9, 10],
    "phrygian" : [0, 1, 3, 5, 7, 8, 10 ],
    "minor_pentatonic" : [0, 3, 5, 7, 10],
    "major_pentatonic" : [0, 2, 4, 7, 9],
    "harmonic_minor" : [0, 2, 3, 5, 7, 8, 10,],
    "aeolian" : [0, 2, 3, 5, 7, 8, 10,],
    "minor_blues" : [0, 3, 5, 6, 7, 10],
    "locrian" : [0, 1, 3, 5, 6, 8, 10,],
    "lydian" :[0, 2, 4, 6, 7, 9, 11,],
}

# Creating strings of guitar
start_strings = []
strings = {i:0 for i in 'EADGB'}
for i in strings.keys():
    start = whole_notes.index(i)
    strings[i] = whole_notes[start:start+20]


print('Notes in the A string: ', strings['A'])
print('Notes in the G string: ', strings['G'])