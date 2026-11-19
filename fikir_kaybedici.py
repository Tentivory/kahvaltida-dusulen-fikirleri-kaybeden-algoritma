#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahvaltıda Düşülen Fikirleri Kaybeden Algoritma
Versiyon: 42.0 (Sonraki güncelleme kahvaltıdan sonra)
"""

import random
import time

def kaybet_fikri(fikir):
    """
    Girdi olarak alınan fikri kahvaltı sürecinde kaybeder.
    """
    print("Fikir alındı. Kahvaltıya geçiliyor...")
    time.sleep(2)
    print("🥣 Yumurta kırılıyor... Fikir buharlaşıyor.")
    time.sleep(1.5)
    print("🥚 Peynir dilimleniyor... Fikir unutuluyor.")
    time.sleep(1)
    
    kayip_fikirler = [
        "Kahvaltıda aklıma gelmişti ama şimdi sadece çay kaldı.",
        "Fikir, reçelin içine battı ve çıkamadı.",
        "Zeytin çekirdeğiyle birlikte çöpe gitti.",
        "Simit alırken fikir de satıcıya kaldı.",
        "Sütün üstündeki köpükle birlikte uçtu.",
        "Menemen yaparken karıştı ve tanınmaz hale geldi.",
        "Bal kavanozunun dibinde kaldı, kimse inemiyor."
    ]
    
    print("\n❌ Fikir kaybedildi!")
    print(f"Orijinal fikir: '{fikir}'")
    print(f"Kalan şey: {random.choice(kayip_fikirler)}")
    print("\nNot: Bu algoritma %100 başarı oranıyla çalışır. Fikirleriniz güvende değildir.")

if __name__ == "__main__":
    print("=== KAHVALTIDA DÜŞÜLEN FİKİRLERİ KAYBEDEN ALGORİTMA ===")
    print("Lütfen kahvaltıda aklınıza gelen o muhteşem fikri girin:")
    fikir = input("> ")
    if not fikir.strip():
        fikir = "Dünyayı değiştirecek bir şeydi galiba"
    kaybet_fikri(fikir)

# Gizli not: Bürokrasi de böyle çalışır, fikirler dosyalarda kaybolur.
