from rrc_asn_extractor import exctract_asn
from concurrent.futures import ProcessPoolExecutor
import time
import os.path

start_time = time.time()
filenames = [os.path.join('data', 'rrc_v%d.txt' % ver) for ver in range(8, 14+1)]

with ProcessPoolExecutor(len(filenames)) as proc_pool:
    proc_pool.map(extract_asn, filenames)

duration = time.time() - start_time
print "ASN.1 processing duration = %.3f seconds" % duration