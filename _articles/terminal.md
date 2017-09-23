---
title: Terminal Commands
date: 2017-09-23
layout: article
---

# Terminal Commands

Terminal commands specific for macOS and Linux.

Open a file from the terminal (macOS):

```bash
open fileA.txt            # open a file in its default application
open -a safari fileA.txt  # opens with the specified application
open -R fileA.txt         # selects the file in a Finder window
```

Mount and unmount a volume (macOS):

```bash
hdiutil attach Secure.dmg       # mount a dmg volume named "Secure.dmg"
hdiutil detach /Volumes/Secure  # unmount a volume named "Secure"
```

My preferred permissions for folders and files:

```bash
chmod 755   # folder permissions
chmod 644   # file permissions
```

Copy all the files in a folder into another folder:

```bash
cp -R folderA/. folderB
```

List the contents of a folder or of a specified folder:

```bash
ls
ls folderA/
```

Rename a file or folder:

```bash
mv oldname.txt newname.txt
mv oldfolder/ newfolder/
```

Remove a folder that already contains files:

```bash
rm -rf folderA/
```

