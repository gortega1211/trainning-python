# Reading a Memory-Mapped File With Python’s
import mmap
import timeit

def regular_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        text = file_obj.read()

def mmap_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read()

filename = "resources/the_history_of_don_quixote.txt"

print(timeit.repeat(
    "regular_io(filename)",
    repeat=3,
    number=1,
    setup="from __main__ import regular_io, filename"))

print(timeit.repeat(
"mmap_io(filename)",
    repeat=3,
    number=1,
    setup="from __main__ import mmap_io, filename"))

## mmap Object Creation
mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ)
# * ACCESS_READ creates a read-only memory map.
# * ACCESS_DEFAULT defaults to the mode specified in the optional prot argument, which is used for memory protection.
# * ACCESS_WRITE and ACCESS_COPY are the two write modes, which you’ll learn about below.

## mmap Objects as Strings
import mmap

def mmap_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            print(mmap_obj[10:20])

## Search a Memory-Mapped File
# * mmap operates on bytes, not strings.
import mmap
import timeit

def regular_io_find(filename):
    with open(filename, mode="r", encoding="utf-8") as file_obj:
        text = file_obj.read()
        print(text.find(" the "))

def mmap_io_find(filename):
    with open(filename, mode="r", encoding="utf-8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            print(mmap_obj.find(b" the "))
            pass

filename = "resources/the_history_of_don_quixote.txt"

print(timeit.repeat(
    "regular_io_find(filename)",
    repeat=3,
    number=1,
    setup="from __main__ import regular_io_find, filename"))

print(timeit.repeat(
    "mmap_io_find(filename)",
    repeat=3,
    number=1,
    setup="from __main__ import mmap_io_find, filename"))

import re
import mmap
import timeit

def mmap_io_re(filename):
    five_letter_word = re.compile(rb"\b[a-zA-Z]{5}\b")

    with open(filename, mode="r", encoding="utf-8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            for word in five_letter_word.findall(mmap_obj):
                print(word)

def regular_io_re(filename):
    five_letter_word = re.compile(r"\b[a-zA-Z]{5}\b")

    with open(filename, mode="r", encoding="utf-8") as file_obj:
        for word in five_letter_word.findall(file_obj.read()):
            print(word)

filename = "resources/the_history_of_don_quixote.txt"

print(timeit.repeat(
    "regular_io_re(filename)",
    repeat=3,
    number=1,
    setup="from __main__ import regular_io_re, filename"))

print(timeit.repeat(
    "mmap_io_re(filename)",
    repeat=3,
    number=1,
    setup="from __main__ import mmap_io_re, filename"))

## Memory-Mapped Objects as Files

import mmap

def mmap_io_find_and_seek(filename):
    with open(filename, mode="r", encoding="utf-8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            mmap_obj.seek(10000)
            mmap_obj.find(b" the ")

def regular_io_find_and_seek(filename):
    with open(filename, mode="r", encoding="utf-8") as file_obj:
        file_obj.seek(10000)
        text = file_obj.read()
        text.find(" the ")

import timeit

filename = "resources/the_history_of_don_quixote.txt"

print(timeit.repeat(
    "regular_io_find_and_seek(filename)",
    repeat=3,
    number=1,
    setup="from __main__ import regular_io_find_and_seek, filename"))
    
print(timeit.repeat(
    "mmap_io_find_and_seek(filename)",
    repeat=3,
    number=1,
    setup="from __main__ import mmap_io_find_and_seek, filename"))

## Writing a Memory-Mapped File With Python’s

# * ACCESS_WRITE specifies write-through semantics, meaning the data will be written through memory and persisted on disk.
# * ACCESS_COPY does not write the changes to disk, even if flush() is called.

import mmap

def mmap_io_write(filename, text):
    with open(filename, mode="w", encoding="utf-8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
            mmap_obj.write(text)
    
import mmap

def mmap_io_write(filename):
    with open(filename, mode="r+") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
            mmap_obj[10:16] = b"python"
            mmap_obj.flush()

## Search and Replace Text

import mmap
import os
import shutil

def regular_io_find_and_replace(filename):
    with open(filename, "r", encoding="utf-8") as orig_file_obj:
        with open("tmp.txt", "w", encoding="utf-8") as new_file_obj:
            orig_text = orig_file_obj.read()
            new_text = orig_text.replace(" the ", " eht ")
            new_file_obj.write(new_text)

    shutil.copyfile("tmp.txt", filename)
    os.remove("tmp.txt")

def mmap_io_find_and_replace(filename):
    with open(filename, mode="r+", encoding="utf-8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
            orig_text = mmap_obj.read()
            new_text = orig_text.replace(b" the ", b" eht ")
            mmap_obj[:] = new_text
            mmap_obj.flush()

import timeit

filename = "resources/the_history_of_don_quixote.txt"

print(timeit.repeat(
    "regular_io_find_and_replace(filename)",
    repeat=3,
    number=1,
    setup="from __main__ import regular_io_find_and_replace, filename"))

print(timeit.repeat(
    "mmap_io_find_and_replace(filename)",
    repeat=3,
    number=1,
    setup="from __main__ import mmap_io_find_and_replace, filename"))

## Sharing Data Between Processes With Python’s

import mmap

with mmap.mmap(-1, length=100, access=mmap.ACCESS_WRITE) as mmap_obj:
    mmap_obj[0:100] = b"a" * 100
    print(mmap_obj[0:100])

import mmap

def sharing_with_mmap():
    BUF = mmap.mmap(-1, length=100, access=mmap.ACCESS_WRITE)

    pid = os.fork()
    if pid == 0:
        # Child process
        BUF[0:100] = b"a" * 100
    else:
        time.sleep(2)
        print(BUF[0:100])

from multiprocessing import Process

def modify(buf):
    buf[0:100] = b"xy" * 50

if __name__ == "__main__":
    BUF = mmap.mmap(-1, length=100, access=mmap.ACCESS_WRITE)
    BUF[0:100] = b"a" * 100
    p = Process(target=modify, args=(BUF,))
    p.start()
    p.join()
    print(BUF[0:100])

from multiprocessing import Process
from multiprocessing import shared_memory

def modify(buf_name):
    shm = shared_memory.SharedMemory(buf_name)
    shm.buf[0:50] = b"b" * 50
    shm.close()

if __name__ == "__main__":
    shm = shared_memory.SharedMemory(create=True, size=100)

    try:
        shm.buf[0:100] = b"a" * 100
        proc = Process(target=modify, args=(shm.name,))
        proc.start()
        proc.join()
        print(bytes(shm.buf[:100]))
    finally:
        shm.close()
        shm.unlink()