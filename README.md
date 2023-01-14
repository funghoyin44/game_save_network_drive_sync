# game_save_network_drive_sync
>File Explaination:

main.py -> User Interface and Logic<br />
Database.py -> Location of network drive and local game save<br />
Logic.py -> Logic of uploading and downloading<br />

>Setting Up The Path

[Database.py] <br />
```remote_drive = "I:"``` //Set the assigned letter of your intended network drive<br />
```username = "PC"```  //Set the name of your backup file (Will be added to your backup folder)<br />
```
Blue_Reflection_Path = "\"C:\\Users\\Fung\\Documents\\KoeiTecmo\\BLUE REFLECTION\""
Blue_Reflection_Remote = "\"{}\\Blue Reflection\"".format(remote_drive)
```
//Setting Up Game Path<br />
Here I use blue reflection as an example. ```Blue_Reflection_Path``` is the local path of my game save. ```Blue_Reflection_Remote``` is the path of my intended uplaod location.
You don't need the drive letter cause it is formatted with ```remote_drive"```. For example if your remote path is ```"I:\BLUE REFLECTION"```, then you just need ```"{}\BLUE REFLECTION\".format(remote_drive)```.
Remember to deal with \ in a string or it will cause error. For example, the above path should be ```"\"{}\\BLUE REFLECTION\"".format(remote_drive)``` You can add as many game as you want. Just make some minor change to ```main.py```.
