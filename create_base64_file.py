import base64
src_file = open("LLATRON.S",'r')
data = src_file.read()
encoded_bytes = base64.b64encode(data.encode('utf-8'))
encoded_str = encoded_bytes.decode('utf-8')
output_file = open("LLATRON.S.b64",'w')
output_file.write(encoded_str)
output_file.flush()

