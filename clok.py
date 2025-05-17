import matplotlib.pyplot as plt
import numpy as np
import datetime
import time

def draw_clock():
    while True:
        now = datetime.datetime.now()
        hour = now.hour % 12
        minute = now.minute
        second = now.second

        
        hour_angle = (360 / 12) * (hour + minute / 60)
        minute_angle = (360 / 60) * minute

        fig, ax = plt.subplots()
        ax.set_facecolor("black")
        ax.set_aspect("equal")
        ax.axis("off")

        
        circle = plt.Circle((0, 0), 1, color='white', fill=False, linewidth=4)
        ax.add_artist(circle)

        
        for i in range(12):
            angle = np.radians(i * 30)
            x_outer = np.sin(angle)
            y_outer = np.cos(angle)
            x_inner = 0.9 * np.sin(angle)
            y_inner = 0.9 * np.cos(angle)
            ax.plot([x_inner, x_outer], [y_inner, y_outer], color='white')

        
        hour_angle_rad = np.radians(90 - hour_angle)
        ax.plot([0, 0.5 * np.cos(hour_angle_rad)], [0, 0.5 * np.sin(hour_angle_rad)], color='hotpink', linewidth=6)

        
        minute_angle_rad = np.radians(90 - minute_angle)
        ax.plot([0, 0.8 * np.cos(minute_angle_rad)], [0, 0.8 * np.sin(minute_angle_rad)], color='lime', linewidth=3)

        
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)

        plt.title(now.strftime("%H:%M:%S"), color="white", fontsize=16)
        plt.pause(1)
        plt.clf()


draw_clock()
