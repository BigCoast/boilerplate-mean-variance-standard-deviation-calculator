import numpy as np

def calculate(list):
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    
    matrix=np.array(list).reshape(3,3)

    calculations={}
    calculations["mean"]=[[i for i in matrix.mean(axis=0)],[i for i in matrix.mean(axis=1)],matrix.mean()]
    calculations["variance"]=[[i for i in matrix.var(axis=0)],[i for i in matrix.var(axis=1)],matrix.var()]
    calculations["standard deviation"]=[[i for i in matrix.std(axis=0)],[i for i in matrix.std(axis=1)],matrix.std()]
    calculations["max"]=[[i for i in matrix.max(axis=0)],[i for i in matrix.max(axis=1)],matrix.max()]
    calculations["min"]=[[i for i in matrix.min(axis=0)],[i for i in matrix.min(axis=1)],matrix.min()]
    calculations["sum"]=[[i for i in matrix.sum(axis=0)],[i for i in matrix.sum(axis=1)],matrix.sum()]


    return calculations