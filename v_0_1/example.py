import json
import time
from torrent_reader import torrent_reader

tr = torrent_reader()
torrent_file_path = "../test.txt.torrent"

with open(torrent_file_path, "rb") as file:
    bytes = file.read()
    start_time = time.perf_counter()
    for num in range(100000):
        tr.read(bytes, hash_type="hex")
    print(time.perf_counter() - start_time) # 5.999820799999725
exit()

# 读取bytes
with open(torrent_file_path, "rb") as file:
    bytes = file.read()
    # 遇到hash值，将以十六进制返回
    print(tr.read(bytes, hash_type="hex"))
    # 遇到hash值，将以bytes格式返回
    print(tr.read(bytes, hash_type="byte"))
# 其实判断是否为hash值是靠报错，所以可能出现误判为hash或者是hash但是判断成字符串的情况，这部分我还没了解过


# 读取文件
print(tr.read_file(torrent_file_path, hash_type="hex"))
print(tr.read_file(torrent_file_path, hash_type="byte"))

# 保存json
with open("./test.json", "w", encoding="utf8") as file:
    json.dump(
        tr.read_file(torrent_file_path, hash_type="hex"), file, ensure_ascii=False
    )
