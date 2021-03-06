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

# bin/activate script causes set -u to get mad,
# 'unset' that param in bin/activate:
check=$(cat bin/activate | grep "set +u")
if [ -z check ]; then
	sed -i.bak '1i''set +u' bin/activate
fi

set -e
set -u
set -o pipefail
source bin/activate

buildPyQt=1

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
    -—premade*)
    buildPyQt=0
    shift
    ;;
    *)
    echo "Enter operating system, (I don't work with windows)"     # unknown option
    ;;
esac
done

bin/pip3 install sklearn opencv-python numpy pandas sip pillow scipy

# Decide if PyQt library needs to be
# built:

if [ $buildPyQt -eq 1 ]; then


file=""
sipfile="sip-4.19.8"

if [ $os = "macos" ]; then
	file="PyQt4_gpl_mac-4.12.1"
	curl -o PyQt4.tar.gz --tlsv1.2 "https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/${file}.tar.gz"
	curl -o "${sipfile}.tar.gz" --tlsv1.2 "https://sourceforge.net/projects/pyqt/files/sip/${sipfile}/${sipfile}.tar.gz"
fi

if [ $os = "linux" ]; then
	file="PyQt4_gpl_x11-4.12.1"
	wget -O PyQt4.tar.gz "https://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/${file}.tar.gz"
	wget -O "${sipfile}.tar.gz" "https://sourceforge.net/projects/pyqt/files/sip/${sipfile}/${sipfile}.tar.gz"
fi

tar -xzf PyQt4.tar.gz

tar -xzf "${sipfile}.tar.gz"
rm PyQt4.tar.gz
rm "${sipfile}.tar.gz"

cd $sipfile
python3 "configure.py"
make
make install
cd ..

cd $file
python3 "configure.py"

make
make install
cd ..

fi # End of building stuff.

bash makeCharacters
deactivate
