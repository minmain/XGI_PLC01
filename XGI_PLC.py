

import socket
import binascii
from contextlib import closing

class Mc:
    def __init__(self,
                 ip,
                 port,
                 bit_or_word,
                 device_num,
                 device_code,
                  data_num,
                 word_num='00',
                  double_word_num='00',
                  bit_on_off='00') :

        self.ip = ip
        self.port = port
        self.subhead = '5000'
        self.network = '00'
        self.pc_num = 'FF'
        self. i o num = 'FF03'
        self.office_num = '00'
        self.monitoring_timer = '0400'
        self.device_num = data_num
        self.device_code = device_code
        self.data_num = data_num
        self.word_num = word_num
        self.double_word_num = double_word_num
        self.bit_on_off = bit_on_off

     def pin_write(self):
         header = '500000FFFF0300'
         command = self.monitoring_timer + '0114 + '0100'
         device = '01000090' # M0001 지정의 경우
         number = '0100'+'00'  #켜기 00: 끄기
         command_protocol + code_num + command_protocol
         print(_send)
         mc_send=binascii.a2b_hex(_send)
         sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         print(mc_send)
         with closing(sock)
             try:
                 sock.connect((self.ip,self.port))
                 sock.sand(mc_send)
                 res_data=sock.recv(4096)
                 res_data=binascii.b2a_hex(res_data)
                 res_data=res_data.decode()
                 error_check(res_data[18:22])
             except:
                 print('write error')

              def hex_change_XXXX(data):
                  if(type(data)==str):
                      data_int=int(data)
                  else:
                      data_int=data
                   data=hex(data_int)
                  if(data_int<=15):
                      data='0'+data[2:]+'00'
                  if(data_int<=255 and data_int>15):
                      data=data[2:]+'00'
                  if(data_int>255 and data_int<=4095):
                      data=data[4:6]+data[2:4]
                  return data
              def error_check(error_code):
                  if(error_code=='0000'):
                      return
                  else:
                      print('error::'+error_code)

             mc_send = Mc(ip = '192.168.0.40,'
                           port = 32767,
                           bit_or_word = 'bit' ,# 'word' or 'bit'
                           device_num = 1  #주소
                           device_code = '90'
                           data_num = 1,
                           bit_or_off = '10')  #대상수

             mc_send.pin_write()  #비트 on 및 off


















