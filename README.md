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
