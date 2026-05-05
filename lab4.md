1. A rendeleseknel az id amire kuldjuk a kerest az a server
   a valaszban is visszatukrozi es berakja a html be igy ha oda html t irunk azt mar nem szivegkent ertelmezi hanem html kent amit be is szur
   es futtat ugymond

![alt text](<Screenshot 2026-05-05 160939.png>)
![alt text](<Screenshot 2026-05-05 161332.png>)
sikeres break

2.  mint latszik a kereso mezobe irva is az tortenik mint az elobb es beszurodik a html elem a keresovel is
    ![alt text](image.png)
    A baj hogy innerHTML van hasznalva
    ![alt text](image-1.png)

3.  Mivel csak klines oldali ellenorzes van egy fetch keres atuti a html/klines oldali js vedelelmet, es modosul mit kuldunk a szervernek es mentodik a xss warning a db ben es igy mikor az administration t toltjuk be bejon a warning
    ![alt text](<Screenshot 2026-05-05 174057.png>)
    ![alt text](<Screenshot 2026-05-06 002345.png>)

4.  Mivel nincsenek megfeleloen vedve a bemenetek igy mikor az sql kerdi le az emailcimet, injectionnel athatolunk a vedelmen es adminkent tudunk bejelentkezni
    ![alt text](<Screenshot 2026-05-06 002447.png>)
    ![alt text](<Screenshot 2026-05-06 002457.png>)

5.  ![alt text](<Screenshot 2026-05-06 003430.png>)
    ![alt text](<Screenshot 2026-05-06 003435.png>)
    ![alt text](<Screenshot 2026-05-06 003457.png>)

    Az ID szinten megint kozvetlenul hasznalodik fel es mivel tudjuk hogy nosql van es ismerjuk a sleep t, hasznalatval tulterhelheto a db

6.  ![alt text](<Screenshot 2026-05-06 003804.png>)
    ![alt text](<Screenshot 2026-05-06 003929.png>)
    ![alt text](<Screenshot 2026-05-06 004342.png>)
    ![alt text](<Screenshot 2026-05-06 004349.png>)
    ![alt text](<Screenshot 2026-05-06 004531.png>)
    ![alt text](<Screenshot 2026-05-06 004717.png>)
    Samuel
    ![alt text](<Screenshot 2026-05-06 004733.png>)
    ![alt text](<Screenshot 2026-05-06 004741.png>)
    A reviwek alapjan rajottunk hogy mi az erdeklodesi kore, gy Star Trek vonatkozású megjegyzés utalt arra, hogy Jim valójában James T. Kirk kapitányt mintázza es ebbol tudtuk hogy Samuel a biztonsagi valasz igy, plane miutan az elozo modszerrel bejelntkeztunk fiokjba, a kiszallitasi cimek is megerositettek ezt, igy mar biztos volt a sejtes es tudtunk jelszot cserelni
