class CCD231(object):
    def __init__(self):
        # defaults from datasheet
        # pixel size assuming square pixels [mu.m]
        self.px = 15.  # microm
        self.py = 15.  # microm
        # efficiency to quantise photons to electrons
        # quatisation efficiency 0<=Q<=1
        self.qe = 0.9  # quantisation efficiency
        # charge transfer efficiency 0<=e<=1
        self.cte = 0.99999  # charge transfer efficiency
        # thermal dark current [e/p/s]
        # in data sheet give as [e/p/hr]
        self.dark = 0.000152778  # dark current [e/p/s]
        # time independent readout noise [e/p]
        self.read = 2.8  # readout noise [e/p]

# -fin-
