# Agroecological Cover Crop Weed Suppression Planner

Strumento open-source per la pianificazione e classificazione di colture di copertura (*cover crops*) finalizzate alla soppressione ecologica delle erbe infestanti in assenza di diserbanti chimici.

---

## 🌾 Razionale Scientifico e Letteratura (PubMed)

La gestione sostenibile delle malerbe in agricoltura biologica e rigenerativa non-chimica si fonda sull'intensificazione ecologica (*ecological intensification*). Questo strumento implementa criteri di selezione supportati da recenti studi scientifici:

1. **Menalled & Ryan (2026)** - *Selecting suitable predecessors: Ecosystem services from cover crops to reduce tillage and fertilizer*. Scientific Reports, [PMID: 42129302](https://pubmed.ncbi.nlm.nih.gov/42129302/):
   - Valuta 80 combinazioni cover crop / cash crop.
   - Mostra che l'accurata selezione della cover crop produce una riduzione di **2,6 volte della biomassa delle infestanti** e un incremento fino a 7,3 volte della resa della coltura da reddito successiva senza diserbo ausiliario.

2. **Eroğlu et al. (2026)** - *Characterization of black oat root exudates in the presence of interspecific weed species and intraspecific neighbors, and their effects on root traits*. Frontiers in Plant Science, [PMID: 41959575](https://pubmed.ncbi.nlm.nih.gov/41959575/):
   - Dimostra l'azione degli essudati radicali di specie come l'Avena nera (*Avena strigosa*) nell'inibizione attiva dell'allungamento radicale e dello sviluppo delle malerbe consociate.

3. **Menalled, Smith, Cordeau et al. (2023)** - *Phylogenetic relatedness can influence cover crop-based weed suppression*. Scientific Reports, [PMID: 37833350](https://pubmed.ncbi.nlm.nih.gov/37833350/):
   - Evidenzia come le cover crop possano ridurre **fino al 99% della biomassa delle infestanti**.
   - Dimostra che la vicinanza filogenetica e la sincronizzazione fenologica con le malerbe target ne massimizzano la soppressione, e che le finestre di svernamento (overwintering) alterano strutturalmente la comunità di infestanti.

4. **Fernando & Shrestha (2023)** - *The Potential of Cover Crops for Weed Management: A Sole Tool or Component of an Integrated Weed Management System?*. Plants, [PMID: 36840100](https://pubmed.ncbi.nlm.nih.gov/36840100/):
   - Rassegna sistematica dei meccanismi di soppressione (competizione per luce/azoto, pacciamatura fisica, allelopatia) ed evidenzia la superiorità dei miscugli polifitici rispetto alle monocolture.

---

## 🔍 Meccanismi di Soppressione Integrati

Il modello calcola un indice composito di soppressione (*Weed Suppression Index*, 0-100) pesando:
- **Biomassa e Pacciamatura Residua (45%)**: spessore del pacciame (*roller-crimper* o allettamento naturale) che blocca la penetrazione luminosa e impedisce fisicamente l'emergenza dei germinelli.
- **Velocità di Chiusura della Canopia (35%)**: intercettazione rapida delle radiazioni PAR nelle prime 2-4 settimane, togliendo energia alle malerbe fotoblastiche.
- **Attività Allelopatica Biochimica (20%)**: rilascio di essudati radicali o metaboliti secondari di decomposizione (es. composti DIBOA/BOA nella segale, sorgoleone nel sorgo, glucosinolati nelle brassicacee).

---

## 🚀 Utilizzo

### Esecuzione di base
```bash
python cover_crop_planner.py
```

### Filtro per stagione di semina
```bash
python cover_crop_planner.py --season Inverno
python cover_crop_planner.py --season Estate
```

### Filtro per coltura da reddito (Cash Crop) successiva
```bash
python cover_crop_planner.py --cash-crop Soia
python cover_crop_planner.py --cash-crop Mais
```

---

## 🌿 Specie Attualmente Incluse

- **Segale invernale** (*Secale cereale*) - Indice: 89.5/100
- **Sorgo-Sudangrass** (*Sorghum bicolor x S. sudanense*) - Indice: 94.3/100
- **Avena nera / strigosa** (*Avena strigosa*) - Indice: 87.3/100
- **Rafano da sovescio / Daikon** (*Raphanus sativus var. longipinnatus*) - Indice: 82.6/100
- **Grano saraceno** (*Fagopyrum esculentum*) - Indice: 78.6/100
- **Veccia vellutata** (*Vicia villosa*) - Indice: 77.5/100
- **Trifoglio incarnato** (*Trifolium incarnatum*) - Indice: 70.1/100

---

## 🤝 Contributi e Collaborazioni
Invitiamo ricercatori in agroecologia, agronomi e sviluppatori a collaborare per:
- Espandere il database delle specie e cultivar locali.
- Integrare modelli pedoclimatici regionali.
- Validare sperimentalmente i coefficienti di soppressione su specifiche flore infestanti.
