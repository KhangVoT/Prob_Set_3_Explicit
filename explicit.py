# Module Name: explicit
# Author: Khang Vo
# Date Created: 10/16/2021
# Date Last Modified: 10/17/2021
# Python Version: 3.9

import os

import pandas as pd


def calc(nx, nt):

    if type(nx) == int or type(nx) == float:
        nx = [nx]
    if type(nt) == int or type(nt) == float:
        nt = [nt]

    # Physical parameters
    kappa = 1e-6  # rock thermal diffusivity [m2/s]

    for index in range(len(nx)):
        t = pd.read_csv("initial_condtitions_" + str(nx[index]) + "_" + str(nt[index]) + ".txt",
                        sep="\t", index_col=0, header=0)
        t.columns = t.columns.astype(float)

        # Numerical parameters
        dx = t.columns[1] - t.columns[0]
        dt = t.index[1] - t.index[0]

        for n in range(len(t.index) - 1):
            for i in range(len(t.columns) - 1):
                t.iloc[n + 1, i] = t.iloc[n, i] + kappa * dt * \
                                    ((t.iloc[n, i + 1] - (2 * t.iloc[n, i]) + t.iloc[n, i - 1]) / (dx ** 2))

        t.to_csv("explicit_result_" + str(nx[index]) + "_" + str(nt[index]) + ".txt", sep="\t")


if __name__ == "__main__":
    root = os.getcwd() + "/files"
    os.chdir(root)

    # setup number of nodes for both x and t
    nx = 100, 200, 300
    nt = 400, 500, 600
    calc(nx, nt)
