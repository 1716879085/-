def lossfunciton(b, w, points):
    cnt = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        cnt += (y - (w * x + b)) ** 2
    return cnt / float(len(points))

def gradient(b,w,points,learningRate):
    b = 0

