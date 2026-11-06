#!/usr/bin/env python3
"""Apply distinct, title-led SEO copy to every Volkswagen Motor product page."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
catalog_path = ROOT / "data" / "urunler.json"
products = json.loads(catalog_path.read_text(encoding="utf-8"))

def code_list(value):
    import re
    codes = re.findall(r"(?<![A-Z])[A-Z]{3,4}(?![A-Z])", value or "")
    return ", ".join(dict.fromkeys(codes)) or value

def description(p, i):
    codes = code_list(p.get("codes", ""))
    brand, model, engine = p["brand"], p["models"], p["engine"]
    templates = [
        f"{brand} {model} {engine} komple motor seçenekleri: {codes} kodları için ürün ve uyumluluk bilgisi. Şasi ve motor koduyla teyit alın.",
        f"{model} {engine} motor arayanlara {brand} için {codes} kodlu motor bilgileri. Doğru seçim, mevcut motor kodu ve şasiyle doğrulanır.",
        f"{brand} {model} için {engine} komple motor ve {codes} kodları hakkında bilgi alın. Model yılına göre uyumluluk kontrolü yapılır.",
        f"{model} {engine} komple motor ilanı. {codes} kodlarının aracınıza uygunluğu motor etiketi ve şasi numarasıyla kontrol edilmelidir.",
        f"{brand} {model} motor değişimi için {engine} {codes} kod grubu hakkında bilgi. Ekipman ve şasi uyumu sipariş öncesi teyit edilir.",
        f"{brand} {model} {engine} motor seçeneklerini inceleyin. {codes} motor kodu, araç yılı ve şasi bilgisi birlikte değerlendirilir.",
    ]
    return templates[i % len(templates)]

def body(p, i):
    codes = code_list(p.get("codes", ""))
    brand, model, engine = p["brand"], p["models"], p["engine"]
    intros = [
        f"{model} için {engine} komple motor araştırırken ilk kontrol edilmesi gereken bilgi, araç üzerindeki motor kodudur.",
        f"{brand} {model} motor değişiminde yalnızca motor hacmine bakmak yeterli değildir; doğru motor kodu ve teknik donanım birlikte değerlendirilmelidir.",
        f"{model} {engine} motor ihtiyacında kasa nesli, üretim yılı ve motorun tam kodu doğru ürünün belirlenmesine yardımcı olur.",
        f"{brand} araçlarda aynı motor hacmi farklı güç ve donanım seçenekleriyle sunulabildiğinden, {model} için motor seçimi araç bilgileriyle yapılmalıdır.",
        f"{model} modeline yönelik komple motor arayışında mevcut motorun kodu ve üzerindeki yardımcı ekipmanlar karşılaştırılmalıdır.",
        f"{brand} {model} için motor tedarikinde doğru eşleşme; motor kodu, üretim yılı, şasi ve bağlantı detaylarının birlikte incelenmesiyle belirlenir.",
        f"{engine} motor seçerken {model} modelinin tam kasa ve motor versiyonunu dikkate almak gerekir.",
        f"{model} aracınız için motor araştırmasını motor kodu üzerinden yapmak, yalnızca model adına göre seçim yapmaktan daha sağlıklıdır.",
    ]
    family = p.get("family", "")
    if "EA211" in family:
        technical = f"Bu ilan {codes} kodlarıyla ilişkilendirilen EA211 1.4 TSI/TFSI motor ailesine odaklanır. Aynı ailedeki kodlar her model yılına veya güç seçeneğine doğrudan uymaz."
    elif "CAV" in codes:
        technical = f"İlan {codes} kod ailesine odaklanır. CAVA ve CAVD gibi varyantlarda güç, motor yönetimi ve yardımcı ekipmanlar farklılaşabileceğinden tam kod kontrolü önemlidir."
    elif "CAX" in codes:
        technical = f"Bu sayfa {codes} kodlu EA111 1.4 TSI/TFSI motor seçenekleri için hazırlanmıştır. CAXA ve CAXC ayrımı, motor üzerindeki tam kod ve araç verileriyle doğrulanmalıdır."
    elif "EA888" in family:
        technical = f"İlan {codes} kodlu EA888 2.0 TFSI motor ailesini kapsar. Devirdaim, yağ soğutucu ve diğer yardımcı parçaların teslimata dahil olup olmadığı ürün bazında netleştirilmelidir."
    else:
        technical = f"Bu ilan {codes} kodlu {family or engine} motor seçeneğiyle ilgilidir. Bağlantılar, emisyon donanımı ve yardımcı parçalar araç versiyonuna göre değişebilir."
    endings = [
        "Teklif öncesinde mevcut motor kodunu, şasi numarasını ve üretim yılını paylaşın; ürünün araçla uyumu ve teslim kapsamı birlikte kontrol edilsin.",
        "Sipariş vermeden önce motor etiketi veya mevcut motor üzerindeki kod ile şasi numarasını karşılaştırın. Güncel ürün durumu ve donanım kapsamını iletişim kurarak öğrenebilirsiniz.",
        "Uyumluluk için ruhsat bilgisi tek başına yeterli olmayabilir. Motor kodu fotoğrafı ve şasi numarasıyla kontrol talep ederek yanlış ürün seçimi riskini azaltabilirsiniz.",
        "Sıfır, çıkma veya rektefeli seçeneklerin güncel bulunabilirliği ayrıca sorulmalıdır. Ürünün üzerindeki ekipmanlar ve teslim içeriği teklif sırasında netleştirilir.",
        "Aracınızın motor kodunu ve şasi numarasını ilettiğinizde doğru varyant, yardımcı ekipmanlar ve tedarik seçeneği hakkında bilgi alabilirsiniz.",
        "Model yılına göre farklı motor versiyonları bulunabileceği için sipariş öncesinde kod ve şasi teyidi yapılmalıdır. Stok ve teslimat bilgisi ayrıca paylaşılır.",
        "İletişime geçerken araç modeli, üretim yılı, motor kodu ve varsa motor fotoğrafını iletmeniz doğru eşleşmenin kontrolünü kolaylaştırır.",
        "Ürün fotoğrafı ve başlık, tek başına tüm donanımın teslim edileceği anlamına gelmez. Motorun kapsamını ve uyumluluğunu siparişten önce yazılı olarak teyit edin.",
    ]
    return f"{intros[i % len(intros)]} {technical} {endings[(i * 3) % len(endings)]}"

index_path = ROOT / "index.html"
index_html = index_path.read_text(encoding="utf-8")
for i, p in enumerate(products):
    old_desc = p.get("description", "")
    old_body = p.get("body", "")
    new_desc = description(p, i)
    new_body = body(p, i)
    p["description"] = new_desc
    p["body"] = new_body
    page_path = ROOT / "urun" / f"{p['slug']}.html"
    page_html = page_path.read_text(encoding="utf-8")
    if old_desc:
        page_html = page_html.replace(old_desc, new_desc)
        index_html = index_html.replace(old_desc, new_desc)
    if old_body:
        page_html = page_html.replace(old_body, new_body)
    page_path.write_text(page_html, encoding="utf-8")

catalog_path.write_text(json.dumps(products, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
index_path.write_text(index_html, encoding="utf-8")

# Keep the requested brand image as the favicon on all product pages.
for page_path in (ROOT / "urun").glob("*.html"):
    page_html = page_path.read_text(encoding="utf-8")
    page_html = page_html.replace("favicon.svg", "volkswagen-motor.jpg")
    page_path.write_text(page_html, encoding="utf-8")
index_html = index_path.read_text(encoding="utf-8")
index_html = index_html.replace("favicon.svg", "volkswagen-motor.jpg")
index_path.write_text(index_html, encoding="utf-8")
print(f"SEO copy applied to {len(products)} individual motor pages.")
