# learn-ebpf

Repository with notes and code created while learning eBPF

## Prerequisites

* install [Lima](https://github.com/lima-vm/lima)
* use Lima:
  * ``limactl start``
  * ``lima``
  * ``sudo apt install python3 python3-pip python3-venv bpfcc-tools linux-headers-$(uname -r)``
  * ``cd /tmp/lima``
  * ``python3 -m venv venv``
  * ``source venv/bin/activate``
  * ``pip3 install bcc-python``
  * ``pip3 list``
  * ``limactl list``
  * ``limactl stop``
  * ``limactl delete default``

## Programs

* ``sudo python3 bcc_1.py``
* ``sudo python3 bcc_2.py``

## Links

* [learning eBPF](https://github.com/lizrice/learning-ebpf)
