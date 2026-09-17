#!/usr/bin/env python3
"""
Agroecological Cover Crop Weed Suppression Planner
==================================================
Questo strumento valuta e classifica diverse specie di colture di copertura (cover crops)
per la soppressione biologica delle erbe infestanti senza l'ausilio di diserbanti chimici.

I punteggi e i pesi si basano su evidenze della letteratura scientifica agroecologica:
- Menalled & Ryan (2026), Sci Rep (PMID: 42129302)
- Eroğlu et al. (2026), Front Plant Sci (PMID: 41959575)
- Menalled et al. (2023), Sci Rep (PMID: 37833350)
- Fernando & Shrestha (2023), Plants (PMID: 36840100)
"""

import sys
import argparse
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class CoverCrop:
    common_name: str
    scientific_name: str
    family: str
    recommended_seasons: List[str]
    biomass_score: float          # 1 - 10 (potenziale di biomassa secca per mulch)
    canopy_closure_score: float    # 1 - 10 (rapidità di chiusura chioma e ombreggiamento)
    allelopathy_score: float       # 1 - 10 (attività allelopatica biochimica)
    mechanisms: List[str]
    target_cash_crops: List[str]
    notes: str

    @property
    def weed_suppression_index(self) -> float:
        """
        Indice composito di soppressione malerbe (0 - 100).
        Biomassa (45%), Copertura canopia (35%), Allelopatia (20%).
        """
        weighted = (
            (self.biomass_score * 0.45) +
            (self.canopy_closure_score * 0.35) +
            (self.allelopathy_score * 0.20)
        )
        return round(weighted * 10, 1)

def get_cover_crops_database() -> List[CoverCrop]:
    return [
        CoverCrop(
            common_name="Segale invernale (Cereal Rye)",
            scientific_name="Secale cereale",
            family="Poaceae",
            recommended_seasons=["Autunno-Inverno", "Invernale"],
            biomass_score=9.5,
            canopy_closure_score=8.5,
            allelopathy_score=8.5,
            mechanisms=[
                "Spessa pacciamatura post-terminazione con roller-crimper",
                "Essudati radicali e rilascio di composti DIBOA / BOA da residui",
                "Forte competizione precoce per azoto minerale e luce"
            ],
            target_cash_crops=["Soia", "Mais", "Girasole"],
            notes="Standard d'oro nei sistemi biologici a minima lavorazione (no-till)."
        ),
        CoverCrop(
            common_name="Avena nera / strigosa (Black Oat)",
            scientific_name="Avena strigosa",
            family="Poaceae",
            recommended_seasons=["Autunno-Inverno", "Primaverile"],
            biomass_score=8.5,
            canopy_closure_score=9.0,
            allelopathy_score=8.8,
            mechanisms=[
                "Essudati radicali con fitotossicità provata su infestanti a seme piccolo",
                "Accestimento vigoroso autunnale con rapido effetto pacciamante"
            ],
            target_cash_crops=["Soia", "Orticole", "Mais"],
            notes="Ottima suscettibilità alla terminazione meccanica; eccellente sanità radicale."
        ),
        CoverCrop(
            common_name="Veccia vellutata (Hairy Vetch)",
            scientific_name="Vicia villosa",
            family="Fabaceae",
            recommended_seasons=["Autunno-Inverno", "Invernale"],
            biomass_score=8.0,
            canopy_closure_score=9.0,
            allelopathy_score=5.0,
            mechanisms=[
                "Fissazione biologica di azoto (N) per la coltura successiva",
                "Abito strisciante/rampicante che soffoca la flora spontanea"
            ],
            target_cash_crops=["Mais", "Pomodoro", "Zucca"],
            notes="Decomposizione rapida; altamente consigliata in miscela con graminacee."
        ),
        CoverCrop(
            common_name="Sorgo-Sudangrass (Sorghum-Sudan)",
            scientific_name="Sorghum bicolor x S. sudanense",
            family="Poaceae",
            recommended_seasons=["Primavera-Estate", "Estiva"],
            biomass_score=9.8,
            canopy_closure_score=9.2,
            allelopathy_score=9.0,
            mechanisms=[
                "Biomassa secca massiccia (>8-12 t/ha)",
                "Produzione e secrezione radicale di sorgoleone ad azione erbicida naturale",
                "Intercettazione quasi totale della radiazione solare"
            ],
            target_cash_crops=["Cereali autunno-vernini", "Leguminose autunnali"],
            notes="Ideale per soppressione estiva intensiva e rigenerazione rapida del terreno."
        ),
        CoverCrop(
            common_name="Grano saraceno (Buckwheat)",
            scientific_name="Fagopyrum esculentum",
            family="Polygonaceae",
            recommended_seasons=["Primavera-Estate", "Estiva tardiva"],
            biomass_score=6.5,
            canopy_closure_score=9.8,
            allelopathy_score=7.5,
            mechanisms=[
                "Chiusura completa della canopia in meno di 2-3 settimane",
                "Ciclo cortissimo (30-45 gg), ideale per finestre colturali ristrette",
                "Rilascio di acidi organici chelanti fosforo"
            ],
            target_cash_crops=["Orticole autunnali", "Brassiche", "Cereali"],
            notes="Attira impollinatori ed entomofauna utile durante la fioritura."
        ),
        CoverCrop(
            common_name="Rafano da sovescio / Daikon (Tillage Radish)",
            scientific_name="Raphanus sativus var. longipinnatus",
            family="Brassicaceae",
            recommended_seasons=["Autunno-Inverno", "Fine Estate"],
            biomass_score=7.8,
            canopy_closure_score=9.0,
            allelopathy_score=8.0,
            mechanisms=[
                "Biofumigazione naturale tramite idrolisi di glucosinolati in isotiocianati",
                "Ampie foglie basali che bloccano la germinazione fotoblastica dei semi infestanti",
                "Fittone profondo che perfora le suole di lavorazione (bio-drilling)"
            ],
            target_cash_crops=["Mais", "Soia", "Ortaggi a radice"],
            notes="Sensibile alle forti gelate (winter-kill), semplificando la semina su sodo a primavera."
        ),
        CoverCrop(
            common_name="Trifoglio incarnato (Crimson Clover)",
            scientific_name="Trifolium incarnatum",
            family="Fabaceae",
            recommended_seasons=["Autunno-Inverno", "Primaverile"],
            biomass_score=7.2,
            canopy_closure_score=8.2,
            allelopathy_score=4.5,
            mechanisms=[
                "Fissazione simbiotica dell'azoto",
                "Copertura fitta del suolo per pacciamatura viva (living mulch)",
                "Ottima risorsa pollinifera primaverile"
            ],
            target_cash_crops=["Mais", "Pomodoro"],
            notes="Componente chiave per miscele bi- o trifitiche per equilibrare C:N."
        )
    ]

