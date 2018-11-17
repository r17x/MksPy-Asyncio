import time
from datetime import datetime


def Tidur():
    print('TIDUR {}\n'.format(datetime.now()))
    time.sleep(1)


def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print('Tugas {}: Menghitung factorial({})'.format(name, i))
        Tidur()
        f *= i
    print('Tugas {}: factorial({}) adalah {}\n'.format(name, number, f))


start = time.time()

daftarTugas = [
    factorial("A", 10),
    factorial("B", 4),
    factorial("C", 3),
    factorial("D", 2),
    factorial("E", -2),
]

map(lambda tugas: tugas(), daftarTugas)

"""
for i in daftarTugas:
    i()
"""

end = time.time()

print("Total time: {}".format(end - start))
