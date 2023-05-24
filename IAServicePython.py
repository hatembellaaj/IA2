import os
import sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
os.environ['AUTOGRAPH_VERBOSITY'] = '1'
#import tensorflow as tf
import tensorflow 
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
tensorflow.autograph.set_verbosity(0)
#from tn.mdweb.dsi.tfar import IAService

#class IAServicePython(IAService):
class IAServicePython():
    param=[]
    a1=""
    def preduction_keras(self):
        dataset=np.genfromtxt('matTab.csv',delimiter=',',skip_header=True,usecols=(1,6,7))
        model = Sequential()
        #model.compile(loss='mse', optimizer='rmsprop', metrics=['mse'])
        model.compile(loss='mse', optimizer='rmsprop', metrics=['accuracy'])
        model.add(Dense(12, input_dim=2, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(1, activation='linear'))
        x=dataset[:,0:2]
        y=dataset[:,2]
        model.fit(x,y,epochs=100)
        #predictions=model.predict(x)
        print("type x = " , type(x))
        #for i in range(5):
            #print('%s => %d (expected %d)' % (x[i].tolist(), predictions[i], y[i]))
            #self.a1=self.a1+"{a} => {b} (expected {c})\n".format(a=x[i].tolist(), b=predictions[i], c=y[i])
        
        
        #return self.a1;
        print("self.param = " , self.param)
        L = ['Math','Physique']
        x_test = np.asarray([self.param])
        print("x_test : ", x_test)
        p = model.predict(x_test)
        return p



print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

i=IAServicePython()
i.param.append(float(sys.argv[1]))
i.param.append(float(sys.argv[2]))

print("i.param : ", i.param)
print(i.preduction_keras())

