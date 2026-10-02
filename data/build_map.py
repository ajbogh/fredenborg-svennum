import json, math
sog=json.load(open('sogne_local.geojson'))

# --- data -------------------------------------------------------------
# (name, lat, lon, group, note)  groups: god = godparent residence, court = 1676 court record, reg = register place on the same page, ctx = context
pts=[
 ("Fredenborg · matr. 9, Svennum",57.28060,10.12073,"found","House site from the 1884 General Staff sheet, placed by its own survey grid and checked against lidar contours: the large building north of the smithy. Today the north side of the Hellumvej 23 farmyard, 25 m north of the farmhouse. ±15 m."),
 ("Jerslev kirke & præstegård",57.2836,10.0904,"god","Marie Fischer, the priest’s wife, lived here. Also Kjeld Nors the parish clerk, if he is “Kield Andersøn”. Anders of Fredenborg took the tithe from Kirsten Jensdatter’s field on Jerslev mark in 1676."),
 ("Kølskegård",57.2497,10.1163,"god","Knud Kampmann lived here with his sister’s household; died here 1704. "),
 ("Nørre Trøgdrup (approx.)",57.196,10.124,"court","Jens Nielsen and the Nørre Trøgdrup tenants: the party that summoned Peder Andersen of Fredenborg on 7 Sep 1676. Position approximate, from Trøgdrupvej."),
 ("Sønder Trøgdrup (approx.)",57.187,10.131,"court","The other village in the Bløden dispute. Peder Andersen of Fredenborg was summoned on this side, with Klausholm and Allerup. Position approximate."),
 ("Klausholm",57.1816,10.1357,"court","Christen Mortensen of Klausholm, also written ‘i sdr Trøgdrup’, led the Sønder Trøgdrup side in 1676."),
 ("Allerup",57.2304,10.1924,"court","Peder Andersen of Allerup, a former forest warden, summoned with Fredenborg and Klausholm."),
 ("Landvad",57.2119,10.2061,"court","Povl Sørensen of Landvad, born in Trøgdrup, gave the 64-year memory testimony."),
 ("Hellevad kirke",57.2129,10.1527,"ctx","Hellevad parish church at Klokkerholm. Hellevad’s own registers begin in 1646."),
 ("Svennum",57.2792,10.1139,"reg","Hamlet in Jerslev parish. The Jerslev burial register for 15 Jan 1688 places Fredenborg here: ‘Niels, Peder Andersens [barn] i Fredenborg i Svennum’."),
 ("Sterup",57.3130,10.1055,"reg","“Stærup” in the register; village, recorded 1408."),
 ("Øster Mellerup",57.2923,10.0849,"reg","“Møllerup/Mellerup”; recorded 1491. Placed by its road."),
 ("Vester Mellerup",57.2977,10.0516,"reg","Manor farm, recorded 1578. Placed by its road."),
 ("Løt",57.3125,10.0835,"reg","“Lött”; recorded 1688 as Løtte. Placed by its road."),
 ("Dårbak",57.3152,10.1552,"reg","“Daarbak”, Jan 1698 entry; recorded 1662. Placed by its road."),
 ("Krattet",57.3199,10.1332,"reg","Sterupkrat 1606. Placed by its road."),
 ("Abildgård",57.3232,10.0885,"reg","Single farm, 1500s. Placed by its road."),
 ("Hjulskov",57.2991,10.1283,"reg","Vester Hjulskov hamlet; recorded 1457."),
 ("Klæstrup",57.2819,10.0547,"reg","Village; recorded 1366."),
 ("Kirkholt",57.3040,10.1636,"reg","Recorded 1662."),
 ("Lindholt",57.3594,10.1666,"reg","Farm in the Vrejlev enclave; Jan 1698 godparents came from here."),
 ("Hallund kirke",57.2387,10.1026,"ctx","Neighbouring parish church, Dronninglund herred."),
 ("Hellum kirke",57.2615,10.1610,"ctx","Jerslev’s later annex parish (from 1859)."),
 ("Stubdrup",57.2642,10.0258,"ctx","Øster Brønderslev parish; Anders Pedersen of Stubdrup in the Oct 1676 court session."),
 ("Burholt",57.2510,9.9615,"ctx","Øster Brønderslev parish; Sofie Bloch, Knud Kampmann’s mother, died here 1719."),
]
# weighted centre for the primary zone
w=[(57.2836,10.0904,3),(57.2497,10.1163,1),(57.205,10.175,1)]
clat,clon=57.28060,10.12073
R1=0.06
blat,blon=57.187,10.131
RB=1.5

