
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

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


def find_notes(scale):
    notes_strings = {i:0 for i in "EADGB"}
    # for every string 
    for key in strings.keys():
        # we create an empty list of indexes
        indexes = []
        for note in scale:
            # append index where note of the scale is found in
            ind = strings[key].index(note)
            indexes.append(ind)
            # because there are 20 frets, there are duplicate notes in the string
            if ind <= 7:
                # we must also append these to indexes
                indexes.append(ind+12)
        notes_strings[key] = indexes
    return notes_strings




def plot(key, intervals, night=True):
    scale = get_notes(key, intervals)
    # Plot Strings
    fig, ax = plt.subplots(figsize=(20,6))
    background = ['white', 'black']
    for i in range(1,7):
        ax.plot([i for a in range(22)])
    # Plotting Frets
    for i in range(1,21):
        if i == 12:
            ax.axvline(x=i, color='gray', linewidth=3.5)
            continue
        ax.axvline(x=i, color=background[night-1], linewidth=0.5)
    
    #ax.grid(linestyle='-', linewidth='0.5', color='black')
    ax.set_axisbelow(True)
    
    # setting height and width of displayed guitar
    ax.set_xlim([0.5, 21])
    ax.set_ylim([0.4, 6.5])
    ax.set_facecolor(background[night])
    to_plot = find_notes(scale)
    
    # ACHTUNG!!!
    for y_val, key in zip([1,2,3,4,5,6], 'EADGBE'):
        for i in to_plot[key]:
            font = 12
            x = i+0.5  # /figheight
            p = mpatches.Circle((x, y_val), 0.2)
            ax.add_patch(p)
            note = strings[key][i]
            # if note is root make it a bit bigger
            if note == scale[0]:
                font=14.5
            ax.annotate(note, (i+0.5, y_val), color='w', weight='bold', 
                            fontsize=font, ha='center', va='center')
                
    plt.title('_| _| _| _| _|'*16)
    plt.yticks(np.arange(1,7), ['E', 'A', 'D', 'G', 'B', 'E'])
    plt.xticks(np.arange(21)+0.5, np.arange(0,22))
    plt.show()    
    
    plot('G', scales['major'])
    