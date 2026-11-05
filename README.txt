MojaFi website — FINAL package (Oct 31, 2026)
==============================================

WHAT IS WHAT
  index.html     -> the website (single file, works offline: double-click to open)
  og-image.jpg   -> share-preview image (WhatsApp/Facebook). Keep next to index.html when uploading
  backups/       -> every earlier version (NEVER upload these)
  source/        -> everything needed to rebuild/change the site (logos, photos, fonts, mascots)

WHEN YOU GO ONLINE (cPanel > File Manager > public_html)
  1. Rename any old index.html there to index-old.html
  2. Upload index.html + og-image.jpg only
  3. Hard-refresh (Ctrl+Shift+R). Facebook Sharing Debugger > "Scrape Again" to refresh share preview
  The site's address inside the file is https://mojafi.com.bd/ (canonical + share tags).
  If you launch on another domain first, tell Claude (or search & replace "mojafi.com.bd" in index.html).

THINGS TO CHECK BEFORE GOING LIVE
  - The top banner says "আমরা এখন রাস্তায়" (we are on the street now). Publish only when the cart is really running.
  - Menu photos are reference visuals (a note under the menu says so). Replace with your own food photos when ready:
    put new JPGs (1600px wide or more) in source/photo_src/ (same file names), then see "REBUILD" below.
  - Live-location buttons all open https://linktr.ee/MojaFi. To change: search index.html for  const LOC_URL=
  - Contact: WhatsApp +880 1846-829909; Instagram mojafi.food; Facebook MojaFi.food; TikTok @mojafi_food;
    YouTube @MojaFii; LinkedIn company/mojafi  (confirm these are all correct before launch)
  - Certificates: only partner/issuer LOGOS are shown (ICCA Dubai, Unilever Food Solutions, WACS, Cloud Assess,
    eFoodHandlers, Safefood). No certificate images are on the site, by your choice.

REBUILD (optional, needs Python 3)
  cd source ; python3 build.py   -> creates source/index.html from template4.html + assets

CHECKS DONE ON THIS VERSION
  6 automated test suites (481 checks) pass; no console errors; no blurry images; no overflow/clipped text or
  overlapping stickers at 13 screen widths (320-1920px); text contrast >= WCAG AA; keyboard + popup work.

--- Nov 2 final check updates ---
* Contrast fixes (WCAG AA), landscape-phone layout, Safari/old-iPhone fallbacks
* Off-screen animations pause automatically (smoother on slow phones)
* Search-engine info (JSON-LD) added

--- Nov 3 SEO update ---
* New title/description, Twitter+OG cards, hreflang, robots meta
* Structured data (Organization, WebSite, FAQ) for Google
* robots.txt, sitemap.xml, logo.png added -> upload ALL of these next to index.html
* Keyboard "skip to content" link added

--- Nov 3 FAST BUILD (important) ---
* index.html এখন ছোট (150KB); ছবি/font আলাদা "assets" folder-এ। 
  => index.html আর assets folder সবসময় একসাথে রাখতে হবে (pendrive-এও)।
* Online করতে হলে এই folder-এর সব কিছু (assets সহ, .htaccess সহ) host-এর public_html-এ upload করো।
  Files: index.html, assets/, og-image.jpg, logo.png, favicon.ico, robots.txt, sitemap.xml, 404.html, .htaccess
* standalone/index-single-file.html = পুরনো এক-ফাইলের version (শুধু একা খুলে দেখানোর জন্য, ৩MB, online-এ দিও না)
* Host-এ "Force HTTPS" চালু করে দিও (cPanel: Domains > Force HTTPS Redirect)।
* Online হওয়ার পর: Google Search Console-এ domain verify করে sitemap.xml জমা দাও।

--- Nov 3 UX update ---
* Phone-এ menu এখন ২ column (page ছোট হয়েছে, scroll কম)
