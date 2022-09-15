from torrent_reader import torrent_reader

tr = torrent_reader()

with open("./test.txt.torrent", "rb") as file:
    print(tr.read(file.read(), hash_type = "hex"))