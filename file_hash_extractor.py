import os
import hashlib
import json

#known malicious hashes (example)
malicious_hashes = {
    "d41d8cd98f00b204e9800998ecf8427e": "Example Malware 1",
    "0cc175b9c0f1b6a831c399e269772661": "Example Malware 2",
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855": "Example Malware 3"
}

def compute_hash(file_path):
    """Compute hash of a file."""
    hash_md5 = hashlib.md5()
    hash_sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
                while chunk := f.read(8192):           #rb means read binary > reads exact bytes > correct hash
                    hash_md5.update(chunk)
                hash_sha256.update(chunk)

    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None, None

    return hash_md5.hexdigest(),hash_sha256.hexdigest()  

def scan_directory(directory):
    """Scan directory for files and compute their hashes."""
    results = []
    for root,dirs,files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root,file)
            md5_hash, sha256_hash = compute_hash(file_path)
            if md5_hash and sha256_hash:
                result={
                    "file_path": file_path,
                    "md5" : md5_hash,
                    "sha256": sha256_hash,
                    "malicious": malicious_hashes.get(md5_hash) or malicious_hashes.get(sha256_hash) or "clean"
                }
                results.append(result)
    return results

if __name__ == "__main__":
    # Test directory path - add your directory path here
    test_directory = "/tmp/test_files"
    results = scan_directory(test_directory)
    print(json.dumps(results, indent=2)) 