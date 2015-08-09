# VoiceControlledScreen
Create a voice controlled display screen

There are a number of dependencies for this example. Make sure you have Alex T's repos sourced. Instructions here: 

http://alextgalileo.altervista.org/edison-package-repo-configuration-instructions.html

Then, install the necessary library dependencies:

$ opkg install libjack
$ opkg install --nodeps jack-dev
$ opkg install libportaudio-dev
$ opkg install flac-dev 
$ opkg install git
$ opkg install numpy

You'll also need mraa 

$ echo "src mraa-upm http://iotdk.intel.com/repos/1.1/intelgalactic" > /etc/opkg/mraa-upm.conf
$ opkg update
$ opkg install libmraa0

Install pip

$ wget https://bootstrap.pypa.io/get-pip.py
$ python get-pip.py

Install the python libraries

$ pip install --allow-external pyaudio --allow-unverified pyaudio pyaudio
$ pip install SpeechRecognition

And finally, either git clone the ILI9341 repo or pull the base library file. 

$ git clone https://github.com/smoyerman/EdisonILI9341.git

OR

$ wget https://raw.githubusercontent.com/smoyerman/EdisonILI9341/master/ILI9341.py

Make sure this file is in the same directory as the ILI9341.py file so that it sources it properly.
