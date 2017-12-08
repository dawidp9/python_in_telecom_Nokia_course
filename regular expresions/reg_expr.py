import re


def get_regural_expresion():
    return r"(\d+\.\d+[-]\s*\d+\.\d+)\s+sec\s*(\d+\.\d+)\s*MBytes\s*(\d+\.+\d+)\s*Mbits\Wsec\s*(\d+.\d+)\s*ms\s*(\d+)\W\s*(\d+)\s*\W(\d+[.]*\d*)"


def get_data():
    file_log = open("iperf_udp_server.log", "r")
    for line in file_log:
        matched = re.search(get_regural_expresion(), line)
        if matched:
            interval = matched.group(1)
            transfer = matched.group(2)
            bandwidth = matched.group(3)
            jitter = matched.group(4)
            lost = matched.group(5)
            total = matched.group(6)
            datagrams = matched.group(7)
            iperf_record = {'interval': interval,
                            'transfer': transfer,
                            'bandwidth': bandwidth,
                            'jitter': jitter,
                            'lost': lost,
                            'total': total,
                            'datagrams': datagrams}

    print iperf_record

get_data()