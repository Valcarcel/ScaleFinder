
notes_in_song = ['E','D','C', 'A', 'G'] #Evil Woman, ELO
#notes_in_song = ['C'] #Evil Woman, ELO
#notes_in_song = ['B', 'C#','D', 'E', 'F#','G#','A'] #B Dorian, A major, E major pentatonic scale

chromatic = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
whole_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']*3

def get_notes(key, intervals):
    # finding start of slice
    root = whole_notes.index(key)
    # taking 12 consecutive elements
    octave = whole_notes[root:root+12]
    # accesing indexes specified by `intervals` to retrieve notes
    return [octave[i] for i in intervals]  

# create a scale dictionary:

scales = { 
    "major" : [0, 2, 4, 5, 7, 9, 11],
    "minor" : [0, 2 , 3, 5, 7, 10, 11],
    "dorian" : [0,  2,  3,  5,  7,  9, 10],
    "phrygian" : [0, 1, 3, 5, 7, 8, 10],
    "minor_pentatonic" : [0, 3, 5, 7, 10],
    "major_pentatonic" : [0, 2, 4, 7, 9],
    "harmonic_minor" : [0, 2, 3, 5, 7, 8, 10],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "minor_blues" : [0, 3, 5, 6, 7, 10],
    "locrian" : [0, 1, 3, 5, 6, 8, 10],
    "lydian" :[0, 2, 4, 6, 7, 9, 11],
}


for scale in scales:
    #print scale
    for chromaticnotes in chromatic:
        #print chromaticnotes
        currentscale = (get_notes(chromaticnotes, scales[scale]))
        #print "key of ",chromaticnotes, scale, currentscale, " AND ", notes_in_song
        if all(x in currentscale for x in notes_in_song):
        #if set(notes_in_song).intersection(set(currentscale)) == set(currentscale):
            print (scale, chromaticnotes, currentscale,"contains notes of interest")

#print get_notes('C', scales['minor'])
    
# https://github.com/diegopenilla/PythonGuitar

