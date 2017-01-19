../obj/dbg/matrix.o: matrix.cpp matrix.h rand.h error.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -g -D_DEBUG -c matrix.cpp -o ../obj/dbg/matrix.o
