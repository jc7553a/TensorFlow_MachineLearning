import tensorflow as tf
import numpy as np
import pylab
from random import randint
#import scipy
from matplotlib.pylab import *
import pandas as pd


def normalize(train):
    train = np.array(train)
    shape = np.shape(train)
    
    k = 0
    while k <shape[1]:
        maxim = 0
        minim = 0
        for i in range(shape[0]):
            if train[i][k] > maxim:
                maxim = train[i][k]
            if train[i][k] < minim:
                minim = train[i][k]
        denom = maxim - minim
        if denom == 0:
            denom = .0000000001
        for t in range(shape[0]):
            train[t][k] = (train[t][k] - minim)/denom
        k +=1

    return train


def changePoints(mat):
    delta = 0.3


    n = len(mat)

    b = -2
    c = 2
    r = 4
    d = (c-b)/(r-2)
    eps = .7
    gamma = 0.1

    xi = np.zeros((n, r))

    B = b*np.ones((n,1))
    C = c*np.ones((n,1))


    temp = np.zeros((n,1))

    for i in range(n):
        if mat[i] <= B[i][0]:
            xi[i][0] = 1
        else:
            xi[i][0] = 0
    j = 1
#while j < r:
    for h in range(n):
        if mat[h] > C[h][0]:
            xi[h][3] = 1
        else:
            xi[h][3] = 0
    #j +=1

    m = 2
    temp = np.zeros((n,1))
    temp2 = np.zeros((n,1))
    temp3 = np.zeros((n,1))

    while m < r:
        
        for i in range(n):
            if mat[i] > B[i][0]+(d*(m-2)):
                temp[i][0] = 1
            else:
                temp[i][0] = 0
        for j in range(n):
            if mat[j] <= B[i][0] +(d*(m-1)):
                temp2[j][0] = 1
            else:
                temp2[j][0] = 0
    #print(temp2)
        for t in range(n):
            temp3[t][0] = temp[t][0]*temp2[t][0]
        for q in range(n):
            xi[q][m-1] = temp3[q][0]
        m = m+1

    #print(xi)

    k = 1
    p = np.zeros((1,r))
    q = np.zeros((1,r))
    S = []

    while k < n-3:
        mean = 0
        'Find P'
        for i in range(r):
            for h in range(k):
                mean += xi[h][i]
            mean = mean/k
            p[0][i] = mean

        'Find q'
        mean = 0
        for j in range(r):
            beb = k
            while beb < n:
                mean += xi[beb][j]
                beb +=1
            mean = mean/(n-k)
            q[0][j] = mean
        #if k ==2:
            #print(p)
        'Find u'
        u = 0
        for i in range(r):
            if q[0][i] == 0:
                u+=1
        ep = eps/(n-k)

        z = np.zeros((r,1))
    #S = np.zeros(((n-3),1))
        for m in range(r):
            if p[0][m] > 0:
                if u == 0:
                    z[m][0] = p[0][m] *np.log(p[0][m]/q[0][m])
                elif q[0][m] == 0:
                    z[m][0] = p[0][m]*np.log(p[0][m]/ ep*u)
                else:
                    z[m][0] = p[0][m] *np.log(p[0][m]/q[0][m]/(1-ep))
            adder = 0
        for u in range(r):
            adder += z[u][0]
        S.append(adder) 
        k +=1


    margin = gamma*n
    t = int(margin)
    temp = -1
    while t < int(n-margin):
        if S[t] > temp:
            temp = S[t]
        t +=1
    print(temp)
    
    Smax = max(S[(int(margin)):(int(n-margin))])
    k = (int (margin))
    while k < (int(n-margin)):
        if S[k] > Smax -0.0000001:
            nuhat = k
        k +=1
    print("NUHAT")
    print(nuhat)
    W = []
    for i in range(n):
        W.append(0)

    for i in range(800):
        W[i+100] = max([0, W[i+99]+S[i+100]-S[i+99]])

    plot(W)
    show()
        
    
print("Training on Class 1 ")

