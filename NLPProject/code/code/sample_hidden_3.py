import tensorflow as tf
import numpy as np 
import pickle


with open("../data/input_shak.txt",'r') as pd:
	text = pd.read()

with open("../data/uniqueChar.pickle",'rb') as uc:
	unique_char = pickle.load(uc)

with open("../data/uniqueCharToInt.pickle",'rb') as uc1:
	uniqueCharToInt = pickle.load(uc1)

with open("../data/intToUniqueChar.pickle",'rb') as uc2:
	intToUniqueChar = pickle.load(uc2)

nOutputs = len(unique_char)
nInputs = len(unique_char)
nHiddenUnits = 512
nSteps = 1
path = "../hidden_3_shak/"

x = tf.placeholder(tf.float32,[None,nInputs])

hPrev1 = tf.placeholder(tf.float32,[nHiddenUnits,1])
cPrev1 = tf.placeholder(tf.float32,[nHiddenUnits,1])

hPrev2 = tf.placeholder(tf.float32,[nHiddenUnits,1])
cPrev2 = tf.placeholder(tf.float32,[nHiddenUnits,1])

hPrev3 = tf.placeholder(tf.float32,[nHiddenUnits,1])
cPrev3 = tf.placeholder(tf.float32,[nHiddenUnits,1])

weights = {
    # (nInputs, nHiddenUnit1)
    'input': tf.Variable(tf.random_normal([nInputs, nHiddenUnits]), name = 'weightsIn'),

    'i1' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]), name = 'weightsi1'),
    'f1' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]),name = 'weightsf1'),
    'o1' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]),name = 'weightso1'),
    'g1' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]),name = 'weightsg1'),
    # (nHiddenUnits1, nOutputs)

    'hh' : tf.Variable(tf.random_normal([nHiddenUnits,nHiddenUnits]), name = 'weightshh'),

    'i2' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]), name = 'weightsi2'),
    'f2' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]),name = 'weightsf2'),
    'o2' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]),name = 'weightso2'),
    'g2' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]),name = 'weightsg2'),

    'hhh' : tf.Variable(tf.random_normal([nHiddenUnits,nHiddenUnits]), name = 'weightshhh'),

    'i3' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]), name = 'weightsi3'),
    'f3' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]),name = 'weightsf3'),
    'o3' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]),name = 'weightso3'),
    'g3' : tf.Variable(tf.random_normal([nHiddenUnits,(2 * nHiddenUnits)]),name = 'weightsg3'),

    # (nHiddenUnits1, nOutputs)
    'output': tf.Variable(tf.random_normal([nHiddenUnits, nOutputs]),name = 'weightsOut')
}
biases = {
    # (nHiddenUnits1, )
    'input': tf.Variable(tf.constant(0.0, shape=[nHiddenUnits, ]),name = 'biasesIn'),

    'i1' : tf.Variable(tf.constant(0.00,shape=[nHiddenUnits, ]), name = 'biasesi1'),
    'f1' : tf.Variable(tf.constant(0.00,shape=[nHiddenUnits, ]), name = 'biasesf1'),
    'o1' : tf.Variable(tf.constant(0.00,shape=[nHiddenUnits, ]), name = 'biaseso1'),
    'g1' : tf.Variable(tf.constant(0.00,shape=[nHiddenUnits, ]), name = 'biasesg1'),

    'hh' : tf.Variable(tf.constant(0.0,shape=[nHiddenUnits, ]), name = 'biaseshh'),

    'i2' : tf.Variable(tf.constant(0.0,shape=[nHiddenUnits, ]), name = 'biasesi2'),
    'f2' : tf.Variable(tf.constant(0.0,shape=[nHiddenUnits, ]), name = 'biasesf2'),
    'o2' : tf.Variable(tf.constant(0.0,shape=[nHiddenUnits, ]), name = 'biaseso2'),
    'g2' : tf.Variable(tf.constant(0.0,shape=[nHiddenUnits, ]), name = 'biasesg2'),    

    'hhh' : tf.Variable(tf.constant(0.0,shape=[nHiddenUnits, ]), name = 'biaseshhh'),

    'i3' : tf.Variable(tf.constant(0.0,shape=[nHiddenUnits, ]), name = 'biasesi3'),
    'f3' : tf.Variable(tf.constant(0.0,shape=[nHiddenUnits, ]), name = 'biasesf3'),
    'o3' : tf.Variable(tf.constant(0.0,shape=[nHiddenUnits, ]), name = 'biaseso3'),
    'g3' : tf.Variable(tf.constant(0.0,shape=[nHiddenUnits, ]), name = 'biasesg3'),    


    # (nOutputs, )
    'output': tf.Variable(tf.constant(0.0, shape=[nOutputs, ]), name = 'biasesOut')
}



