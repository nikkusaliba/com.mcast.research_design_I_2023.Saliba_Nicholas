import hashlib
import time

start = time.time()

for i in range(82000000):
    hashlib.sha256(b"cpu-cycle-test-%d" % i).hexdigest()
    if i % 1000000 == 0:
        print(f"Processed {i} hashes...")

end = time.time()
print(f"Finished analysis in {round(end - start, 2)} seconds.")
