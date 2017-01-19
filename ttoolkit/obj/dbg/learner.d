../obj/dbg/learner.o: learner.cpp learner.h matrix.h rand.h error.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -g -D_DEBUG -c learner.cpp -o ../obj/dbg/learner.o
