# SIMPWAGGEN
Simple Wagon File Generator for ORTS

This script will create a starting point for generic Open Rails Wagons (eg; USA Freight Cars) and will allow car definitions to be based on 'config.ini' settings.
The script will create the WAGON file from scratch and will be named according to the contents of the config file.  By default, it will create a wagon file for an unloaded car, but will create the loaded version when the passed the "--loaded" command line argument.

It will also allow you to use alternate config files by specifying '--config-path' followed by a full file path to the alternate config file.

This python 3 script was created mainly because I often create typo-graphical errors when I create these files from scratch.

Yes, you do need to install Python 3 to use the script.

And, I know its a silly piece of code... but I use it... so maybe somebody else will.

It's not finished... but works well enough to use at this point.  Handling Freight_Anim and Lights are a future goal and do not currently function.


