WordSimilarity —— Demonstrating a new technique against spoofed phishing.
----

### Introduction:
This project is an experiment to rate the similarity between text, with the
goal of using this to detect the likelyness of a message being spoofed 
(by comparing names and addresses).

The overall purpose is to utilize machine learning technologies to better approach spoofing, 
a technique used in phishing.
Many cyber crimes are instances of [phishing](https://blog.barkly.com/phishing-statistics-2016), 
the goal of this project is to better demonstrate the possibility 
of machines being able to better adapt to threats against the human component of security. 
The desired result of this project would be the increased development of
security technologies based on or inspired by this work.

### Getting da software:
* python: [python3](https://www.python.org/downloads/)
* java:
  * windows and macos: [openjdk](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
  * linux: 
    * debian: `sudo apt-get install openjdk-8-jdk openjdk-8-jre-headless`
    * ubuntu: `sudo add-apt-repository ppa:openjdk-r/ppa && sudo apt-get update && sudo apt-get install openjdk-7-jdk`
    * fedora: `sudo dnf install java-1.8.0-openjdk-devel java-1.8.0-openjdk`
* virtualenv: `pip install virtualenv`
* qt: 
  * linux:
    * debian: `sudo apt-get install python-qt4 libxext-dev build-essential`
    * ubuntu: `sudo apt-get install python-qt4 qt4-dev-tools libxext-dev build-essential`

### Setting the stuff up: 
* `virtualenv $(pwd)`
* `bash setup.sh --macos` if macos
* `bash setup.sh --linux` if linux

### Using the software:
After following the instructions above, to properly use the code in this directory:
* Before you start running the software here, run `source bin/activate` from the WordSimilarity folder.
* After using the software here, run `deactivate`.
* All of these instructions assume you are running commands from this directory (WordSimilarity).
* I would recommend you go through the folders in this order: charSim, then wordSim.
  * Don't worry about the stuff in the characters folder (unless you want to look at the code there).
* Read the README.md files in the two folders to find out how to run the software.

<dl>
<p style="font-size:16px">This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.</p>
<p style="font-size:16px">To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.</p>
</dl>