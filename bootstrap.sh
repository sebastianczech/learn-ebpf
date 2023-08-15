sudo apt install python3 python3-pip python3-venv bpfcc-tools linux-headers-$(uname -r)
cd /tmp/lima
python3 -m venv venv
source venv/bin/activate
pip3 install bcc-python
pip3 list