mat =[]
for line in open('shuttleTrain.txt').readlines():
    holder = line.split(' ')
    i = 0
    for i in range (len(holder)):
            holder[i] = float(holder[i])
    mat.append(holder)



Fours = []
for j in range(len(mat)):
    if mat[j][9] == 1:
        Fours.append(mat[j][:])
Fours.sort(key=lambda row: row[0:])
shape = np.shape(Fours)



Fours = np.delete(Fours, [0,9],1)
Fours = normalize(Fours)

shuttleData = np.array(Fours).astype('float32')
shape = np.shape(shuttleData)


mat2 =[]
for line in open('shuttleTest.txt').readlines():
    holder = line.split(' ')
    i = 0
    for i in range (len(holder)):
            holder[i] = float(holder[i])
    mat2.append(holder)

class1 = []
class2 = []
class3 = []
class4 = []
class5 = []
class6 = []
class7 = []

for w in range(len(mat2)):
    if mat2[w][9] == 1:
        class1.append(mat2[w][:])
    if mat2[w][9] == 2:
        class2.append(mat2[w][:])
    if mat2[w][9] == 3:
        class3.append(mat2[w][:])
    if mat2[w][9] == 4:
        class4.append(mat2[w][:])
    if mat2[w][9] == 5:
        class5.append(mat2[w][:])
    if mat2[w][9] == 6:
        class6.append(mat2[w][:])
    if mat2[w][9] == 7:
        class7.append(mat2[w][:])

class1.sort(key=lambda row: row[0:])
class2.sort(key=lambda row: row[0:])
class3.sort(key=lambda row: row[0:])
class4.sort(key=lambda row: row[0:])
class5.sort(key=lambda row: row[0:])
class6.sort(key=lambda row: row[0:])
class7.sort(key=lambda row: row[0:])

class1 = normalize(class1)
class2 = normalize(class2)
class3 = normalize(class3)
class4 = normalize(class4)
class5 = normalize(class5)
class6 = normalize(class6)
class7 = normalize(class7)

class1 = np.delete(class1, [0,9], 1)
class2 = np.delete(class2, [0,9],1)
class3 = np.delete(class3, [0,9], 1)
class4 = np.delete(class4, [0,9],1)
class5 = np.delete(class5, [0,9], 1)
class6 = np.delete(class6, [0,9], 1)
class7 = np.delete(class7, [0,9], 1)


shapeTest = np.shape(class1)
shapeTest2 = np.shape(class2)
shapeTest3 = np.shape(class3)
shapeTest4 = np.shape(class4)
shapeTest5 = np.shape(class5)
shapeTest6 = np.shape(class6)
shapeTest7 = np.shape(class7)




shuttleTest = np.array(class1[0:shapeTest[0]][:]).astype('float32')
shuttleTest2 = np.array(class2[0:shapeTest2[0]][:]).astype('float32')
shuttleTest3 = np.array(class3[0:shapeTest3[0]][:]).astype('float32')
shuttleTest4 = np.array(class4[0:shapeTest4[0]][:]).astype('float32')
shuttleTest5 = np.array(class5[0:shapeTest5[0]][:]).astype('float32')
shuttleTest6 = np.array(class6[0:shapeTest6[0]][:]).astype('float32')
shuttleTest7 = np.array(class7[0:shapeTest7[0]][:]).astype('float32')




n_hidden = 5
n_features = shape[1]



x = tf.placeholder(tf.float32 , [None , n_features], name = 'x')
#learnRate = tf.placeholder(tf.float32, shape = [], name = 'LR')

'Weights and Biases to Hidden Layer'

w = tf.Variable(tf.truncated_normal([n_features ,n_hidden], stddev = .001), name = 'weights_h')
b = tf.Variable(tf.truncated_normal([n_hidden], stddev = .001), name = 'biases_h')

'Weights and Biases to Output Layer'
wo = tf.Variable(tf.truncated_normal([n_hidden, n_features],stddev = .001), name = 'weights_o')
bo = tf.Variable(tf.truncated_normal([n_features], stddev = .001), name = 'biases_o')

