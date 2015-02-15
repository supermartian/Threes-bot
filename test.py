#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Yuzhong Wen <supermartian@gmail.com>
#
# Distributed under terms of the MIT license.

import game
import random
import sys

def randomGameMoveTest():
    g = game.gameBoard()
    g.initRandomBoard()
    while g != None:
        m = random.randint(0, 4)
        print g.maxtile
        g.printBoard()
        g = g.getNextState(m)

def regularPlayTest():
    g = game.gameBoard()
    g.initRandomBoard()
    gameover = False
    randomPool = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 3, 3, 3, 3]
    randomtile = randomPool[random.randint(0, len(randomPool) -1)]
    print "======", randomtile, "========"
    g.printBoard()
    while not gameover:
        action = sys.stdin.read(1)
        k = g
        if action == 'w':
            g = g.getNextStateWithRandomTile(0, randomtile)
        elif action == 'd':
            g = g.getNextStateWithRandomTile(1, randomtile)
        elif action == 's':
            g = g.getNextStateWithRandomTile(2, randomtile)
        elif action == 'a':
            g = g.getNextStateWithRandomTile(3, randomtile)
        else:
            continue

        if g == None:
            g = k
            continue

        print "======", randomtile, "========"
        g.printBoard()
        randomtile = randomPool[random.randint(0, len(randomPool) -1)]
        print "==================="
        if not g.maxtile in randomPool:
            randomPool.append(g.maxtile)

#randomGameMoveTest()
regularPlayTest()
