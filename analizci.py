import datetime

# Hisse verileri (Bunları her gün buradan güncelleyebilirsin)
gunun_hisseleri = [
    {"hisse": "ASELS", "sinyal": "GÜÇLÜ AL", "hedef": "120.50"},
    {"hisse": "THYAO", "sinyal": "TUT", "hedef": "315.00"},
    {"hisse": "EREGL", "sinyal": "AL", "hedef": "62.00"}
]

rapor_tarihi = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

# signaliz_borsa.txt dosyasını oluşturma
with open("signaliz_borsa.txt", "w", encoding="utf-8") as f:
    f.write(f"--- SİGNALİZEHUB GÜNLÜK ANALİZ RAPORU ---\n")
    f.write(f"Tarih: {rapor_tarihi}\n")
    f.write(f"{'='*40}\n\n")
    
    f.write("🚀 GÜNÜN YILDIZ TABLOSU:\n\n")
    f.write(f"{'HİSSE':<10} | {'DURUM':<12} | {'HEDEF':<10}\n")
    f.write("-" * 38 + "\n")
    
    for hisse in gunun_hisseleri:
        f.write(f"{hisse['hisse']:<10} | {hisse['sinyal']:<12} | {hisse['hedef']:<10}\n")
    
    f.write(f"\n{'='*40}\n")
    f.write("💡 ANALİST NOTU:\n")
    f.write("Piyasadaki hacim artışı teknoloji hisselerini destekliyor.\n")
    f.write("Kısa vadeli direnç noktalarına dikkat edilmeli.\n")

print("Rapor başarıyla güncellendi! signaliz_borsa.txt dosyasını kontrol edebilirsin.")
