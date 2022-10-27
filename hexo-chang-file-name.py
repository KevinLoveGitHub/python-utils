import os
import re

path = '/Users/Kevin/Workspaces/Hexo/source/_posts'
new_path = '/Users/Kevin/Workspaces/Hexo/source/new_posts/'

for root, dirs, files in os.walk(path):
    for file in files:
        file_name = os.path.join(root, file)
        if not file_name.endswith('.md'):
            continue
        print(file_name)
        with open(file_name, 'r') as f:
            content = f.read()
            # print(content)
        time = re.findall('date: (.*?) ', content, re.S)[0]
        with open(new_path + time + '-' + file, 'w') as f:
            f.write(content)
