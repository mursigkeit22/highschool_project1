import sys
from time import gmtime, strftime

print(sys.executable)
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
sys.stdout.flush()