'Calculations for Encoder and Decoder'
encoder = tf.nn.sigmoid(tf.matmul(x, w) + b)
#hidden1 = tf.nn.sigmoid(tf.matmul(encoder, w2)+b2)
#hidden2 = tf.nn.sigmoid(tf.matmul(hidden1, w3)+b3)
decoder = tf.matmul(encoder, wo) +bo
y = decoder



'Objective Functions'
y_true = tf.placeholder(tf.float32, [None, n_features], name = 'y_true')
loss = tf.reduce_mean(tf.square(y_true - y))
optimizer = tf.train.GradientDescentOptimizer(.05).minimize(loss)
#train = optimizer.minimize(loss)



'Uncomment to Look at Graph and Nodes'
#print(tf.get_default_graph().as_graph_def())

losses = []
mini_epochs = 400
batch_size = 5


'Load Graph'
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)



train_losses = []
print("Start Training Batches....")
batchTot = []
for t in range(200):
    batch_losses = []
    for y in range(mini_epochs):
        rando = randint(0,shape[0]-5)
        batch_xs = shuttleData[rando:rando+batch_size][0:shape[1]]
        batch_ys = shuttleData[(rando):(rando+batch_size)][0:shape[1]]
        sess.run(optimizer, feed_dict = {x: batch_xs, y_true: batch_ys})
        batch_losses.append(sess.run(loss, feed_dict = {x: batch_xs, y_true: batch_ys}))
    if t%10 ==0:
        batchTot.append(np.average(batch_losses))
#plot(batchTot)
#show()


print("Start Online Training....")
for q in range(4):
    losses = []
    for t in range(shape[0]-1):
        temp = randint(0,shape[0]-1) 
        batch_xs = [shuttleData[temp][0:shape[1]]]
        batch_ys = [shuttleData[temp][0:shape[1]]]
        sess.run(optimizer, feed_dict = {x: batch_xs, y_true: batch_ys})
        losses.append(sess.run(loss, feed_dict = {x: batch_xs, y_true: batch_ys}))
   # print(np.average(losses))



test_losses = []
print("")
print("Testing....")
print("")

for u in range(1000):
    bobweir = np.array([shuttleTest[u][:]])
    test_act = np.array([shuttleTest[u][:]])
    #sess.run([train], feed_dict = {x: bobweir, y_true: test_act})
    check =tf.sigmoid(tf.matmul(bobweir, w)+b)
    check2 = tf.matmul(check, wo)+bo
    test_losses.append(sess.run(tf.reduce_sum(tf.square(check2 - test_act))))
    
'''
mean = np.average(test_losses)
print("Class 1 Average Loss ", mean)
print("")
'''

test_losses2 = []
for l in range(shapeTest2[0]):
    bobweir = np.array([shuttleTest2[l][:]])
    test_act = np.array([shuttleTest2[l][:]])
    check =tf.sigmoid(tf.matmul(bobweir, w)+b)
    check2 = tf.matmul(check, wo)+bo
    test_losses2.append(sess.run(tf.reduce_sum(tf.square(check2 - test_act))))
'''
mean =(np.average(test_losses2))

print("Class 2 Average Loss ", mean)
print("")
'''
test_losses3 = []
for l in range(shapeTest3[0]):
    bobweir = np.array([shuttleTest3[l][:]])
    test_act = np.array([shuttleTest3[l][:]])
    check =tf.sigmoid(tf.matmul(bobweir, w)+b)
    check2 = tf.matmul(check, wo)+bo
    test_losses3.append(sess.run(tf.reduce_sum(tf.square(check2 - test_act))))
'''
mean =(np.average(test_losses3))
print("Class 3 Average Loss ", mean)
print("")
'''

test_losses4 = []
for z in range(2):
    bobweir = np.array([shuttleTest4[z][:]])
    test_act = np.array([shuttleTest4[z][:]])
    check =tf.sigmoid(tf.matmul(bobweir, w)+b)
    check2 = tf.matmul(check, wo)+bo
    test_losses4.append(sess.run(tf.reduce_sum(tf.square(check2 - test_act))))
