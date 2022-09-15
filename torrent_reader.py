class torrent_reader:
    # 读取 强制byte类型
    #   hash_type(hash返回格式)(其实遇上所有decode失败的bytes都会判断是否转换)
    #       hex 十六进制字符串(默认)
    #       byte byte型
    #       (其实只要不是hex，都返回byte)
    def read(self, torrent_content, hash_type="hex"):
        self.now = 0
        self.torrent_content = torrent_content
        self.hash_type = hash_type
        return self.type_select()

    # 格式判断并获取值
    def type_select(self):
        if self.now_char() == "d":
            # 字典
            self.now += 1
            result = self.get_dict()
        elif self.now_char() == "i":
            # 整数
            self.now += 1
            result = self.get_int()
        elif self.now_char() == "l":
            # 列表
            self.now += 1
            result = self.get_list()
        elif self.torrent_content[self.now] >= 47 and self.torrent_content[self.now] <= 58:
            # 字符串
            length = int(self.get_until_colon())
            self.now += 1
            result = self.get_string(length)

        return result

    # 返回冒号之前的数据
    def get_until_colon(self):
        string = ""
        while self.now_char() != ":":
            string += self.now_char()
            self.now += 1
        return string

    # 返回当前byte
    def now_char(self):
        return chr(self.torrent_content[self.now])

    # 读取整数
    def get_int(self):
        int_string = ""
        while self.now_char() != "e":
            int_string += self.now_char()
            self.now += 1
        self.now += 1
        return int(int_string)

    # 读取字符串
    def get_string(self, length):
        string = self.torrent_content[self.now:self.now + length]
        try:
            string = string.decode('utf-8')
        except UnicodeDecodeError:
            # 疑似hash值的转化成十六进制
            if self.hash_type == "hex":
                string = self.byte_to_hex(string)
            else:
                pass

        self.now += length
        return string

    # 读取字典
    def get_dict(self):
        dict = {}
        while self.now_char() != "e":
            key = self.type_select()
            value = self.type_select()
            dict[key] = value
        self.now += 1
        return dict

    # 读取列表
    def get_list(self):
        list = []
        while self.now_char() != "e":
            value = self.type_select()
            list.append(value)
        self.now += 1
        return list

    # 字节转十六进制
    def byte_to_hex(self, string):
        hex_string = ""
        for each_byte in string:
            hex_string += hex(each_byte).replace("0x",
                                                 "").upper().rjust(2, "0")
        return hex_string
