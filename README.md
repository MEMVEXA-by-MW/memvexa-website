# MEMVEXA-by-MW

Offizielle Website für die Android-Apps MEMVEXA, AmbientGuard und CreateMyNFT.

**Website öffnen:** https://memvexa-by-mw.github.io/memvexa-website/

## App-Seiten

- [MEMVEXA – Erinnerungen und Dokumente](https://memvexa-by-mw.github.io/memvexa-website/memvexa.html)
- [AmbientGuard – Geräte- und Netzwerkumgebung](https://memvexa-by-mw.github.io/memvexa-website/ambientguard.html)
- [CreateMyNFT – KI-NFT-Entwürfe und Testnetz-Minting](https://memvexa-by-mw.github.io/memvexa-website/createmynft.html)
- [CreateMyNFT – Testzugang und Kaufinfo](https://memvexa-by-mw.github.io/memvexa-website/createmynft-kaufen.html)

Die vorhandenen App-, Test-, Support- und Datenschutzseiten bleiben unter ihren bisherigen Adressen erreichbar. Der CreateMyNFT-Direktverkauf ist weiterhin nicht freigeschaltet.

## Veröffentlichung

Die statischen Dateien werden mit GitHub Pages veröffentlicht: Branch `main`, Verzeichnis `/ (root)`. `.nojekyll` sorgt dafür, dass die fertigen HTML-Dateien unverändert ausgeliefert werden. Ein zusätzlicher Build oder JavaScript ist nicht erforderlich.

Dies ist eine GitHub-Pages-Projektwebsite. Der Pfad `/memvexa-website/` gehört zur vollständigen Adresse. Die reine Adresse `https://memvexa-by-mw.github.io/` hat aktuell keine eigene Startseite.

## Suchmaschinen

Alle zwölf Inhaltsseiten enthalten individuelle Titel und Beschreibungen, eine eindeutige kanonische HTTPS-Adresse, freigegebene Indexierung sowie Open-Graph-/Twitter-Vorschaudaten. Strukturierte Daten beschreiben Website, Seiten und die drei Apps; es werden keine Bewertungen, Verkaufspreise oder Verifizierungen erfunden.

Die [XML-Sitemap](https://memvexa-by-mw.github.io/memvexa-website/sitemap.xml) enthält alle zwölf kanonischen Seitenadressen. Bei neuen Seiten muss sie ergänzt werden. `index.html` verweist als kanonische Adresse auf das Projektverzeichnis mit abschließendem `/`.

### Google Search Console einrichten

1. [Google Search Console](https://search.google.com/search-console/) mit dem Google-Konto des Betreibers öffnen.
2. Eine **URL-Präfix-Property** für `https://memvexa-by-mw.github.io/memvexa-website/` hinzufügen. Eine Domain-Property eignet sich ohne Kontrolle über die GitHub-DNS-Einträge nicht.
3. Die Inhaberschaft mit dem von Google erzeugten HTML-Tag in `index.html` oder der unverändert hochgeladenen Google-HTML-Datei bestätigen. Keine Beispielwerte als Verifizierung veröffentlichen.
4. Unter **Sitemaps** `sitemap.xml` einreichen.
5. Die vollständige Startseitenadresse in der URL-Prüfung prüfen und die Indexierung beantragen.

Die Anmeldung und die Einreichung sind erst abgeschlossen, wenn Google sie im Betreiberkonto bestätigt. Die Website allein ersetzt diese Kontoschritte nicht. Google entscheidet selbst über Aufnahme und Zeitpunkt; eine sofortige Aufnahme oder Platzierung wird nicht zugesagt.

### robots.txt bei einer Projektwebsite

Suchmaschinen lesen `robots.txt` nur direkt an der Wurzel des Hosts, hier unter `https://memvexa-by-mw.github.io/robots.txt`. Eine Datei im Projektordner `/memvexa-website/robots.txt` hätte keine Wirkung auf das Crawling. Der derzeitige HTTP-404-Status der robots-Datei sperrt keine Seiten.

Falls später eine eigene Hauptwebsite oder Domain eingerichtet wird, dort eine passende `robots.txt` mit der absoluten Sitemap-Adresse ergänzen. Die bestehenden URLs und die CreateMyNFT-/WalletConnect-Identität nur mit einem geplanten Umzug ändern.

Quellen: [Google: Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [Google: robots.txt](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec), [Google: Indexierung beantragen](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl).
