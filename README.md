# Panopto Downloader

CLI tool to download videos from Panopto. Adapted from [this gist](https://gist.github.com/FrederickGeek8/eb7301eeef3103948a0cc74db9fbf4e9). Created for CMU [11-785](https://deeplearning.cs.cmu.edu/).

## Usage

```console
foo@bar:~$ python3 panopto_downloader.py -h

Download videos from Panopto.

positional arguments:
  URL         URL from "Subscribe to RSS" button
  DEST        Directory where to save videos

optional arguments:
  -h, --help  show this help message and exit
```