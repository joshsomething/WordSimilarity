# WordSimilarity
> Demonstrating a new technique against spoofed phishing.


[![GitHub last commit](https://img.shields.io/github/last-commit/joshsomething/WordSimilarity.svg)](https://github.com/joshsomething/WordSimilarity/commits)
[![GitHub issues](https://img.shields.io/github/issues/joshsomething/WordSimilarity.svg)](https://github.com/joshsomething/WordSimilarity/issues)
[![GitHub stars](https://img.shields.io/github/stars/joshsomething/WordSimilarity.svg)](https://github.com/joshsomething/WordSimilarity/stargazers)
[![GitHub search hit counter](https://img.shields.io/github/search/joshsomething/WordSimilarity/goto.svg)](https://github.com/joshsomething/WordSimilarity)
[![GitHub top language](https://img.shields.io/github/languages/top/joshsomething/WordSimilarity.svg)]()

## Introduction:
This project is an experiment to rate the similarity between text, with the
goal of using this to detect the likelyness of a message being spoofed in a specific way. This project focuses on phishers that don’t *completely* disguise as someone else (to avoid DMARC et al), but make it easy for their messages to be **mistaken as coming from someone else**
(as in the names and addresses are similar).

The overall purpose is to utilize machine learning technologies to better approach spoofing, 
a technique used in phishing.
Many cyber crimes are instances of [phishing](https://blog.barkly.com/phishing-statistics-2016), 
the goal of this project is to better demonstrate the possibility 
of machines being able to better adapt to threats against the human component of security. 
The desired result of this project would be the increased development of
security technologies based on or inspired by this work.

### Installing da software:

#### Mac Os (work in progress):
* [python3](https://www.python.org/downloads/)
* virtualenv: `pip install virtualenv`

#### Gnu/Linux: 

* debian: `sudo apt-get install python3 libxext-dev python3-pip virtualenv python3-pyqt4 fonts-arkpandora`
  * To build qt4: `sudo apt-get install build-essential libxext-dev python-qt4-dev python3-pip virtualenv libqt4-dev fonts-arkpandora`
* ubuntu (not tested): `sudo apt-get install build-essential libext-dev python3 python3-pip virtualenv qt4-dev-tools libqt4-dev fonts-arkpandora`
* fedora (under development):


### Setting the stuff up: 
* `cd path/to/WordSimilarity`
* `virtualenv —-system-site-packages -—always-copy -p python3 $(pwd)`
* `bash setup.sh --macos` if macos
* Linux:
  * If you preinstalled pyqt4: `bash setup.sh --linux —-premade`
  * Otherwise: `bash setup.sh --linux`

### Using the software:
After following the instructions above, to properly use the code in this directory:
* Before you start running the software here, run `source bin/activate` from the WordSimilarity folder.
* After using the software here, run `deactivate`.
* All of these instructions assume you are running commands from this directory (WordSimilarity).
* I would recommend you go through the folders in this order: [charSim](charSim/README.md), then [wordSim](wordSim/README.md).
  * Don't worry about the stuff in the characters folder (unless you want to look at the code there).
* Read the README.md files in the two folders to find out how to run the software.

### Extra stuff:
Author - Josh Danielpour.

All of the code here is distributed under the Gnu Affero General Public License (wow, that's long!)

See [COPYING](COPYING) for more information.

### Contributing:
1. [Fork me!](https://github.com/joshsomething/WordSimilarity/fork)
2. Commit & push your changes to your fork.
3. Create a Pull Request (in a timely and organized manner).
4. [See more](CONTRIBUTING.md).

<dl>
<br></br>
<br></br>
<samp>This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.</samp>
<samp> To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
</samp>
</dl>
