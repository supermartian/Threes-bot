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
import ai

def randomGameMoveTest():
    g = game.gameBoard()
    g.initRandomBoard()
    while g != None:
        m = random.randint(0, 4)
        g.printBoard()
        g = g.getNextState(m)

def randomPlayTest():
    g = game.gameBoard()
    g.initRandomBoard()
    gameover = False
    randomtile = g.randomPool[random.randint(0, len(g.randomPool) - 2)]
    print "======", randomtile, "========"
    g.printBoard()
    while not g.isGameOver():
        action = random.randint(0, 3)
        k = g
        g = g.getNextStateWithRandomTile(action, randomtile)

        if g == None:
            g = k
            continue

        e = ai.boardEvaluator(g)
        heuristic = e.boardHeuristic()

        randomtile = g.randomPool[random.randint(0, len(g.randomPool) -1)]
        print "==Next Coming==", randomtile, "========"
        g.printBoard()
        print "==Evaluation===", heuristic, "========"
        print "==================="

def naivePlayTest():
    g = game.gameBoard()
    g.initRandomBoard()
    gameover = False
    randomtile = g.randomPool[random.randint(0, len(g.randomPool) - 2)]
    print "======", randomtile, "========"
    g.printBoard()
    while not g.isGameOver():
        k = g
        maxmove = 0
        maxvalue = -1
        state = ai.gameState()
        state.taketurn = 1
        state.nexttile = randomtile
        for move in range(4):
            state.lastmove = move
            nextg = g.getNextState(move)
            if nextg == None:
                continue
            s = ai.boardSolver(nextg)
            v = s.evaluateMove(state, 4)
            if v > maxvalue:
                maxvalue = v
                maxmove = move
        g = g.getNextStateWithRandomTile(maxmove, randomtile)

        if g == None:
            g = k
            continue

        randomtile = g.randomPool[random.randint(0, len(g.randomPool) -1)]
        print "==Next Coming==", randomtile, "========"
        g.printBoard()
        print "==Evaluation===", maxvalue, "========"
        print "==Next Move ===", maxmove, "========"
        print "==================="

def monteCarloPlayTest():
    g = game.gameBoard()
    g.initRandomBoard()
    gameover = False
    randomtile = g.randomPool[random.randint(0, len(g.randomPool) - 2)]
    print "======", randomtile, "========"
    g.printBoard()
    while not g.isGameOver():
        k = g
        maxmove = 0
        maxvalue = -1
        for move in range(4):
            s = ai.monteCarloSolver(g)
            v = s.evaluateMove(move, 1000)
            if v > maxvalue:
                maxvalue = v
                maxmove = move
        g = g.getNextStateWithRandomTile(maxmove, randomtile)

        if g == None:
            g = k
            continue

        randomtile = g.randomPool[random.randint(0, len(g.randomPool) -1)]
        print "==Next Coming==", randomtile, "========"
        g.printBoard()
        print "==Evaluation===", maxvalue, "========"
        print "==Next Move ===", maxmove, "========"
        print "==================="



def regularPlayTest():
    g = game.gameBoard()
    g.initRandomBoard()
    gameover = False
    randomtile = g.randomPool[random.randint(0, len(g.randomPool) - 2)]
    print "======", randomtile, "========"
    g.printBoard()
    while not g.isGameOver():
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

        e = ai.boardEvaluator(g)
        heuristic = e.boardHeuristic()

        randomtile = g.randomPool[random.randint(0, len(g.randomPool) -1)]
        print "======", randomtile, "========"
        g.printBoard()
        print "==Evaluation===", heuristic, "========"
        print "==================="

print "Starting random initial state test"
print "=================================="
randomGameMoveTest()

print "Starting random gameplay test"
print "=================================="
randomPlayTest()

print "Starting naive AI gameplay test"
print "=================================="
naivePlayTest()

#print "Starting Monte Carlo AI gameplay test"
#print "=================================="
#monteCarloPlayTest()

#print "Starting regular gameplay test, use w s a d to control the game"
#print "=================================="
#regularPlayTest()
