
def recv(self, output: dict):
    logger.error('recv')
    buf_size = 1024 * 10
    buf = ctypes.create_string_buffer(buf_size)
    buf_size_output = ctypes.create_string_buffer(4)

    self.hanaw_module.MCI_RECV.argtypes = (ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)
    self.hanaw_module.MCI_RECV.restype = ctypes.c_int
    result = self.hanaw_module.MCI_RECV(self.fd_sock, buf, buf_size_output, 0)
    # buf.value.decode('euc-kr')[530:]
    # buf = 응답값
    output["buf"] = buf
    output["buf_size"] = buf_size_output
    return result


def recv_pooling(self):
    logger.error('recv_pooling')
    while True:
        print(f"recv mci ======>{datetime.now()}")
        output = {}
        # 응답값 받아옴,,
        result = self.recv(output)
        if result != 0:
            self.hanaw_module.MCI_CALL_ERRMSG.argtypes = ()
            self.hanaw_module.MCI_CALL_ERRMSG.restype = ctypes.c_char_p
            result = self.hanaw_module.MCI_CALL_ERRMSG().decode('euc-kr')
            self.packet_get_output(self.hanaw_module.MCI_CALL_ERRMSG(), output)
            try:
                if int(result) == -2:
                    self.reconnect_mci()
            except:
                pass
            # continue
        else:
            self.packet_get_output(output["buf"], output)
        if len(output["output_buf"]) == 0:
            print("recv empty")
        else:
            handle = self.get_window_handle(output["buf"])
            # print(f"handle {handle}")
            # print(f"buf {output['buf']}")
            # self.packet_get_output(output["output_buf"], output)
            # print(f"output_buf raw decode {output['output_buf'].decode('euc-kr')}")
            e = self.get_recv_event_in_window(handle)
            self.set_recv_data_in_window(handle, output)
            e.set()
            print(f"event {e}")
        print("recv mci <======")


    def packet_get_output(self, output_buffer: ctypes.c_char_p, output: dict):
        buf_size_output = ctypes.create_string_buffer(4)

        self.hanaw_module.MCI_PACKET_GET_OUTPUT.argtypes = (ctypes.c_char_p, ctypes.c_void_p)
        self.hanaw_module.MCI_PACKET_GET_OUTPUT.restype = ctypes.c_char_p
        output_bytes = self.hanaw_module.MCI_PACKET_GET_OUTPUT(output_buffer, buf_size_output)
        logger.error(f'output_bytes: {output_bytes}')
        # output_bytes b'p\x02@'... None으로만 체크하면 기도메타됨,,,
        # b'[TS2621]\xc7\xd8\xbf\xdc\xc1\xd6\xbd\xc4 \xbc\xd2\xbc\xf6\xc1\xa1\xb8\xc5\xb8\xc5 \xbd\xc5\xc3\xbb\xb0\xe8\xc1\xc2\xb0\xa1 \xbe\xc6\xb4\xd5\xb4\xcf\xb4\xd9.'
        if len(output_bytes) < 20:
            output["output_buf"] = output_buffer
        else:
            output["output_buf"] = output_bytes
        output["output_buf_size"] = buf_size_output
        return