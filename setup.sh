#     Copyright 2018 Joshua Danielpour

#    This file is part of WordSimilarity.

#    WordSimilarity is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    WordSimilarity is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#  along with WordSimilarity.  If not, see <http://www.gnu.org/licenses/>.
    

#!/bin/bash

source bin/activate

for i in "$@"
do
case $i in
    --macos*)
    os="macos"
    shift # past argument=value
    ;;
    --linux*)
    os="linux"
    shift # past argument=value
    ;;
    *)
    echo "Enter operating system, (I don't work with windows)"     # unknown option
    ;;
esac
done

bin/pip install sklearn opencv-python numpy pandas sip
if [$os -eq "macos"];
	curl -o PyQt4.tar.gz --tlsv1.2 https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_mac-4.12.1.tar.gz
if [$os -eq "linux"];
	curl -o PyQt4.tar.gz --tlsv1.2 https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_mac-4.12.1.tar.gz

tar -xfz PyQt4.tar.gz
if [-e PyQt4/configure-ng.py];
	python PyQt4/configure-ng.py
else;
	python PyQt4/configure.py

make -C PyQt4
make -C PyQt4 install

javac TextToGraphics.java
bash makeCharacters
deactivate