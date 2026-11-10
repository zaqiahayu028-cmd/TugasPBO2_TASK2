class Mahasiswa:
    def __init__(self, nim, nama, prodi, angkatan):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.angkatan = angkatan

    def __str__(self):
        return f"{self.nim} - {self.nama}"