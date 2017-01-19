../obj/opt/filter.o: filter.cpp filter.h matrix.h learner.h rand.h error.h
	g++ -I/usr/local/include/SDL -D_THREAD_SAFE -DDARWIN -I/sw/include -I../../../src -no-cpp-precomp -O3 -c filter.cpp -o ../obj/opt/filter.o
