K=int(input())
bin_K=format(K+1,'b')[1:] #2진수로 변환하여 가장 앞의 자리를 제외하고 가져온다.
print(bin_K.replace('0','4').replace('1','7'))  #0은4로 1은7로 변환하여 준다.