# --- projection --------------------------------------------------------
W,H=3012,1786
def P(lat,lon):
    return (5523.031143961996*lon+14.27543309854616*lat+-55042.21525673557, 1.218596177302099*lon+-10203.51653886586*lat+584863.7947258598)
def km(d): return d*91.67336952688382
kx=111.32*math.cos(math.radians(57.24)); ky=111.32

def ring_path(coords):
    d=[]
    for i,c in enumerate(coords):
        lon,lat=c[0],c[1]
        x,y=P(lat,lon); d.append(("M" if i==0 else "L")+f"{x:.1f},{y:.1f}")
    return " ".join(d)+" Z"
polys=[]
for f in sog['features']:
    name=f['properties']['SOGNENAVN']; g=f['geometry']
    rings=[]
    if g['type']=='Polygon': rings=[g['coordinates'][0]]
    else: rings=[p[0] for p in g['coordinates']]
    path=" ".join(ring_path(r) for r in rings)
    # label at mean of ring points
    allp=[c for r in rings for c in r]; mlon=sum(c[0] for c in allp)/len(allp); mlat=sum(c[1] for c in allp)/len(allp)
    polys.append((name,path,P(mlat,mlon)))

svg=[]
miny=min(P(p[1],p[2])[1] for p in pts); y0=min(0,int(miny)-90)
svg.append(f'<svg viewBox="0 {y0} {W} {H-y0}" width="100%" role="img" aria-labelledby="maptitle" style="display:block;max-width:100%;height:auto">')
svg.append('<title id="maptitle">Map of places named in the 1698 Jerslev baptism and the 1676 court records, with the located Fredenborg house</title>')
svg.append(f'<rect x="0" y="{y0}" width="{W}" height="{H-y0}" fill="var(--map-bg)"/>')
svg.append('<g id="L-sat"><image href="data:image/jpeg;base64,'+open('bg.b64').read()+f'" x="0" y="0" width="{W}" height="{H}" preserveAspectRatio="none"/></g>')
svg.append('<defs>'
 '<pattern id="h1" width="24" height="24" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="24" class="hatch e1"/></pattern>'
 '<pattern id="h2" width="24" height="24" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><line x1="0" y1="0" x2="0" y2="24" class="hatch e2"/></pattern>'
 '<pattern id="h3" width="24" height="24" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="24" class="hatch e3"/></pattern>'
 '</defs>')
# parishes
for name,path,(lx,ly) in polys:
    cls="parish jerslev" if name=="Jerslev" else "parish"
    svg.append(f'<path class="{cls}" d="{path}"/>')
    if name=="Jerslev": jerslev_path=path
for name,path,(lx,ly) in polys:
    if 0<lx<W and 0<ly<H:
        svg.append(f'<text class="parish-label" x="{lx:.0f}" y="{ly:.0f}" text-anchor="middle">{name.upper()}</text>')
# --- event layers ----------------------------------------------------
ev=[]
fx,fy=P(57.28060,10.12073)
ev.append(f'<g id="L-parish"><path class="ev-parish" d="{jerslev_path}"/></g>')
# E1: tithe fight on Jerslev mark, 31 Aug 1676 — the grain was carted home to Fredenborg; ring = Fredenborg to the Jerslev village fields (1.8 km)
ev.append(f'<g id="L-e1"><circle class="ev e1" cx="{fx:.1f}" cy="{fy:.1f}" r="{km(1.8):.1f}"/>'
          f'<text class="ev-lbl e1" x="{fx:.1f}" y="{fy-km(1.8)-18:.1f}" text-anchor="middle">31 Aug 1676 · tithe grain carted from Jerslev mark to Fredenborg</text></g>')
# E2: Bløden, the common between Nørre and Sønder Trøgdrup, 7 Sep 1676 — travel line from Fredenborg
nlat,nlon=57.196,10.124; slat,slon=57.187,10.131
mlat,mlon=(nlat+slat)/2,(nlon+slon)/2; x2,y2=P(mlat,mlon)
dkm=math.hypot((mlat-57.28092)*ky,(mlon-10.12088)*kx)
ev.append(f'<g id="L-e2"><line class="ev-line e2" x1="{fx:.1f}" y1="{fy:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'
          f'<ellipse class="ev-core e2" cx="{x2:.1f}" cy="{y2:.1f}" rx="{km(0.45):.1f}" ry="{km(0.7):.1f}" transform="rotate(-25 {x2:.1f} {y2:.1f})"/>'
          f'<text class="ev-lbl e2" x="{x2+60:.1f}" y="{y2+10:.1f}" text-anchor="start">7 Sep 1676 · Bløden common, {dkm:.1f} km from Fredenborg</text></g>')
