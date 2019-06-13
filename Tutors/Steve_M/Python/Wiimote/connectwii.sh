#!/bin/bash
sleep 1 # Wait until Bluetooth services are fully initialized
hcitool dev | grep hci >/dev/null
if test $? -eq 0 ; then
    wminput -d -c /home/pi/GlosLibCodeClub/Tutors/Steve_Martin/Python/Wiimote/winput.config 00:1C:BE:F1:B1:68 &
else
    echo "Blue-tooth adapter not present!"
    exit 1
fi
