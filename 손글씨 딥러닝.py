import numpy #numpy는 선형대수 (행렬, 벡터) 연산 수행하는 라이브러리
import scipy.special #시그모이드 함수 expit()을 사용하기 위해 scipy.special 불러옴
import matplotlib.pyplot #행렬 시각화를 위한 라이브러리

%matplotlib inline #시각화가 외부 윈도우가 아닌 현재의 노트북 내에서 보이도록 설정
 

class neuralNetwork: #신경망 클래스 정의

    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate): #신경망 초기화

        self.inodes=inputnodes #입력,은닉,출력 계층 노드 개수 설정
        self.onodes=outputnodes
        self.hnodes=hiddennodes

        #가중치 행렬
        #배열 내 가중치는 wab로 표시. 노드 a에서 다음 계층 노드 b로 연결됨을 의미.
        self.wih=numpy.random.normal(0.0,pow(self.hnodes,-0.5),(self.hnodes,self.inodes))
        self.who=numpy.random.normal(0.0,pow(self.onodes,-0.5),(self.onodes,self.hnodes))

        #학습률
        self.lr=learningrate

        #활성화 함수로 시그모이드 함수
        self.activation_function=lambda x: scipy.special.expit(x)

       
    #신경망 학습
    def train(self,inputs_list,targets_list):
        
        #입력 리스트를 2차원 행렬로 전환 *******이해 안가는 부분 있음***********
        #1.몇행 몇열인지는 안 정함? 전치행렬은 왜 함?
        inputs=numpy.array(inputs_list,ndmin=2).T
        targets=numpy.array(targets_list,ndmin=2).T

        #은닉 계층으로의 입력값을 가중치와 입력값을 "행렬 내적"함      
        hidden_inputs=numpy.dot(self.wih,inputs)
        #이건 활성화 함수 씌우고 은닉에서의 출력값 계산
        hidden_outputs=self.activation_function(hidden_inputs)

        
  
        final_inputs=numpy.dot(self.who,hidden_outputs)

        final_outputs=self.activation_function(final_inputs)

        
        #출력 계층의 오차 = 실제(목표)값-계산(출력)값
        output_errors=targets-final_outputs
        #은닉 계층 오차는 가중치에 의해 나뉜 출력 계층의 오차들을 재조합해 계산.
        hidden_errors=numpy.dot(self.who.T,output_errors)

        #훈련 시 진행상황을 보기위해 임의의 가중치 값 출력
        print(self.who[9][9])
        
        #은닉~출력 가중치 업뎃
        self.who+=self.lr*numpy.dot((output_errors*final_outputs*(1.0-final_outputs)),numpy.transpose(hidden_outputs))
        #입력~은닉 가중치 업뎃
        self.wih+=self.lr*numpy.dot((hidden_errors*hidden_outputs*(1.0-hidden_outputs)),numpy.transpose(inputs))

        
    #질의
    def query(self,inputs_list):
        
        #입력 리스트를 2차원으로 변환
        inputs=numpy.array(inputs_list,ndmin=2).T

        
        #은닉 인풋
        hidden_inputs=numpy.dot(self.wih,inputs)
        #히든 아웃풋
        hidden_outputs=self.activation_function(hidden_inputs)

        
        #파이널 인풋
        final_inputs=numpy.dot(self.who,hidden_outputs)
        #파이널 아웃풋
        final_outputs=self.activation_function(final_inputs)
        
        return final_outputs

#입력,은닉,출력 노드의 
input_nodes=784 
hidden_nodes=200
output_nodes=10

#학습률
learning_rate=0.1

#신경망의 인스턴스 생성
n=neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)

    
#mnist학습 데이터 csv파일을 불러온다.
training_data_file=open("mnist_train.csv","r")
training_data_list=training_data_file.readlines()
training_data_file.close()

#학습 주기 (데이터가 사용되는 횟수)
epochs=5

i=1 #몇번째 훈련인지 보여주기 위해

for e in range(epochs):
    
    #학습 데이터 모음 내의 모든 레코드 탐색
    for record in training_data_list:
     
        #레코드를 쉼표에 의해 분리
        all_values=record.split(',')
       
        #입력 값의 범위와 값 조정
        #최댓값이 255이고 255로 나눠서 0~1값으로 만든 뒤 0.99 곱하고 0.01을 더함
        #따라서 0이 안 나오게 만들었음
        inputs=(numpy.asfarray(all_values[1:])/255.0*0.99)+0.01
        
        #결과 값 생성 (실제 값인 0.99 외엔 모두 0.01)
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
