import iisignature
import numpy as np

DEPTH = 4

big = np.random.uniform(size = (1000, 22))
bigsig = iisignature.sig(big, DEPTH)


s = iisignature.prepare(22, DEPTH)
biglogsig = iisignature.logsig(big, s)

print("big shapes:")
print(bigsig.shape, biglogsig.shape)
small = np.random.uniform(size = (1000, 5))
smallsig = iisignature.sig(small, DEPTH)


s = iisignature.prepare(5, DEPTH)
smalllogsig = iisignature.logsig(small, s)
print("small shapes:")
print(smallsig.shape, smalllogsig.shape)