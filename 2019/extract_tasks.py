import os
import re
import urllib.request
from bs4 import BeautifulSoup


def remove_tags(s):
    pattern = re.compile('<.*?>')
    return re.sub(pattern, '', str(s))


current_dir = os.path.dirname(os.path.realpath(__file__))

# only extracts the tasks, the resources has to be downloaded after auth
# the author asked not to automate stuff too much, therefore I downloaded
# those manually

# also mind you, some of the tasks had multiple parts which gets unlocked if
#  you submit a correct answer to the first. this script only pulls the
# first parts of the tasks
for i in range(1, 25):
    with urllib.request.urlopen(
            f'https://adventofcode.com/2019/day/{i}', ) as response:
        if response.code == 200:
            html = response.read()
            soup = BeautifulSoup(html, features='html.parser')
            task = remove_tags(soup.article)
            if not os.path.exists(f'{current_dir}\\d{i}'):
                os.makedirs(f'{current_dir}\\d{i}')
            with open(f'{current_dir}\\d{i}\\task.txt', 'w') as f:
                f.write(task)
