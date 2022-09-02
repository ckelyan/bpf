# BPF, binary pattern finder
## Project inspired by a [Stand-up Maths video](https://www.youtube.com/watch?v=dET2l8l3upU)

## How to
### 1. Convert
Convert your input digits into a usable file using converter.py
```py
# line 21
with open('path/to/file.txt', 'r') as f:
```
or leave it as-is; the first 1 million digits of PI are being used by default.

### 2. Create your pattern
To do so, you can either do it manually (see line 6 of main.py for the format) or use my [interactive pattern creator](https://github.com/ckelyan/pcreate).

### 3. Configure the program
In main.py, change the SEP and FILENAME constant if you changed them in converter.py.

### 4. Launch main.py and watch.
