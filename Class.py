class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, lebar {self.lebar} cm,"
    
    def main():
        try:
            panjang = float(input("Masukkan Panjang Persegi Panjang (cm): "))
            lebar = float(input("Masukkan Lebar Persegi Panjang (cm): "))
            pp = PersegiPanjang(panjang, lebar)
            print(pp)
            print("Keliling :", pp.keliling(), "cm")    
            print("Luas :", pp.luas(), "cm²")
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    PersegiPanjang.main()