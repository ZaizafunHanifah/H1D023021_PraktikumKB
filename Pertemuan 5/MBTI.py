import tkinter as tk
from pyswip import Prolog
from tkinter import messagebox
from tkinter import ttk

prolog = Prolog()
prolog.consult("MBTI.pl")

dimensi = ["ei", "sn", "tf", "jp"]
index_dimensi = 0
index_pertanyaan = 0
pertanyaan_dimensi = dict()
current_gejala = ""

def mulai_diagnosa():
    global index_dimensi, index_pertanyaan, pertanyaan_dimensi
    prolog.retractall("jawaban(_)")

    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)

    index_dimensi = 0
    index_pertanyaan = -1

    pertanyaan_dimensi = {
        d: [p["X"] for p in list(prolog.query(f"pertanyaan({d}, X)"))] for d in dimensi
    }

    pertanyaan_selanjutnya()

def pertanyaan_selanjutnya():
    global index_dimensi, index_pertanyaan, current_gejala

    while index_dimensi < len(dimensi):
        d = dimensi[index_dimensi]
        daftar_pertanyaan = pertanyaan_dimensi.get(d, [])

        index_pertanyaan += 1
        if index_pertanyaan < len(daftar_pertanyaan):
            current_gejala = daftar_pertanyaan[index_pertanyaan]
            hasil = list(prolog.query(f"teks_pertanyaan({current_gejala}, T)"))
            if hasil:
                tampilkan_pertanyaan(hasil[0]["T"])
            return
        else:
            index_dimensi += 1
            index_pertanyaan = -1

    hasil_diagnosa()

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"jawaban({current_gejala})")
    pertanyaan_selanjutnya()

def hasil_diagnosa():
    hasil = list(prolog.query("mbti(Tipe)"))
    if hasil:
        messagebox.showinfo("Hasil MBTI", f"Tipe kepribadian Anda: {hasil[0]['Tipe']}")
    else:
        messagebox.showinfo("Hasil MBTI", "Tidak dapat menentukan tipe kepribadian.")

    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

root = tk.Tk()
root.title("Sistem Pakar MBTI")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Tes Kepribadian MBTI", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(mainframe, height=4, width=40, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = tk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = tk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(mainframe, text="Mulai Tes", command=mulai_diagnosa)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()
