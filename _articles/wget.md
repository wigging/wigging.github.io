---
title: Wget to Download Files
date: 2017-09-23
layout: article
---

# Wget to Download Files

GNU Wget is a free software package for retrieving files using HTTP, HTTPS and
FTP. It is a non-interactive commandline tool that can be called from scripts,
cron jobs, terminals, etc. The tool is useful for downloading all images or
PDFs from a web page.

The terminal command below demonstrates downloading all jpg and png images from
the Ray Wenderlich home page and saving into a folder named "ray".  The `-nd`
option will save all files to the current folder without creating subfolders.
Recursive retrieving is turned on by the `-r` option. The directory to save the
files is declared with the `-P` statement. To accept files of a certain type,
use the `-A` option.

```bash
wget -nd -r -P ./ray -A jpg,png http://www.raywenderlich.com
```

The next command will download all PDFs on a web page and place them into a 
folder named "docs".

```bash
wget -nd -r -P ./docs -A pdf http://www.website.com
```

## Further Reading

[GNU Wget](https://www.gnu.org/software/wget/) introduction and documentation  
[Install and 
configure](http://coolestguidesontheplanet.com/install-and-configure-wget-on-os-x/) 
Wget on OS X  

