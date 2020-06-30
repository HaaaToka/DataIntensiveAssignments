
def resultF1(TP,FP,TN,FN):

   alll=TP+FP+TN+FN

   precision = TP/(TP+FP)
   recall = TP/(TP+FN)
   f1score= 2*(precision*recall)/(precision+recall)
   accuracy = (TP+TN) / (alll)
   error_rate = (FP+FN)/(alll)
   sensivity = TP / (TP+FP)

   print("Precision = ",precision)
   print("recall = ",recall)
   print("F1-Score = ",f1score)
   print("Accuracy = ",accuracy)
   print("error-rate = ",error_rate)
   print("sensivity = ",sensivity)

def perf_measure(y_actual, y_hat):
   TP = 0
   FP = 0
   TN = 0
   FN = 0

   for i in range(len(y_hat)): 
      if y_actual[i]==y_hat[i]==1:
         TP += 1
      if y_hat[i]==1 and y_actual[i]!=y_hat[i]:
         FP += 1
      if y_actual[i]==y_hat[i]==0:
         TN += 1
      if y_hat[i]==0 and y_actual[i]!=y_hat[i]:
         FN += 1

   print("TP\tFP\tTN\tFN")
   print(TP,"\t",FP,"\t",TN,"\t",FN)
   resultF1(TP,FP,TN,FN)

"""
   Actual
Positive  Negative
TP          FP       Positive    Prediction
FN          TN       Negative

"""
# y_true = [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]
# y_pred = [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]

# perf_measure(y_true,y_pred)
resultF1(96,8,19,4)




##############################################################


def jaccard_index(actual,predict):
   intersect = 0
   for i in range(len(actual)):
      if actual[i]==predict[i]:
         intersect+=1
   union = (2*len(actual))-intersect
   print(intersect/union)

act = [0,0,0,0,0,1,1,1,1,1]
pre = [1,1,0,0,0,1,1,1,1,1]

# jaccard_index(act,pre)



#########################################################


def logDenklem(xler,yler):
   xU,yU = sum(xler)/len(xler),sum(yler)/len(yler)
   print("Xu-Yu",xU,yU)

   theta0,theta1=0,0

   pay,payda=0,0
   for i in range(len(xler)):
      pay+=(xler[i]-xU)*(yler[i]-yU)
      payda+=(xler[i]-xU)**2
   
   theta1 = pay/payda
   theta0 = yU - (theta1*xU)
   print("yU =",theta0,"+",str(theta1)+"x1")

xs=[2,2.4,1.5,3.5,3.5,3.5,3.5,3.7,3.7]
ys=[196,221,136,255,244,230,232,255,267]
print(len(xs),len(ys))
logDenklem(xs,ys)


