#!/usr/bin/bash

for each in {0000..10000}
do
	wget "https://www.larvalabs.com/cryptopunks/cryptopunk$each.png" 
done
