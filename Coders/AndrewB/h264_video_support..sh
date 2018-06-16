sudo apt-get install -y gpac
MP4Box -add video.h264 video.mp4

#VLC Player:
sudo apt install vlc

#OMX Player:
sudo apt install omxplayer

#Experimental direct capture feature

#If you are running VNC Server on a Raspberry Pi without a GUI and would like to try the experimental direct capture feature,
#add the following parameter settings to /root/.vnc/config.d/vncserver-x11:

#CaptureTech=raspi
#ExperimentalRaspiCapture=1
#ServerPreferredEncoding=JPEG

#Then restart VNC Server in Service Mode with:
#sudo systemctl restart vncserver-x11-serviced