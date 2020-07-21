import time

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
    #"dorian" : [0,  2,  3,  5,  7,  9, 10, 12],
    #"phrygian" : [0, 1, 3, 5, 7, 8, 10, 12],
    #"minor_pentatonic" : [0, 3, 5, 7, 10],
    #"major_pentatonic" : [0, 2, 4, 7, 9],
    #"harmonic_minor" : [0, 2, 3, 5, 7, 8, 10, 12],
    #"mixolydian": [0, 2, 4, 5, 7, 9, 10],
    #"minor_blues" : [0, 3, 5, 6, 7, 10],
    #"locrian" : [0, 1, 3, 5, 6, 8, 10, 12],
    #"lydian" :[0, 2, 4, 6, 7, 9, 11, 12],
}


for scale in scales:
    #print (scale) #output is "major", "minor", etc.
    print ("scale is ", scale)
    intervals = scales[scale]
    print intervals
    for key in whole_notes:
        print ("The ", key, scale, "notes are: ")
        #key is C, D, D#, etc.
        root = whole_notes.index(key) # if key is C, root is 0
        #print ("root is ", root) #print 0 to 11
        octave = whole_notes[root:root+12]
        #print octave #prints chromatic scale starting with root.
        for interval in intervals:
            print (octave[interval])
        #print ("\r")
        
    
   # print get_notes('C', scales['minor'])

    """
    list_of_intervals = (scales.values())
    for intervals in list_of_intervals:
        #print get_notes('C', scale)
        for single_interval in intervals:
            print single_interval
    print "\r"
    """

#print get_notes('C', scales['minor'])

# creat a list of notes found in the song
# Start with the first scale (major)
# Iterate through all the keys in that scale. If a note is not in the key/scale, remove it from the list of potential scales
# Repeat with the next scale.
    
# https://github.com/diegopenilla/PythonGuitar

