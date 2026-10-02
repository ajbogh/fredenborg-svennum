# Finding Fredenborg

Where was "Fredenborg", the house named in the Jerslev parish register at the baptism of Christen, son of Søren, on 13 February 1698?

**Answer:** a cottage in the village of Svennum, Jerslev parish, Børglum herred, Vendsyssel, Denmark. Its site is the north side of today's farmyard at Hellumvej 23, 9740 Jerslev:

    57.28060 N, 10.12073 E  (±15 m)
    https://www.google.com/maps?q=57.28060,10.12073

Open `index.html` for the full write-up: an annotated map, a then-and-now slider between the 1884 General Staff sheet, the lidar terrain model and the 2024 orthophoto, the chain of records, the house's history 1676–1725, and the source documents.

## The chain of records

| Year | Source | Finding |
|---|---|---|
| 1676 | Jerslev herred court books | Anders and Peder Andersen "i Fredenborg"; the household harvests a strip on Jerslev mark and is summoned over Trøgdrup common |
| 1688 | Christian V's matrikel, modelbog 1781 (Jerslev herred), fol. 112–114 | Svennum no. 8: Niels Andersen, *Huus*, owner Johan Kaas, hartkorn 0:1:0:1:1 |
| 1688 | Jerslev burials, 15 Jan | "Peder Andersens barn i Fredenborg i Svennum" — the line that places the house |
| 1698 | Jerslev baptisms, 13 Feb | Christen, "Sørens udj Fredenborg" |
| 1702 | Jerslev baptisms, 10 Sep | Jens, "Søren Jensen Fredenborgs" — the father's patronymic |
| 1813 | Original 1 cadastral map, Jerslev By sheet 2 | Plot No 9, house 7, Ole Nielsen |
| 1844 | Matrikel for Børglum Herred, Jerslev sogn fol. 395–397 | New no. 9, old hartkorn 0-1-0-1 = 1688 no. 8 |
| 1884 | Original 2 cadastral map; General Staff 1:20,000 "Jerslev" | Plot 9a with house; two buildings north of the smithy, ditch at today's pond |
| today | Danmarks Højdemodel, GeoDanmark orthophoto, Matriklen | The farmyard at Hellumvej 23 |

## Contents

- `index.html` — the page (self-contained apart from `img/`)
- `img/` — figures and the co-registered layers used by the slider (frame 57.27413–57.28946 N, 10.09786–10.13113 E)
- `registers/` — crops of the Jerslev parish register entries
- `maps/` — crops of the historical maps and matrikel pages
- `kmz/` — Google Earth overlays: the georeferenced 1884 General Staff sheet, lidar hillshade, 0.5 m and 2.5 m contours, and the fitted cadastral sheets
- `data/` — modern cadastral parcels of Svennum By (`svennum_parcels.json`), the final coordinates, and the map-build script
- `Finding-Fredenborg.pdf` — a print of an earlier version of the page

## Sources

- Jerslev sogn kirkebog 1684– (Rigsarkivet; images via Danish Family Search, sogn 359)
- Jerslev herreds tingbøger 1631–1688, transcribed by Bjarne Nørgaard-Pedersen, brejl.dk
- Rentekammeret, Christian 5.s matrikel, modelbog (Arkivalieronline bsid 408328) and Matrikel for Børglum Herred 1844 (bsid 212810)
- Klimadatastyrelsen, historiskekort.dk: Original 1 and Original 2 matrikelkort for Jerslev By and Svennum By; Generalstabens høje målebordsblade "Jerslev" (1884) and "Aas" (1885)
- Klimadatastyrelsen / Dataforsyningen: Danmarks Højdemodel, GeoDanmark ortofoto 2024, Matriklen
- Trap Danmark, 5th ed.; S. V. Wiberg, Præstehistorie; C. Klitgaard, Vendsysselske Præstefamilier
- Danmarks Stednavne (Københavns Universitet)

Historical maps and aerial photos are Danish public data under the Klimadatastyrelsen open-data terms. The Google Maps satellite image behind the main map is used for private research.

Research done with Claude, October 2026.
