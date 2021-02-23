import datetime
import random
import serial
import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()


COM = '/dev/tty.SLAB_USBtoUART'
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
time.sleep(3)
print(ser.name)


def read_data():
    m = 0
    n = 0
    val = str(ser.readline().decode().strip('\r\n'))
    print(val)
    e = val.split(',')
    if len(e) > 4:
        l = int(e[6]) + int(e[7])
        num = l / 2
        nuu = int(e[7])
        print(int(e[9]))
        if l > 5000:
            print("Up")
            keyboard.press(Key.space)
            sleep(1)
            keyboard.release(Key.space)
        else:
            print("Stay")
        m = num
        n = nuu
    return m, n


def animate(frame, xs, ys):


    # Read data
    dat = read_data()

    xs.append(datetime.datetime.now().strftime('%S'))
    ys.append(dat[0])

    size_limit = 30
    xs = xs[-size_limit:]
    ys = ys[-size_limit:]

    ax.clear()
    ax.plot(xs, ys)

    plt.grid()
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)

    plt.title('Brain wave data')
    plt.ylabel('Alpha wave amplitude')
    plt.xlabel('Time')


if __name__ == '__main__':
    e = 0
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    x_data = []
    y_data = []

    ani = animation.FuncAnimation(fig, animate, fargs=(x_data, y_data), interval=200)
    plt.show()