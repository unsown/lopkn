Intall tkinter
sudo apt-get install python-tk
pip install tkinter

pip install pygame
pip install ipython
pip freeze > requirements.txt    
python tracking.py
python tracking2.py

# start pulseaudio for pygame
pulseaudio -D
python Space_Invaders/spaceinvaders.py

docker run \
  -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e PULSE_SERVER=unix:/run/user/1000/pulse/native -v /run/user/1000/pulse:/run/user/1000/pulse \
  -v $(pwd):/home/python/code \
  --rm -it lasery/codebench:python bash

