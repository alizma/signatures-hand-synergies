import pandas as pd
import numpy as np
from normalizers import *

class Path():
    def __init__(self, vals, dims, reps=range(1, 7), norm_vals=True):
        self.vals = vals.reset_index(drop=True, inplace=False)
        self.dims = dims
        if norm_vals:
            self.vals = better_normalize(self.vals, reps, dims=self.dims)

class DB5Path(Path):
    def __init__(self, vals, exercise, repetition, dims=None):
        if dims is None:
            temp_dims = vals.shape[1] - 2
        else:
            temp_dims = dims
        super().__init__(vals, temp_dims)
        self.exercise = exercise
        self.repetition = repetition
    
    def naive_padding(self, length) -> np.array:
        tempdf = pd.DataFrame(np.random.standard_normal(size = (length, self.dims)))
        tempdf['stimulus'] = pd.Series(np.ones(length) * self.exercise)
        tempdf['repetition'] = pd.Series(np.ones(length) * self.repetition)
        return tempdf
    
    def get_windows(self, window_size, overlap, use_padding=False) -> np.array:
        """
        returns a list of dataframes
        """
        begin = 0
        ans = []
        n = len(self.vals)
        while(begin < n):
            if (begin + window_size < n):
                ans.append(self.vals[begin:begin + window_size])
            else:
                # need to pad it out
                if use_padding:
                    overflow = (n - begin) % window_size
                    ans.append(pd.concat([self.vals[begin:], self.naive_padding(window_size - overflow)], ignore_index=True))
                else:
                    pass  # other option is to drop the last bit
            begin += window_size - overlap
        return ans
    
    def downsample(self, window_size):
        samples = []
        shrink_factor = len(self.vals) // window_size
        for mod in range(shrink_factor):
            uncut = self.vals[self.vals.index % shrink_factor == mod].reset_index()
            if len(uncut) > window_size:
                uncut = uncut[:window_size]
            samples.append(uncut)
        return samples
    