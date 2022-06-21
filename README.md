## Automatic Ball Sort Game Solver
### The Game
[Ball Sort Puzzle](https://play.google.com/store/apps/details?id=com.GMA.Ball.Sort.Puzzle&hl=en&gl=US)
is a game where you have n tubes, and k different colors.    
each tube can store 4 balls at a time, and the goal is the sort   
all the balls into seperate tubes.    
For example, this level:

<img src="https://external-preview.redd.it/XSo_QIU2xDjoIKqPMIGBDOixX6yCxoqlfsnGhdtZP-k.jpg?auto=webp&s=ac07c23c1fe0911d7336f54d8320e948789b9dc7" alt="Level 3" width="50%"/>

Can be sorted like this:
[Link To Gif](https://im4.ezgif.com/tmp/ezgif-4-c7dca51719.gif)

However, a ball can only be moved on top of another if they have 
the same color and if the amount of balls already in the tube is less than 4.

### How to use my bot
First you need to mirror your android's screen to your PC.
You must set your monitor's resolution to 1920x1080.
To mirror your android to your screen, download [Scrcpy](https://github.com/Genymobile/scrcpy)
to mirror your phone.

You need to [Enable USB Debugging](https://www.google.com/search?q=how+to+enable+usb+debugging&oq=how+to+enable+usb+debugging)
and then connect your phone to your PC via a USB cable.

Then, start the screen mirroring by issuing the command:
```shell
./scrcpy --fullscreen 
```
You must open Scrcpy in full screen mode because otherwise the location
would be off.

After you have mirrored your phone, then you can use `MainDFS.py`.
I suggest editing the code a bit to your liking.

### Note
This project is not complete, the algorithms aren't the most optimized yet.
Im planning on improving the algorithm and maybe even use Reinforcement Learning.
Also, `MainBestFS.py` uses a different technique that makes the bot find solutions in less moves, but 
finding the solution takes more time.