def cell(x,cPrev,hPrev, layer):
	
	x = tf.reshape(x,[nHiddenUnits,1])
	hPrev = tf.reshape(hPrev,[nHiddenUnits,1])
	cPrev = tf.reshape(cPrev,[nHiddenUnits,-1])

	
	ic = tf.reshape(tf.concat([hPrev,x], axis = 0),[2*nHiddenUnits,-1])
	ib = tf.reshape(biases['i'+str(layer)],[nHiddenUnits,-1])
	i = tf.sigmoid(tf.matmul(weights['i' + str(layer)],ic) + ib)

	fc = tf.reshape(tf.concat([hPrev,x], axis = 0),[2*nHiddenUnits,-1])
	fb = tf.reshape(biases['f'+str(layer)],[nHiddenUnits,-1])
	f = tf.sigmoid(tf.matmul(weights['f'+str(layer)],fc) + fb)

	oc = tf.reshape(tf.concat([hPrev,x], axis = 0),[2*nHiddenUnits,-1])
	ob = tf.reshape(biases['o'+str(layer)],[nHiddenUnits,-1])
	o = tf.sigmoid(tf.matmul(weights['o'+str(layer)],oc) + ob)

	gc = tf.reshape(tf.concat([hPrev,x], axis = 0),[2*nHiddenUnits,-1])
	gb = tf.reshape(biases['g'+str(layer)],[nHiddenUnits,-1])
	g = tf.tanh(tf.matmul(weights['g'+str(layer)],gc) + gb)

	
	cCurrent = tf.add(tf.multiply(f,cPrev) , tf.multiply(i,g))
	hCurrent = tf.multiply(o,tf.tanh(cCurrent))

	return cCurrent,hCurrent

	
def unroll_LSTM(x, cPrev, hPrev,layer):
	cStates = list()
	hStates = list()
	
	for i in range(nSteps):
		cCurrent,hCurrent = cell(x[i],cPrev,hPrev, layer)
		cStates.append(cCurrent)
		hStates.append(hCurrent)

		cPrev = cCurrent
		hPrev = hCurrent
		
		
	return tf.reshape(hStates,[nSteps,nHiddenUnits]),tf.reshape(cPrev,[nHiddenUnits,1]),tf.reshape(hPrev,[nHiddenUnits,1])

x = tf.reshape(x,[-1,nInputs])

inputHidden1 = tf.add(tf.matmul(x,weights['input']),biases['input'])

hStates1,cPrev1Batch,hPrev1Batch = unroll_LSTM(inputHidden1, cPrev1, hPrev1,1)

inputHidden2 = tf.matmul(hStates1, weights['hh']) + biases['hh']

hStates2,cPrev2Batch,hPrev2Batch = unroll_LSTM(inputHidden2, cPrev2,hPrev2,2)

inputHidden3 = tf.matmul(hStates2, weights['hhh']) + biases['hhh']

hStates3,cPrev3Batch,hPrev3Batch = unroll_LSTM(inputHidden3,cPrev3,hPrev3,3)

results = tf.matmul(hStates3, weights['output']) + biases['output']
results = tf.nn.softmax(tf.reshape(results,[nSteps,nOutputs]))



