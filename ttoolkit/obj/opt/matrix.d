../obj/opt/matrix.o: matrix.cpp matrix.h rand.h error.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -O3 -c matrix.cpp -o ../obj/opt/matrix.o
