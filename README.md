# Security Scripts

This repository contains two Python security utilities:

- `file_hash_extractor.py` — computes file hashes and detects known malicious files.
- `port_scanner.py` — scans a target host for open TCP ports and returns a list of open ports.

## Features

- Recursive directory scanning
- MD5 and SHA256 hash computation
- Malware detection via hash comparison
- TCP socket port scanning
- Open-port collection for downstream use

## Usage

### File hash extractor

```bash
python3 file_hash_extractor.py
```

Edit the `test_directory` variable in the script to specify which directory to scan.

### Port scanner

```bash
python3 port_scanner.py
```

By default, the script scans `127.0.0.1` and a set of common ports. Modify `target_ip` or `ports` in the script to test a different host or port range.

## Output

### File hash extractor

The script outputs a JSON array with file information including:
- `file_path`: Full path to the scanned file
- `md5`: MD5 hash of the file
- `sha256`: SHA256 hash of the file
- `malicious`: Detection result (`clean` or malware name)

### Port scanner

The script prints the status of each scanned port and then prints:
- `Open ports found`: list of ports that accepted a TCP connection

## Configuration

Update the `malicious_hashes` dictionary in `file_hash_extractor.py` to add your known malicious file hashes.

Adjust `target_ip` and `ports` in `port_scanner.py` for different scan targets and port sets.
