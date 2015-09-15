# coding:utf-8
__author__ = 'YingZheng'

import numpy as np
import math


class recommendation():
    def __init__(self):
        self.critics = {
            'Lisa Rose': {
                'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0
            },
            'Gene Seymour': {
                'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5,
                'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'The Night Listener': 3.0
            },
            'Michael Phillips': {
                'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                'Superman Returns': 3.5, 'The Night Listener': 4.0
            },
            'Claudia Puig': {
                'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                'Superman Returns': 4.0, 'You, Me and Dupree': 2.5, 'The Night Listener': 4.5
            },
            'Mick LaSalle': {
                'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0,
                'Superman Returns': 3.0, 'You, Me and Dupree': 2.0, 'The Night Listener': 3.0
            },
            'Jack Matthews': {
                'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'The Night Listener': 3.0
            },
            'Toby': {
                'Snakes on a Plane': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 1.0
            }
        }

    def sim_distance(self, person1, person2):
        si = {}
        for item in self.critics[person1]:
            if item in self.critics[person2]:
                si[item] = 1
        if len(si) == 0:
            return 0
        sum_of_squres = sum([pow(self.critics[person1][item] - self.critics[person2][item], 2)
                             for item in si])
        return 1 / (1 + math.sqrt(sum_of_squres))

    def topMatches(self, person, n=5, similarity=sim_distance):
        scores = [(similarity(self, person, other), other)
                  for other in self.critics if other != person]
        scores.sort()
        scores.reverse()
        return scores[0:n]

    def getRecommendations(self, person, similarity=sim_distance):
        totals = {}
        simSums = {}
        for other in self.critics:
            if other == person:
                continue
            sim = similarity(self, person, other)

            if sim <= 0:
                continue
            for item in self.critics[other]:
                if item not in self.critics[person] or self.critics[person] == 0:
                    totals.setdefault(item, 0)
                    totals[item] += self.critics[other][item]*sim

                    simSums.setdefault(item, 0)
                    simSums[item] += sim

        rankings = [(totals[item]/simSums[item], item) for item in totals]
        rankings.sort()
        rankings.reverse()
        return rankings


if __name__ == '__main__':
    r = recommendation()
    # print r.sim_distance('Lisa Rose', 'Gene Seymour')
    # print r.topMatches('Lisa Rose', 3)
    print r.getRecommendations('Toby')