'''
mean=(np.average(test_losses4))
print("Class 4 Average Loss ", mean)
print("")
'''
test_losses5 = []
for v in range(2):
    bobweir = np.array([shuttleTest5[v][:]])
    test_act = np.array([shuttleTest5[v][:]])
    check =tf.sigmoid(tf.matmul(bobweir, w)+b)
    check2 = tf.matmul(check, wo)+bo
    test_losses5.append(sess.run(tf.reduce_sum(tf.square(check2 - test_act))))
'''
mean = (np.average(test_losses5))
print("Class 5 Average ", mean)
print("")
'''

test_losses6 = []
for r in range(shapeTest6[0]):
    bobweir = np.array([shuttleTest6[r][:]])
    test_act = np.array([shuttleTest6[r][:]])
    check =tf.sigmoid(tf.matmul(bobweir, w)+b)
    check2 = tf.matmul(check, wo)+bo
    test_losses6.append(sess.run(tf.reduce_sum(tf.square(check2 - test_act))))
'''
mean = (np.average(test_losses6))
print("Class 6 Average ", mean)
print("")
'''
test_losses7 = []
for s in range(shapeTest7[0]):
    bobweir = np.array([shuttleTest7[s][:]])
    test_act = np.array([shuttleTest7[s][:]])
    check =tf.sigmoid(tf.matmul(bobweir, w)+b)
    check2 = tf.matmul(check, wo)+bo
    test_losses7.append(sess.run(tf.reduce_sum(tf.square(check2 - test_act))))
'''
mean = (np.average(test_losses7))
print("Class 7 Average ", mean)
print("")
'''

positive = 0
falsePositive = 0
negative = 0
falseNegative = 0
mean = 0
for i in range(len(test_losses)):
    mean = mean + test_losses[i]

mean = mean /len(test_losses)
stdDev = np.std(test_losses)
threshhold = mean + 1.25*stdDev

conf = []


for j in range(len(test_losses)):
    if test_losses[j] > threshhold:
        falseNegative += 1
        conf.append(1)
    else:
        positive += 1
        conf.append(0)


for i in range(len(test_losses4)):
    if test_losses4[i] > threshhold:
        negative +=1
        conf.append(1)
    else:
        falsePositive += 1
        conf.append(0)
        
for i in range(len(test_losses5)):
    if test_losses5[i] > threshhold:
        negative += 1
        conf.append(1)
    else:
        falsePositive += 1
        conf.append(0)
for i in range(len(test_losses3)):
    if test_losses3[i] > threshhold:
        negative += 1
        conf.append(1)
    else:
        falsePositive += 1
        conf.append(0)

for i in range(len(test_losses2)):
    if test_losses2[i] > threshhold:
        negative += 1
        conf.append(1)
    else:
        falsePositive += 1
        conf.append(0)
for i in range(len(test_losses6)):
    if test_losses6[i] > threshhold:
        negative += 1
        conf.append(1)
    else:
        falsePositive += 1
        conf.append(0)
        
for i in range(len(test_losses7)):
    if test_losses7[i] > threshhold:
        negative += 1
        conf.append(1)
    else:
        falsePositive += 1
        conf.append(0)

acts = []
for i in range(len(test_losses)):
    acts.append(0)
longL = len(test_losses4)+len(test_losses2)+len(test_losses3)+len(test_losses5)+len(test_losses6)+len(test_losses7)
for j in range(longL):
    acts.append(1)
'''
print("Positive ", positive)
print("False Positive ", falsePositive)
print("Negative ", negative)
print("False Negative ", falseNegative)
'''
tot = negative+positive +falsePositive + falseNegative
pos = negative + positive
acc = float(pos/tot)
y_pred = pd.Series(conf, name = 'Predicted')
y_act = pd.Series(acts, name = 'Actual')
df_confusion = pd.crosstab(y_pred, y_act, rownames = ['Actual'], colnames = ['Predicted'], margins = True)
print(df_confusion)
print("")
print("True Positive ", positive)
print("False Positive ", falsePositive)
print("True Negative ", negative)
print("False Negative ", falseNegative)
print("")
print("Accuracy % = ", acc*100)
print("")
changePoints(test_losses)
print("")
print(test_losses)
