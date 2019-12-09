#!/bin/sh
sudo apt install octave -y
cd
cp /usr/share/librtimulib-utils/RTEllipsoidFit ./ -a
cd RTEllipsoidFit
RTIMULibCal
