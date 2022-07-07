import sys
import os
import subprocess

subprocess.run(["pip","install","kraken"], shell=True)
subprocess.run(["pip","install","pysimplegui"], shell=True)
subprocess.run(["sudo","apt-get","install","python3-tk"],shell=True)