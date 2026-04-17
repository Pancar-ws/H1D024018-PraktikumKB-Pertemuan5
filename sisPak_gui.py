import tkinter as tk
from tkinter import messagebox, scrolledtext

gejala = {
    "G1": "Nafas abnormal", "G2": "Suara serak", "G3": "Perubahan kulit",
    "G4": "Telinga penuh", "G5": "Nyeri bicara menelan", "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher", "G8": "Pendarahan hidung", "G9": "Telinga berdenging",
    "G10": "Airliur menetes", "G11": "Perubahan suara", "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung", "G14": "Serangan vertigo", "G15": "Getah bening",
    "G16": "Leher bengkak", "G17": "Hidung tersumbat", "G18": "Infeksi sinus",
    "G19": "Beratbadan turun", "G20": "Nyeri telinga", "G21": "Selaput lendir merah",
    "G22": "Benjolan leher", "G23": "Tubuh tak seimbang", "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah", "G26": "Dahi sakit", "G27": "Batuk",
    "G28": "Tumbuh dimulut", "G29": "Benjolan dileher", "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga", "G32": "Tenggorokan gatal", "G33": "Hidung meler",
    "G34": "Tuli", "G35": "Mual muntah", "G36": "Letih lesu", "G37": "Demam"
}

penyakit = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

def jalankan_diagnosa():
    selected_indices = listbox_gejala.curselection()
    
    if not selected_indices:
        messagebox.showwarning("Peringatan", "Silakan pilih minimal satu gejala terlebih dahulu!")
        return

    kunci_gejala = list(gejala.keys())
    gejala_input = [kunci_gejala[i] for i in selected_indices]

    hasil_diagnosa = []
    
    for nama_penyakit, list_gejala_penyakit in penyakit.items():
        cocok = set(gejala_input).intersection(set(list_gejala_penyakit))
        persentase_kecocokan = (len(cocok) / len(list_gejala_penyakit)) * 100
        
        if persentase_kecocokan > 0:
            hasil_diagnosa.append({
                "penyakit": nama_penyakit,
                "kecocokan": persentase_kecocokan,
                "gejala_cocok": cocok
            })

    hasil_diagnosa = sorted(hasil_diagnosa, key=lambda x: x['kecocokan'], reverse=True)

    text_hasil.config(state=tk.NORMAL)
    text_hasil.delete(1.0, tk.END)    
    
    if hasil_diagnosa:
        text_hasil.insert(tk.END, "HASIL DIAGNOSA PENYAKIT THT:\n")
        text_hasil.insert(tk.END, "="*50 + "\n")
        for i, h in enumerate(hasil_diagnosa):
            gejala_teks = ", ".join([gejala[g] for g in h['gejala_cocok']])
            text_hasil.insert(tk.END, f"{i+1}. {h['penyakit']} (Tingkat Kecocokan: {h['kecocokan']:.2f}%)\n")
            text_hasil.insert(tk.END, f"   Gejala yang cocok: {gejala_teks}\n\n")
    else:
        text_hasil.insert(tk.END, "Gejala tidak mengarah ke penyakit manapun di dalam basis pengetahuan kami.")
        
    text_hasil.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Sistem Pakar Diagnosa THT")
root.geometry("650x550")
root.config(padx=20, pady=20)

label_judul = tk.Label(root, text="Aplikasi Sistem Pakar Penyakit THT", font=("Arial", 14, "bold"))
label_judul.pack(pady=(0, 10))

label_instruksi = tk.Label(root, text="Pilih gejala yang Anda alami pada daftar di bawah ini (bisa pilih lebih dari satu):")
label_instruksi.pack(anchor="w")

frame_listbox = tk.Frame(root)
frame_listbox.pack(fill=tk.BOTH, expand=True, pady=10)

scrollbar = tk.Scrollbar(frame_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_gejala = tk.Listbox(frame_listbox, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set, font=("Arial", 10), width=50)
for kode, nama in gejala.items():
    listbox_gejala.insert(tk.END, f"[{kode}] - {nama}")
listbox_gejala.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox_gejala.yview)

btn_diagnosa = tk.Button(root, text="Mulai Diagnosa", font=("Arial", 12, "bold"), bg="lightblue", command=jalankan_diagnosa)
btn_diagnosa.pack(pady=10)

label_hasil = tk.Label(root, text="Hasil Diagnosa:", font=("Arial", 10, "bold"))
label_hasil.pack(anchor="w")

text_hasil = scrolledtext.ScrolledText(root, height=10, width=70, font=("Arial", 10), state=tk.DISABLED)
text_hasil.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root.mainloop()