../obj/opt/main.o: main.cpp learner.h matrix.h rand.h baseline.h error.h filter.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -O3 -c main.cpp -o ../obj/opt/main.o
