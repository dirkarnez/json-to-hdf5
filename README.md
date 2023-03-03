json-to-hdf5
============
### Notes
- It is better not to use hdf5 because:
  - it cannot be version controlled
  - prone to file corruption
  - costly to maintain + develop
- Alternatives
  - [ndjson](http://ndjson.org/)
- Otherwise
  - Try to write conversion logic ourselves (if the [CLI tools](jsontoh5.cmd) does not work)
    - [h5json Package — HDF5/JSON v1.2-dev](https://hdf5-json.readthedocs.io/en/latest/tools/h5json.html#cli-tools)

### Tools
- [HDFView 3.1.4](https://portal.hdfgroup.org/display/support/HDFView+3.1.4)

### Reference
- [【python】读取json文件数据并保存为HDF5文件_json文件转换hdf5__ether的博客-CSDN博客](https://blog.csdn.net/aaether/article/details/100805874)
- [cmselemental/hdf.py at main · MolSSI/cmselemental](https://github.com/MolSSI/cmselemental/blob/main/cmselemental/util/hdf.py)
- [python3 读取numpy和写入numpy到hdf5_农民小飞侠的博客-CSDN博客](https://blog.csdn.net/w5688414/article/details/90200752)
- [HDF5保存numpy读取numpy_hdf5 numpy_只取一勺的博客-CSDN博客](https://blog.csdn.net/qq_41736190/article/details/115140797)
