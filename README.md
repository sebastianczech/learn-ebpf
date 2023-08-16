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

* basic BCC:
  * ``sudo python3 bcc_1.py``
  * [bpf_trace_printk](https://github.com/iovisor/bcc/blob/master/docs/reference_guide.md#1-bpf_trace_printk)
* BPF maps:
  * ``sudo python3 bcc_2.py``
  * [bpf_get_current_uid_gid](https://github.com/iovisor/bcc/blob/master/docs/reference_guide.md#5-bpf_get_current_uid_gid)
* ring buffers:
  * ``sudo python3 bcc_3.py``
  * [bpf_get_current_pid_tgid](https://github.com/iovisor/bcc/blob/master/docs/reference_guide.md#4-bpf_get_current_pid_tgid)
  * [bpf_get_current_comm](https://github.com/iovisor/bcc/blob/master/docs/reference_guide.md#6-bpf_get_current_comm)
  * [bpf_probe_read_kernel](https://github.com/iovisor/bcc/blob/master/docs/reference_guide.md#1-bpf_probe_read_kernel)

## Links

* [learning eBPF](https://github.com/lizrice/learning-ebpf)
