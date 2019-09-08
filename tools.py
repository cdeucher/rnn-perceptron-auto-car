import numpy as np
import os.path

class oTool():

    def save(self, file, q_table):
        np.savetxt('data/'+file, q_table)

    def read(self, file):
        if os.path.exists('data/'+file) :
            data = np.loadtxt('data/'+file)
        else :
            data = []
        return data           