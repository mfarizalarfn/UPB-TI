print("Nama : Febro Herdyanto")
print("NIM : 312010043")
print("Kelas : TI.20.B.1")
print("=======================")
print()

kontak = {"Ari": "085215565501", "Dina": "08788767778"}
print("Nama | Nomor Telepon")
print("Menampilkan Dictionary Kontak")
print(kontak)
print("----------------------------------------------")
print("Menampilkan Kontak Ari")
print(kontak['Ari'])
print("----------------------------------------------")
print("Menambahkan kontak baru dengan nama Riko - 087654544")
kontak['Riko'] = '087654544'
print(kontak['Riko'])
print("----------------------------------------------")
print("Ubah kontak Dina dengan nomor baru 088999776")
kontak['Dina'] = '088999776'
print(kontak['Dina'])
print("----------------------------------------------")
print("Tampilkan semua Nama")
print(kontak.keys())
print("----------------------------------------------")
print("Tampilkan semua Nomor")
print(kontak.values())
print("----------------------------------------------")
print("Tampilkan daftar nama dan nomor")
print(kontak.items())
print("----------------------------------------------")
print("Hapus kontak Dina")
del kontak['Dina']
print(kontak)