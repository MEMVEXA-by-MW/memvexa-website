# CreateMyNFT – kostenlose Demo auf MEMVEXA-by-MW veröffentlichen

Die Website-Seite [CreateMyNFT – Demo & Pro](https://memvexa-by-mw.github.io/memvexa-website/createmynft-kaufen.html) ist bereits vorbereitet. Der Download-Knopf erscheint **erst, wenn die signierte Demo-APK wirklich öffentlich verfügbar ist**. Das verhindert kaputte Links und die versehentliche Bereitstellung der Play-AAB.

## Einmalige Einrichtung

1. Auf GitHub in **Settings → Developer settings → Personal access tokens → Fine-grained tokens** einen neuen Token anlegen. Als Resource Owner **MEMVEXA-by-MW**, als Repository **nur `memvexa-website`** auswählen. Unter Repository Permissions **Contents → Read and write** erlauben; Ablaufdatum sinnvoll setzen.
2. Im **privaten** Repository [CreatemyNFT](https://github.com/MEMVEXA-by-MW/CreatemyNFT) unter **Settings → Secrets and variables → Actions → New repository secret** den Namen `WEBSITE_RELEASE_TOKEN` anlegen und den Token-Wert **nur dort** hinterlegen. **Niemals in Chats, Issues, Dateien oder Website-Code kopieren.**
3. Im privaten App-Repository auf **Actions → Publish free Demo APK to Website → Run workflow → main → Run workflow** klicken.
4. Der Workflow prüft den Quellcode, erstellt eine signierte APK mit **`ENABLE_MAINNET_WRITES=false`** und **ohne Kaufprüfserver-URL**, erzeugt eine SHA-256-Prüfsumme und veröffentlicht beides als GitHub Release im **öffentlichen Website-Repository**.
5. Auf dieser Seite prüfen: https://github.com/MEMVEXA-by-MW/memvexa-website/releases/tag/createmynft-demo

Nach erfolgreicher Veröffentlichung erkennt die Website das vorhandene GitHub Release und zeigt automatisch den echten APK-Download an. Der stabile Dateiname lautet `CreateMyNFT-Demo.apk`.

## Wichtig für bestehende Play-Tester

- Die öffentliche APK besitzt aktuell **dieselbe Paket-ID** wie die Google-Play-Test-App. Bei unterschiedlichen Android-Signaturen lässt sie sich möglicherweise **nicht als Update** installieren.
- Deshalb **nicht** die Play-Test-App nur für den Direktdownload deinstallieren – lokale Projekte könnten dabei verloren gehen.
- Der **geschlossene Google-Play-Test** sowie seine bisherigen Tester und das AAB bleiben unverändert.
- Über den Website-Download ist kein Pro-Kauf möglich. Der geplante Kauf erfolgt später über die offizielle Play-Version mit sicherer Kaufprüfung.
- Test-ETH ist wertlos; KI-/IPFS-Anbieter können trotzdem Gebühren verlangen.

## Technischer Veröffentlichungsweg

Quelle: `MEMVEXA-by-MW/CreatemyNFT/.github/workflows/publish-website-demo.yml`.

**Release-Tag:** `createmynft-demo` (stabil für spätere Updates)

**APK:** `https://github.com/MEMVEXA-by-MW/memvexa-website/releases/download/createmynft-demo/CreateMyNFT-Demo.apk`

**SHA-256:** `https://github.com/MEMVEXA-by-MW/memvexa-website/releases/download/createmynft-demo/CreateMyNFT-Demo.apk.sha256`

Diese Links werden **erst nach erfolgreicher Release-Erstellung nutzbar**. Kein Token bedeutet kein Upload, nicht etwa einen heimlich abgeschwächten Sicherheitscheck.
