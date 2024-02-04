import numpy as np

def mots(signal):
    signal = np.array(signal)
    x1 = signal[:-2]
    x2 = signal[1:-1]
    x3 = signal[2:]

    mot = 1*(x1 > x2) * (x2 > x3) + 2*(x1 > x3) * (x3 > x2) + 3*(x2 > x1) * (x1 > x3) + 4*(x3 > x1) * (x1 > x2) + 5*(x2 > x3) * (x3 > x1) + 6*(x3 > x2) * (x2 > x1)

    return mot

def motifs(array):
    xmotif = np.apply_along_axis(mots,-1,array)
    return xmotif





    
