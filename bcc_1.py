#!/usr/bin/python3  
from bcc import BPF

program = r"""
int bcc_first_program(void *ctx) {
    bpf_trace_printk("First eBPF program!");
    return 0;
}
"""

b = BPF(text=program)
syscall = b.get_syscall_fnname("execve")
b.attach_kprobe(event=syscall, fn_name="bcc_first_program")

b.trace_print()