saver = tf.train.Saver()
with tf.Session() as sess:
	saver.restore(sess,path + "model_checkpoint/save_net.ckpt")
	print ("Model Restored")
	cPrev1Sess = np.zeros(shape = [nHiddenUnits,1])
	hPrev1Sess = np.zeros(shape = [nHiddenUnits,1])
	cPrev2Sess = np.zeros(shape = [nHiddenUnits,1])
	hPrev2Sess = np.zeros(shape = [nHiddenUnits,1])
	cPrev3Sess = np.zeros(shape = [nHiddenUnits,1])
	hPrev3Sess = np.zeros(shape = [nHiddenUnits,1])

	for t in text[:100]:
		ch = np.zeros(shape = [1,nInputs])
		ch[0,uniqueCharToInt[t]] = 1
		nextCharProb, cPrev3Sess, hPrev3Sess, cPrev2Sess, hPrev2Sess, cPrev1Sess, hPrev1Sess = sess.run([results, cPrev3Batch, hPrev3Batch, cPrev2Batch,hPrev2Batch,cPrev1Batch,hPrev1Batch],{ x : ch, cPrev1 : cPrev1Sess, hPrev1 : hPrev1Sess, cPrev2 : cPrev2Sess, hPrev2 : hPrev2Sess, cPrev3 : cPrev3Sess, hPrev3 : hPrev3Sess})



	predictedChar = []
	startChar = np.zeros(shape = [1,nInputs])
	startChar[0,uniqueCharToInt[text[100]]] = 1

	for i in range(1000):
		nextCharProb, cPrev3Sess, hPrev3Sess, cPrev2Sess, hPrev2Sess, cPrev1Sess, hPrev1Sess = sess.run([results, cPrev3Batch, hPrev3Batch, cPrev2Batch,hPrev2Batch,cPrev1Batch,hPrev1Batch],{ x : ch, cPrev1 : cPrev1Sess, hPrev1 : hPrev1Sess, cPrev2 : cPrev2Sess, hPrev2 : hPrev2Sess, cPrev3 : cPrev3Sess, hPrev3 : hPrev3Sess})
		nextCharIndex = np.random.choice(range(nOutputs), p = nextCharProb.ravel())
		nextChar = intToUniqueChar[nextCharIndex]
		predictedChar.append(nextChar)
		startChar = np.zeros(shape = [1,nInputs])
		startChar[0,nextCharIndex] = 1
		
	print ("text sampled")
	print ("".join(predictedChar))

	with open("sampledTextHidden3.txt","w") as f:
		f.write("".join(predictedChar))

	## evaluate the model for all the testing set characters

	cPrev1Sess = np.zeros(shape = [nHiddenUnits,1])
	hPrev1Sess = np.zeros(shape = [nHiddenUnits,1])
	cPrev2Sess = np.zeros(shape = [nHiddenUnits,1])
	hPrev2Sess = np.zeros(shape = [nHiddenUnits,1])
	cPrev3Sess = np.zeros(shape = [nHiddenUnits,1])
	hPrev3Sess = np.zeros(shape = [nHiddenUnits,1])

	acc = []

	for i,t in enumerate(text[:1000]):
		ch = np.zeros(shape = [1,nInputs])
		ch[0,uniqueCharToInt[t]] = 1
		nextCharProb, cPrev3Sess, hPrev3Sess, cPrev2Sess, hPrev2Sess, cPrev1Sess, hPrev1Sess = sess.run([results, cPrev3Batch, hPrev3Batch, cPrev2Batch,hPrev2Batch,cPrev1Batch,hPrev1Batch],{ x : ch, cPrev1 : cPrev1Sess, hPrev1 : hPrev1Sess, cPrev2 : cPrev2Sess, hPrev2 : hPrev2Sess, cPrev3 : cPrev3Sess, hPrev3 : hPrev3Sess})
		nextCharIndex = np.random.choice(range(nOutputs), p = nextCharProb.ravel())
		nextChar = intToUniqueChar[nextCharIndex]
		if (i+1) < len(text):
			if nextChar == text[i+1]:
				acc.append(1)
			else:
				acc.append(0)
	#print acc
	print (np.mean(acc))


