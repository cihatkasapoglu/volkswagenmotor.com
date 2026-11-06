# VolkswagenMotor.com — HTML / GitHub Pages site

Bu proje sunucu veya veritabanı gerektirmeyen statik HTML/CSS/JavaScript sitesidir. GitHub Pages üzerinde yayınlanmaya hazırdır.

## Dosyalar
- `index.html`: Ana sayfa
- `404.html`: Bulunamayan adresler için hata sayfası
- `urun/`: Motor kodu ve araç grubu bazında ayrı ürün sayfaları
- `kategori/`: Sıfır, çıkma ve rektefeli motor kategori sayfaları
- `blog/`: Blog ana sayfası ve üç bilgilendirici yazı
- `kvkk.html`, `gizlilik.html`, `garanti-ve-sorumluluk.html`, `fiyat-bilgilendirme.html`: Yasal/bilgilendirme sayfaları
- `sitemap.xml`, `robots.txt`, `CNAME`: Google ve alan adı dosyaları (47 URL)
- `data/urunler.json`: Ürün ekleme/düzenleme alanı (ziyaretçiye açık bir yönetim paneli değildir)
- `scripts/build_site.py`: JSON ürün verisinden statik ürün sayfaları, ana sayfa ve site haritası üretir

## Görseller
`assets/ASSETLERI-BURAYA-KOPYALA.txt` içindeki 10 görseli, dosya adlarını ve uzantılarını değiştirmeden `assets/` klasörüne kopyalayın. Bu çalışma oturumunda logo/banner/ürün fotoğrafları yüklenmiş dosyalar arasında görünmediğinden site şimdilik SVG yedek görseller kullanır. Özgün dosyaları eklediğinizde sayfa otomatik olarak onları gösterir.

## Yeni ürün ekleme
1. `data/urunler.json` dosyasını açın.
2. Var olan bir ürün nesnesini kopyalayarak yeni `slug`, `title`, `brand`, `models`, `engine`, `codes`, `image`, `description`, `body`, `fit` ve `keywords` değerlerini girin.
3. Görseli `assets/` klasörüne ekleyin.
4. Proje ana klasöründe `python scripts/build_site.py` komutunu çalıştırın.
5. Değişen HTML dosyalarını, JSON dosyasını ve `sitemap.xml` dosyasını GitHub'a gönderin.

Ürün sayfaları bu komutla her motor/marka/model grubu için ayrı statik HTML olarak oluşturulur. Site içinde ziyaretçiye görünen bir ürün ekleme ekranı veya yönetim paneli bulunmaz.

## GitHub Pages yayını
1. GitHub'da yalnızca bu siteye ait, ayrı bir repository oluşturun (örnek ad: `volkswagenmotor.com`). Bu paket başka bir siteye veya mevcut repository'ye bağlı değildir.
2. Bu klasörün içindeki tüm dosya ve klasörleri yeni repository'nin ana dizinine yükleyin.
3. Repository > Settings > Pages bölümünde Source olarak **GitHub Actions** seçin. `.github/workflows/pages.yml` her `main` güncellemesinde siteyi yayınlar.
4. GitHub Pages alan adı ayarına `volkswagenmotor.com` girin. `CNAME` dosyası da repoda yer almalıdır. Alan adınızın DNS kayıtlarını GitHub Pages'in güncel resmi yönergelerine göre düzenleyin; DNS yayılımı tamamlandıktan sonra HTTPS'i etkinleştirin.
5. Yayınlanan siteyi açıp ürün fotoğraflarının göründüğünü ve telefon/WhatsApp bağlantılarını test edin.

## Google'a bildirme
- Google Search Console'da `volkswagenmotor.com` alan adını doğrulayın.
- `https://volkswagenmotor.com/sitemap.xml` site haritasını gönderin.
- Ana sayfa, kategori ve ürün sayfaları için URL Denetimi ile tarama isteği gönderebilirsiniz.
- Site haritasında bu sürümde **32 ayrı ürün sayfası** yer alır. Her yeni ürün eklendiğinde build komutu sitemap'i günceller.

## SEO ve uyumluluk notları
- Hiçbir statik site Google'da bütün aramalarda ilk sırayı garanti edemez. Bu proje teknik SEO, benzersiz ürün sayfaları, iç bağlantı, mobil uyum, canonical, yapılandırılmış veri ve sitemap temelini hazırlar. Sıralama; rekabet, site geçmişi, içerik kalitesi, güvenilir bağlantılar, kullanıcı deneyimi ve Google'ın değerlendirmesine bağlıdır.
- Motor kodu/araç eşleşmeleri ürün aileleri için araştırılmış başlangıç bilgileridir. Aynı modelin her yıl ve donanımında aynı motor bulunmaz. Satıştan önce motor kodu, şasi numarası ve aksesuar uyumu teyit edilmelidir.
- Müşteri yorumu veya Google puanı uydurulmamıştır. Gerçek ve yayımlama izni alınmış müşteri yorumları geldikçe ekleyin.
- KVKK sayfasında veri sorumlusunun tam yasal unvanı ve resmî başvuru kanalı henüz verilmediği için yayına almadan önce işletme bilgileriyle tamamlanması gerektiği belirtilmiştir. Hukuk danışmanı kontrolü önerilir.
- Fiyatlar siteye eklenmez; bilgilendirme sayfası ithal ürünlerde döviz kuru ve tedarik maliyetlerindeki değişkenliği açıklar.
