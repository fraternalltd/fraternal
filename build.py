from PIL import Image
import base64, io

# Compress the cabin image
img_path = "/sessions/youthful-inspiring-ramanujan/mnt/fraternal.html/ChatGPT Image Jul 11, 2026, 06_52_03 PM.png"
try:
    img = Image.open(img_path).convert("RGB")
    max_w = 1400
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(img.height * ratio)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=82, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    HERO_BG = "data:image/jpeg;base64," + b64
    print(f"Image embedded: {len(buf.getvalue())//1024}KB")
except Exception as e:
    HERO_BG = "https://images.unsplash.com/photo-1449158743715-0a90ebb6d2d8?w=1800&q=80&auto=format&fit=crop"
    print(f"Fallback URL used: {e}")

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fraternal — Rent-to-own cabins, built in Hawke's Bay</title>
  <meta name="description" content="Warm, Healthy-Homes sleepouts built by hand in Hawke's Bay. From about $130 a week — no council consent, yours at the end.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root{--ink:#1E1C1A;--cedar:#B5623B;--cedar-dark:#8A4A2C;--cedar-light:#D4875E;--bone:#F4EDDE;--stone:#E7DECC;--stone-light:#EDE6D8;--slate:#6B6A64;--mist:#D9D2C4;--white:#FFFFFF;--charcoal:#2D2B29;--nav-h:68px;--r:6px;--r-lg:12px;--shadow:0 4px 24px rgba(0,0,0,.08);--shadow-lg:0 16px 56px rgba(0,0,0,.16)}
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    html{scroll-behavior:smooth}
    body{font-family:'Inter',-apple-system,sans-serif;color:var(--ink);background:var(--bone);line-height:1.7;overflow-x:hidden;-webkit-font-smoothing:antialiased}
    img{max-width:100%;display:block}
    a{text-decoration:none;color:inherit}
    input,select,textarea,button{font-family:inherit}
    h1,h2,h3{font-family:'Outfit',-apple-system,sans-serif;line-height:1.12;letter-spacing:-.3px}
    h1{font-size:clamp(2.1rem,5.2vw,3.8rem);font-weight:700}
    h2{font-size:clamp(1.7rem,3.3vw,2.5rem);font-weight:700}
    h3{font-size:clamp(1.1rem,2vw,1.35rem);font-weight:600}
    .label{display:block;font-size:.72rem;font-weight:600;letter-spacing:.13em;text-transform:uppercase;color:var(--cedar);margin-bottom:.65rem;font-family:'Outfit',sans-serif}
    .wrap{max-width:1120px;margin:0 auto;padding:0 24px}
    section{padding:96px 0}
    section.tight{padding:68px 0}
    .btn{display:inline-flex;align-items:center;gap:7px;padding:13px 26px;border-radius:var(--r);font-size:.9rem;font-weight:600;cursor:pointer;border:2px solid transparent;transition:all .2s ease;white-space:nowrap;line-height:1;font-family:'Outfit',sans-serif}
    .btn-cedar{background:var(--cedar);color:var(--bone);border-color:var(--cedar)}
    .btn-cedar:hover{background:var(--cedar-dark);border-color:var(--cedar-dark);transform:translateY(-1px)}
    .btn-black{background:var(--ink);color:var(--bone);border-color:var(--ink)}
    .btn-black:hover{background:#111;transform:translateY(-1px)}
    .btn-hero-sec{background:rgba(255,255,255,.95);color:var(--ink);border-color:rgba(255,255,255,.95)}
    .btn-hero-sec:hover{background:#fff;border-color:#fff;transform:translateY(-1px);box-shadow:0 6px 20px rgba(0,0,0,.18)}
    .btn-white-outline{background:transparent;color:#fff;border-color:rgba(255,255,255,.6)}
    .btn-white-outline:hover{background:rgba(255,255,255,.1);border-color:#fff}
    .btn-bone-outline{background:transparent;color:var(--bone);border-color:rgba(244,237,222,.5)}
    .btn-bone-outline:hover{background:rgba(244,237,222,.1);border-color:var(--bone)}
    .upload-btn{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;background:rgba(255,255,255,.92);color:var(--ink);border:1.5px solid var(--mist);border-radius:var(--r);font-size:.78rem;font-weight:600;cursor:pointer;transition:all .2s;font-family:'Outfit',sans-serif}
    .upload-btn:hover{background:#fff;border-color:var(--cedar);color:var(--cedar)}
    .logo-lockup{display:inline-flex;align-items:center;gap:13px;text-decoration:none;line-height:1;flex-shrink:0}
    .logo-icon{flex-shrink:0;color:var(--cedar)}
    .logo-text{display:flex;flex-direction:column;gap:4px}
    .logo-name{font-family:'Outfit',sans-serif;font-size:1.28rem;font-weight:600;color:#fff;letter-spacing:.3px;line-height:1}
    .logo-rule-el{display:block;height:1.5px;background:var(--cedar);width:100%}
    .logo-desc{font-size:.52rem;font-weight:500;letter-spacing:.22em;color:rgba(255,255,255,.38);text-transform:lowercase}
    #nav{position:fixed;top:0;left:0;right:0;z-index:1000;height:var(--nav-h);background:rgba(30,28,26,.97);backdrop-filter:blur(14px);border-bottom:1px solid rgba(255,255,255,.05);display:flex;align-items:center}
    .nav-inner{display:flex;align-items:center;justify-content:space-between;width:100%;max-width:1120px;margin:0 auto;padding:0 24px}
    .nav-links{display:flex;gap:28px;list-style:none}
    .nav-links a{color:rgba(255,255,255,.6);font-size:.85rem;font-weight:500;transition:color .2s}
    .nav-links a:hover{color:#fff}
    .nav-actions{display:flex;gap:10px}
    .burger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px}
    .burger span{display:block;width:22px;height:2px;background:#fff;border-radius:2px}
    #drawer{display:none;position:fixed;top:var(--nav-h);left:0;right:0;background:var(--ink);padding:28px 24px;z-index:999;flex-direction:column;gap:18px;border-bottom:1px solid rgba(255,255,255,.08)}
    #drawer.open{display:flex}
    #drawer a{color:#fff;font-size:1.05rem;font-weight:600;padding:6px 0;border-bottom:1px solid rgba(255,255,255,.07)}
    #float-cta{position:fixed;bottom:26px;right:22px;z-index:900;opacity:0;transform:translateY(80px);transition:all .4s cubic-bezier(.34,1.56,.64,1)}
    #float-cta.show{opacity:1;transform:translateY(0)}
    #float-cta .btn{box-shadow:0 8px 28px rgba(181,98,59,.42);padding:15px 24px}
    #hero{position:relative;min-height:100svh;display:flex;align-items:center;padding-top:var(--nav-h);overflow:hidden}
    .hero-bg{position:absolute;inset:0;background-image:url('HERO_BG_PLACEHOLDER');background-size:cover;background-position:center 40%;opacity:.48;animation:hzoom 14s ease-out forwards}
    @keyframes hzoom{from{transform:scale(1.06)}to{transform:scale(1)}}
    .hero-grad{position:absolute;inset:0;background:linear-gradient(135deg,rgba(30,28,26,.85) 0%,rgba(30,28,26,.32) 55%,rgba(30,28,26,.78) 100%)}
    .hero-content{position:relative;z-index:2;max-width:700px}
    .hero-pill{display:inline-flex;align-items:center;gap:8px;background:var(--cedar);color:var(--bone);padding:8px 16px;border-radius:100px;font-size:.77rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;margin-bottom:24px;font-family:'Outfit',sans-serif}
    .hero-pill-dot{width:7px;height:7px;background:var(--bone);border-radius:50%;opacity:.9;animation:blink 2s infinite}
    @keyframes blink{0%,100%{opacity:.9}50%{opacity:.3}}
    #hero h1{color:#fff;margin-bottom:16px}
    .hero-own{color:rgba(255,255,255,.92);font-size:1rem;margin-bottom:36px;font-weight:600;background:rgba(30,28,26,.32);display:inline-block;padding:7px 14px;border-radius:var(--r);border-left:3px solid var(--cedar)}
    .hero-btns{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:44px}
    .hero-stats{display:flex;gap:0;flex-wrap:wrap;background:rgba(30,28,26,.48);border-radius:var(--r-lg);overflow:hidden;border:1px solid rgba(255,255,255,.08)}
    .hstat{flex:1;min-width:130px;padding:18px 24px;border-right:1px solid rgba(255,255,255,.08)}
    .hstat:last-child{border-right:none}
    .hstat-num{font-family:'Outfit',sans-serif;font-size:2rem;font-weight:700;color:#fff;line-height:1}
    .hstat-lbl{font-size:.75rem;color:rgba(255,255,255,.62);margin-top:4px;font-weight:500}
    .hero-upload-wrap{position:absolute;bottom:24px;right:24px;z-index:10}
    #trust{background:var(--ink);border-bottom:1px solid rgba(255,255,255,.05)}
    .trust-row{display:flex;flex-wrap:wrap}
    .trust-item{flex:1;min-width:210px;display:flex;align-items:center;gap:11px;padding:20px 26px;color:rgba(255,255,255,.65);font-size:.83rem;font-weight:500;border-right:1px solid rgba(255,255,255,.05)}
    .trust-item:last-child{border-right:none}
    .t-icon{width:36px;height:36px;flex-shrink:0;background:rgba(181,98,59,.14);border-radius:8px;display:flex;align-items:center;justify-content:center;color:var(--cedar)}
    #cabins{background:var(--bone)}
    .cabin-section-hd{text-align:center;margin-bottom:52px}
    .cabin-section-title{font-family:'Outfit',sans-serif;font-size:clamp(2.4rem,5vw,3.8rem);font-weight:700;color:var(--ink);line-height:1.1;margin-bottom:6px;letter-spacing:-.5px}
    .cabin-section-sub{font-size:1rem;color:var(--slate)}
    .cabin-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start}
    .img-main{border-radius:var(--r-lg);overflow:hidden;aspect-ratio:4/3;cursor:pointer;background:var(--stone)}
    .img-main img{width:100%;height:100%;object-fit:cover;transition:transform .5s ease;display:block}
    .img-main:hover img{transform:scale(1.03)}
    .cabin-drag-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:10px}
    .cabin-drag-item{position:relative;border-radius:7px;overflow:visible;user-select:none;cursor:grab}
    .cabin-drag-item.is-dragging{opacity:.3;cursor:grabbing}
    .cabin-drag-item.drag-over .cabin-di-img{outline:3px solid var(--cedar);outline-offset:2px;border-radius:9px}
    .cabin-di-img{aspect-ratio:4/3;border-radius:7px;overflow:hidden;background:var(--stone);cursor:pointer}
    .cabin-di-img img{width:100%;height:100%;object-fit:cover;display:block;pointer-events:none}
    .photo-main-badge{position:absolute;bottom:22px;left:4px;background:var(--cedar);color:var(--bone);font-size:.58rem;font-weight:600;padding:2px 5px;border-radius:3px;pointer-events:none;z-index:3;font-family:'Outfit',sans-serif}
    .di-controls{display:flex;align-items:center;justify-content:center;gap:3px;margin-top:4px}
    .drag-arrow-btn{background:rgba(255,255,255,.85);border:1px solid var(--mist);border-radius:4px;padding:1px 7px;font-size:.7rem;cursor:pointer;font-weight:600;color:var(--ink);transition:all .15s;line-height:1.6}
    .drag-arrow-btn:hover{background:#fff;border-color:var(--cedar);color:var(--cedar)}
    .drag-del-btn{width:20px;height:20px;background:#dc2626;color:#fff;border:2px solid #fff;border-radius:50%;font-size:12px;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:5;padding:0;position:absolute;top:-7px;right:-7px;transition:background .15s}
    .drag-del-btn:hover{background:#b91c1c}
    .cabin-upload-row{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:10px}
    .cabin-upload-hint{font-size:.72rem;color:var(--slate)}
    .cabin-empty-state{aspect-ratio:4/3;border-radius:var(--r-lg);border:2px dashed var(--mist);background:var(--stone-light);flex-direction:column;align-items:center;justify-content:center;gap:10px;color:var(--slate);font-size:.85rem;text-align:center;padding:24px;display:none}
    .drag-hint-text{font-size:.7rem;color:var(--slate);margin-top:6px;text-align:center;display:none}
    .stock-pill{display:inline-flex;align-items:center;gap:7px;background:rgba(181,98,59,.1);border:1px solid rgba(181,98,59,.35);color:var(--cedar-dark);padding:4px 12px;border-radius:100px;font-size:.77rem;font-weight:600;margin-bottom:14px;font-family:'Outfit',sans-serif}
    .stock-pill::before{content:'';width:6px;height:6px;background:var(--cedar);border-radius:50%;flex-shrink:0;animation:blink 2s infinite}
    .price-row{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-bottom:22px}
    .price-main{font-family:'Outfit',sans-serif;font-size:2.6rem;font-weight:700;color:var(--cedar)}
    .price-alt{font-size:.95rem;color:var(--slate)}
    .specs{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:24px}
    .spec{display:flex;flex-direction:column;gap:1px}
    .spec-l{font-size:.7rem;color:var(--slate);text-transform:uppercase;letter-spacing:.07em}
    .spec-v{font-size:.88rem;font-weight:600;color:var(--ink)}
    .feat-list{list-style:none;display:flex;flex-direction:column;gap:9px;margin-bottom:30px}
    .feat-list li{display:flex;align-items:flex-start;gap:9px;font-size:.875rem;color:var(--charcoal)}
    .feat-list li::before{content:'';flex-shrink:0;margin-top:3px;width:16px;height:16px;border-radius:50%;background:var(--cedar);background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='none'%3E%3Cpath d='M3.5 8l3 3L12.5 5' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")}
    .cabin-ctas{display:flex;gap:10px;flex-wrap:wrap}
    #amenities{background:var(--cedar)}
    #amenities .label{color:rgba(244,237,222,.6)}
    .amen-intro{color:rgba(244,237,222,.75);max-width:500px;margin-bottom:44px}
    .amen-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:var(--r-lg);overflow:hidden;gap:1px}
    .amen-cell{background:rgba(138,74,44,.55);padding:22px;display:flex;gap:13px;align-items:flex-start;transition:background .2s}
    .amen-cell:hover{background:rgba(138,74,44,.8)}
    .amen-ico{width:38px;height:38px;flex-shrink:0;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.2);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem}
    .amen-title{display:block;color:#fff;font-size:.875rem;font-weight:600;margin-bottom:2px;font-family:'Outfit',sans-serif}
    .amen-sub{font-size:.77rem;color:rgba(255,255,255,.6)}
    #how{background:var(--stone)}
    .process-hd{text-align:center;margin-bottom:52px}
    .process-title{font-family:'Outfit',sans-serif;font-size:clamp(2.4rem,5vw,3.8rem);font-weight:700;color:var(--ink);line-height:1.1;margin-bottom:10px;letter-spacing:-.5px}
    .process-sub{font-size:1rem;color:var(--slate)}
    .pay-steps{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}
    .pay-step{background:var(--bone);border-radius:var(--r-lg);padding:26px 18px;text-align:center;border:1.5px solid var(--mist);display:flex;flex-direction:column;align-items:center}
    .pay-step-n{font-family:'Outfit',sans-serif;font-size:2.6rem;font-weight:700;color:var(--cedar);line-height:1;margin-bottom:12px;opacity:.9}
    .pay-step-t{font-weight:700;font-size:.9rem;color:var(--ink);margin-bottom:6px;font-family:'Outfit',sans-serif;line-height:1.2}
    .pay-step-d{font-size:.77rem;color:var(--slate);line-height:1.5}
    #finance{background:var(--bone)}
    .fin-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start}
    .fin-display{font-family:'Outfit',sans-serif;font-size:clamp(2.8rem,5.5vw,4.2rem);font-weight:700;color:var(--ink);line-height:1.05;margin-bottom:12px;letter-spacing:-.5px}
    .fin-subtitle{font-size:clamp(1rem,1.8vw,1.2rem);color:var(--cedar-dark);font-weight:600;margin-bottom:24px;line-height:1.4;font-family:'Outfit',sans-serif}
    .fin-info p{color:var(--slate);line-height:1.8;margin-bottom:18px}
    .own-callout{background:var(--ink);color:var(--bone);border-radius:var(--r-lg);padding:18px 22px;margin-bottom:24px;font-weight:600;font-size:.95rem;line-height:1.55;font-family:'Outfit',sans-serif}
    .own-callout span{display:block;font-size:.8rem;font-weight:400;color:rgba(244,237,222,.7);margin-top:4px;font-family:'Inter',sans-serif}
    .own-callout em{color:var(--cedar);font-style:normal;font-weight:700}
    .mtf-badge{display:flex;align-items:center;gap:11px;background:var(--stone);border:1px solid var(--mist);border-radius:8px;padding:13px 16px;font-size:.82rem;color:var(--slate);margin-top:24px}
    .mtf-ico{width:34px;height:34px;flex-shrink:0;background:var(--ink);border-radius:6px;display:flex;align-items:center;justify-content:center;color:var(--bone);font-weight:700;font-size:.8rem;font-family:'Outfit',sans-serif}
    .calc-card{background:var(--white);border-radius:var(--r-lg);padding:36px;box-shadow:var(--shadow-lg);border:3px solid var(--cedar)}
    .calc-card h3{margin-bottom:24px;color:var(--ink)}
    .fg{margin-bottom:18px}
    .fg label{display:block;font-size:.72rem;font-weight:600;color:var(--slate);letter-spacing:.07em;text-transform:uppercase;margin-bottom:5px;font-family:'Outfit',sans-serif}
    .fg input,.fg select{width:100%;padding:11px 13px;border:1.5px solid var(--mist);border-radius:var(--r);font-size:.95rem;color:var(--ink);background:var(--bone);transition:border-color .2s;-webkit-appearance:none}
    .fg input:focus,.fg select:focus{outline:none;border-color:var(--cedar)}
    .calc-result{background:var(--ink);border-radius:10px;padding:24px;text-align:center;margin:24px 0}
    .cr-label{color:rgba(244,237,222,.5);font-size:.78rem;margin-bottom:4px}
    .cr-amount{font-family:'Outfit',sans-serif;font-size:3rem;font-weight:700;color:var(--cedar-light);line-height:1}
    .cr-sub{color:rgba(244,237,222,.3);font-size:.72rem;margin-top:8px}
    #gallery{background:var(--stone)}
    .gallery-hd{text-align:center;margin-bottom:36px}
    .gallery-title{font-family:'Outfit',sans-serif;font-size:clamp(2.4rem,5vw,3.8rem);font-weight:700;color:var(--ink);line-height:1.1;margin-bottom:8px;letter-spacing:-.5px}
    .gallery-sub{font-size:1rem;color:var(--slate)}
    .gal-dyn-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;min-height:60px}
    .gal-dyn-item{position:relative;border-radius:8px;overflow:visible;cursor:pointer;user-select:none}
    .gal-dyn-item.wide{grid-column:span 2}
    .gal-dyn-item.full-w{grid-column:span 3}
    .gal-dyn-item.is-dragging{opacity:.3}
    .gal-dyn-item.drag-over .gal-di-img{outline:3px solid var(--cedar);outline-offset:2px;border-radius:10px}
    .gal-di-img{aspect-ratio:4/3;border-radius:8px;overflow:hidden;background:var(--stone-light)}
    .gal-dyn-item.wide .gal-di-img,.gal-dyn-item.full-w .gal-di-img{aspect-ratio:16/9}
    .gal-di-img img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .3s}
    .gal-dyn-item:hover .gal-di-img img{transform:scale(1.04)}
    .gal-empty-state{grid-column:1/-1;border:2px dashed var(--mist);border-radius:12px;padding:52px 24px;text-align:center;color:var(--slate);font-size:.88rem;line-height:1.7}
    .gallery-upload-row{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:14px}
    #lbx{display:none;position:fixed;inset:0;background:rgba(30,28,26,.97);z-index:2000;align-items:center;justify-content:center}
    #lbx.open{display:flex}
    #lbx img{max-width:90vw;max-height:86vh;object-fit:contain;border-radius:4px}
    .lbx-close{position:absolute;top:18px;right:22px;background:none;border:none;color:#fff;font-size:2.2rem;cursor:pointer;opacity:.7;line-height:1}
    .lbx-close:hover{opacity:1}
    .lbx-arrow{position:absolute;top:50%;transform:translateY(-50%);background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);color:#fff;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:1.2rem;transition:background .2s}
    .lbx-arrow:hover{background:rgba(255,255,255,.2)}
    #lbx-prev{left:18px}
    #lbx-next{right:18px}
    #about-problem{background:var(--ink);padding:80px 0}
    .ap-inner{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}
    .ap-quote{font-family:'Outfit',sans-serif;font-size:clamp(1.6rem,3vw,2.2rem);font-weight:700;color:var(--bone);line-height:1.2}
    .ap-quote em{color:var(--cedar);font-style:normal}
    .ap-body p{color:rgba(244,237,222,.7);font-size:1rem;line-height:1.85}
    #about{background:var(--bone)}
    .about-grid{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:start}
    .team-cards{display:grid;grid-template-columns:1fr 1fr;gap:20px}
    .team-member{display:flex;flex-direction:column;gap:10px}
    .tm-photo{border-radius:10px;overflow:hidden;aspect-ratio:3/4;background:var(--stone)}
    .tm-photo img{width:100%;height:100%;object-fit:cover;display:block}
    .tm-empty{aspect-ratio:3/4;border-radius:10px;border:2px dashed var(--mist);background:var(--stone-light);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:var(--slate);font-size:.78rem;text-align:center;padding:16px}
    .tm-upload-row{display:flex;gap:6px;flex-wrap:wrap}
    .tm-info{text-align:center}
    .tm-info strong{display:block;font-size:.92rem;font-weight:700;color:var(--ink);font-family:'Outfit',sans-serif;margin-bottom:2px}
    .tm-role{display:block;font-size:.75rem;color:var(--cedar);font-weight:600}
    .tm-sub{display:block;font-size:.7rem;color:var(--slate);margin-top:1px}
    .about-text h2{font-size:clamp(2.2rem,3.8vw,3rem);margin-bottom:16px;color:var(--ink)}
    .about-text p{color:var(--slate);line-height:1.8;margin-bottom:18px}
    .creds{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:28px}
    .cred{display:flex;align-items:center;gap:9px;background:var(--white);border:1px solid var(--mist);border-radius:7px;padding:11px 13px;font-size:.81rem;font-weight:600;color:var(--ink);font-family:'Outfit',sans-serif}
    .cred-dot{width:8px;height:8px;background:var(--cedar);border-radius:50%;flex-shrink:0}
    #about-cta{background:var(--cedar);padding:60px 0}
    .about-cta-inner{display:flex;align-items:center;justify-content:space-between;gap:36px;flex-wrap:wrap}
    .about-cta-text h2{color:var(--bone);font-size:clamp(1.4rem,2.5vw,2rem);margin-bottom:8px}
    .about-cta-text p{color:rgba(244,237,222,.75);font-size:.95rem;max-width:520px;line-height:1.6}
    #faq{background:var(--bone)}
    .faq-hd{text-align:center;margin-bottom:52px}
    .faq-display{font-family:'Outfit',sans-serif;font-size:clamp(2.4rem,5vw,3.8rem);font-weight:700;color:var(--ink);line-height:1.1;margin-bottom:8px;letter-spacing:-.5px}
    .faq-subtitle{font-size:1rem;color:var(--slate)}
    .faq-list{max-width:700px;margin:0 auto;display:flex;flex-direction:column;gap:4px}
    .faq-item{background:var(--white);border:1px solid var(--mist);border-radius:8px;overflow:hidden}
    .faq-q{width:100%;padding:18px 22px;display:flex;align-items:center;justify-content:space-between;gap:14px;background:none;border:none;text-align:left;cursor:pointer;font-size:.9rem;font-weight:600;color:var(--ink);transition:background .2s;font-family:'Outfit',sans-serif}
    .faq-q:hover{background:var(--bone)}
    .faq-chev{flex-shrink:0;color:var(--cedar);transition:transform .3s}
    .faq-item.open .faq-chev{transform:rotate(180deg)}
    .faq-a{max-height:0;overflow:hidden;transition:max-height .35s ease}
    .faq-item.open .faq-a{max-height:240px}
    .faq-a p{padding:15px 22px 18px;color:var(--slate);font-size:.875rem;line-height:1.7;border-top:1px solid var(--mist)}
    #newsletter{background:var(--ink);padding:72px 0}
    .nl-inner{text-align:center;max-width:500px;margin:0 auto}
    .nl-inner .label{color:rgba(181,98,59,.8)}
    .nl-inner h2{color:var(--bone);margin-bottom:10px}
    .nl-inner>p{color:rgba(244,237,222,.65);margin-bottom:26px}
    .nl-form{display:flex;max-width:420px;margin:0 auto 10px}
    .nl-form input{flex:1;padding:13px 16px;border:none;border-radius:var(--r) 0 0 var(--r);font-size:.9rem;outline:none;color:var(--ink);background:var(--bone)}
    .nl-form button{padding:13px 22px;background:var(--cedar);color:var(--bone);border:none;border-radius:0 var(--r) var(--r) 0;font-size:.875rem;font-weight:600;cursor:pointer;white-space:nowrap;transition:background .2s;font-family:'Outfit',sans-serif}
    .nl-form button:hover{background:var(--cedar-dark)}
    .nl-sub{font-size:.72rem;color:rgba(244,237,222,.38)}
    #contact{background:var(--stone)}
    .contact-grid{display:grid;grid-template-columns:1fr 1.4fr;gap:60px;align-items:start}
    .contact-info h2{margin-bottom:14px;color:var(--ink)}
    .contact-info>p{color:var(--slate);margin-bottom:28px;line-height:1.7}
    .cm-list{display:flex;flex-direction:column;gap:14px;margin-bottom:28px}
    .cm{display:flex;align-items:center;gap:13px;font-size:.875rem}
    .cm-ico{width:38px;height:38px;flex-shrink:0;background:var(--cedar);border-radius:8px;display:flex;align-items:center;justify-content:center;color:var(--bone)}
    .cm strong{display:block;font-size:.73rem;color:var(--slate);font-weight:600;margin-bottom:1px}
    .cm a,.cm span{color:var(--ink);font-weight:600}
    .cm a:hover{color:var(--cedar)}
    .socials{display:flex;gap:9px}
    .soc-link{width:38px;height:38px;background:var(--ink);border-radius:8px;display:flex;align-items:center;justify-content:center;color:var(--bone);transition:background .2s}
    .soc-link:hover{background:var(--cedar)}
    .soc-note{font-size:.72rem;color:var(--slate);margin-top:8px}
    .cf{background:var(--white);border-radius:var(--r-lg);padding:36px;box-shadow:var(--shadow);border:1px solid var(--mist)}
    .cf-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
    .cf input,.cf select,.cf textarea{width:100%;padding:11px 13px;border:1.5px solid var(--mist);border-radius:var(--r);font-size:.875rem;color:var(--ink);background:var(--bone);transition:border-color .2s;-webkit-appearance:none}
    .cf input:focus,.cf select:focus,.cf textarea:focus{outline:none;border-color:var(--cedar)}
    .cf textarea{resize:vertical;min-height:90px}
    .cf .fg{margin-bottom:14px}
    .cf-submit .btn{width:100%;justify-content:center;padding:15px;font-size:.95rem;margin-top:6px}
    .cf-note{text-align:center;color:var(--slate);font-size:.75rem;margin-top:9px}
    footer{background:var(--ink);color:rgba(244,237,222,.5);padding:52px 0 30px}
    .foot-top{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:44px;padding-bottom:40px;margin-bottom:30px;border-bottom:1px solid rgba(255,255,255,.07)}
    .foot-brand p{font-size:.83rem;line-height:1.65;margin-top:14px;color:rgba(244,237,222,.45)}
    .foot-col h4{color:var(--bone);font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.1em;margin-bottom:14px;font-family:'Outfit',sans-serif}
    .foot-col ul{list-style:none;display:flex;flex-direction:column;gap:9px}
    .foot-col ul li a{font-size:.82rem;color:rgba(244,237,222,.4);transition:color .2s}
    .foot-col ul li a:hover{color:var(--bone)}
    .foot-bottom{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px}
    .foot-bottom p{font-size:.77rem}
    .foot-links{display:flex;gap:18px}
    .foot-links a{font-size:.77rem;color:rgba(244,237,222,.3);transition:color .2s}
    .foot-links a:hover{color:var(--bone)}
    .roofline{display:flex;align-items:center;margin:20px 0}
    .roofline .rl-line{height:1.5px;background:var(--cedar);flex:1}
    .roofline .rl-peak{width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-bottom:8px solid var(--cedar)}
    #save-toast{position:fixed;bottom:90px;left:50%;transform:translateX(-50%);background:var(--ink);color:var(--bone);padding:9px 22px;border-radius:100px;font-size:.8rem;font-weight:600;z-index:3000;opacity:0;transition:opacity .3s;pointer-events:none;font-family:'Outfit',sans-serif;white-space:nowrap;border:1px solid rgba(255,255,255,.1)}
    .fu{opacity:0;transform:translateY(28px);transition:opacity .6s ease,transform .6s ease}
    .fu.on{opacity:1;transform:translateY(0)}
    @media(max-width:920px){.fu{opacity:1 !important;transform:none !important;transition:none !important}}
    @media(max-width:1020px){.pay-steps{grid-template-columns:repeat(3,1fr)}}
    @media(max-width:920px){.hero-bg{background-size:100% auto;background-position:center top;background-repeat:no-repeat}#hero{min-height:70svh}.nav-links,.nav-actions{display:none}.burger{display:flex}section{padding:64px 0}section.tight{padding:48px 0}.cabin-grid,.about-grid,.fin-grid,.contact-grid{grid-template-columns:1fr;gap:36px}.ap-inner{grid-template-columns:1fr;gap:28px}.gal-dyn-grid{grid-template-columns:1fr 1fr}.gal-dyn-item.wide,.gal-dyn-item.full-w{grid-column:span 2}.foot-top{grid-template-columns:1fr 1fr}.amen-grid{grid-template-columns:repeat(2,1fr)}.cabin-drag-grid{grid-template-columns:repeat(3,1fr)}.about-cta-inner{flex-direction:column;text-align:center}.hstat{min-width:45%}.hero-upload-wrap{bottom:16px;right:16px}}
    @media(max-width:680px){.pay-steps{grid-template-columns:1fr 1fr}.hero-btns{flex-direction:column}.hero-btns .btn{width:100%;justify-content:center}}
    @media(max-width:580px){.gal-dyn-grid{grid-template-columns:1fr}.gal-dyn-item.wide,.gal-dyn-item.full-w{grid-column:span 1}.gal-di-img,.gal-dyn-item.wide .gal-di-img,.gal-dyn-item.full-w .gal-di-img{aspect-ratio:4/3}.specs,.cf-row,.creds{grid-template-columns:1fr}.hstat{min-width:50%;border-right:none !important}.amen-grid{grid-template-columns:1fr}.foot-top{grid-template-columns:1fr}.nl-form{flex-direction:column}.nl-form input{border-radius:var(--r)}.nl-form button{border-radius:var(--r)}#float-cta{bottom:14px;right:14px}#float-cta .btn{padding:13px 18px;font-size:.83rem}.trust-item{border-right:none;border-bottom:1px solid rgba(255,255,255,.05)}.cabin-drag-grid{grid-template-columns:repeat(2,1fr)}.team-cards{grid-template-columns:1fr}.tm-photo,.tm-empty{aspect-ratio:4/3}.pay-steps{grid-template-columns:1fr}}
  </style>
</head>
<body>
<input type="file" id="heroBgInput" accept="image/*" style="display:none" onchange="changeHeroBg(this)">
<input type="file" id="cabinMultiInput" accept="image/*" multiple style="display:none" onchange="addCabinPhotos(this)">
<input type="file" id="galMultiInput" accept="image/*" multiple style="display:none" onchange="addGalleryPhotos(this)">
<input type="file" id="aboutImgInput" accept="image/*" style="display:none" onchange="changeAboutImg(this)">
<input type="file" id="about2ImgInput" accept="image/*" style="display:none" onchange="changeAbout2Img(this)">
<div id="save-toast"></div>
<nav id="nav">
  <div class="nav-inner">
    <a href="#hero" class="logo-lockup">
      <svg class="logo-icon" width="46" height="41" viewBox="0 0 80 72" fill="none" aria-hidden="true"><g stroke="currentColor" stroke-width="3" stroke-linejoin="round"><path d="M24,52 L48,64 L48,44 L36,24 L24,32 Z"/><path d="M48,64 L48,44 L64,36 L64,56 Z"/><path d="M48,44 L36,24 L52,16 L64,36 Z"/></g><polygon points="30,55 40,60 40,46 30,41" fill="currentColor"/></svg>
      <span class="logo-text"><span class="logo-name">Fraternal</span><span class="logo-rule-el"></span><span class="logo-desc">cabins &middot; hawke's bay</span></span>
    </a>
    <ul class="nav-links"><li><a href="#cabins">Our Cabins</a></li><li><a href="#finance">Finance</a></li><li><a href="#about-problem">Our Purpose</a></li><li><a href="#faq">FAQs</a></li><li><a href="#contact">Contact</a></li></ul>
    <div class="nav-actions"><a href="#contact" class="btn btn-white-outline" style="padding:10px 18px;font-size:.82rem;">Enquire</a><a href="https://apply.mtf.co.nz/?originatorid=2173" target="_blank" class="btn btn-cedar" style="padding:10px 18px;font-size:.82rem;">Get Finance</a></div>
    <div class="burger" onclick="toggleDrawer()"><span></span><span></span><span></span></div>
  </div>
</nav>
<div id="drawer">
  <a href="#cabins" onclick="toggleDrawer()">Our Cabins</a><a href="#finance" onclick="toggleDrawer()">Finance</a><a href="#about-problem" onclick="toggleDrawer()">Our Purpose</a><a href="#faq" onclick="toggleDrawer()">FAQs</a><a href="#contact" onclick="toggleDrawer()">Contact</a>
  <a href="https://apply.mtf.co.nz/?originatorid=2173" target="_blank" class="btn btn-cedar" style="margin-top:6px;">Get Finance &rarr;</a>
</div>
<div id="float-cta"><a href="https://apply.mtf.co.nz/?originatorid=2173" target="_blank" class="btn btn-cedar">Get Finance &rarr;</a></div>
<section id="hero">
  <div class="hero-bg" id="heroBgDiv"></div><div class="hero-grad"></div>
  <div class="wrap"><div class="hero-content">
    <div class="hero-pill"><span class="hero-pill-dot"></span>3 Cabins Available Now &mdash; Hawke's Bay</div>
    <h1>Own your cabin in four years, for the price of renting it.</h1>
    <div class="hero-own">From ~$130 a week &mdash; no $20k up front. Yours at the end.</div>
    <div class="hero-btns"><a href="#cabins" class="btn btn-cedar">See the Cabin</a><a href="#finance" class="btn btn-hero-sec">See Weekly Payments</a></div>
    <div class="hero-stats">
      <div class="hstat"><div class="hstat-num">~$130</div><div class="hstat-lbl">Per week</div></div>
      <div class="hstat"><div class="hstat-num">4 yrs</div><div class="hstat-lbl">Own it outright</div></div>
      <div class="hstat"><div class="hstat-num">1 day</div><div class="hstat-lbl">Delivery &amp; placement</div></div>
      <div class="hstat"><div class="hstat-num">0</div><div class="hstat-lbl">Council consents needed</div></div>
    </div>
  </div></div>
  <div class="hero-upload-wrap"><button class="upload-btn" onclick="document.getElementById('heroBgInput').click()"><svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M17 8l-5-5-5 5M12 3v12"/></svg>Change Background Photo</button></div>
</section>
<div id="trust"><div class="wrap" style="padding:0 24px;"><div class="trust-row">
  <div class="trust-item"><div class="t-icon"><svg width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg></div>EWOF Certified Per Cabin</div>
  <div class="trust-item"><div class="t-icon"><svg width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h6M9 12h6M9 15h4"/></svg></div>Schedule 1 Consent-Exempt</div>
  <div class="trust-item"><div class="t-icon"><svg width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>12-Month Structural Warranty</div>
</div></div></div>
<section id="cabins"><div class="wrap">
  <div class="cabin-section-hd fu"><div class="cabin-section-title">Our Cabins</div><p class="cabin-section-sub">3 available &mdash; ready to deliver within Hawke's Bay</p></div>
  <div class="cabin-grid">
    <div class="fu">
      <div class="img-main" id="cabinMainSlot" onclick="openLightbox(cabinPhotos,0)"><img id="cabinMainImg" src="https://images.unsplash.com/photo-1609766418204-94aae0ecf4e5?w=900&q=80&auto=format&fit=crop" alt="Cabin exterior"></div>
      <div class="cabin-empty-state" id="cabinEmptyState"><svg width="40" height="40" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" style="color:var(--mist)"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="m3 9 4-4 4 4 4-4 4 4"/><circle cx="8.5" cy="13.5" r="1.5"/></svg><p style="font-size:.85rem;margin-top:4px">Upload photos to display your cabin</p></div>
      <div class="cabin-drag-grid" id="cabinDragGrid"></div>
      <p class="drag-hint-text" id="cabinDragHint">Drag to reorder &middot; &#8592; &#8594; to move &middot; &times; to delete</p>
      <div class="cabin-upload-row" style="margin-top:12px"><button class="upload-btn" onclick="document.getElementById('cabinMultiInput').click()"><svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M17 8l-5-5-5 5M12 3v12"/></svg>Upload Cabin Photos</button><span class="cabin-upload-hint">First photo becomes the main image</span></div>
    </div>
    <div class="fu">
      <div class="stock-pill">3 Available &mdash; Ready to Deliver</div>
      <h2>The Standard</h2>
      <div class="price-row"><span class="price-main">~$130<small style="font-size:1.15rem;font-weight:700">/wk</small></span><span class="price-alt">or $20,000 outright</span></div>
      <div class="specs"><div class="spec"><span class="spec-l">Floor Area</span><span class="spec-v">8.64 m&sup2; (3.6 &times; 2.4m)</span></div><div class="spec"><span class="spec-l">Delivery</span><span class="spec-v">One Day</span></div><div class="spec"><span class="spec-l">Cladding</span><span class="spec-v">Cedar + Colorsteel</span></div><div class="spec"><span class="spec-l">Council Consent</span><span class="spec-v">Not Required</span></div></div>
      <ul class="feat-list"><li>Hand-built cedar weatherboard with Colorsteel cladding &amp; mono-pitch roof</li><li>Full insulation &mdash; R1.8 walls, R2.6 ceiling (Healthy Homes compliant)</li><li>Double-glazed aluminium joinery &mdash; window + sliding door</li><li>Warm stained ply interior with laminate flooring</li><li>LED lighting, switchboard &amp; plug-in main power lead</li><li>EWOF certified before delivery &middot; 12-month structural warranty</li></ul>
      <div class="cabin-ctas"><a href="#contact" class="btn btn-black">Book a Viewing</a><a href="https://apply.mtf.co.nz/?originatorid=2173" target="_blank" class="btn btn-cedar">Get Finance</a></div>
    </div>
  </div>
</div></section>
<section id="amenities" class="tight"><div class="wrap">
  <span class="label">What's Included</span><h2 style="color:#fff;margin-bottom:10px">What's in every cabin</h2><p class="amen-intro">Every cabin ships complete. No extras. No add-ons.</p>
  <div class="amen-grid fu">
    <div class="amen-cell"><div class="amen-ico">&#127968;</div><div><span class="amen-title">Cedar Weatherboard</span><span class="amen-sub">Exterior + Colorsteel cladding</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#127777;&#65039;</div><div><span class="amen-title">Full Insulation</span><span class="amen-sub">R1.8 walls / R2.6 ceiling</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#129695;</div><div><span class="amen-title">Double-Glazed Joinery</span><span class="amen-sub">Aluminium window + sliding door</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#9968;&#65039;</div><div><span class="amen-title">Colorsteel Roof</span><span class="amen-sub">Mono-pitch design</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#129683;</div><div><span class="amen-title">Stained Ply Interior</span><span class="amen-sub">Warm timber lining</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#9889;</div><div><span class="amen-title">Power Ready</span><span class="amen-sub">Switchboard + 2 double points</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#128161;</div><div><span class="amen-title">LED Lighting</span><span class="amen-sub">Interior + exterior</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#9989;</div><div><span class="amen-title">EWOF Certified</span><span class="amen-sub">Issued before delivery</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#128737;&#65039;</div><div><span class="amen-title">12-Month Warranty</span><span class="amen-sub">Structural defects covered</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#128667;</div><div><span class="amen-title">One-Day Delivery</span><span class="amen-sub">Within Hawke's Bay</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#128203;</div><div><span class="amen-title">Consent-Exempt</span><span class="amen-sub">Schedule 1, Building Act 2004</span></div></div>
    <div class="amen-cell"><div class="amen-ico">&#127968;</div><div><span class="amen-title">Laminate Flooring</span><span class="amen-sub">Durable, easy to clean</span></div></div>
  </div>
</div></section>
<section id="how"><div class="wrap">
  <div class="process-hd fu"><div class="process-title">The Process</div><p class="process-sub">From first enquiry to front door in days</p></div>
  <div class="pay-steps fu">
    <div class="pay-step"><div class="pay-step-n">01</div><div class="pay-step-t">Select Your Cabin</div><div class="pay-step-d">Visit our yard in Hastings or enquire online &mdash; see it, walk through it, ask anything.</div></div>
    <div class="pay-step"><div class="pay-step-n">02</div><div class="pay-step-t">Apply for Rent to Own</div><div class="pay-step-d">Apply through MTF Napier online in minutes. We walk you through it.</div></div>
    <div class="pay-step"><div class="pay-step-n">03</div><div class="pay-step-t">Finance Assessment</div><div class="pay-step-d">MTF reviews your application and confirms your exact weekly amount &mdash; no surprises.</div></div>
    <div class="pay-step"><div class="pay-step-n">04</div><div class="pay-step-t">Delivery &amp; Installation</div><div class="pay-step-d">We deliver and place your cabin in one day. EWOF certified, ready to plug in.</div></div>
    <div class="pay-step"><div class="pay-step-n">05</div><div class="pay-step-t">Pay Weekly. Own Outright.</div><div class="pay-step-d">~$130/wk over 4 years &mdash; then the payments stop and the cabin is entirely yours.</div></div>
  </div>
</div></section>
<section id="finance"><div class="wrap"><div class="fin-grid">
  <div class="fin-info fu">
    <h2 class="fin-display">Finance</h2>
    <p class="fin-subtitle">Fast approvals. Weekly payments. Backed by MTF Napier.</p>
    <div class="own-callout">You own it at the end.<span>Every weekly payment builds toward something that's yours &mdash; no landlord, no lease, no rent review. <em>Own it in four years.</em></span></div>
    <p>We've teamed up with MTF Napier to make it straightforward. Apply online in minutes and get your exact weekly amount confirmed.</p>
    <div class="mtf-badge"><div class="mtf-ico">MTF</div><span>Weekly payments arranged through <strong>MTF Napier</strong> &mdash; your exact amount confirmed once you apply</span></div>
  </div>
  <div class="fu"><div class="calc-card">
    <h3>Payment Estimator</h3>
    <div class="fg"><label>Cabin Price ($)</label><input type="number" id="cPrice" value="20000" min="1000" step="500" oninput="calcPay()"></div>
    <div class="fg"><label>Deposit (%)</label><input type="number" id="cDep" value="5" min="0" max="100" oninput="calcPay()"></div>
    <div class="fg"><label>Loan Term</label><select id="cTerm" onchange="calcPay()"><option value="2">2 years</option><option value="3">3 years</option><option value="4" selected>4 years</option><option value="5">5 years</option></select></div>
    <div class="calc-result"><div class="cr-label">Estimated weekly payment</div><div class="cr-amount" id="cOut">$118</div><div class="cr-sub">Estimate only &mdash; MTF Napier will confirm your exact weekly amount</div></div>
    <a href="https://apply.mtf.co.nz/?originatorid=2173" target="_blank" class="btn btn-cedar" style="width:100%;justify-content:center;">Get Finance with MTF Napier &rarr;</a>
  </div></div>
</div></div></section>
<section id="gallery" class="tight"><div class="wrap">
  <div class="gallery-hd fu"><div class="gallery-title">Gallery</div><p class="gallery-sub">Click to enlarge &middot; Drag or use arrows to reorder &middot; &times; to delete</p></div>
  <div class="gal-dyn-grid fu" id="galDynGrid"></div>
  <div class="gallery-upload-row fu"><button class="upload-btn" onclick="document.getElementById('galMultiInput').click()"><svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M17 8l-5-5-5 5M12 3v12"/></svg>Add Gallery Photos</button><span style="font-size:.72rem;color:var(--slate)">Photos save to your browser automatically</span></div>
</div></section>
<div id="lbx" onclick="lbxBgClose(event)"><button class="lbx-close" onclick="closeLbx()">&times;</button><button class="lbx-arrow" id="lbx-prev" onclick="lbxStep(-1)">&#8592;</button><img id="lbx-img" src="" alt=""><button class="lbx-arrow" id="lbx-next" onclick="lbxStep(1)">&#8594;</button></div>
<section id="about-problem"><div class="wrap"><div class="ap-inner">
  <div class="fu"><span class="label" style="color:rgba(181,98,59,.8)">Why We Exist</span><p class="ap-quote">You've done the maths in your head <em>a hundred times.</em></p></div>
  <div class="ap-body fu"><p>The extra room would change everything &mdash; space for a growing family, a teenager who needs their own four walls, a home office that isn't the kitchen table. But buying a cabin outright means finding $20,000 you don't have sitting in the bank, and renting one means paying $130 a week, forever, for something that stays someone else's. So you wait. And every week, that rent money goes out the door with nothing to show for it.</p></div>
</div></div></section>
<section id="about"><div class="wrap"><div class="about-grid">
  <div class="team-cards fu">
    <div class="team-member">
      <div class="tm-photo" id="aboutImgSlot" style="display:none"><img id="aboutImgEl" src="" alt="Tipene Douglas"></div>
      <div class="tm-empty" id="aboutImgEmpty"><svg width="36" height="36" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" style="color:var(--mist)"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="m3 9 4-4 4 4 4-4 4 4"/><circle cx="8.5" cy="13.5" r="1.5"/></svg><p>Upload photo</p></div>
      <div class="tm-upload-row"><button class="upload-btn" onclick="document.getElementById('aboutImgInput').click()"><svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M17 8l-5-5-5 5M12 3v12"/></svg>Upload</button><button id="aboutImgRemoveBtn" onclick="removeAboutImg()" class="upload-btn" style="display:none;color:#dc2626;border-color:#fca5a5">Remove</button></div>
      <div class="tm-info"><strong>Tipene Douglas</strong><span class="tm-role">Builder &amp; Co-Founder</span><span class="tm-sub">8 years&rsquo; carpentry experience</span></div>
    </div>
    <div class="team-member">
      <div class="tm-photo" id="about2ImgSlot" style="display:none"><img id="about2ImgEl" src="" alt="Tihema Douglas"></div>
      <div class="tm-empty" id="about2ImgEmpty"><svg width="36" height="36" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" style="color:var(--mist)"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="m3 9 4-4 4 4 4-4 4 4"/><circle cx="8.5" cy="13.5" r="1.5"/></svg><p>Upload photo</p></div>
      <div class="tm-upload-row"><button class="upload-btn" onclick="document.getElementById('about2ImgInput').click()"><svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M17 8l-5-5-5 5M12 3v12"/></svg>Upload</button><button id="about2ImgRemoveBtn" onclick="removeAbout2Img()" class="upload-btn" style="display:none;color:#dc2626;border-color:#fca5a5">Remove</button></div>
      <div class="tm-info"><strong>Tihema Douglas</strong><span class="tm-role">Co-Founder</span></div>
    </div>
  </div>
  <div class="about-text fu">
    <span class="label" style="font-size:.9rem;letter-spacing:.15em">Our Purpose</span>
    <h2>The only local, family-built, rent-to-own cabin in Hawke's Bay.</h2>
    <p>Fraternal started with a simple frustration: watching good local families pay enough each week to own something, yet never getting to own anything. The rent-to-own cabins that could fix that were all run from Auckland or Wellington &mdash; brands you deal with at arm's length, by people you'll never meet.</p>
    <p>So we built the thing that was missing right here. Every Fraternal cabin is made by hand in Hawke's Bay by a qualified local carpenter, inspected before it leaves the yard, and delivered to your site in a day &mdash; no council consent, no fuss. For roughly the same weekly payment as renting, the cabin becomes yours outright. Then the payments stop, and you're left holding something real.</p>
    <div class="creds"><div class="cred"><div class="cred-dot"></div>EWOF Certified</div><div class="cred"><div class="cred-dot"></div>MTF Finance Partner</div><div class="cred"><div class="cred-dot"></div>12-Month Warranty</div><div class="cred"><div class="cred-dot"></div>Schedule 1 Exempt</div><div class="cred"><div class="cred-dot"></div>Stock Insured</div><div class="cred"><div class="cred-dot"></div>Hawke's Bay Built</div></div>
  </div>
</div></div></section>
<section id="about-cta"><div class="wrap"><div class="about-cta-inner fu">
  <div class="about-cta-text"><h2>Come and meet the builder.</h2><p>Walk through a cabin, see the rent-vs-own numbers for yourself &mdash; book a chat and let's find the finish line together.</p></div>
  <div style="display:flex;gap:12px;flex-shrink:0;flex-wrap:wrap"><a href="#contact" class="btn btn-bone-outline">Book a Viewing</a><a href="https://apply.mtf.co.nz/?originatorid=2173" target="_blank" class="btn btn-black">Get Finance &rarr;</a></div>
</div></div></section>
<section id="faq"><div class="wrap">
  <div class="faq-hd fu"><div class="faq-display">Questions</div><p class="faq-subtitle">Frequently Asked Questions</p></div>
  <div class="faq-list fu">
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">Do I need council consent?<svg class="faq-chev" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg></button><div class="faq-a"><p>No. Our cabins are consent-exempt sleepouts under Schedule 1 of the Building Act 2004. No council paperwork required.</p></div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">How do the weekly payments work?<svg class="faq-chev" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg></button><div class="faq-a"><p>You pay weekly through MTF Napier &mdash; around $130 a week over 4 years. At the end of the term, the cabin is fully yours.</p></div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">How much is the deposit?<svg class="faq-chev" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg></button><div class="faq-a"><p>5% at contract signing &mdash; about $1,000 on a $20,000 cabin. MTF Napier funds the rest once your application is approved.</p></div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">How long does delivery take?<svg class="faq-chev" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg></button><div class="faq-a"><p>One day. The HIAB truck arrives, places the cabin, we do a full walk-through, and you're done before sunset.</p></div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">What site prep do I need?<svg class="faq-chev" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg></button><div class="faq-a"><p>A clear, level area and access wide enough for a HIAB crane truck. We'll walk you through specifics at viewing.</p></div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">What if I rent my property?<svg class="faq-chev" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg></button><div class="faq-a"><p>You'll need written consent from your landlord before delivery. We can provide a template letter to help with that conversation.</p></div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">Do the cabins come with power?<svg class="faq-chev" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg></button><div class="faq-a"><p>Cabins arrive EWOF certified and ready to plug in via extension lead. Permanent connection requires a licensed electrician.</p></div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">What's the warranty?<svg class="faq-chev" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg></button><div class="faq-a"><p>12 months on structural defects &mdash; materials and workmanship.</p></div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">Can I customise a cabin?<svg class="faq-chev" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg></button><div class="faq-a"><p>Yes. Custom builds available on a 3&ndash;5 week lead time. Get in touch for a quote.</p></div></div>
    <div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)">Where do you deliver?<svg class="faq-chev" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"/></svg></button><div class="faq-a"><p>Napier, Hastings, Central Hawke's Bay, and Wairoa as standard. Other locations by quote.</p></div></div>
  </div>
</div></section>
<section id="newsletter"><div class="wrap"><div class="nl-inner fu">
  <span class="label">Stay Updated</span><h2>Get notified when new cabins are ready</h2><p>We build in small batches. Be first in line for the next ones.</p>
  <div class="nl-form"><input type="email" id="nlEmail" placeholder="your@email.com"><button onclick="nlSubmit()">Notify Me</button></div>
  <p class="nl-sub">No spam. Unsubscribe any time.</p>
</div></div></section>
<section id="contact"><div class="wrap"><div class="contact-grid">
  <div class="fu">
    <span class="label">Get in Touch</span><h2>Get in Touch</h2>
    <p>Viewings by appointment at our Hastings yard. Fill in the form and we'll get back to you within 24 hours.</p>
    <div class="cm-list">
      <div class="cm"><div class="cm-ico"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg></div><div><strong>Phone</strong><a href="tel:0273580914">027 358 0914</a></div></div>
      <div class="cm"><div class="cm-ico"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg></div><div><strong>Email</strong><a href="mailto:fraternalltd@gmail.com">fraternalltd@gmail.com</a></div></div>
      <div class="cm"><div class="cm-ico"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg></div><div><strong>Location</strong><span>Hastings, New Zealand</span></div></div>
    </div>
    <div class="socials"><a href="#" class="soc-link"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a><a href="#" class="soc-link"><svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a></div>
    <p class="soc-note">@fraternalcabins &mdash; pages launching soon</p>
  </div>
  <div class="fu"><form class="cf" onsubmit="cfSubmit(event)">
    <div class="cf-row"><div class="fg"><label>Name *</label><input type="text" placeholder="Your name" required></div><div class="fg"><label>Phone *</label><input type="tel" placeholder="Phone number" required></div></div>
    <div class="fg"><label>Email *</label><input type="email" placeholder="you@email.com" required></div>
    <div class="fg"><label>What are you looking for?</label><select><option value="">Select an option...</option><option>Cabin for myself</option><option>Cabin for a family member</option><option>Rental income property</option><option>Just having a look</option><option>Other</option></select></div>
    <div class="fg"><label>Message</label><textarea placeholder="Tell us about your situation &mdash; location, timeline, any questions..."></textarea></div>
    <div class="fg"><label>How did you hear about us?</label><select><option value="">Select...</option><option>Facebook / Instagram</option><option>Word of mouth</option><option>Google search</option><option>MTF Napier</option><option>Other</option></select></div>
    <div class="cf-submit"><button type="submit" class="btn btn-cedar">Send Enquiry &rarr;</button></div>
    <p class="cf-note">We reply within 24 hours (Mon&ndash;Fri)</p>
  </form></div>
</div></div></section>
<footer><div class="wrap">
  <div class="foot-top">
    <div class="foot-brand">
      <a href="#hero" class="logo-lockup"><svg class="logo-icon" width="40" height="36" viewBox="0 0 80 72" fill="none"><g stroke="currentColor" stroke-width="3" stroke-linejoin="round"><path d="M24,52 L48,64 L48,44 L36,24 L24,32 Z"/><path d="M48,64 L48,44 L64,36 L64,56 Z"/><path d="M48,44 L36,24 L52,16 L64,36 Z"/></g><polygon points="30,55 40,60 40,46 30,41" fill="currentColor"/></svg><span class="logo-text"><span class="logo-name">Fraternal</span><span class="logo-rule-el"></span><span class="logo-desc">cabins &middot; hawke's bay</span></span></a>
      <p>Fraternal builds warm, rent-to-own cabins by hand in Hawke's Bay. Delivered in a day, no council consent.</p>
      <div class="socials" style="margin-top:16px;"><a href="#" class="soc-link"><svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a><a href="#" class="soc-link"><svg width="15" height="15" fill="currentColor" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a></div>
    </div>
    <div class="foot-col"><h4>Navigate</h4><ul><li><a href="#hero">Home</a></li><li><a href="#cabins">Our Cabins</a></li><li><a href="#finance">Finance</a></li><li><a href="#about-problem">Our Purpose</a></li><li><a href="#faq">FAQs</a></li><li><a href="#contact">Contact</a></li></ul></div>
    <div class="foot-col"><h4>Contact</h4><ul><li><a href="tel:0273580914">027 358 0914</a></li><li><a href="mailto:fraternalltd@gmail.com">fraternalltd@gmail.com</a></li><li><a href="#contact">Hastings, New Zealand</a></li></ul><div class="mtf-badge" style="margin-top:18px;padding:10px 12px;background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.08)"><div class="mtf-ico" style="width:28px;height:28px;font-size:.7rem;">MTF</div><span style="font-size:.75rem;color:rgba(244,237,222,.45)">Weekly payments via MTF Napier</span></div></div>
  </div>
  <div class="roofline" style="margin:0 0 22px;"><span class="rl-line"></span><span class="rl-peak"></span></div>
  <div class="foot-bottom"><p>&copy; 2026 Fraternal Ltd &middot; Hawke's Bay, New Zealand &middot; All cabins EWOF certified</p><div class="foot-links"><a href="#">Privacy Policy</a><a href="#">Terms &amp; Conditions</a></div></div>
</div></footer>
<script>
function toggleDrawer(){document.getElementById('drawer').classList.toggle('open')}
window.addEventListener('scroll',function(){document.getElementById('float-cta').classList.toggle('show',window.scrollY>450);},{passive:true});
function toggleFaq(btn){var item=btn.parentElement;var open=item.classList.contains('open');document.querySelectorAll('.faq-item.open').forEach(function(el){el.classList.remove('open');});if(!open)item.classList.add('open');}
function calcPay(){var price=parseFloat(document.getElementById('cPrice').value)||20000;var depStr=document.getElementById('cDep').value;var dep=(depStr==='')?5:parseFloat(depStr);if(isNaN(dep))dep=5;dep=Math.min(Math.max(dep,0),100);var yrs=parseFloat(document.getElementById('cTerm').value)||4;var loan=price*(1-dep/100);if(loan<=0){document.getElementById('cOut').textContent='$0';return;}var wr=0.129/52;var n=yrs*52;var pmt=loan*(wr*Math.pow(1+wr,n))/(Math.pow(1+wr,n)-1);document.getElementById('cOut').textContent='$'+Math.ceil(pmt);}
function compressImg(src,maxW,q){maxW=maxW||1200;q=q||0.82;return new Promise(function(resolve){var img=new Image();img.onload=function(){var scale=Math.min(1,maxW/img.width);var c=document.createElement('canvas');c.width=Math.round(img.width*scale);c.height=Math.round(img.height*scale);c.getContext('2d').drawImage(img,0,0,c.width,c.height);resolve(c.toDataURL('image/jpeg',q));};img.src=src;});}
function readFileCompressed(file){return new Promise(function(resolve){var r=new FileReader();r.onload=function(e){compressImg(e.target.result).then(resolve);};r.readAsDataURL(file);});}
function showToast(msg){var t=document.getElementById('save-toast');t.textContent=msg;t.style.opacity='1';clearTimeout(window._tt);window._tt=setTimeout(function(){t.style.opacity='0';},2500);}
function trySave(key,data){try{localStorage.setItem(key,JSON.stringify(data));return true;}catch(e){return false;}}
function applyHeroBg(src){var bg=document.getElementById('heroBgDiv');bg.style.backgroundImage='url('+src+')';bg.style.backgroundSize='cover';bg.style.backgroundPosition='center';bg.style.opacity='.48';}
function changeHeroBg(input){if(!input.files[0])return;var r=new FileReader();r.onload=function(e){compressImg(e.target.result,1600,0.85).then(function(src){applyHeroBg(src);try{localStorage.setItem('frat_hero',src);}catch(e){}showToast('Banner photo updated');});};r.readAsDataURL(input.files[0]);}
function applyAboutImg(src){document.getElementById('aboutImgEl').src=src;document.getElementById('aboutImgSlot').style.display='';document.getElementById('aboutImgEmpty').style.display='none';document.getElementById('aboutImgRemoveBtn').style.display='';}
function changeAboutImg(input){if(!input.files[0])return;readFileCompressed(input.files[0]).then(function(src){applyAboutImg(src);try{localStorage.setItem('frat_about',src);}catch(e){}showToast('Photo saved');});input.value='';}
function removeAboutImg(){document.getElementById('aboutImgEl').src='';document.getElementById('aboutImgSlot').style.display='none';document.getElementById('aboutImgEmpty').style.display='';document.getElementById('aboutImgRemoveBtn').style.display='none';try{localStorage.removeItem('frat_about');}catch(e){}showToast('Photo removed');}
function applyAbout2Img(src){document.getElementById('about2ImgEl').src=src;document.getElementById('about2ImgSlot').style.display='';document.getElementById('about2ImgEmpty').style.display='none';document.getElementById('about2ImgRemoveBtn').style.display='';}
function changeAbout2Img(input){if(!input.files[0])return;readFileCompressed(input.files[0]).then(function(src){applyAbout2Img(src);try{localStorage.setItem('frat_about2',src);}catch(e){}showToast('Photo saved');});input.value='';}
function removeAbout2Img(){document.getElementById('about2ImgEl').src='';document.getElementById('about2ImgSlot').style.display='none';document.getElementById('about2ImgEmpty').style.display='';document.getElementById('about2ImgRemoveBtn').style.display='none';try{localStorage.removeItem('frat_about2');}catch(e){}showToast('Photo removed');}
function loadSaved(){try{var cab=localStorage.getItem('frat_cabin');if(cab){var arr=JSON.parse(cab);if(arr&&arr.length){cabinPhotos=arr;cabinDefaultsActive=false;}}var gal=localStorage.getItem('frat_gal');if(gal){var garr=JSON.parse(gal);if(garr&&garr.length){galPhotos=garr;}}var a1=localStorage.getItem('frat_about');if(a1){applyAboutImg(a1);}var a2=localStorage.getItem('frat_about2');if(a2){applyAbout2Img(a2);}}catch(e){}}
var CABIN_DEFAULTS=['https://images.unsplash.com/photo-1609766418204-94aae0ecf4e5?w=900&q=80&auto=format&fit=crop','https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=500&q=80&auto=format&fit=crop','https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=500&q=80&auto=format&fit=crop'];
var cabinPhotos=CABIN_DEFAULTS.slice(),cabinDefaultsActive=true,cabinDragSrc=null;
async function addCabinPhotos(input){if(!input.files.length)return;var isFirst=cabinDefaultsActive;if(isFirst){cabinPhotos=[];cabinDefaultsActive=false;}showToast('Processing...');var files=Array.from(input.files);for(var i=0;i<files.length;i++){cabinPhotos.push(await readFileCompressed(files[i]));}input.value='';renderCabinGrid();if(!trySave('frat_cabin',cabinPhotos)){showToast('Could not save — photos too large');return;}showToast('Saved');}
function renderCabinGrid(){var ms=document.getElementById('cabinMainSlot'),es=document.getElementById('cabinEmptyState'),dg=document.getElementById('cabinDragGrid'),hint=document.getElementById('cabinDragHint');if(!cabinPhotos.length){ms.style.display='none';es.style.display='flex';dg.innerHTML='';hint.style.display='none';return;}ms.style.display='';es.style.display='none';document.getElementById('cabinMainImg').src=cabinPhotos[0];dg.innerHTML='';cabinPhotos.forEach(function(src,i){var item=document.createElement('div');item.className='cabin-drag-item';item.draggable=true;var la=i>0?'<button class="drag-arrow-btn" onclick="event.stopPropagation();moveCabin('+i+',-1)">&#8592;</button>':'<span style="width:26px;display:inline-block"></span>';var ra=i<cabinPhotos.length-1?'<button class="drag-arrow-btn" onclick="event.stopPropagation();moveCabin('+i+',1)">&#8594;</button>':'<span style="width:26px;display:inline-block"></span>';item.innerHTML='<div class="cabin-di-img" onclick="event.stopPropagation();openLightbox(cabinPhotos,'+i+')"><img src="'+src+'" alt="Cabin" loading="lazy"></div>'+(i===0?'<div class="photo-main-badge">MAIN</div>':'')+'<button class="drag-del-btn" onclick="event.stopPropagation();deleteCabin('+i+')" title="Remove">&times;</button>'+(cabinPhotos.length>1?'<div class="di-controls">'+la+ra+'</div>':'');item.addEventListener('dragstart',function(e){cabinDragSrc=i;e.dataTransfer.effectAllowed='move';setTimeout(function(){item.classList.add('is-dragging');},0);});item.addEventListener('dragover',function(e){e.preventDefault();item.classList.add('drag-over');});item.addEventListener('dragleave',function(){item.classList.remove('drag-over');});item.addEventListener('drop',function(e){e.preventDefault();item.classList.remove('drag-over');if(cabinDragSrc===null||cabinDragSrc===i)return;var tmp=cabinPhotos[cabinDragSrc];cabinPhotos[cabinDragSrc]=cabinPhotos[i];cabinPhotos[i]=tmp;cabinDragSrc=null;renderCabinGrid();trySave('frat_cabin',cabinPhotos);});item.addEventListener('dragend',function(){item.classList.remove('is-dragging','drag-over');cabinDragSrc=null;});dg.appendChild(item);});hint.style.display=cabinPhotos.length>1?'block':'none';}
function moveCabin(idx,dir){var ni=idx+dir;if(ni<0||ni>=cabinPhotos.length)return;var tmp=cabinPhotos[idx];cabinPhotos[idx]=cabinPhotos[ni];cabinPhotos[ni]=tmp;renderCabinGrid();trySave('frat_cabin',cabinPhotos);}
function deleteCabin(idx){cabinPhotos.splice(idx,1);renderCabinGrid();trySave('frat_cabin',cabinPhotos);}
var galPhotos=[],galDragSrc=null;
async function addGalleryPhotos(input){if(!input.files.length)return;showToast('Processing...');var files=Array.from(input.files);for(var i=0;i<files.length;i++){galPhotos.push(await readFileCompressed(files[i]));}input.value='';renderGalGrid();if(!trySave('frat_gal',galPhotos)){showToast('Could not save');return;}showToast('Saved');}
function renderGalGrid(){var grid=document.getElementById('galDynGrid');grid.innerHTML='';if(!galPhotos.length){var empty=document.createElement('div');empty.className='gal-empty-state';empty.innerHTML='<svg width="40" height="40" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" style="color:var(--mist);margin:0 auto 12px"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="m3 9 4-4 4 4 4-4 4 4"/><circle cx="8.5" cy="13.5" r="1.5"/></svg><p>Upload photos to fill your gallery</p>';grid.appendChild(empty);return;}galPhotos.forEach(function(src,i){var isWide=i===0&&galPhotos.length>=2,isFull=i===0&&galPhotos.length===1;var item=document.createElement('div');item.className='gal-dyn-item'+(isWide?' wide':'')+(isFull?' full-w':'');item.draggable=true;var la=i>0?'<button class="drag-arrow-btn" onclick="event.stopPropagation();moveGal('+i+',-1)">&#8592;</button>':'<span style="width:26px;display:inline-block"></span>';var ra=i<galPhotos.length-1?'<button class="drag-arrow-btn" onclick="event.stopPropagation();moveGal('+i+',1)">&#8594;</button>':'<span style="width:26px;display:inline-block"></span>';item.innerHTML='<div class="gal-di-img"><img src="'+src+'" alt="Gallery" loading="lazy"></div><button class="drag-del-btn" onclick="event.stopPropagation();deleteGal('+i+')" title="Remove">&times;</button>'+(galPhotos.length>1?'<div class="di-controls" style="margin-top:4px">'+la+ra+'</div>':'');item.querySelector('img').addEventListener('click',function(e){e.stopPropagation();openLightbox(galPhotos,i);});item.addEventListener('dragstart',function(e){galDragSrc=i;e.dataTransfer.effectAllowed='move';setTimeout(function(){item.classList.add('is-dragging');},0);});item.addEventListener('dragover',function(e){e.preventDefault();item.classList.add('drag-over');});item.addEventListener('dragleave',function(){item.classList.remove('drag-over');});item.addEventListener('drop',function(e){e.preventDefault();item.classList.remove('drag-over');if(galDragSrc===null||galDragSrc===i)return;var tmp=galPhotos[galDragSrc];galPhotos[galDragSrc]=galPhotos[i];galPhotos[i]=tmp;galDragSrc=null;renderGalGrid();trySave('frat_gal',galPhotos);});item.addEventListener('dragend',function(){item.classList.remove('is-dragging','drag-over');galDragSrc=null;});grid.appendChild(item);});}
function moveGal(idx,dir){var ni=idx+dir;if(ni<0||ni>=galPhotos.length)return;var tmp=galPhotos[idx];galPhotos[idx]=galPhotos[ni];galPhotos[ni]=tmp;renderGalGrid();trySave('frat_gal',galPhotos);}
function deleteGal(idx){galPhotos.splice(idx,1);renderGalGrid();trySave('frat_gal',galPhotos);}
var lbxSources=[],lbxIdx=0;
function openLightbox(sources,idx){lbxSources=(sources||[]).filter(function(s){return!!s;});if(!lbxSources.length)return;lbxIdx=Math.max(0,Math.min(idx,lbxSources.length-1));document.getElementById('lbx-img').src=lbxSources[lbxIdx];document.getElementById('lbx').classList.add('open');document.body.style.overflow='hidden';}
function closeLbx(){document.getElementById('lbx').classList.remove('open');document.body.style.overflow='';}
function lbxBgClose(e){if(e.target===document.getElementById('lbx'))closeLbx();}
function lbxStep(d){if(lbxSources.length<2)return;lbxIdx=(lbxIdx+d+lbxSources.length)%lbxSources.length;document.getElementById('lbx-img').src=lbxSources[lbxIdx];}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeLbx();if(e.key==='ArrowLeft')lbxStep(-1);if(e.key==='ArrowRight')lbxStep(1);});
function nlSubmit(){var el=document.getElementById('nlEmail');if(!el.value||!el.value.includes('@')){alert('Please enter a valid email.');return;}alert("You're on the list!");el.value='';}
function cfSubmit(e){e.preventDefault();alert("Thanks - we'll be in touch within 24 hours.");e.target.reset();}
(function(){
  var fus=document.querySelectorAll('.fu');
  if(window.innerWidth<=920||!('IntersectionObserver' in window)){fus.forEach(function(el){el.classList.add('on');});return;}
  var obs=new IntersectionObserver(function(entries){entries.forEach(function(en){if(en.isIntersecting){en.target.classList.add('on');obs.unobserve(en.target);}});},{threshold:0});
  fus.forEach(function(el){obs.observe(el);});
  setTimeout(function(){document.querySelectorAll('.fu:not(.on)').forEach(function(el){el.classList.add('on');});},800);
})();
calcPay();loadSaved();renderCabinGrid();renderGalGrid();
</script>
</body>
</html>"""

# Inject the hero image
html = html.replace("url('HERO_BG_PLACEHOLDER')", "url('" + HERO_BG + "')")

out = "/sessions/youthful-inspiring-ramanujan/mnt/fraternal.html/fraternal.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Done. {len(html)//1024}KB written to fraternal.html")
