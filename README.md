# Network-Tools

A collection of Python-based networking utilities: SSH remote commands, TCP/UDP proxying, netcat-like scripts, and more.

> ⚠️ **Use responsibly:** these utilities can send, receive, or relay network traffic. Only run them on networks or hosts you own or have permission to test. Unauthorized use may violate laws or network policies.

---

## Requirements

* Python 3.x
* Likely no extra dependencies (pure Python), but some scripts may require `paramiko` or other libraries depending on implementation.
* On Linux, some tools (especially raw sockets or proxying) may require root privileges.

---

## Quick Start

```bash
git clone https://github.com/ilyasSerjaoui/Network-Tools.git
cd Network-Tools
python3 netcat.py   # example usage
```

If any tool in the repo requires root (e.g. raw sockets), use:

```bash
sudo python3 <tool>.py
```

---

## Files & Descriptions

Below are the primary scripts in the repo and what they do:

| Filename          | Purpose / Description                                                                         |
| ----------------- | --------------------------------------------------------------------------------------------- |
| `netcat.py`       | A Python reimplementation of **netcat** — connect/read/write raw TCP/UDP streams.             |
| `tcp_proxy.py`    | A simple TCP proxy / forwarder. Useful to bridge connections or tunnel traffic.               |
| `sshcmd.py`       | SSH remote command executor. Connects to a remote server via SSH and runs a command.          |
| `bh_sshserver.py` | Backdoor SSH server — listens for incoming SSH-like connections and allows command execution. |
| `bh_sshRcmd.py`   | Remote SSH command client to talk to `bh_sshserver`.                                          |
| `tcp_script.py`   | Generic TCP-based script (could be client/server or custom logic).                            |
| `udp_script.py`   | UDP-based script for sending/receiving UDP datagrams.                                         |
| `tcp_server.py`   | A simple TCP server that listens for connections and handles them.                            |
| `netcap_usage.py` | Tool for capturing data or usage of network interfaces (depends on what it implements).       |

---

## Usage Tips & Examples

1. **netcat.py**
   Example: connect to remote host’s port 1234

   ```bash
   python3 netcat.py 192.168.0.100 1234
   ```

2. **tcp_proxy.py**
   Example: forward local port 9999 to remote host:port

   ```bash
   python3 tcp_proxy.py 127.0.0.1 9999 192.168.0.100 80
   ```

3. **sshcmd.py**
   Example: run `ls /` on remote host via SSH

   ```bash
   python3 sshcmd.py user@remote_host "ls /"
   ```

4. **bh_sshserver.py** + **bh_sshRcmd.py**

   * Run `bh_sshserver.py` on a listening machine.
   * Then use `bh_sshRcmd.py` from client side to connect and execute commands over it.

---

## Common Issues & Fixes

* **Permission errors / raw sockets**
  Some scripts may fail without root privileges. Use `sudo` or elevated permissions.

* **Port already in use**
  When running proxies or servers, if a port is already used, choose another or kill the process using it.

* **Firewall / network restrictions**
  If your network blocks certain ports or protocols, these scripts may not connect or may be dropped.

* **Python versions**
  If code uses Python 2 syntax (e.g. `raw_input`), update to Python 3 (`input()`, bytes/str conversions).

---

## Suggestions for Improvement

* Add `argparse` support so every script accepts flags (`-p`, `-l`, `--host`, etc.).
* Add logging and verbose modes.
* Add timeout handling for network operations.
* Add SSL/TLS support (for `sshcmd` or proxies) if you plan secure usage.
* Add unit tests or usage examples in separate folder.

---

## License & Contribution

If you want to allow open use, include a `LICENSE` file (e.g. **MIT License**).
You can also add a `CONTRIBUTING.md` to explain how others can contribute scripts or features.

---

## Author

ilyasSerjaoui — networking and security tools for learning and experimentation.
