# -*- coding: utf-8 -*
import serial
import time
#open
ser = serial.Serial("/dev/ttyS1", 57600)
def bmp_set():
    ser.write(chr(0x6F))#o
    ser.write('\x83')#131
    ser.write('\x01')#column 1
    ser.write({0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, 
               0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, 
               0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  
               0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x60,0x1C,0x18,0x60,0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00})
    time.sleep(0.1)
    ser.write(chr(0x6F))#o
    ser.write('\x83')#131
    ser.write('\x02')#column 1
    ser.write({0x00,0x00,0x14,0x16,0x93,0xF3,0x3E,0x7E,0xD2,0x92,0x12,0x00,0xFE,0xFE,0x86,0x86,0x86,0x86,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFE,0xFE,0x06,0x66,
               0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x66,0x06,0xFE,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xCC,0xCC,0xCC,0xFC,0xFC,0xC6,0xC6,0xC4,0x80,0x8C,
               0x08,0x10,0x20,0x00,0xFE,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x30,0x30,0xFF,0xFF,0x30,0x30,0x00,0x18,0x18,0x18,0x18,0xFF,0xFF,0x18,0x18,0x18,
               0x18,0x00,0x00,0x04,0x04,0x0C,0x14,0x14,0x24,0x24,0x44,0xC4,0x04,0x04,0x03,0x00,0x00,0x00,0x00,0x03,0x04,0x04,0xC4,0x44,0x24,0x24,0x14,0x14,0x0C,0x04,0x04,0x00})
    time.sleep(0.1)
    ser.write(chr(0x6F))#o
    ser.write('\x83')#131
    ser.write('\x03')#column 1
    ser.write({0x00,0x04,0x06,0x07,0xFD,0x2C,0x2C,0x2C,0x2C,0x2D,0x2F,0x2C,0x2D,0x2D,0x2D,0x2D,0xFD,0xFD,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFF,0x00,0x00,
               0x7F,0x7F,0x63,0x63,0x63,0x63,0x63,0x7F,0x7F,0x00,0x00,0xFF,0xFF,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x20,0x70,0x38,0x0E,0xFF,0xFF,0x06,0x1C,0x10,0x60,0x61,
               0x63,0x66,0x34,0x30,0xFF,0xFF,0x30,0x30,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x18,0x0C,0xFF,0xFF,0x06,0x03,0x00,0x03,0x0F,0x1F,0xF3,0xE3,0xE3,0xF3,0x3B,0x0F,
               0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x40,0x78,0x27,0x10,0x10,0x08,0x08,0x04,0x04,0x04,0x04,0x08,0x08,0x10,0x10,0x27,0x78,0x40,0x00,0x00,0x00,0x00,0x00,0x00})
    time.sleep(0.1)
    ser.write(chr(0x6F))#o
    ser.write('\x83')#131
    ser.write('\x04')#column 1
    ser.write({0x00,0x00,0x00,0x00,0x07,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x07,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x07,0x07,0x00,0x00,
               0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x06,0x06,0x06,0x07,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x07,0x07,0x00,0x00,0x00,0x00,0x00,
               0x00,0x00,0x00,0x00,0x07,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x06,0x06,0x07,0x07,0x00,0x00,0x06,0x06,0x03,0x03,0x01,0x01,0x01,0x01,0x03,0x02,
               0x04,0x04,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00})
    

def main():
    while True:
        count = ser.inWaiting()
        if count != 0:

            recv = ser.read(count)
            print recv
            if recv[0]=='B':
                if recv[3]=='2':
                    print 'volume down'
                    ser.write(chr(0x4C))#L
                    ser.write('\x08')
                    ser.write(chr(0x52))#R
                    ser.write(chr(0x20))
                    ser.write(chr(0x47))#G
                    ser.write(chr(0xFF))
                    ser.write(chr(0x42))#B
                    ser.write('\x00')
                if recv[3]=='1':
                    print 'start button'
                    bmp_set()
                if recv[3]=='3':
                    print 'volume up'
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write('\x00')
                    ser.write('4')
                    time.sleep(0.1)
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write('\x01')
                    ser.write('3')
                    time.sleep(0.1)
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write('\x02')
                    ser.write('2')
                    time.sleep(0.1)
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write('\x03')
                    ser.write('1')
                    time.sleep(0.1)
            if recv[0]=='T':
                if recv[3]=='1':
                    print '1'
                if recv[3]=='2':
                    print '2'
                if recv[3]=='3':
                    print '3'
                if recv[3]=='4':
                    print '4'
                if recv[3]=='5':
                    print '5'
                if recv[3]=='6':
                    print '6'
                if recv[3]=='7':
                    print '7'
                if recv[3]=='8':
                    print '8'
                if recv[3]=='9':
                    print '9'
                if recv[3]=='A':
                    print 'A'
                if recv[3]=='B':
                    print 'B'
                if recv[3]=='C':
                    print 'C'
                if recv[3]=='D':
                    print 'D'
                if recv[3]=='E':
                    print 'E'
            time.sleep(0.5)
        ser.flushInput()

        time.sleep(0.1)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()