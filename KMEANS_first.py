import random
import math
import numpy as np
import matplotlib.pyplot as plt


# k == 2 임을 생각하고 짜보자
# L == 10 개의 점이 random 하게 분포되어있다고 가정


# 여기서부터는 sample point 생성

points = np.empty([0,1])
targets = np.empty([0,1])
red_cluster = np.empty([0,1])
yellow_cluster = np.empty([0,1])

red_dummy = None
yellow_dummy = None


k = 2
L = 20

random.seed(1)


for i in range(L):
    random_point = np.array([random.random(), random.random()])
    if i == 0:
        targets = np.append(targets, random_point)
    else:
        targets = np.vstack([targets, random_point])


plt.scatter(targets[:, :1], targets[:, 1:], c = 'g', alpha=1)

random.seed(10)

for i in range(k):
    random_point = np.array([random.random(), random.random()])
    if i == 0:
        points = np.append(points, random_point)
    else:
        points = np.vstack([points, random_point])

plt.scatter(points[:, :1], points[:, 1:], c = 'r', alpha=1)


print(targets)
print(points)

def u_distance(p1, p2):

    dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    return dist

def is_changed(cluster_1, cluster_2):

    return not np.array_equal(cluster_1, cluster_2)


plt.show()

def get_cluster_center(cluster):

    len_ = len(cluster) + 0.000001
    sum_x = np.sum(cluster[:, :1])
    sum_y = np.sum(cluster[:, 1:])

    return sum_x/len_ + sum_y/len_



while True:

    if not is_changed(red_dummy, red_cluster):
        break

    for i in range(L):

        if u_distance(points[0], targets[i]) > u_distance(points[1], targets[i]):

            if len(red_cluster) == 0:
                red_cluster = np.append(red_cluster, targets[i])
            else:
                #print("red cluster shape, type:", red_cluster.shape, type(red_cluster))
                red_cluster = np.vstack([red_cluster, targets[i]])
        else:
            if len(yellow_cluster) == 0:
                yellow_cluster = np.append(yellow_cluster, targets[i])
            else:
                yellow_cluster = np.vstack([yellow_cluster, targets[i]])

    plt.scatter(red_cluster[:, :1], red_cluster[:, 1:], c = 'r', alpha=1)
    plt.scatter(yellow_cluster[:, :1], yellow_cluster[:, 1:], c = 'y', alpha=1)

    plt.show()

    points[0] = np.array([get_cluster_center(red_cluster)])
    points[1] = np.array([get_cluster_center(yellow_cluster)])

    red_dummy = red_cluster.copy()
    yellow_dummy = yellow_cluster.copy()

    red_cluster = np.empty([0,1])
    yellow_cluster = np.empty([0,1])





