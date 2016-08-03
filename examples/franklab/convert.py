#!/usr/bin/env python3

import argparse 
import scipy.io as sio

parser = argparse.ArgumentParser("usage: %(prog)s pos.mat spikes.mat out")
parser.add_argument("pos", help="position data")
parser.add_argument("spikes", help="spike data")
parser.add_argument("out", help="spike data")

args = parser.parse_args()

# index last element -- this is how Frank lab stores data (data always stored in day number of array)
pos = sio.loadmat(args.pos)['pos'][0][-1][0]


pos[0].dtype.names # struct variable names


epoch_struct = pos[0][0][0] # data for first epoch - 

pos[6][0][0] # data for seventh epoch

arg = epoch_struct[0]
descript = epoch_struct[1]
fields = epoch_struct[2]
data = epoch_struct[3] 
'''
>> print epoch_struct.shape # dimensions of data
(35982, 5)     
# 35982 samples, 5 variables (variable names given in "fields")
'''
cmperpixel = epoch_struct[4]



'''
    >> load bonpos03
    pos  -- variable with position data
        -- data will be in cell 3 (cell 1-2 will be empty)
    
    pos{3} -- a cell array
           -- 1x7 cell array -- one for each epoch
           
    
    pos{3}{1} -- data from first epoch of recording (location over time in pixel coordinates)
              -- MATLAB Struct 
                    - arg - arguments to the MATLAB function that generated this data set
                    - descript - not useful
                    - fields - a space-delimited string identifying the columns/variables in 'data'
                    - data - this is actual data
                    - cmperpixel (cm per pixel) - useful for converting from pixels to cm
'''

spikes = sio.loadmat(args.spikes)['spikes']
'''
    >> load bonspikeso3
    spikes - variable with spike times (post sorted)
           - data will be in  cell 3
    
    spikes{3} -- a cell array of 1x29 cells
    
    spikes{3}{2} --  each cells represents data from a single tetrode
    
    spikes{3}{2}{1} -- cell array of structures
                    -- each structure corresponds to a neuron
    
    
    spikes{3}{2}{1}{1} -- a MATLAB structure
                       
                        - data -- the data
                        - descript  -- not useful
                        - fields -- almost-space-delimited string specifying fields in data
                        - depth -- not useful to me
                        - spikewidth -- not useful to me
                        - timerange -- start and end units of 100 microseconds (10k per second)
'''

