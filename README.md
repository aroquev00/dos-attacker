# dos-attacker
A simple script to spawn multiple hping commands to flood a victim host at a given port.


MADE FOR EDUCATIONAL PURPOSES ONLY. DO __NOT__ USE OVER THE INTERNET.


IF YOU RUN THIS OVER THE INTERNET YOU WILL GET BANNED.

Try it on your localhost or on your local network only.

You must first install the `hping3` tool.

To run, do:
```shell
python3 attacker.py <victim_port> <victim_ip>
```

For example:
```shell
python3 attacker.py 8080 192.168.10.5
```

The script will continuously ask you how many processes do you want to spawn simultaneously. The maximum number depends on your system's capabilities.
