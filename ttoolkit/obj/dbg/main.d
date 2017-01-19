../obj/dbg/main.o: main.cpp learner.h matrix.h rand.h baseline.h error.h filter.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -g -D_DEBUG -c main.cpp -o ../obj/dbg/main.o
