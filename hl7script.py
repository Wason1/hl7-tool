import hl7
from hl7.datatypes import parse_datetime

with open(r'H:\txt\train_adt_07-02-1740.txt', 'r') as f:
    read_data = f.read()

read_data2 = read_data.replace('\n', '\r')

i = hl7.parse(read_data2)

len(i[0])
len(i)

str(i)