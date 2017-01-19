../obj/opt/error.o: error.cpp error.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -O3 -c error.cpp -o ../obj/opt/error.o
