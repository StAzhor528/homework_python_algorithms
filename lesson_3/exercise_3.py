import hashlib

our_str = "papa"
hash_set = set()
for i in range(len(our_str)):
    for j in range(i + 1, len(our_str) + 1):
        if our_str[i:j] != our_str:
            hash_obj = hashlib.sha256(our_str[i:j].encode()).hexdigest()
            hash_set.add(hash_obj)

print(f"{our_str} - {len(hash_set)} уникальных подстрок")
