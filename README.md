# vidya-smartinspector

# Devlopent
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