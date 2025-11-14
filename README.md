# SF-Circle
Advanced "Draw a Perfect Circle" App. Leaderboard feature available
# Flask Circle Drawing App | Daire Çizme Uygulaması

A simple **Flask leaderboard app** that tracks scores for three categories: `circle`, `square`, and `triangle`.  
Üç kategori için skorları saklayan basit bir **Flask lider tablo uygulaması**: `circle`, `square`, `triangle`.

---

<div style="background-color:#f0f4f8; padding:10px; border-left:5px solid #2b7a78; margin-bottom:10px;">
<strong>Features | Özellikler</strong>

<ul>
<li><strong>Web Interface | Web Arayüzü:</strong> Access the main page at <code>/</code> / Ana sayfaya <code>/</code> adresinden erişilebilir</li>
<li><strong>API Endpoints | API Uç Noktaları:</strong>
  <ul>
    <li><code>GET /leaderboard.json</code> → Returns current leaderboard data / Mevcut lider tablo verilerini döner</li>
    <li><code>POST /leaderboard.json</code> → Update leaderboard data via JSON / JSON ile lider tablo güncelleme</li>
  </ul>
</li>
<li><strong>Persistent Leaderboard | Kalıcı Lider Tablosu:</strong> Scores are stored in <code>leaderboard.json</code>, auto-created if missing / Skorlar <code>leaderboard.json</code> içinde saklanır, yoksa otomatik oluşturulur</li>
</ul>
</div>

<div style="background-color:#fef9f9; padding:10px; border-left:5px solid #d00000; margin-bottom:10px;">
<strong>Requirements | Gereksinimler</strong>

<ul>
<li>Python 3.10+</li>
<li>Flask</li>
</ul>

Install Flask:  
<pre>pip install Flask</pre>
</div>

<div style="background-color:#f0f4f8; padding:10px; border-left:5px solid #2b7a78; margin-bottom:10px;">
<strong>Usage | Kullanım</strong>

<ol>
<li>Clone or download the repository / Repo’yu klonla veya indir</li>
<li>Navigate to the project directory / Terminalden proje dizinine geç</li>
<li>Run the app: <pre>python app.py</pre></li>
<li>Open your browser at <a href="http://localhost:3000">http://localhost:3000</a> / Tarayıcıdan adresi aç</li>
<li>Access or update leaderboard at <code>/leaderboard.json</code> / Lider tabloya ulaş veya güncelle</li>
</ol>
</div>

<div style="background-color:#fef9f9; padding:10px; border-left:5px solid #d00000; margin-bottom:10px;">
<strong>Leaderboard JSON Format | Lider Tablosu JSON Formatı</strong>

<pre>{
  "circle": [],
  "square": [],
  "triangle": []
}</pre>

Each category contains a list of scores / Her kategori skor listesi içerir
</div>

<div style="background-color:#f0f4f8; padding:10px; border-left:5px solid #2b7a78; margin-bottom:10px;">
<strong>Contributing | Katkıda Bulunma</strong>

Open source! Feel free to fork, improve, and submit a pull request.  
Açık kaynak! Fork yapabilir, geliştirme ekleyebilir ve pull request gönderebilirsin.
</div>

<div style="background-color:#fef9f9; padding:10px; border-left:5px solid #d00000;">
<strong>License | Lisans</strong>

MIT License
</div>
