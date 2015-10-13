#!/usr/bin/env python
# encoding: utf-8

import re
import subprocess
import time
import json


def get_temperatures(disks):
    sensors = subprocess.check_output("sensors")
    temperatures = {match[0]: float(match[1]) for match in re.findall("^(.*?)\:\s+\+?(.*?)°C", sensors, re.MULTILINE)}
    for disk in disks:
        output = subprocess.check_output(["smartctl", "-A", disk])
        temperatures[disk] = int(re.search("Temperature.*\s(\d+)\s*(?:\([\d\s]*\)|)$", output, re.MULTILINE).group(1))
    return temperatures


def main():
    while True:
        print json.dumps(get_temperatures(("/dev/sda", "/dev/sdc")))
        time.sleep(20)


if __name__ == "__main__":
    main()
