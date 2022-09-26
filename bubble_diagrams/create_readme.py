# get a list of all .html files in folder
from pathlib import Path
html_files = [f for f in Path('bubble_diagrams').glob('*.html') if f.is_file()]
# create a list of links
url_prefix = 'https://valrcs.github.io/latviesu_avizes_200/bubble_diagrams/'
links = [f'* [{f.stem}]({url_prefix}{f.name})' for f in html_files]
# write to readme.md
with open('bubble_diagrams/README.md', 'w') as f:
    f.write('\n'.join(links))

# append to ROOT readme.md
with open('README.md', 'a') as f:
    f.write('\n## Bubble diagrams\n')
    f.write('\n'.join(links))

