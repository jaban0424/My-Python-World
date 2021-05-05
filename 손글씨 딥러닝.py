import numpy

import scipy.special

import matplotlib.pyplot

 

%matplotlib inline

 

class neuralNetwork:

    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):

        self.inodes=inputnodes

        self.onodes=outputnodes

        self.hnodes=hiddennodes

        

        self.wih=numpy.random.normal(0.0,pow(self.hnodes,-0.5),(self.hnodes,self.inodes))

        self.who=numpy.random.normal(0.0,pow(self.onodes,-0.5),(self.onodes,self.hnodes))

        

        self.lr=learningrate

        

        self.activation_function=lambda x: scipy.special.expit(x)

        

    def train(self,inputs_list,targets_list):

        inputs=numpy.array(inputs_list,ndmin=2).T

        targets=numpy.array(targets_list,ndmin=2).T

        

        hidden_inputs=numpy.dot(self.wih,inputs)

        hidden_outputs=self.activation_function(hidden_inputs)

        

        final_inputs=numpy.dot(self.who,hidden_outputs)

        final_outputs=self.activation_function(final_inputs)

        

        output_errors=targets-final_outputs

        hidden_errors=numpy.dot(self.who.T,output_errors)

        #print(self.who)
        print(self.who[9][9])
        self.who+=self.lr*numpy.dot((output_errors*final_outputs*(1.0-final_outputs)),numpy.transpose(hidden_outputs))
        
        #print(self.wih)
        #print(self.wih[9][9])
        self.wih+=self.lr*numpy.dot((hidden_errors*hidden_outputs*(1.0-hidden_outputs)),numpy.transpose(inputs))

        

    def query(self,inputs_list):

        inputs=numpy.array(inputs_list,ndmin=2).T

        

        hidden_inputs=numpy.dot(self.wih,inputs)

        hidden_outputs=self.activation_function(hidden_inputs)

        

        final_inputs=numpy.dot(self.who,hidden_outputs)

        final_outputs=self.activation_function(final_inputs)

        

        return final_outputs

    

input_nodes=784

hidden_nodes=200

output_nodes=10

 

learning_rate=0.1

 

n=neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)

    

training_data_file=open("mnist_train.csv","r")

training_data_list=training_data_file.readlines()

training_data_file.close()

 

epochs=5

 
i=1
for e in range(epochs):

    for record in training_data_list:
        
        all_values=record.split(',')

        inputs=(numpy.asfarray(all_values[1:])/255.0*0.99)+0.01

        targets=numpy.zeros(output_nodes)+0.01

        targets[int(all_values[0])]=0.99

        print(i,"번째 훈련")
        n.train(inputs,targets)
        i+=1
 
print("\n====================훈련끝=======================\n")
test_data_file=open("mnist_test.csv","r")

test_data_list=test_data_file.readlines()

test_data_file.close()

 

scorecard=[]



for record in test_data_list:

    all_values=record.split(',')

    correct_label=int(all_values[0])

    inputs=(numpy.asfarray(all_values[1:])/255.0*0.99)+0.01

    outputs=n.query(inputs)

    label=numpy.argmax(outputs)
    image_array=numpy.asfarray(all_values[1:]).reshape((28,28))
    matplotlib.pyplot.imshow(image_array,cmap='Greys',interpolation='None')
    print("컴퓨터가 낸 정답 : ",label)
    #print(correct_label,"is correct answer")

    if(label==correct_label):

        scorecard.append(1)
        print("정답!")

    else:

        scorecard.append(0)
        print("오답!")
        
scorecard_array=numpy.asarray(scorecard)

print("정답률 = ",scorecard_array.sum()/scorecard_array.size)
