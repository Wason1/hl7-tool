import hl7apy

with open(r'H:\txt\train_adt_07-02-1740.txt', 'r') as f:
    read_data = f.read()

#read_data.replace('\n', '\r')



from hl7apy.parser import parse_message

message = parse_message(read_data)