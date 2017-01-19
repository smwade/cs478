../obj/dbg/error.o: error.cpp error.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -g -D_DEBUG -c error.cpp -o ../obj/dbg/error.o
