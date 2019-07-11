import numpy as np
#Save the Model file
import pickle
filename = './genrated_models/CorrosionCARF_mode2.sav'


#load the model File and predict
#Prediction
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))



#give todays rh , t , rainfall , so2,ph and ci value
def functionpredict(paramlist):
    # Average of all the param
    rh = 75.09
    t = 17.58
    rainfall = 159.74
    S02 = 0.089
    ph = 6.14
    ci = 0.221

    templist = paramlist
    test = []
    #better to use dictionary no time using list
    if templist[0] != 0 :
        rh = (rh + paramlist[0])/2
    test.append(rh)
    if templist[1] != 0 :
        t = (t + paramlist[0])/2
    test.append(t)
    if templist[1] != 0 :
        rainfall = (rainfall + paramlist[0])/2
    test.append(rainfall)

    if templist[1] != 0 :
        S02 = (S02 + paramlist[0])/2
    test.append(S02)
    if templist[1] != 0 :
        ph = (ph + paramlist[0])/2
    test.append(ph)
    if templist[1] != 0:
        ci = (ci + paramlist[0]) / 2
    test.append(ci)

    testdata = []
    testdata.append(test)
    #test = [[100,100,0,19,37,0]]
    result = loaded_model.predict(testdata)
    print(result)
    if result == "R5" :
        return {
            "result":"R5",
            "desc":"Corrosion Index: Very High , predicted corrosion rate : 40-60 um/a"}
    if result == "R4" :
        return {
            "result":"R4",
            "desc":"Corrosion Index :High , predicted corrosion rate : 33-40 um/a"}
    if result == "R3" :
        return {
            "result":"R3",
            "desc":"Corrosion Index :Medium ,predicted corrosion rate : 31-32 um/a"}
    if result == "R2" :
        return {
            "result":"R2",
            "desc":"Corrosion Index: Low , predicted corrosion rate : 29-30 um/a"}
    if result == "R1" :
        return {
            "result":"R1",
            "desc":"Corrosion Index : Very Low, predicted corrosion rate : 25-28 um/a"}


test = [75.09,17.58,159.74,0.089,6.14,0.221]
index = functionpredict(test)
print(index)