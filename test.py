import sys
f = open(sys.argv[1],'w',encoding="utf-8")  #test5에서 넘겨준 방식처럼 argv[1]자리에 우리가 만든 파일을 argv로 넘겨줌.넘겨줄때 우리가 이름을 정해주면 그 정해준 이름대로 파일이 생성됨.
#오전에는 file이름을 hard-code 시켰다.
#오후에 commandline arument로 받겠다.
for i in range(1,10):
     f.write(sys.argv[2]+"\n") #만들어준 파일이름에 들어갈 내용
f.close()


from Work.b import Addb


