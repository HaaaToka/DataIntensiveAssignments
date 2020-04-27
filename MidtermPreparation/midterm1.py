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


y_true = [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]
y_pred = [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0]

perf_measure(y_true,y_pred)