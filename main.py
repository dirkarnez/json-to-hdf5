import h5py
import numpy as np

# import json
# data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
# data2 = json.dumps(data)
# print(data2)

with h5py.File('name.hdf5','w', libver='latest') as f:
    grp = f.create_group("my-group")
    grp.create_dataset("my-dataset", data=np.arange(100).reshape((10,10)))