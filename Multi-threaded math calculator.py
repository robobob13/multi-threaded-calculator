import threading
import time
def find(x):
  while True:
    print("x")
 
t1 = threading.Thread(target=find, args=(0,))
t2 = threading.Thread(target=find, args=(10,))
t3 = threading.Thread(target=find, args=(20,))
t4 = threading.Thread(target=find, args=(30,))
t5 = threading.Thread(target=find, args=(40,))
t6 = threading.Thread(target=find, args=(50,))
t7 = threading.Thread(target=find, args=(60,))
t8 = threading.Thread(target=find, args=(70,))
t9 = threading.Thread(target=find, args=(80,))
t10 = threading.Thread(target=find, args=(90,))
t11 = threading.Thread(target=find, args=(100,))
t12 = threading.Thread(target=find, args=(110,))
t13 = threading.Thread(target=find, args=(120,))
t14 = threading.Thread(target=find, args=(130,))
t15 = threading.Thread(target=find, args=(140,))
t16 = threading.Thread(target=find, args=(150,))
# starting threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()

# wait until threads are completely executed
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()
t13.join()
t14.join()
t15.join()
t16.join()
 
#all are done
print("Done")
