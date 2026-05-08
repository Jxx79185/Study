import struct
import json

res=struct.pack('q',128000000000)
res1=struct.unpack('q',res)
print(res)
print(res1[0])

obj=struct.unpack('q',res)
print(obj)

header_dic={'filename':"xxx.txt",
                        'md5':'xxdxxx',
                        'total_size':8888888888888888888888888888888888888888}
            
header_json=json.dumps(header_dic)
print(type(header_json))
header_bytes=header_json.encode('utf-8')