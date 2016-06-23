#linear regression using covariance and variance

# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# import numpy as np
#
# X = [[6],[8],[10],[14],[18]]
# y = [[7],[9],[13],[17.5],[18]]
#
# plt.figure()
# plt.xlabel("diameter in inches")
# plt.ylabel("price in dollar")
# plt.plot(X,y,'k.')
#
# model = LinearRegression()
# model.fit(X,y)
#
# #mean
# print "prdicted is", model.predict(X)
# print "r squared is ", np.mean((model.predict(X)-y)**2)
#
# #variance
# print np.var(X,ddof=1)
#
# #covariance
# print np.cov([6,8,10,14,18],[7,9,13,17.5,18])[0][1]
# plt.axis([0,25,0,25])
# plt.grid(True)
# plt.show()


#multivariate and normal eq

# from numpy.linalg import  inv
# from numpy import dot, transpose
# X= [[1,6,2],[1,8,1],[1,10,0],[1,14,2],[1,18,0]]
# Y =[[7],[9],[13],[17.5],[18]]
#
# b = dot(inv(dot(transpose(X),X)),dot(transpose(X),Y))
# print b
# X_test = [[1,8,2],[1,9,0],[1,11,2],[1,16,2],[1,12,0]]
#
# pred_y = dot(X_test,b)
#
# print "predicted manually with normal equation"
# print pred_y
#
#
# from sklearn.linear_model import LinearRegression
#
# X_train= [[6,2],[8,1],[10,0],[14,2],[18,0]]
# Y_train =[[7],[9],[13],[17.5],[18]]
#
# model = LinearRegression()
# model.fit(X_train,Y_train)
#
#
# X_test = [[8,2],[9,0],[11,2],[16,2],[12,0]]
# Y_test = [[11],[8.5],[15],[18],[11]]
#
# print "prdicted using sklearn"
# prediction = model.predict(X_test)
# print prediction
#
# for i,pred in enumerate(prediction):
#     print "prdiction=",pred,"original=",Y_test[i]


#polynomila regression

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
#
# X_train = [[6],[8],[10],[14],[18]]
# Y_train = [[7],[9],[13],[17.5],[18]]
#
# X_test= [[6],[8],[11],[16]]
# Y_test =[[8],[12],[15],[18]]
#
# regressor =LinearRegression()
# regressor.fit(X_train,Y_train)
#
# xx = np.linspace(0,26,100)
# yy = regressor.predict(xx.reshape(xx.shape[0],1))
#
# plt.plot(xx,yy)


#pixel intesities

# from sklearn import datasets
# digits = datasets.load_digits()
# print digits
# print "Digigt:",digits.target[3]
# print digits.images[3]
# print "feature vector:", digits.images[3].reshape(-1,64)

import numpy as nps
from skimage.feature import corner_harris,corner_peaks
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.exposure import equalize_hist

def show_corners(corners,image):
    fig = plt.figure()
    plt.gray()
    plt.imshow(image)
    y_corner,x_corner = zip(*corners)
    plt.plot(x_corner,y_corner,'or')
    plt.xlim(0,image.shape[1])
    plt.ylim(image.shape[0],0)
    fig.set_size_inches(nps.array(fig.get_size_inches())*1.5)
    plt.show()

image  =io.imread('new.jpg')
image = equalize_hist(rgb2gray(image))
corners  =corner_peaks(corner_harris(image),min_distance=2)
show_corners(corners,image)
