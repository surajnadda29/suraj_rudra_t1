import sys
import numpy
import pandas
import matplotlib
import scipy

print("RE-T1 Python Environment Test")
print("-----------------------------")

print("Python:", sys.version.split()[0])
print("NumPy:", numpy.__version__)
print("Pandas:", pandas.__version__)
print("Matplotlib:", matplotlib.__version__)
print("SciPy:", scipy.__version__)

print("-----------------------------")
print("Environment OK")