'''Nama = Tariq Ahmad
    Nim = 2400597
    Kelas= RPL 1B'''


def fibonacci(n):
    
    deret_fibonacci = [1, 2]
    
    for i in range(2, n):
        nilai_selanjutnya = deret_fibonacci[-1] + deret_fibonacci[-2]
        deret_fibonacci.append(nilai_selanjutnya)
    
    return deret_fibonacci[:n]

N = int(input("n kali deret fibonacci = "))

hasil_fibonacci = fibonacci(N)
print("Deret Fibonacci sebanyak", N, "angka:", hasil_fibonacci)
