#!/bin/sh

desktop=/home/pi/Desktop
gloslib=/home/pi/GlosLibCodeClub

#Coders
#======
ln -sfn $gloslib/Coders $desktop/Coders 

#Exercises
#=========
exercises=$gloslib/Exercises

#1 Scratch
#---------
scratch=$exercises/Scratch
ln -sfn $scratch/Beginner/     $desktop/Scratch\ Beginner
ln -sfn $scratch/Intermediate/ $desktop/Scratch\ Intermediate
ln -sfn $scratch/Advanced/     $desktop/Scratch\ Advanced

#2 Python
#--------
python=$exercises/Python
ln -sfn $python/Beginner/      $desktop/Python\ Beginner 
ln -sfn $python/Intermediate/  $desktop/Python\ Intermediate 
ln -sfn $python/Advanced/      $desktop/Python\ Advanced

#3 Javascript
#------------
javascript=$exercises/Javascript
ln -sfn $javascript/              $desktop/Javascript
#ln -sfn $javascript/Beginner/     $desktop/Javascript\ Beginner
#ln -sfn $javascript/Intermediate/ $desktop/Javascript\ Intermediate
#ln -sfn $javascript/Advanced/     $desktop/Javascript\ Advanced

#4. HTML CSS
#-----------
htmlcss=$exercises/HTML-CSS
ln -sfn $htmlcss/                 $desktop/HTML\ CSS
#ln -sfn $htmlcss/Beginner/        $desktop/HTML\ CSS\ Beginner
#ln -sfn $htmlcss/Intermediate/    $desktop/HTML\ CSS\ Intermediate
#ln -sfn $htmlcss/Advanced/        $desktop/HTML\ CSS\ Advanced

#Help
#====

ln -sfn $exercises/Help $desktop/Help

exit
