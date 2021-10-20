# Module Name: setup_problem
# Author: Khang Vo
# Date Created: 10/16/2021
# Date Last Modified: 10/17/2021
# Python Version: 3.9

import os

import pandas as pd
import numpy as np


def nodes(nx, nt, ts, t_left, t_right):

    if type(nx) == int or type(nx) == float:
        nx = [nx]
    if type(nt) == int or type(nt) == float:
        nt = [nt]

    # Physical parameters
    l = 100  # length of domain [m]
    t_rock = 300  # rock temperature [C]
    w = 5  # dike width [m]
    t_magma = 1200  # magma temperature [C]

    for index in range(len(nx)):
        # Numerical parameters
        dx = l / nx[index]  # grid spacing
        dt = ts * (60 * 60 * 24)  # timestep per day (seconds)

        # Set nodes
        x_nodes = np.arange(-l / 2, (l / 2) + dx, dx)
        t_nodes = np.arange(0, (nt[index] * dt + dt), dt)
        t = pd.DataFrame(index=t_nodes, columns=x_nodes)
        t = t.fillna(t_rock)
        t.loc[:, (-w / 2):(w / 2)] = t_magma
        t.iloc[:, 0] = t_left
        t.iloc[:, -1] = t_right
        t.iloc[1:, 1:-1] = 0

        t.to_csv("initial_condtitions_" + str(nx[index]) + "_" + str(nt[index]) + ".txt", sep="\t")


if __name__ == "__main__":
    root = os.getcwd() + "/files"
    os.chdir(root)

    # setup number of nodes for both x and t
    nx = 100, 200, 300  # number of nodes for x
    nt = 400, 500, 600  # number of nodes for t
    ts = 100  # timestep
    Tleft = 300  # left temperature boundary
    Tright = 600  # left temperature boundary
    nodes(nx, nt, ts, Tleft, Tright)
