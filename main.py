# Project Name: Prob_Set_3_Explicit
# Author: Khang Vo
# Date Created: 10/16/2021
# Date Last Modified: 10/17/2021
# Python Version: 3.9

import os
import time

import setup_problem
import explicit
import plot_timestep


def main():
    root = os.getcwd() + "/files"
    os.chdir(root)

    # Parameters
    nx = 100, 200  # number of nodes for x
    nt = 400, 500  # number of nodes for t
    ts = 1  # timestep/day
    Tleft = 300  # left temperature boundary
    Tright = 300  # left temperature boundary

    # Uncomment both modules to setup new problems if initial parameters are changed
    # setup_problem.nodes(nx, nt, ts, Tleft, Tright)
    # explicit.calc(nx, nt)

    # Uncomment specific modules to plot static limits or dynamic limits
    plot_timestep.plot_static_axis(nx, nt)
    # plot_timestep.plot_dynamic_axis(nx[1], nt[1])


if __name__ == "__main__":
    # timer start
    time_start = time.perf_counter()

    main()

    # timer end
    time_end = time.perf_counter()
    time_total = time_end - time_start
    print("Elapsed time: " + str(time_total) + " seconds")
