from torrent_reader import torrent_reader

tr = torrent_reader()

with open("./test.txt.torrent", "rb") as file:
    # 遇到hash值，将以十六进制返回
    print(tr.read(file.read(), hash_type = "hex"))
    # 遇到hash值，将以bytes格式返回
    print(tr.read(file.read(), hash_type = "byte"))
    # 其实判断是否为hash值是靠报错，所以可能出现误判为hash或者是hash但是判断成字符串的情况，这部分我还没了解过