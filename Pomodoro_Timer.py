# -*- coding: utf-8 -*-
# @Time    : 18-10-16 上午10:47
# @Author  : Mingan Luan
# @File    : Pomodoro_Timer.py
"""
A Pomodoro Technique.
How it works:
    1. Set a pomodoro timer (default is 25 min).
    2. When the timer ends, a short break timer (default is 5 min) kicks in.
    3. Go to step 1.
    4. After four pomodoro cycles (step 1 to 3), take a longer break (default
       is 30 min).
"""
import datetime
import time


def convert_string_to_time(times):
    # times = datetime.datetime.strptime(time, '%M:%S')
    # times.time()
    times = int(times)
    times = datetime.timedelta(seconds=times)
    return times


def main():
    pomodoro_timer = input("Please input your pomodoro timer(for example: 25(min)):")
    break_timer = input("Please input your pomodoro timer(for example: 5(min)):")
    big_break_timer = input("Please input your pomodoro timer(for example: 30(min)):")
    the_number_of_pt = int(input("Please input your the number of pomodoro timer(for example: 4):"))
    the_number_of_pt_round = int(input("How many numbers do you want to learning(for example: 4):"))
    #convert_string_to_time()
    #pomodoro_timer = convert_string_to_time(pomodoro_timer)
    #break_timer = convert_string_to_time(break_timer)
    #big_break_timer = convert_string_to_time(big_break_timer)
    seconds = datetime.timedelta(seconds=1)
    judge = datetime.timedelta(0)
    Number = 0
    number = 0
    print(datetime.datetime.now())
    while Number != the_number_of_pt_round:
        while number != the_number_of_pt:
            pomodoro_timers = convert_string_to_time(pomodoro_timer)
            while pomodoro_timers != judge:
                pomodoro_timers -= seconds
                print(pomodoro_timers)
                time.sleep(1)
            print("It's time to rest")
            break_timers = convert_string_to_time(break_timer)
            while break_timers != judge:
                print(break_timers)
                break_timers -= seconds
                time.sleep(1)
            print("!!!!!It's time to work")
            number += 1
        print("You should have a big rest!")
        big_break_timers = convert_string_to_time(big_break_timer)
        while big_break_timers != judge:
            big_break_timers -= seconds
            time.sleep(1)
        print("!!!!!It's time to work")
        Number += 1
    print(datetime.datetime.now())


#if __name__ == '__main__':
main()