#################################
# Created by: Cadehlinha        #
# https://github.com/Cadehlinha #
#################################

import gi # pip install PyGObject
import sys
import time
import subprocess

gi.require_version('Notify', '0.7')
from gi.repository import Notify

# config global vars
loop_time = 5 # 5 seconds
low_threshold = 80 # 80% for low
critical_threshold = 50 # 50% for critical



class BatteryNotifier:
    def __init__(self):
        # Initialize the notification system
        Notify.init("Battery Status")

        # Initial state
        state_process = subprocess.Popen(["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT0"], stdout=subprocess.PIPE)
        state_output = state_process.communicate()[0].decode("utf-8")
        self.prev_state = [line.split(":")[1].strip() for line in state_output.split("\n") if "state" in line][0]
        self.low_notified = 0
        self.crit_low_notified = 0


    def send_notification(self, urgency, timeout, message):
        notification = Notify.Notification.new("Battery Status", message)
        notification.set_urgency(urgency)
        notification.set_timeout(timeout)
        notification.show()


    def check_battery_capacity(self):
        with open("/sys/class/power_supply/BAT0/capacity", "r") as capacity_file:
            capacity = int(capacity_file.read())

        state_process = subprocess.Popen(["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT0"], stdout=subprocess.PIPE)
        state_output = state_process.communicate()[0].decode("utf-8")
        state = [line.split(":")[1].strip() for line in state_output.split("\n") if "state" in line][0]

        if state != self.prev_state:
            self.send_notification(Notify.Urgency.NORMAL, 5000, "Battery is now " + state)
            self.prev_state = state

        if critical_threshold <= capacity < low_threshold and self.low_notified == 0:
            self.send_notification(Notify.Urgency.NORMAL, 8000, "Battery is low: {}%".format(capacity))
            self.low_notified = 1
            self.crit_low_notified = 0  # Reset critically low notification variable
        elif capacity < critical_threshold and self.crit_low_notified == 0:
            self.send_notification(Notify.Urgency.CRITICAL, 8000, "Battery is critically low: {}%".format(capacity))
            self.crit_low_notified = 1
            self.low_notified = 0  # Reset low notification variable
        elif capacity >= low_threshold:
            self.low_notified = 0  # Reset low notification variable
            self.crit_low_notified = 0  # Reset critically low notification variable


    def run(self):
        # Check battery capacity at a set interval (e.g., every 5 seconds)
        while True:
            try:
                self.check_battery_capacity()
                time.sleep(loop_time)
            except KeyboardInterrupt:
                print("Exited")
                sys.exit()



if __name__ == "__main__":
    notifier = BatteryNotifier()
    notifier.run()