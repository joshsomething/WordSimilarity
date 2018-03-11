WordSimilarity —— Important Instructions:
----

###Getting da software:
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
 * windows: `curl https://download.lfd.uci.edu/pythonlibs/n1rrk3iq/PyQt4-4.11.4-cp35-cp35m-win_amd64.whl`

###Setting the stuff up: 
* `virtualenv $(pwd)`
* `bash setup.sh --macos` if macos
* `bash setup.sh --linux` if linux

###Using the software:
After following the instructions above, to properly use the code in this directory:
* Before you start running the software here, run `source bin/activate` from the WordSimilarity folder.
* After using the software here, run `deactivate`.
* All of these instructions assume you are running commands from this directory (WordSimilarity).
* I would recommend you go through the folders in this order: charSim, then wordSim.
 * Don't worry about the stuff in the characters folder (unless you want to look at the code there).
* Read the README.md files in the two folders to find out how to run the software.