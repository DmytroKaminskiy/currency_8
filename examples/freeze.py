import subprocess

import f


cmd = ['pip', 'freeze']
command = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# open('ex.txt', 'w').write(command.stdout.decode())

# super(), ClassName.__mro__
