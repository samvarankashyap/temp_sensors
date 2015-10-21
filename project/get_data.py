import sys
import pprint
import os
from subprocess import Popen, PIPE
from datetime import datetime

#initialise table
"""
ID   | Name            | Type                     | Reading    | Units | Event
64   | POST Error      | System Firmware Progress | N/A        | N/A   | N/A
112  | Memory ECC      | Memory                   | N/A        | N/A   | N/A
160  | ACPI State      | System ACPI Power State  | N/A        | N/A   | 'S0/G0'
208  | PCI Reset       | Module/Board             | N/A        | N/A   | 'OK'
256  | CPU0 Fan R0     | Fan                      | 10822.51   | RPM   | 'OK'
320  | CPU1 Fan R0     | Fan                      | 10822.51   | RPM   | 'OK'
384  | Rear Sys Fan1   | Fan                      | 8210.18    | RPM   | 'OK'
448  | Front Sys Fan1  | Fan                      | 8818.34    | RPM   | 'OK'
512  | System 12V      | Voltage                  | 11.98      | V     | 'OK'
576  | System 5V       | Voltage                  | 5.05       | V     | 'OK'
640  | System 3.3V     | Voltage                  | 3.29       | V     | 'OK'
704  | System AUX 3.3V | Voltage                  | 3.27       | V     | 'OK'
768  | System AUX 2.5V | Voltage                  | 2.49       | V     | 'OK'
832  | System AUX 1.8V | Voltage                  | 1.82       | V     | 'OK'
896  | System AUX 1.2V | Voltage                  | 1.22       | V     | 'OK'
960  | System -12V     | Voltage                  | -14.40     | V     | 'OK'
1024 | CPU0 VCCP       | Voltage                  | 1.07       | V     | 'OK'
1088 | CPU1 VCCP       | Voltage                  | 1.08       | V     | 'OK'
1152 | CPU0 Dmn 0 Temp | Temperature              | 28.00      | C     | 'OK'
1216 | CPU0 Dmn 1 Temp | Temperature              | 28.50      | C     | 'OK'
1280 | CPU1 Dmn 0 Temp | Temperature              | 30.50      | C     | 'OK'
1344 | CPU1 Dmn 1 Temp | Temperature              | 29.00      | C     | 'OK'
1408 | DIMM Rear Temp  | Temperature              | 0.00       | C     | 'OK'
1472 | Inlet Amb Temp  | Temperature              | 19.00      | C     | 'OK'
1536 | PCI Amb Temp    | Temperature              | 0.00       | C     | 'OK'
"""
# getting the data and converting into json 
output = Popen(["ipmi-sensors", "--ipmimonitoring-legacy-output"], stdout=PIPE).communicate()[0]
print output
time_stamp = str(datetime.now())
fd = open("data.txt","a")
fd.write("\n"+time_stamp+"\n")
fd.write(str(output))
fd.close()
output = output.split("\n")
print output
sensors_list = []
pp = pprint.PrettyPrinter(indent=4)
#Record ID | Sensor Name | Sensor Group | Sensor Units | Sensor Reading
for line in output[1:-2]:
    line = line.split("|")
    sensors_json = {}
    sensors_json["record_id"]=line[0]
    sensors_json["sensor_name"]=line[1]
    sensors_json["sensor_group"]=line[2]
    sensors_json["sensor_units"]=line[3]
    sensors_json["sensor_reading"]=line[4]
    pp.pprint(sensors_json)
    sensors_list.append(sensors_json)
