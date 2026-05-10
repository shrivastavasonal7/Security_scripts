# File Hash Extractor

A Python utility to scan directories and compute MD5/SHA256 hashes of files, comparing them against a database of known malicious hashes.

## Features

- Recursive directory scanning
- MD5 and SHA256 hash computation
- Malware detection via hash comparison
- JSON formatted output

## Usage

```bash
python3 file_hash_extractor.py
```

Edit the `test_directory` variable in the script to specify which directory to scan.

## Output

The script outputs a JSON array with file information including:
- `file_path`: Full path to the scanned file
- `md5`: MD5 hash of the file
- `sha256`: SHA256 hash of the file
- `malicious`: Detection result ("clean" or malware name)

## Configuration

Update the `malicious_hashes` dictionary in the script to add your known malicious file hashes.
