# concurrency in python using tread


import asyncio

async def make_tea():
    print("Boiling water...")
    await asyncio.sleep(2)
    print("Tea ready!")

async def make_snacks():
    print("Frying samosa...")
    await asyncio.sleep(3)
    print("Samosa ready!")

async def main():
    await asyncio.gather(make_tea(), make_snacks())

asyncio.run(main())




# Parallelism with multiprocessing):

from multiprocessing import Process
import time

def make_cha():
    print("Boiling water...")
    time.sleep(2)
    print("Tea ready!")

def make_snack():
    print("Frying samosa...")
    time.sleep(3)
    print("Samosa ready!")

if __name__ == "__main__":
    p1 = Process(target=make_cha)
    p2 = Process(target=make_snack)

    p1.start()
    p2.start()

    p1.join()
    p2.join()  # join means , we have complete the work and now just come back to me please







# queue





from multiprocessing import Process, Queue
import time

def producer(q):
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)   # queue তে data পাঠানো
        time.sleep(1)
    q.put(None)  # কাজ শেষের সংকেত

def consumer(q):
    while True:
        item = q.get()   # queue থেকে data নেওয়া
        if item is None:
            break
        print(f"Consuming {item}")
        time.sleep(2)

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()




# //value

from multiprocessing import Process, Value
import time

def increment(counter):
    for _ in range(100):
        with counter.get_lock():   # lock করে update করা
            counter.value += 1
        time.sleep(0.01)

if __name__ == "__main__":
    counter = Value('i', 0)   # 'i' মানে integer, শুরুতে 0

    processes = [Process(target=increment, args=(counter,)) for _ in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("Final Counter Value:", counter.value)


#
#
# 1. Asyncio, Event loop, Coroutine, Await
#
# 👉 ভাবো – তুমি একা ঘরে রান্না করছো। ভাত বসিয়েছো, এখন সেটা ফোটার জন্য ১০ মিনিট অপেক্ষা করতে হবে।
#
# যদি সাধারণ ফাংশন হয় → তুমি শুধু দাঁড়িয়ে থাকবা (ব্লকড হয়ে গেলো)।
#
# কিন্তু যদি coroutine + await ব্যবহার করো → ভাত ফোটার অপেক্ষায় থাকাকালীন তুমি মাছ কাটতে পারো, ডাল ধুতে পারো, মানে সময় নষ্ট হবে না।
#
#  Python-এ এরকম করার জন্য asyncio event loop ব্যবহার হয় → ওটাই ঠিক করে কে কখন চলবে।




import asyncio

async def cook_rice():
    print("ভাত বসানো হলো")
    await asyncio.sleep(3)   # ভাত রান্না হচ্ছে
    print("ভাত হয়ে গেছে")

async def cut_fish():
    print("মাছ কাটা শুরু")
    await asyncio.sleep(1)
    print("মাছ কাটা শেষ")

async def main():
    await asyncio.gather(cook_rice(), cut_fish())  # দুইটা একসাথে চলবে

asyncio.run(main())


# 👉 এখানে মাছ কাটার সময় ভাতও রান্না হচ্ছে। (সমান্তরাল কাজ = efficiency)




# Asyncio একটি পাইথন লাইব্রেরি যা async/await সিনট্যাক্স ব্যবহার করে অ্যাসিঙ্ক্রোনাস (একই সাথে একাধিক কাজ করার ক্ষমতা)
# # এবং নন-ব্লকিং কোড লিখতে সাহায্য করে। এর মূল কাজ হলো একটি ইভেন্ট লুপ ব্যবহার করে একাধিক কাজ একসাথে চালানো,
# # যাতে একটি কাজ শেষ হওয়ার জন্য অপেক্ষা করার সময় অন্য কাজ চলতে পারে, যেমন ডেটাবেস সংযোগ, নেটওয়ার্ক রিকোয়েস্ট বা ফাইল পড়া ইত্যাদি।




# 1. Asyncio, Event loop, Coroutine, Await
#
# 👉 ভাবো – তুমি একা ঘরে রান্না করছো। ভাত বসিয়েছো, এখন সেটা ফোটার জন্য ১০ মিনিট অপেক্ষা করতে হবে।
#
# যদি সাধারণ ফাংশন হয় → তুমি শুধু দাঁড়িয়ে থাকবা (ব্লকড হয়ে গেলো)।
#
# কিন্তু যদি coroutine + await ব্যবহার করো → ভাত ফোটার অপেক্ষায় থাকাকালীন তুমি মাছ কাটতে পারো, ডাল ধুতে পারো, মানে সময় নষ্ট হবে না।
#
# 🔹 Python-এ এরকম করার জন্য asyncio event loop ব্যবহার হয় → ওটাই ঠিক করে কে কখন চলবে।
#
# উদাহরণ:

import asyncio

async def cook_rice():
    print("ভাত বসানো হলো")
    await asyncio.sleep(3)   # ভাত রান্না হচ্ছে
    print("ভাত হয়ে গেছে")

async def cut_fish():
    print("মাছ কাটা শুরু")
    await asyncio.sleep(1)
    print("মাছ কাটা শেষ")

async def main():
    await asyncio.gather(cook_rice(), cut_fish())  # দুইটা একসাথে চলবে

asyncio.run(main())


# 👉 এখানে মাছ কাটার সময় ভাতও রান্না হচ্ছে। (সমান্তরাল কাজ = efficiency)






#
# 🟠 2. Mixing Threads with Asyncio
#
# 👉 ভাবো তুমি অনলাইনে রান্নার ভিডিও স্ট্রিম করছো (asyncio কাজ), সাথে রান্নার সময় এক্সেল ফাইল খুলে কোনো ক্যালকুলেশন করছো (thread এর কাজ, কারণ এক্সেল ব্লক করে)।
#
# Async দিয়ে নেটওয়ার্ক হ্যান্ডল করা যাবে।
#
# Thread দিয়ে heavy blocking task আলাদা করে চালানো যাবে।
#
# উদাহরণ:

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def heavy_task():
    time.sleep(2)   # ব্লকিং কাজ
    return "কাজ শেষ!"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, heavy_task)
        print(result)

