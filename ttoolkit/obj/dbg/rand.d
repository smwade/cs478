../obj/dbg/rand.o: rand.cpp rand.h error.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -g -D_DEBUG -c rand.cpp -o ../obj/dbg/rand.o
