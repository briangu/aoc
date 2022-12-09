from klongpy import KlongInterpreter
from klongpy.backend import np

klong = KlongInterpreter()
klong['I'] = lambda x,y: np.intersect1d(x,y)
klong('.l("3b.kg")')
