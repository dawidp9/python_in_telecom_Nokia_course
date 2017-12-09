import re


def get_regural_expresion():
    return r"(\d+\.\d+[-]\s*\d+\.\d+)\s+sec\s*(\d+\.\d+)\s*MBytes\s*(\d+\.+\d+)\s*Mbits\Wsec\s*(\d+.\d+)\s*ms\s*(\d+)\W\s*(\d+)\s*\W(\d+[.]*\d*)"


def get_record_from_line(line):
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
        return iperf_record
    return None


def get_data_from_file(file_name):
    file_log = open(file_name, "r")
    record_list = list()
    for line in file_log:
        record = get_record_from_line(line)
        if record is not None:
            record_list.append(record)
    file_log.close()
    return record_list


if __name__ == "__main__":
    for record in get_data_from_file("iperf_udp_server.log"):
        print record