asyncio.run(main())


# 👉 এখানে asyncio event loop থেমে যায়নি, বরং thread-এ কাজ চালিয়ে দিয়েছে।








#
# 🟠 3. Asyncio + Multiprocessing
#
# 👉 CPU-heavy কাজ (যেমন: বড় সংখ্যা ক্যালকুলেশন, AI মডেল ট্রেনিং) thread এ ভালো চলে না, কারণ GIL (Python-এর একটা লক)।
# তাই multiprocessing ব্যবহার হয় – প্রতিটা প্রসেস আলাদা CPU core-এ চলে।
#
# উদাহরণ:

import asyncio
from concurrent.futures import ProcessPoolExecutor

def big_calculation(n):
    return sum(i*i for i in range(n))

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, big_calculation, 10**6)
        print("ফলাফল:", result)

asyncio.run(main())


# 👉 এখানে Asyncio network task হ্যান্ডেল করবে, heavy CPU task প্রসেসে চালাবে।






#
# 🟠 4. Daemon vs Non-Daemon Threads
#
# 👉 ধরো তুমি ঘুমাতে যাচ্ছো।
#
# Daemon worker = বিদ্যুৎ ফ্যান → তুমি ঘুমাতে গেলে ফ্যানও বন্ধ হয়ে যাবে।
#
# Non-Daemon worker = রান্নার হাঁড়ি চুলায় → তুমি ঘুমালেও সেটা শেষ না হওয়া পর্যন্ত চালু থাকবে।
#
# উদাহরণ:

import threading
import time

def worker():
    while True:
        print("কাজ চলছে...")
        time.sleep(1)

t = threading.Thread(target=worker, daemon=True)  # Daemon
t.start()
time.sleep(3)
print("Main thread শেষ → worker-ও শেষ হয়ে গেল")





# 🟠 5. Race Condition & Deadlock
#
# 👉 Race Condition উদাহরণ:
# দুইজন একই সাথে ব্যাংক অ্যাকাউন্ট থেকে টাকা তুলছে। যদি দুজন একসাথে ১০০ টাকা দেখে, দুজনই ১০০ তুলবে → শেষে হিসাব গড়মিল হবে।
# 🔹 সমাধান: Lock ব্যবহার করা।
#
# Deadlock উদাহরণ:
#
# A lock নিয়েছে কলসি, B lock নিয়েছে ডোল।
#
# এখন A ডোল চাইছে, B কলসি চাইছে → দুজনেই একে অপরের জন্য বসে আছে → deadlock।

# 🟢 FastAPI-তে এগুলোর ব্যবহার
#
# FastAPI একেবারে asyncio ভিত্তিক।
#
# প্রতিটা API request একটি coroutine হিসেবে চলে।
#
# Event loop একই সাথে অনেকগুলো request হ্যান্ডল করতে পারে।
#
# যদি ভারি কাজ থাকে (ইমেজ প্রসেসিং/ML model), সেটা আলাদা thread বা process এ চালাতে হবে।

# FastAPI Example:

# from fastapi import FastAPI
# import asyncio
# from concurrent.futures import ThreadPoolExecutor
#
# app = FastAPI()
#
# # Async endpoint (I/O কাজ)
# @app.get("/download")
# async def download_data():
#     await asyncio.sleep(2)  # simulate async I/O
#     return {"msg": "ডাউনলোড শেষ"}
#
# # Thread এ চালানো (Blocking কাজ)
# @app.get("/heavy")
# async def heavy_task():
#     loop = asyncio.get_running_loop()
#     with ThreadPoolExecutor() as pool:
#         result = await loop.run_in_executor(pool, lambda: sum(i*i for i in range(10**6)))
#     return {"result": result}


# 👉 এভাবে FastAPI একসাথে অনেক API call হ্যান্ডল করতে পারে, আবার CPU-heavy কাজকে আলাদা thread/process এ দিয়ে দেয়।




# মাল্টিপ্রসেসিং হলো এমন একটি পদ্ধতি যেখানে একটি কম্পিউটার সিস্টেমের একাধিক প্রসেসিং ইউনিট (যেমন সিপিইউ) একই
# সময়ে একটি প্রোগ্রাম বা একাধিক প্রোগ্রামকে প্রক্রিয়াজাত করে, যার ফলে কম্পিউটারের সামগ্রিক কর্মক্ষমতা বাড়ে। এর মূল কাজ হলো
# কাজগুলোকে ভাগ করে একাধিক প্রসেসরে সমান্তরালভাবে চালানো, যা কর্মক্ষমতা বৃদ্ধি করে এবং বড় কাজগুলো দ্রুত সম্পন্ন করে


