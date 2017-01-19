../obj/opt/learner.o: learner.cpp learner.h matrix.h rand.h error.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -O3 -c learner.cpp -o ../obj/opt/learner.o