svg.extend(ev)
svg.append('<g id="L-points">')
# label offsets to dodge overlaps: (dx,dy,anchor)
off={"Jerslev kirke & præstegård":(10,-8,"start"),"Fredenborg · matr. 9, Svennum":(14,-14,"start"),"Fredensbo (1942)":(10,-8,"start"),"Freden":(-10,4,"end"),"Fredenshus":(10,4,"start"),"Nørre Trøgdrup (approx.)":(-10,-4,"end"),"Sønder Trøgdrup (approx.)":(-10,10,"end"),"Klausholm":(10,10,"start"),"Landvad":(10,4,"start"),"Hellevad kirke":(10,-6,"start"),"Kølskegård":(10,4,"start"),"Trøgdrup (approx.)":(10,4,"start"),"Allerup":(10,4,"start"),
 "Svennum":(10,12,"start"),"Sterup":(10,-6,"start"),"Øster Mellerup":(-10,4,"end"),"Vester Mellerup":(-10,4,"end"),"Løt":(-10,-4,"end"),
 "Dårbak":(10,4,"start"),"Krattet":(10,-4,"start"),"Abildgård":(10,-4,"start"),"Hjulskov":(10,-4,"start"),"Klæstrup":(-10,4,"end"),"Kirkholt":(10,4,"start"),
 "Lindholt":(10,4,"start"),"Hallund kirke":(-10,4,"end"),"Hellum kirke":(10,4,"start"),"Stubdrup":(-10,4,"end"),"Burholt":(10,4,"start")}
for item in pts:
    name,lat,lon,g,note=item
    x,y=P(lat,lon); dx,dy,anc=off.get(name,(10,4,"start"))
    approx=' approx' if 'approx' in name else ''
    if g=="god": shape=f'<rect class="pt god" x="{x-18:.1f}" y="{y-18:.1f}" width="36" height="36" transform="rotate(45 {x:.1f} {y:.1f})"/>'
    elif g=="court": shape=f'<polygon class="pt court{approx}" points="{x:.1f},{y-21:.1f} {x+21:.1f},{y+18:.1f} {x-21:.1f},{y+18:.1f}"/>'
    elif g=="reg": shape=f'<circle class="pt reg" cx="{x:.1f}" cy="{y:.1f}" r="15"/>'
    elif g=="lead": shape=f'<rect class="pt lead" x="{x-15:.1f}" y="{y-15:.1f}" width="30" height="30"/>'
    elif g=="found": shape=f'<g class="pt found"><circle cx="{x:.1f}" cy="{y:.1f}" r="22"/><circle cx="{x:.1f}" cy="{y:.1f}" r="6"/></g>'
    else: shape=f'<circle class="pt ctx" cx="{x:.1f}" cy="{y:.1f}" r="12"/>'
    svg.append(f'<g class="site"><title>{name}: {note}</title>{shape}<text class="lbl {g}" x="{x+dx*3.1:.1f}" y="{y+dy*3.1:.1f}" text-anchor="{anc}">{name.replace(" (approx.)","")}</text></g>')
svg.append('</g>')
# scale bar (5 km) & north
bx,by=120,H-120
svg.append(f'<g class="scale"><line x1="{bx}" y1="{by}" x2="{bx+km(5):.1f}" y2="{by}"/><line x1="{bx}" y1="{by-15}" x2="{bx}" y2="{by+15}"/><line x1="{bx+km(5):.1f}" y1="{by-15}" x2="{bx+km(5):.1f}" y2="{by+15}"/><text x="{bx+km(2.5):.1f}" y="{by-27}" text-anchor="middle">5 km</text></g>')
svg.append(f'<g class="north"><line x1="{W-120}" y1="210" x2="{W-120}" y2="90"/><polygon points="{W-120},72 {W-138},108 {W-102},108"/><text x="{W-120}" y="258" text-anchor="middle">N</text></g>')
svg.append('</svg>')
open('map_sat.svg','w').write("\n".join(svg))

# distances table
def dist(a,b,c,d): 
    return math.hypot((c-a)*ky,(d-b)*kx)
rows=[]
for name,lat,lon,g,note in pts:
    rows.append((name,g,lat,lon,dist(57.28060,10.12073,lat,lon),dist(57.2836,10.0904,lat,lon),note))
json.dump({"centre":[clat,clon],"R1":R1,"B":[blat,blon],"RB":RB,"rows":rows},open('mapdata_sat.json','w'),ensure_ascii=False,indent=1)
print(f"centre {clat:.4f},{clon:.4f}")
for r in rows: print(f"{r[0]:28s} {r[1]:5s} {r[4]:5.1f} km from centre  {r[5]:5.1f} km from church")
