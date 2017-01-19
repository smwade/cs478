../obj/dbg/filter.o: filter.cpp filter.h matrix.h learner.h rand.h error.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -g -D_DEBUG -c filter.cpp -o ../obj/dbg/filter.o
