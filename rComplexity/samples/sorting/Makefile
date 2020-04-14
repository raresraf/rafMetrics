SRCS = $(wildcard *.c)
PROGS = $(patsubst %.c,%,$(SRCS))

all: $(PROGS)

%: %.c
	$(CC) $(CFLAGS) -std=c99 -o $@.out $<

clean:
	rm *.out
