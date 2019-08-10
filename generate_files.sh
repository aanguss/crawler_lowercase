#! /bin/bash
# for n in {1..1000}; do
#     dd if=/dev/urandom of=file$( printf %03d "$n" ).bin bs=1 count=$(( RANDOM + 1024 ))
# done

# seq -w 1 10 | xargs -n1 -I% sh -c 'dd if=/dev/urandom of=file.% bs=$(shuf -i1-10 -n1) count=1024'

# for i in {1..5}; do mktemp File$i.XXX; done

for i in {1..5}; do mktemp $(head -c 100 /dev/urandom | tr -dc 'a-z' | fold -w 5 | head -n 1).XXX; done

for i in {1..5}; do mktemp -d XXX.$(mktemp -u XXX); done