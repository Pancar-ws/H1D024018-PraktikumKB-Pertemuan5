def tampilkan_daftar_gejala():
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
    
    print("="*50)
    print("SISTEM PAKAR DIAGNOSA PENYAKIT THT")
    print("="*50)
    print("Daftar Gejala yang Tersedia:")
    
    items = list(gejala.items())
    for i in range(0, len(items), 2):
        col1 = f"{items[i]}: {items[i][1]}"
        col2 = f"{items[i+1]}: {items[i+1][1]}" if i+1 < len(items) else ""
        print(f"{col1:<35} {col2}")
    print("="*50)
    return gejala

def diagnosa(gejala_input):
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
    return hasil_diagnosa

def main():
    dict_gejala = tampilkan_daftar_gejala()
    
    print("\nMasukkan kode gejala yang Anda alami.")
    print("Gunakan koma untuk memisahkan jika lebih dari satu (Contoh: G37, G12, G5)")
    input_user = input("Input kode gejala: ").upper().replace(" ", "").split(",")
    
    gejala_valid = [g for g in input_user if g in dict_gejala]
    
    if not gejala_valid:
        print("\nKode gejala tidak valid atau tidak ditemukan. Silakan jalankan ulang aplikasi.")
        return

    print("\nGejala yang Anda alami:")
    for g in gejala_valid:
        print(f"- {g}: {dict_gejala[g]}")

    print("\nMelakukan diagnosa...")
    hasil = diagnosa(gejala_valid)

    if hasil:
        print("\nHASIL DIAGNOSA:")
        for i, h in enumerate(hasil[:3]):
            gejala_teks = ", ".join([dict_gejala[g] for g in h['gejala_cocok']])
            print(f"{i+1}. Penyakit: {h['penyakit']} (Kecocokan: {h['kecocokan']:.2f}%)")
            print(f"   Gejala cocok: {gejala_teks}")
    else:
        print("\nMaaf, sistem tidak dapat mendiagnosa penyakit berdasarkan gejala tersebut.")

if __name__ == "__main__":
    main()