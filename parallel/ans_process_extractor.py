from rrc_asn_extractor import exctract_asn
from multiprocessing import Process
import os.path
import time


class Extractor(Process):
    def __init__(self, filename):
        super(Extractor, self).__init__()
        self.filemane = filename

    def run(self):
        exctract_asn(self.filemane)


started_process = []

start_time = time.time()
for version in range(8, 14+1):
    filename = os.path.join('data', 'rrc_v%d.txt' % version)
    task = Extractor(filename)
    task.start()
    started_process.append(task)

for task in started_process:
    task.join()

duration = time.time() - start_time
print "ASN.1 processing duration = %.3f seconds" % duration