#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:11:10 2021

@author: antonjorg
"""

import notify2
import datetime
from datetime import timedelta
import time
import os


class Pomodoro:
    
    def __init__(self, name, worktime=25, breaktime=5, rounds=None):
        notify2.init(name)    
        self.worktime = worktime
        self.breaktime = breaktime
        self.rounds = rounds
        
    def main_loop(self):
        n = notify2.Notification("Session started",
                                 f"{self.rounds} rounds of {self.worktime} minute work sessions and {self.breaktime} minutes breaks."
                                 )
        n.show()

        time.sleep(10)

        while self.rounds > 0 or self.rounds is None:
            self.work_notification()
            time.sleep(self.worktime * 60)
            if self.rounds == 1:
                break
            self.break_notification()
            time.sleep(self.breaktime * 60)

            if self.rounds is not None:
                self.rounds -= 1
        
    def work_notification(self):
        
        now = datetime.datetime.now()
        done = now + timedelta(minutes=self.worktime)
        d = done.strftime("%H:%M")
        
        n = notify2.Notification("Work",
                                 f"{self.worktime} minutes until {d}",
                                 os.path.join(os.getcwd(), "img/work.png")  # Icon name
                                 )
        n.show()
    
    def break_notification(self):
        
        now = datetime.datetime.now()
        done = now + timedelta(minutes=self.breaktime)
        d = done.strftime("%H:%M")
        
        n = notify2.Notification("Break",
                                 f"{self.breaktime} minutes until {d}",
                                 os.path.join(os.getcwd(), "img/break.png")  # Icon name
                                 )
        n.show()


if __name__ == "__main__":    
    timer = Pomodoro("Pymodoro", 0.5, 0.25, 3)
    timer.main_loop()
