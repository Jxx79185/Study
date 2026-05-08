#windows命令
#dir:查看某一个文件夹下的子文件名与子文件夹名
#ipconfig：查看本地网卡的ip信息
#tasklist：查看运行的进程

#linux命令：
#ls
#ifconfig
#ps aux
import os
os.system('dir 试验')

import subprocess
result=subprocess.run('dir /w',
                    shell=True,
                    capture_output=True,
                )
print(result.stdout)



