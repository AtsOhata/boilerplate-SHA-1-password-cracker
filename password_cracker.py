import hashlib

def crack_sha1_hash(hash, use_salts = False):
    with open('top-10000-passwords.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if not use_salts:
                sha1_hash = hashlib.sha1()
                sha1_hash.update(line.strip().encode('utf-8'))
                if hash == sha1_hash.hexdigest():
                    return line.strip()
            else:
                with open('known-salts.txt', 'r', encoding='utf-8') as salt_file:
                    for salt in salt_file:
                        sha1_hash = hashlib.sha1()
                        word = line.strip() + salt.strip()
                        sha1_hash.update(word.encode('utf-8'))
                        if hash == sha1_hash.hexdigest():
                            return line.strip()
                        sha1_hash = hashlib.sha1()
                        word = salt.strip() + line.strip()
                        sha1_hash.update(word.encode('utf-8'))
                        if hash == sha1_hash.hexdigest():
                            return line.strip()
                
    return "PASSWORD NOT IN DATABASE"