"""
Tool to be used during parallelism exercises
    Extracts ASN.1 entries from different versions of LTE RRC standard

:author: 'Grzegorz Latuszek (Nokia)'
"""
import time


def exctract_asn(filename, show=True):
    with open(filename) as raw_rrc_standard:
        asn_output_filename = filename + ".asn1"
        with open(asn_output_filename, 'w') as asn1_rrc_standard:
            start_collecting_asn = False
            for line in raw_rrc_standard:
                if '-- ASN1START' in line:
                    start_collecting_asn = True
                elif '-- ASN1STOP' in line:
                    start_collecting_asn = False
                elif start_collecting_asn:
                    time.sleep(0.001)
                    asn1_rrc_standard.write(line)
    if show:
        print("done: {0}".format(asn_output_filename))
if __name__ == '__main__':
    import os.path
    import time
    start_time = time.time()
    for version in range(8,14+1):
        filename = os.path.join('data', 'rrc_v%d.txt' % version)
        exctract_asn(filename)
    duration = time.time() - start_time
    print "ASN.1 processing duration = %.3f seconds" % duration