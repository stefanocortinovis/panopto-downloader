"""
Built on Python 3.8.2
"""
import argparse
import xml.etree.ElementTree as xml
import urllib.request as urllib
from pathlib import Path
from tqdm import tqdm


class TqdmUpTo(tqdm):
    def __init__(self, title):
        super(TqdmUpTo, self).__init__(desc=f"Downloading {title}", total=9e9, unit="B", unit_scale=True)
        self.n = 0

    def __call__(self, block, block_size, total_size=None):
        self.update_to(block, block_size, total_size)

    def update_to(self, block, block_size, total_size=None):
        if total_size is not None:
            self.total = total_size
        self.update(block * block_size - self.n)
        self.n = block * block_size


parser = argparse.ArgumentParser(description='Download videos from Panopto.')
parser.add_argument('url', metavar='URL', type=str, help='URL from "Subscribe to RSS" button')
parser.add_argument('dest', metavar='DEST', type=str, nargs='?', default='./', help='Directory where to save videos')
args = parser.parse_args()

manifest = args.url
outdir = Path(args.dest)
if not outdir.is_dir():
    raise FileNotFoundError(f'No such file or directory: {outdir}')

# Download manifest
urllib.urlretrieve(manifest, outdir/'manifest.xml')

# Parse XML
e = xml.parse(outdir/'manifest.xml').getroot()

# Download items
for item in e.find('channel'):
    if item.tag == "item":
        title = item.find('title').text.replace("/", "-")
        url = item.find('guid').text
        urllib.urlretrieve(url, outdir/f"{title}.mp4", reporthook=TqdmUpTo(title))
