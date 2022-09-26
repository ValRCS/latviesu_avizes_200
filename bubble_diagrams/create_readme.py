# get a list of all .html files in folder
from pathlib import Path
html_files = [f.name for f in Path('bubble_diagrams').glob('*.html') if f.is_file()]
# create a list of links
url_prefix = 'https://valrcs.github.io/latviesu_avizes_200/bubble_diagrams/'
links = [f'* [Link]({url_prefix}{f})' for f in html_files]
# write to readme.md
with open('bubble_diagrams/README.md', 'w') as f:
    f.write('\n'.join(links))

