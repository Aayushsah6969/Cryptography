from file_hash import hash_file

def verify_integrity(file1, file2):
    """
    Verify the integrity of two files by comparing their SHA-256 hashes.

    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.

    Returns:
        bool: True if the files have the same hash, False otherwise.
    """
    # i want to use the hash_file function from hash-file.py here to compute the hashes of the two files


    hash1 = hash_file(file1)
    hash2 = hash_file(file2)

    if(hash1 == hash2):
        print("The files are identical. Integrity verified.")
        return True
    else:
        print("The files are different. Integrity compromised.")
        return False

verify_integrity("../Samples/sample-file.txt", "../Samples/sample-file-copy.txt")