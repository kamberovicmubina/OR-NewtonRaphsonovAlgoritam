# OR-NewtonRaphsonovAlgoritam

Newton-Raphsonov algoritam (NR) za traženje lokalnog ekstrema funkcije f(x) koristi sljedeću relaciju: <br/>

x<sub>k+1</sub> = x<sub>k</sub> - (f'(x<sub>k</sub>))/(f''(x<sub>k</sub>))<br/>

Uslov zaustavljanja algoritma je dostizanje maksimalnog broja iteracija N ili kada bude ispunjeno <br/>
|f(x<sub>k+1</sub>)−f(x<sub>k</sub>)|< ε, <br/>
nakon čega se usvaja da je x<sub>k+1</sub> rješenje, odnosno tačka lokalnog ekstrema.

Algoritam je testiran na 4 funkcije. U fajlu L2_Z2.py je kod za crtanje 2D grafika za svaku od funkcija, pri čemu su lokalni ekstremi označeni crvenim kružićem, a tačke koje je pronašao algoritam zelenim križićem.