def filter_and_rank(
    database: List[CoverCrop], 
    season: Optional[str] = None, 
    cash_crop: Optional[str] = None
) -> List[CoverCrop]:
    results = database
    if season:
        results = [c for c in results if any(season.lower() in s.lower() for s in c.recommended_seasons)]
    if cash_crop:
        results = [c for c in results if any(cash_crop.lower() in t.lower() for t in c.target_cash_crops)]
    return sorted(results, key=lambda x: x.weed_suppression_index, reverse=True)

def print_table(ranked_crops: List[CoverCrop], title: str):
    print("=" * 100)
    print(f"{title:^100}")
    print("=" * 100)
    header = f"{'Pos':<4} | {'Specie (Comune / Scientifico)':<35} | {'Stagione':<20} | {'Score':<6} | {'Biom':<4} | {'Ombr':<4} | {'Allel':<5}"
    print(header)
    print("-" * 100)
    for idx, crop in enumerate(ranked_crops, start=1):
        name_fmt = f"{crop.common_name.split('(')[0].strip()} ({crop.scientific_name})"
        season_fmt = ", ".join(crop.recommended_seasons)
        print(f"{idx:<4} | {name_fmt:<35} | {season_fmt:<20} | {crop.weed_suppression_index:<6.1f} | {crop.biomass_score:<4.1f} | {crop.canopy_closure_score:<4.1f} | {crop.allelopathy_score:<5.1f}")
        print(f"     Meccanismi: {'; '.join(crop.mechanisms[:2])}")
        print(f"     Rotazione cash crop: {', '.join(crop.target_cash_crops)} | Note: {crop.notes}")
        print("-" * 100)

def print_mixtures():
    print("=" * 100)
    print(f"{'MISCUGLI POLIFITICI CONSIGLIATI PER SINERGIA AGROECOLOGICA':^100}")
    print("=" * 100)
    mixtures = [
        (
            "1. Miscuglio Invernale No-Till: Segale Invernale (75%) + Veccia Vellutata (25%)",
            "Sinergia: La segale produce una pacciamatura durevole (alto C:N) e DIBOA; la veccia fissa N atmosferico "
            "compensando l'immobilizzazione dell'azoto e chiude rapidamente gli interstizi basali."
        ),
        (
            "2. Miscuglio Biofumigante & Decompattante: Avena Nera (60%) + Rafano Daikon (40%)",
            "Sinergia: L'avena crea ombra e barriera orizzontale; il rafano perfora il terreno con fittoni e "
            "rilascia glucosinolati che riducono drasticamente la banca semi delle infestanti."
        ),
        (
            "3. Miscuglio Estivo ad Alto Impatto: Sorgo-Sudangrass (70%) + Grano Saraceno (30%)",
            "Sinergia: Il grano saraceno copre il suolo in 14-20 giorni azzerando la luce per le infestanti emergenti; "
            "il sorgo prende poi il sopravvento producendo fino a 10 t/ha di residuo allelopatico ricco di sorgoleone."
        )
    ]
    for name, desc in mixtures:
        print(name)
        print(f"   ↳ {desc}\n")
    print("=" * 100)

def main():
    parser = argparse.ArgumentParser(description="Pianificatore Cover Crop per Soppressione Malerbe")
    parser.add_argument("--season", type=str, help="Filtra per stagione (es. Inverno, Estate, Primavera, Autunno)")
    parser.add_argument("--cash-crop", type=str, help="Filtra per coltura da reddito successiva (es. Mais, Soia, Pomodoro)")
    args = parser.parse_args()

    db = get_cover_crops_database()
    ranked = filter_and_rank(db, season=args.season, cash_crop=args.cash_crop)

    title = "PIANO DI PIANTAGIONE CLASSIFICATO"
    if args.season:
        title += f" [Stagione: {args.season}]"
    if args.cash_crop:
        title += f" [Cash Crop: {args.cash_crop}]"

    print_table(ranked, title)
    if not args.season and not args.cash_crop:
        print_mixtures()

if __name__ == "__main__":
    main()
