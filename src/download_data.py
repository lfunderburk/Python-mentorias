import os
cmd = 'url=https://bit.ly/2JbKmPs; filename=$(basename "$url"); wget "$url"'
os.system(cmd)