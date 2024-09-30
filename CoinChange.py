def main():
    x = int(input("Masukkan nominal koin: "))

    arr = [1000, 500, 200, 100]
    i = 0

    while x > 0 and i < len(arr):
        jumlahKoin = x // arr[i] 
        if jumlahKoin > 0:
            print(f"Koin {arr[i]}: {jumlahKoin}")
        x = x % arr[i]  
        i += 1  

if __name__ == "__main__":
    main()
