# vidya-smartinspector

## Devlopent

This application required python 3.7+
python 3.7+ installation link - https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/
Setup pip to link 3.7 `python3 -m pip install --upgrade pip`
**Run**
Activate Virtaul Env `source envs/datahack/bin/activate` replace **envs/datahack/bin/activate** with your virtaul env path
Install packages `sudo pip install -r requirements.txt`
Run application `sh run.sh`


# Errors 
* locale.Error: unsupported locale setting
solutions set this environment variable `export LC_ALL=C`
* sudo: pip: command not found
`sudo ln /home/ubuntu/.local/bin/pip /usr/bin/pip -f`

# Produduction Deployment

### clone project to server 

### genrate models 

* python3.7 RandomForest_Model.py
* python3.7 CNN_Model.py
  
### run gunicorn server use `tmux`  to run this server

* run `gunicorn -w 4 app:app -b 0.0.0.0:5000`

## Docker 

Docker image link - https://hub.docker.com/repository/docker/vinaymavi/vidya-smartinspector 