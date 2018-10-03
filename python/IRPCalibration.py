import os
import numpy as np

import gain
import computeoffset
import computebolometerpolynomial
import computeoffsetpolynomial
import inquirer


def user_params():
    print('Welcome to Merlin.')
    print_knight()
    print('\n')

    questions = [
        inquirer.Text('DEVICE_ID', message="Enter Device ID"),
        inquirer.List('RESOLUTION', message="Enter resolution", choices=['VGA(Gen2)', 'QVGA(Atto)']),
        inquirer.Text('PREFIX', message="Enter bolometer prefix"),
        inquirer.Text('SUFFIX', message="Enter bolometer suffix"),
        inquirer.Text('GAIN_LOW', message="Enter low temp value of Gain matrix"),
        inquirer.Text('GAIN_HIGH', message="Enter high temp value of Gain matrix"),
        inquirer.Text('OFFSET_FIRST', message="Enter temp value of first offset reading"),
        inquirer.Text('OFFSET_LAST', message="Enter temp value of last offset reading"),
        inquirer.Text('OFFSET_STEP', message="Enter step value of offset readings")

    ]
    answers = inquirer.prompt(questions)
    print(answers)

    device_id = answers['DEVICE_ID']
    sensor = answers['RESOLUTION']
    if sensor == 'VGA(Gen2)':
        height = 640
        width = 480
    else:
        height = 320
        width = 240
    prefix = answers['PREFIX']
    suffix = answers['SUFFIX']
    g_low = answers['GAIN_LOW']
    g_high = answers['GAIN_HIGH']
    t_low = int(answers['OFFSET_FIRST'])
    t_high = int(answers['OFFSET_LAST'])
    t_high = t_high + 1
    t_step = int(answers['OFFSET_STEP'])

    if input("\n" "Please check entered parameters. Are you sure you want to continue? (y/n)") != "y":
        exit()

    return height, width, g_low, g_high, t_low, t_high, t_step


def print_knight():
    f = open('.knight_small.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()


if __name__ == '__main__':
    height, width, g_low, g_high, t_low, t_high, t_step = user_params()
    #gain.main(height, width, g_low, g_high)
 #   computeoffset.main(g_low, g_high, t_low, t_high, t_step)
    computebolometerpolynomial.main(t_low, t_high, t_step)
   # computeoffsetpolynomial.main(height, width, t_low, t_high, t_step)
