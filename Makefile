CC = gcc
 
all: main.o sort_data.o
	$(CC) -o main.exe main.o sort_data.o
	$(CC) -fPIC -shared -o dll_lib.so main.o sort_data.o
	del *.o

main.o: src/main.c	inc/main.h inc/sort_data.h
	$(CC) -Iinc -g3 -Wall -c src/main.c

sort_data.o: src/sort_data.c		inc/sort_data.h
	$(CC) -Iinc -g3 -Wall -c src/sort_data.c
	
clean:
	del -rf *.s *.o *.exe *.so