../obj/opt/rand.o: rand.cpp rand.h error.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -O3 -c rand.cpp -o ../obj/opt/rand.o
