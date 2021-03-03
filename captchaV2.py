import numpy as np
import cv2
import time
#import torch
#from skimage.measure import compare_ssim
lis="123456789ABCDEFGHIJKLMNPQRSTUVWXYZ"
grayB=np.load("dat.npy")

#from matplotlib import pyplot
#error

def mse(imageA, imageB):

	err = np.sum((imageA.astype("int") - imageB.astype("int")) ** 2)
	err /= int(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def im2tx(grayA):
    temp=mse(grayA, grayB[0])
    ansa=lis[0]
    for x in range(len(lis)):
        #(score, diff) = compare_ssim(grayA, grayB[x], full=True)
        #score=0
        score= mse(grayA, grayB[x])
        #print(score)
#        for i in range(35):
#            for j in range(30):
#                if(grayB[x][i][j]==grayA[i][j]):
#                    score=score+1

        #score=score/140
        if(temp > score):
            temp= score
            ansa=lis[x]
    return ansa

#def im2txv(grayA):
#    temp=0
#    for x in range(len(lis)):
#        (score, diff) = compare_ssim(grayA, grayB[x], full=True)
#        if(temp < score):
#            temp= score
#            ans=lis[x]
#    return ans

def image2txt(path):


    a = cv2.imread(path,0) 
    #a = torch.from_numpy(am)
    for i in range(45):
        for j in range(180):
            if(a[i][j]!= 0 and a[i][j]!= 255 ):
                a[i][j]=255
            if(j%30==0 and a[i][j]==0):
                a[i][j]=255
                for x in range(5):
                    if((j-x)>=0):
                        a[i][j-x]=255
    for i in range(45):
        for j in range(180):           
            if(a[i][j]==0):
                if(i!=0 and j!=0 and i!=44 and j!=179):
                    if(a[i+1][j] ==255 and a[i+1][j+1]==255):
                        if( a[i-1][j] ==255 and a[i][j-1] ==255 and a[i][j+1]==255):
                            if(a[i+1][j-1] ==255 and a[i-1][j+1] ==255 and a[i-1][j-1]==255):
                                a[i][j]=255
    #a=np.dot(a,1/900000)
#    pyplot.imshow(a)
#    pyplot.show()
    #am=a
    #am=np.dot(am,.9)
    
    #pyplot.imshow(a)
    #pyplot.show()
    
    #see if you want extra dope performance over speed then enable this else wise its fine
#    a = np.asarray(cv2.blur(a,(2,2)))
#    for i in range(45):
#        for j in range(180):           
#            if(a[i][j]<255):
#                if( i!=44 and j!=179):
#                    if(a[i+1][j] >0 and a[i+1][j+1]>0):
#                        if( a[abs(i-1)][j]>0 and a[i][abs(j-1)] >0 and a[i][j+1]>0):
#                            if(a[i+1][abs(j-1)]>0 and a[abs(i-1)][j+1]>0 and a[abs(i-1)][j-1]>0):
#                                a[i][j]=255
#                if(i>44 or j>177):
#                    a[i][j]=255
#    for i in range(45):
#        for j in range(180):
#            if(a[i][j]<255):
#                a[i][j]=0
    data=""
    #data2=""
    for i in range(0,179,30):
        
        #s= a[10:45, i:i+30]
        sa=a[10:45, i:i+30]
        data=data+ (im2tx(sa))
        #data2=data2+im2txv(s)
        
    return data
#    if(data==data2):
#        #print(data)
#        return 1
#    else:
#        pyplot.imshow(a)
#        pyplot.show()    
#        pyplot.imshow(am)
#        pyplot.show() 
#        print(data , data2, sep="...")
#        return 0


    
z=input("Enter File Name:-")
if(z[-4:-3]!="."):
	z=z+".jpg"
print()
start_time = time.time()
print(image2txt(z))

print()
print("--- %s seconds ---" % (time.time() - start_time))    
  
print("Made by Vinc3nt all rights reserved" )
input()

