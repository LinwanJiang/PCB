# !/usr/bin/python
# encoding:utf-8

import serial

if __name__ == '__main__':
        serial = serial.Serial('COM7','57600')
        if serial.isOpen():
                print('串口打开成功！\n')
                # f = open('./test.txt','w')
                #pass
        else :
                print('串口打开失败！\n')


        getBytes=b''
        while True:
                count = serial.inWaiting()
                if count > 0:
                        data = serial.read(count)
                        if data != getBytes:
                                print(data)
                                        # f.write(data)#.decode('utf-8'))
                                        # f.write('\n')
                                        #getBytes=data

        # except KeyboardInterrupt:
        #         if serial != None:
        #                 f.close()
        #                 serial.close()