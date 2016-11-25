#!/bin/sh

SOURCE_DIR=$1
DEST_DIRS="Pi1 Pi2 Pi3 Pi4 Pi5 Pi6 Pi7"

echo "Copying Examples in $SOURCE_DIR to Pi Directories"
for DEST_DIR in $DEST_DIRS; do
	if [ ! -d "$DEST_DIR" ]; then
		mkdir $DEST_DIR
	fi

	echo "Copying for RPi $DEST_DIR"
	cp -R $SOURCE_DIR $DEST_DIR/
done

find Pi*/
