import pickle

dataObject={"key":"val","key2":"val2"}

with open("data.pickle","wb")as filehandle:
    pickle.dump(dataObject)