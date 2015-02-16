#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 martian <supermartian@gmail.com>
#
# Distributed under terms of the MIT license.

import random
import game
import copy 

class boardEvaluator:
    def __init__(self, gameBoard):
        self.game = gameBoard
        self.board = gameBoard.board
        self.maxtile = gameBoard.maxtile

    def cornerEvaluate(self):
        if ((self.board[0][0] == self.maxtile) or
        (self.board[3][0] == self.maxtile) or
        (self.board[0][3] == self.maxtile) or
        (self.board[3][3] == self.maxtile)):
            return 50
        else:
            return 0

    def blankEvaluate(self):
        ret = 0
        for i in range(4):
            for j in range(4):
                ret += 1 if self.board[i][j] == 0 else 0
        return ret * 3

    def smoothnessEvaluate(self):
        ret = 0

        "Horizontal lines"
        for i in range(4):
            intr = []
            for j in range(1, 4):
                intr.append(self.board[i][j] - self.board[i][j - 1])
            ret += 1 if min(intr) * max(intr) >= 0 else -1
            ret += intr.count(0) * 3

        "Vertical lines"
        for i in range(4):
            intr = []
            for j in range(1, 4):
                intr.append(self.board[j][i] - self.board[j - 1][i])
            ret += 1 if min(intr) * max(intr) >= 0 else 0

        "Dignoal lines"
        for i in range(4):
            intr.append(self.board[j][i] - self.board[j - 1][i - 1])
            ret += 4 if min(intr) * max(intr) >= 0 else 0
        for i in range(4):
            intr.append(self.board[i][j] - self.board[i - 1][j - 1])
            ret += 4 if min(intr) * max(intr) >= 0 else 0

        return ret * 2

    def boardHeuristic(self):
        ret = 0
        ret += self.cornerEvaluate()
        ret += self.blankEvaluate()
        ret += self.smoothnessEvaluate()
        ret += self.game.maxtile
        return ret

class gameState:
    def __init__(self):
        "0: Player's turn, 1: Randomtile's turn"
        self.taketurn = 0
        self.lastmove = 0
        self.nexttile = 1

class monteCarloSolver:
    def __init__(self, gameBoard):
        self.evaluator = boardEvaluator(gameBoard)
        self.game = gameBoard

    def evaluateMove(self, move, depth):
        if depth == 0 or self.game.isGameOver():
            return self.game.maxtile

        g = self.game
        randomtile = g.randomPool[random.randint(0, len(g.randomPool) - 2)]
        g = g.getNextStateWithRandomTile(move, randomtile)
        if g == None:
            return 0
        s = monteCarloSolver(g)
        return s.evaluateMove(random.randint(0, 3), depth - 1)

class boardSolver:
    def __init__(self, gameBoard):
        self.evaluator = boardEvaluator(gameBoard)
        self.game = gameBoard

    def evaluateMove(self, state, depth):
        if depth == 0 or self.game.isGameOver():
            e = boardEvaluator(self.game)
            return e.boardHeuristic()

        if state.taketurn == 0:
            "Player's turn"
            v = -999999
            for move in range(4):
                d = self.game.getNextState(move)
                if d == None:
                    continue
                s = boardSolver(self.game)
                state.taketurn = 1
                state.lastmove = move
                v = max(v, s.evaluateMove(state, depth - 1))
            return v

        elif state.taketurn == 1:
            "Randomtile's turn"
            newtile = list(set(self.game.randomPool))
            v = 999999
            state.taketurn = 0
            for t in newtile:
                state.nexttile = t
                if state.lastmove == 0:
                    for i in range(4):
                        d = copy.deepcopy(self.game)
                        if not d.addTile(3, i, t):
                            continue
                        s = boardSolver(d)
                        v = min(v, s.evaluateMove(state, depth - 1))
                elif state.lastmove == 2:
                    for i in range(4):
                        d = copy.deepcopy(self.game)
                        if not d.addTile(0, i, t):
                            continue
                        s = boardSolver(d)
                        v = min(v, s.evaluateMove(state, depth - 1))
                elif state.lastmove == 1:
                    for i in range(4):
                        d = copy.deepcopy(self.game)
                        if not d.addTile(i, 0, t):
                            continue
                        s = boardSolver(d)
                        v = min(v, s.evaluateMove(state, depth - 1))
                elif state.lastmove == 3:
                    for i in range(4):
                        d = copy.deepcopy(self.game)
                        if not d.addTile(i, 3, t):
                            continue
                        s = boardSolver(d)
                        v = min(v, s.evaluateMove(state, depth - 1))
            return v
