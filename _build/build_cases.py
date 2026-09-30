"""Builds the case-study pages at work/<slug>/index.html.

Run from the repo root:  python3 _build/build_cases.py
Edit the PROJECTS data below, then re-run. (Jekyll ignores folders starting with "_",
so this script is not published by GitHub Pages.)
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTRA_URL = "https://contra.com/vipin_sao_z8eilxkm/work?r=vipin_sao_z8eilxkm"   # your Contra profile (also in index.html)
ORDER = ["driftlens", "leftova", "streak86", "stillwater"]

PROJECTS = {
# ---------------------------------------------------------------- Driftlens
"driftlens": dict(
  title="Driftlens Product Demo", name="Driftlens",
  kicker="SaaS product demo · Concept",
  tagline="Docs that <em>keep up</em> with your code.",
  summary="A 23-second product demo for a concept AI tool that keeps developer docs in sync with the code. One real change travels from a pull request to the docs, so the value is obvious without a voiceover.",
  concept="Self-initiated concept project. Fictional product, not a client.",
  facts=[("Type","Product demo"),("Format","16:9 · 1080p · 60 fps"),("Length","0:23"),("Year","2026"),("Role","Script, UI, motion, edit"),("Sound","Silent, captions on screen")],
  duration=23.2, vertical=False,
  chapters=[(0,"Hook"),(3,"Reveal"),(6,"PR changes the API"),(7.5,"Finds the broken docs"),(10.5,"Writes the fix"),(15,"One job"),(19,"End card")],
  problem="Stale documentation is an invisible problem. Nobody notices it until a developer copies an example that no longer works, which makes it hard to show in a short video.",
  idea="Make the invisible visible: follow one API change from the code to the exact sentence it breaks, then let the product fix it on screen. Three beats, no narration.",
  beats=[
    (0,"s1","The hook","“You shipped the code. Your docs didn’t get the memo.” Two lines that name a pain every developer knows, before the product is even named."),
    (6,"s3","A pull request changes the API","Login switches to passwordless. <code>auth.login(email, password)</code> becomes <code>auth.signIn({ email, otp })</code> and Driftlens starts scanning 24 pages of docs."),
    (7.5,"s4","It finds the docs it breaks","A line runs from the changed code to the exact sentence on the Authentication page. Doc health drops to 72% and one page is flagged out of date."),
    (10.5,"s6","AI writes the fix. You approve.","A suggested update appears beside the stale line. One click on Apply fix, health climbs to 100% and a docs pull request opens by itself."),
    (19,"s8","One clear ask","The end card lands the promise, “Ship code. Docs follow.”, with a single call to action: Connect your repo."),
  ],
  special="""
<section class="c-special"><div class="wrap">
  <span class="kicker rv">The product in one diff</span>
  <h2 class="rv" style="margin-top:14px">One job: keep your docs <em>true.</em></h2>
  <div class="dl-grid">
    <div class="diff rv" aria-label="Code change and the documentation it breaks">
      <div class="diff-head"><span>auth/session.ts</span><span class="pr">PR · Switch to passwordless login</span></div>
      <pre><span class="ln "><span class="n">23</span>export async function login(req) {</span><span class="ln "><span class="n">24</span>  const { email } = req.body</span><span class="ln del"><span class="n">25</span>- await auth.login(email, password)</span><span class="ln add"><span class="n">25</span>+ await auth.signIn({ email, otp })</span><span class="ln "><span class="n">26</span>  return session.create(email)</span><span class="ln "><span class="n">27</span>}</span></pre>
      <div class="diff-doc"><span class="flag">Out of date</span><div><b>docs / Authentication</b><code>await auth.login(email, password)</code></div></div>
      <div class="diff-fix"><span class="ok">Suggested update</span><code>await auth.signIn({ email, otp })</code><span class="apply">Apply fix</span></div>
    </div>
    <div class="feats">
      <div class="feat rv"><i>01</i><h3>Watches every PR</h3><p>Reads each diff across your repos the moment it merges.</p></div>
      <div class="feat rv"><i>02</i><h3>Flags stale docs</h3><p>Pinpoints the exact line that no longer matches the code.</p></div>
      <div class="feat rv"><i>03</i><h3>Writes the fix</h3><p>Drafts the update and opens a PR for your review.</p></div>
    </div>
  </div>
</div></section>""",
  fonts="family=Geist:wght@400;500;600;700;800&family=Geist+Mono:wght@400;500",
  style="""
:root{--bg:#0a0c09;--surface:#121510;--text:#eef2e6;--muted:#98a28c;--line:rgba(214,240,160,.09);--line-strong:rgba(214,240,160,.18);
--accent:#c6f135;--accent-2:#3ad6b6;--on-accent:#0d1206;--red:#ff6a57;
--display:"Geist",ui-sans-serif,system-ui,sans-serif;--body:"Geist",ui-sans-serif,system-ui,sans-serif;--mono:"Geist Mono",ui-monospace,Menlo,Consolas,monospace;
--display-weight:700;--display-tracking:-.045em;--em-style:normal;--radius:14px;color-scheme:dark}
body{background:radial-gradient(60% 50% at 10% 0%,rgba(198,241,53,.10),transparent 70%),radial-gradient(50% 40% at 100% 30%,rgba(58,214,182,.08),transparent 70%),var(--bg);background-attachment:fixed}
code{font-family:var(--mono);font-size:.88em;background:rgba(198,241,53,.08);color:var(--accent);padding:1px 6px;border-radius:5px}
.dl-grid{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:clamp(20px,3vw,40px);margin-top:40px;align-items:start}
.diff{border:1px solid var(--line-strong);border-radius:14px;background:#0d100b;overflow:hidden;font-size:13px}
.diff-head{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;padding:10px 14px;border-bottom:1px solid var(--line);font-family:var(--mono);font-size:11.5px;color:var(--muted)}
.diff-head .pr{color:var(--accent-2)}
.diff pre{margin:0;padding:14px 0;font-family:var(--mono);font-size:13px;line-height:1.8;overflow-x:auto}
.diff pre>span,.diff pre{white-space:pre}
.diff .n{display:inline-block;width:40px;text-align:right;padding-right:14px;color:#56604c}
.diff .ln{display:block}
.diff .del{background:rgba(255,106,87,.12);color:#ffb3a8}
.diff .add{display:block;background:rgba(198,241,53,.10);color:var(--accent)}
.diff-doc,.diff-fix{margin:0 14px 14px;padding:12px 14px;border-radius:10px;border:1px solid var(--line-strong);display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.diff-doc{border-color:rgba(255,106,87,.5)}
.diff-doc div{display:grid;gap:4px;min-width:0}
.diff-doc b{font-size:12.5px}
.flag,.ok{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;padding:4px 8px;border-radius:6px;background:rgba(255,106,87,.15);color:var(--red)}
.ok{background:rgba(58,214,182,.14);color:var(--accent-2)}
.apply{margin-left:auto;font-weight:600;font-size:12px;background:var(--accent);color:var(--on-accent);padding:6px 12px;border-radius:7px}
.feats{display:grid;gap:12px}
.feat{border:1px solid var(--line-strong);border-radius:14px;padding:20px;background:var(--surface);display:grid;gap:6px}
.feat i{font-style:normal;font-family:var(--mono);font-size:11px;color:var(--accent)}
.feat h3{font-size:22px;letter-spacing:-.03em}
.feat p{color:var(--muted);font-size:15px}
@media (max-width:900px){.dl-grid{grid-template-columns:minmax(0,1fr)}}
"""),

# ---------------------------------------------------------------- Leftova
"leftova": dict(
  title="Leftova Social Ad", name="Leftova",
  kicker="Short-form app ad · Concept",
  tagline="Cook what you <em>already have.</em>",
  summary="A 20-second vertical ad for a concept app that turns a photo of your fridge into meals you can cook right now. Built for Reels, TikTok and Shorts, with the hook landing inside the first second.",
  concept="Self-initiated concept project. Fictional app, not a client.",
  facts=[("Type","Social ad"),("Format","9:16 · 1080×1920 · 60 fps"),("Length","0:20"),("Year","2026"),("Role","Concept, script, illustration, motion"),("Made for","Reels · TikTok · Shorts")],
  duration=20.0, vertical=True,
  chapters=[(0,"Hook"),(2.5,"Snap the fridge"),(7.5,"Pick a meal"),(12.5,"Cook step by step"),(16,"End card")],
  problem="Recipe apps all promise the same thing, and people scroll past app ads in under a second. The ad had to feel like a relatable moment first and an app second.",
  idea="Open on a moment everyone has lived: 7:42 pm, a full fridge and zero ideas. Then show the whole app loop, from scan to meal, in four quick beats, with big type that works with the sound off.",
  beats=[
    (0,"s1","Hook in the first second","“7:42 pm. Fridge: full. Ideas: zero.” A time stamp, a full-bleed tomato-red frame and three punchy lines stop the thumb."),
    (2.5,"s2","Just snap your fridge","A shutter tap, then ingredient detection draws labels around eggs, tomatoes, spinach, feta, lemon and rice. Six ingredients found."),
    (7.5,"s4","Three meals you can cook right now","Swipeable recipe cards: skip the fried rice, land on spinach and feta shakshuka, tagged Tonight’s pick. 18 minutes, uses 5 of your 6."),
    (12.5,"s5","Step by step. No grocery run.","A simmer timer counts down, the step checks off, and the ingredient chips confirm you had everything already."),
    (16,"s6","One clear call to action","The brand lands in forest green with the promise and a single button: Try it free."),
  ],
  special="""
<section class="c-special"><div class="wrap">
  <span class="kicker rv">The whole script</span>
  <h2 class="rv" style="margin-top:14px">31 words. <em>Twenty seconds.</em></h2>
  <p class="lede rv" style="margin-top:14px">Every line on screen, in order. Short-form lives or dies on copy you can read at a glance with the sound off. Tap a line to watch it.</p>
  <ol class="script rv">
    <li><button type="button" data-seek="0"><span>0:00</span><b>7:42 pm.</b></button></li>
    <li><button type="button" data-seek="0.9"><span>0:01</span><b>Fridge: full. Ideas: <mark>zero.</mark></b></button></li>
    <li><button type="button" data-seek="2.5"><span>0:02</span><b>Just <em>snap</em> your fridge.</b></button></li>
    <li><button type="button" data-seek="7.5"><span>0:07</span><b>3 meals you can cook <em>right now.</em></b></button></li>
    <li><button type="button" data-seek="12.5"><span>0:12</span><b>Step by step. <i>No grocery run.</i></b></button></li>
    <li><button type="button" data-seek="16"><span>0:16</span><b>Cook what you <mark>already have.</mark></b></button></li>
    <li><button type="button" data-seek="17.5"><span>0:17</span><b class="pill">Try it free →</b></button></li>
  </ol>
</div></section>""",
  fonts="family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Figtree:wght@400;500;600&family=DM+Mono:wght@400;500",
  style="""
:root{--bg:#fdf3e6;--surface:#fff9f1;--text:#1d2a20;--muted:#6f6657;--line:rgba(60,40,20,.10);--line-strong:rgba(60,40,20,.18);
--accent:#ee4f2d;--accent-2:#1f4d35;--on-accent:#fff;--yellow:#f7c948;--device:#1d2a20;
--display:"Bricolage Grotesque",ui-sans-serif,system-ui,sans-serif;--body:"Figtree",ui-sans-serif,system-ui,sans-serif;--mono:"DM Mono",ui-monospace,Menlo,Consolas,monospace;
--display-weight:800;--display-tracking:-.04em;--em-style:normal;--radius:22px;--shadow:0 30px 70px -35px rgba(120,60,20,.35);color-scheme:light}
.c-hero h1{color:var(--accent)}
.player{background:var(--surface)}
.player.vertical .screen{background:#1d2a20}
.shot.tall{border-color:var(--device)}
.script{list-style:none;margin:40px 0 0;padding:0;display:grid;gap:6px;max-width:820px}
.script button{width:100%;display:grid;grid-template-columns:64px minmax(0,1fr);gap:16px;align-items:baseline;text-align:left;background:none;border:0;border-bottom:1px dashed var(--line-strong);padding:14px 4px;cursor:pointer;transition:background .2s}
.script button:hover{background:rgba(238,79,45,.06)}
.script span{font-family:var(--mono);font-size:13px;color:var(--muted)}
.script b{font-family:var(--display);font-weight:800;letter-spacing:-.03em;font-size:clamp(26px,3.6vw,44px);line-height:1.05}
.script em{font-style:normal;color:var(--accent)}
.script i{font-style:normal;color:var(--accent-2)}
.script mark{background:none;color:var(--accent);font-family:var(--display)}
.script li:nth-child(6) mark{background:var(--yellow);color:var(--accent-2);padding:0 .15em;border-radius:6px}
.script .pill{justify-self:start;display:inline-block;background:var(--yellow);color:var(--accent-2);border-radius:999px;padding:.15em .6em;font-size:clamp(20px,2.6vw,30px)}
"""),

# ---------------------------------------------------------------- Streak '86
"streak86": dict(
  title="Streak '86 Case Study", name="Streak ’86",
  kicker="Mobile UI/UX case study · Concept",
  tagline="A retro habit app built on the <em>discipline</em> of modern fitness apps.",
  summary="A UI/UX case study for a concept habit-tracking app for iOS and Android. The look is 70s track-club warmth, premium rather than costume, and the video walks the whole process from kickoff call to developer handoff.",
  concept="Self-initiated concept project. Fictional app, not a client.",
  facts=[("Type","UI/UX case study"),("Platforms","iOS · Android"),("Length","0:39"),("Year","2026"),("Role","UX flows, UI, design system, motion"),("Tool","Figma")],
  duration=39.0, vertical=False,
  chapters=[(0,"Title"),(3.5,"Kickoff call"),(9.5,"Wireframes → hi-fi"),(15,"Core loop"),(23,"Design system"),(29.5,"Edge cases"),(33.5,"In numbers")],
  problem="Habit apps lose most people in the first week. “Retro” is also easy to get wrong: lean too far and it looks like a costume instead of a product people trust every morning.",
  idea="Design around one daily loop (check in, streak, reward, review) and make the day-7 moment feel earned. Keep the retro warmth in color and type, and keep the structure as disciplined as a modern fitness app.",
  beats=[
    (3.5,"s2","Start with the right questions","The kickoff call ends with five answered questions and a user-flow map: onboarding, pick 3 habits, today, check-in, streak reward, weekly review."),
    (9.5,"s3","Lock the flow, then earn the feeling","Wireframes go to hi-fi with a real feedback round on screen: the client’s comment, my change, and the approval."),
    (15,"s4","Check in. Keep the streak. Feel it.","The core loop in motion: tap to check in, the streak ring fills, the day-7 reward screen bursts in orange, and the weekly stats fill out."),
    (23,"s5","Tokens devs can build from","A Figma design system with color variables for light and dark, a type scale, spacing and radius, 38 components and a tokens.json for developer handoff."),
    (29.5,"s6","Designed, not left to chance","Empty state, offline with saved check-ins, and a forgiving streak freeze instead of a broken streak."),
  ],
  special="""
<section class="c-special"><div class="wrap">
  <div class="stripes" aria-hidden="true"><i></i><i></i><i></i></div>
  <span class="kicker rv">The sprint in numbers</span>
  <div class="nums rv">
    <div><b data-count="52">52</b><span>Mobile screens</span></div>
    <div><b data-count="38">38</b><span>Figma components</span></div>
    <div><b data-count="2">2</b><span>Week design sprint</span></div>
  </div>
  <div class="kick">
    <div class="rv"><span class="kicker">01 · Kickoff call</span><h2 style="margin-top:14px">Five questions before a <em>single pixel.</em></h2>
    <p class="lede" style="margin-top:16px">What I leave every first call with. The answers shape every screen after it.</p></div>
    <ol class="qs rv">
      <li><b>Who is it for?</b><span>Busy 25–40s restarting their routines</span></li>
      <li><b>What is the core loop?</b><span>Check in → streak → reward → review</span></li>
      <li><b>What does “retro” mean here?</b><span>70s track-club warmth. Premium, not costume</span></li>
      <li><b>Which flows and edge cases?</b><span>6 flows, plus empty, error and missed-day states</span></li>
      <li><b>How do we measure success?</b><span>Day-7 retention and daily check-ins</span></li>
    </ol>
  </div>
</div></section>""",
  fonts="family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,800;1,9..144,700;1,9..144,800&family=DM+Sans:wght@400;500;600&family=DM+Mono:wght@400;500",
  style="""
:root{--bg:#16100c;--surface:#211913;--text:#f5ebda;--muted:#ab9b89;--line:rgba(245,235,218,.09);--line-strong:rgba(245,235,218,.17);
--accent:#ec6530;--accent-2:#f2b33a;--teal:#23877c;--on-accent:#1a0f08;
--display:"Fraunces",Georgia,"Times New Roman",serif;--body:"DM Sans",ui-sans-serif,system-ui,sans-serif;--mono:"DM Mono",ui-monospace,Menlo,Consolas,monospace;
--display-weight:800;--display-tracking:-.025em;--em-style:italic;--radius:16px;color-scheme:dark}
body{background:radial-gradient(70% 50% at 90% 0%,rgba(236,101,48,.13),transparent 70%),radial-gradient(60% 50% at 0% 100%,rgba(35,135,124,.10),transparent 70%),var(--bg);background-attachment:fixed}
.c-hero h1{font-style:italic}
.c-hero h1::after{content:"";display:block;height:12px;margin-top:18px;max-width:420px;background:linear-gradient(var(--accent) 0 33%,var(--accent-2) 33% 66%,var(--teal) 66%)}
.stripes{display:grid;gap:4px;margin-bottom:40px}
.stripes i{height:8px;display:block}
.stripes i:nth-child(1){background:var(--accent)}.stripes i:nth-child(2){background:var(--accent-2)}.stripes i:nth-child(3){background:var(--teal)}
.nums{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin:18px 0 clamp(64px,8vw,110px)}
.nums b{display:block;font-family:var(--display);font-weight:800;font-size:clamp(72px,11vw,150px);line-height:.9;letter-spacing:-.04em;font-variant-numeric:tabular-nums}
.nums div:nth-child(2) b{color:var(--accent)}
.nums span{font-family:var(--mono);font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.kick{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:clamp(24px,4vw,64px);align-items:start}
.qs{list-style:none;margin:0;padding:22px 26px;background:#f7efe0;color:#1c140e;border-radius:18px;box-shadow:8px 8px 0 var(--accent);display:grid}
.qs li{display:grid;grid-template-columns:28px minmax(0,1fr);column-gap:12px;padding:14px 0;border-bottom:1px solid rgba(28,20,14,.12)}
.qs li:last-child{border-bottom:0}
.qs li::before{content:"✓";grid-row:1/3;width:24px;height:24px;border-radius:7px;background:var(--teal);color:#fff;display:grid;place-items:center;font-size:13px}
.qs b{font-weight:600;font-size:17px}
.qs span{color:#6b5a4a;font-size:15px}
@media (max-width:900px){.kick{grid-template-columns:minmax(0,1fr)}.nums{grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.nums span{font-size:10px}}
"""),

# ---------------------------------------------------------------- Stillwater
"stillwater": dict(
  title="Stillwater House Retreat Page", name="Stillwater House",
  kicker="Kajabi landing page + booking flow · Concept",
  tagline="A retreat page that <em>fills its own rooms.</em>",
  summary="A retreat landing page designed for Kajabi. Guests read about the retreat, pick a room, register and pay in one flow, and get their confirmation automatically. The video is a designed walkthrough of how the page and booking flow work.",
  concept="Concept project. Fictional brand, AI-generated photography.",
  facts=[("Type","Landing page + booking"),("Platform","Kajabi"),("Length","0:46"),("Year","2026"),("Role","Concept, page design, booking flow, motion"),("Tested on","iPhone SE → desktop")],
  duration=46.5, vertical=False,
  chapters=[(0,"Intro"),(4,"Landing page"),(9,"Choose a room"),(16,"Register & pay"),(23.5,"Confirmation"),(30.5,"Mobile"),(35.5,"Kajabi setup"),(40.5,"End card")],
  problem="Retreat hosts sell a handful of rooms at different prices, often by email and bank transfer. Kajabi can take payments, but it has no room booking built in, and a sold-out room must never be sold twice.",
  idea="Use what Kajabi already does well. One Offer per room type with a quantity limit, custom checkout fields for the details a host needs, and automations for everything after payment. The guest just sees one calm page.",
  beats=[
    (4,"s2","A landing page built from the owner’s content","Hero, dates, what’s included and the rooms, in a quiet editorial style that matches a countryside retreat: “Three quiet days in the Cotswolds.”"),
    (9,"s3","Room selection with real availability","Private room, shared twin priced per bed, and an ensuite suite that is sold out and sends people to a waitlist instead of a dead end."),
    (16,"s4","Register and pay in one flow","The existing Kajabi checkout, with custom fields for dietary needs and arrival, and a clear order summary beside it."),
    (25.5,"s5","The confirmation sends itself","Payment received, guest tagged, confirmation email sent, and a reminder with a packing list goes out 7 days before."),
    (30.5,"s6","Booked from a phone, in a minute","Mobile-first with a sticky Reserve bar, checked on iPhone SE to Pro Max, Pixel, iPad and desktop browsers."),
  ],
  special="""
<section class="c-special"><div class="wrap">
  <span class="kicker rv">Behind the page · Kajabi setup</span>
  <h2 class="rv" style="margin-top:14px">Built on the client’s <em>existing Kajabi.</em></h2>
  <div class="wire rv" role="img" aria-label="Diagram: the retreat page links to three room offers with quantity limits; offers go to a checkout with custom fields, then to tagging and emails; the sold-out suite redirects to a waitlist form.">
    <div class="col"><div class="node dark"><small>Kajabi landing page</small><b>Retreat page</b><span>Hero, what’s included, rooms, FAQ, built from the client’s content</span></div></div>
    <div class="col">
      <div class="node"><small>Offer · qty limit 3</small><b>Private room · £1,450</b><span>Shows rooms left at checkout</span></div>
      <div class="node"><small>Offer · qty limit 4</small><b>Shared twin · £980</b><span>Per-bed availability</span></div>
      <div class="node"><small>Offer · qty limit 1</small><b>Ensuite suite · £1,790</b><span>Limit reached → redirect</span></div>
    </div>
    <div class="col">
      <div class="node"><small>Checkout</small><b>Custom fields</b><span>Dietary needs · arrival · existing payments</span></div>
      <div class="node dashed"><small>Sold-out page</small><b>Waitlist form</b><span>Tags lead · notifies the client</span></div>
    </div>
    <div class="col"><div class="node dark"><small>Automation</small><b>Tag + emails</b><span>Confirmation now, reminder 7 days before</span></div></div>
  </div>
  <div class="qa">
    <div class="rv"><h3>QA checklist in the build plan</h3><ul><li>Test purchases for every room</li><li>Refunds</li><li>Sold-out redirect to the waitlist</li><li>Email delivery</li></ul></div>
    <div class="rv"><h3>Device checklist</h3><ul><li>iPhone SE</li><li>iPhone 16 Pro Max</li><li>Pixel 8 · Chrome</li><li>iPad · Safari</li><li>Desktop · Chrome, Safari, Firefox</li></ul></div>
  </div>
</div></section>""",
  fonts="family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Hanken+Grotesk:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500",
  style="""
:root{--bg:#ede6d9;--surface:#f7f2ea;--text:#1f2620;--muted:#6c685c;--line:rgba(40,45,35,.10);--line-strong:rgba(40,45,35,.2);
--accent:#2f3e31;--accent-2:#a8633f;--sage:#5f7456;--on-accent:#f7f2ea;
--display:"Cormorant Garamond",Garamond,Georgia,serif;--body:"Hanken Grotesk",ui-sans-serif,system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
--display-weight:500;--display-tracking:-.015em;--em-style:italic;--radius:6px;--shadow:0 30px 70px -40px rgba(40,35,20,.4);color-scheme:light}
h1 em,h2 em,.c-hero .tagline em{color:var(--sage)}
.c-hero h1{font-weight:500}
.wire{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(14px,2.5vw,40px);margin-top:44px;align-items:center;position:relative}
.wire .col{display:grid;gap:14px;position:relative}
.wire .col+.col::before{content:"";position:absolute;left:calc(-1 * clamp(14px,2.5vw,40px));width:clamp(14px,2.5vw,40px);top:50%;height:1px;background:var(--line-strong)}
.node{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px;display:grid;gap:3px;box-shadow:0 10px 30px -18px rgba(40,35,20,.35)}
.node small{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent-2)}
.node b{font-weight:600;font-size:16px}
.node span{font-size:13.5px;color:var(--muted);line-height:1.4}
.node.dark{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.node.dark small{color:#c9cfbf}.node.dark span{color:#d6dacd}
.node.dashed{border-style:dashed;border-color:var(--accent-2);background:transparent;box-shadow:none}
.qa{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-top:56px}
.qa h3{font-family:var(--body);font-weight:600;font-size:15px;letter-spacing:0;margin-bottom:12px}
.qa ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.qa li{display:flex;gap:10px;align-items:baseline;font-size:15.5px}
.qa li::before{content:"✓";color:var(--sage);font-weight:600}
@media (max-width:900px){.wire{grid-template-columns:minmax(0,1fr)}.wire .col+.col::before{left:24px;top:-14px;width:1px;height:14px}.qa{grid-template-columns:minmax(0,1fr)}}
"""),
}

PLAY = '<svg viewBox="0 0 24 24"><path d="M7 4l13 8-13 8z"/></svg>'

def page(slug):
    p = PROJECTS[slug]
    i = ORDER.index(slug)
    nxt = ORDER[(i + 1) % len(ORDER)]
    np_ = PROJECTS[nxt]
    mm = lambda t: f"{int(t)//60}:{int(t)%60:02d}"
    facts = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in p["facts"])
    chapters = json.dumps([{"t": t, "label": l} for t, l in p["chapters"]])
    tall = " tall" if p["vertical"] else ""
    beats = "".join(f"""
    <article class="beat rv">
      <button class="shot{tall}" type="button" aria-label="Enlarge still: {title}"><img src="../../assets/work/{slug}-{still}.jpg" alt="{title}, still from the {p['name']} video" loading="lazy"></button>
      <div class="txt"><span class="num">{n:02d} · {mm(t)}</span><h3>{title}</h3><p>{body}</p>
        <button class="jump" type="button" data-seek="{t}">▸ Watch this beat</button></div>
    </article>""" for n, (t, still, title, body) in enumerate(p["beats"], 1))
    cur = ' aria-current="page"'
    idx = "".join(f'<a href="../{s}/" aria-label="{PROJECTS[s]["name"]}"{cur if s == slug else ""}></a>' for s in ORDER)
    skills = {
      "driftlens": ["Motion design","Product demo video","SaaS","UI animation","Explainer video","AI video"],
      "leftova": ["Short-form video","Social media ads","Motion graphics","App promo video","Reels / TikTok","Illustration"],
      "streak86": ["UI/UX design","Mobile app design","Prototyping","Design systems","Wireframing","Gamification"],
      "stillwater": ["Kajabi","Landing page design","Booking flow","Checkout optimisation","Email automation","Mobile responsive"],
    }[slug]
    tools = {"stillwater": ["Code-driven motion (HTML/CSS/JS)","Claude (AI)","AI image generation","ffmpeg"],
             "streak86": ["Figma","Code-driven motion (HTML/CSS/JS)","Claude (AI)","ffmpeg"]}.get(slug, ["Code-driven motion (HTML/CSS/JS)","Claude (AI)","ffmpeg"])
    role = [r.strip()[0].upper()+r.strip()[1:] for r in dict(p["facts"])["Role"].replace(" and ", ", ").split(",")]
    tags = lambda xs: "".join(f'<li class="tag">{x}</li>' for x in xs)
    player_cls = "player vertical" if p["vertical"] else "player"
    rail = '<div class="rail-head"><span class="kicker">Chapters</span></div>' if p["vertical"] else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{p['name']}: {p['kicker']}. Case study by Vipin Sao, AI video &amp; motion designer.">
<meta property="og:title" content="{p['title']} · Vipin Sao">
<meta property="og:image" content="../../assets/work/{slug}.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{p['fonts']}&display=swap">
<link rel="stylesheet" href="../../assets/case.css">
<style>{p['style']}</style>
</head>
<body data-contra="{CONTRA_URL}">
<a class="skip" href="#film">Skip to the video</a>
<header class="c-top">
  <a class="c-back" href="../../#work"><span class="ar" aria-hidden="true">←</span>Vipin Sao</a>
  <nav class="c-idx mono" aria-label="Projects"><span>{i+1:02d} / {len(ORDER):02d}</span>{idx}</nav>
  <a class="c-hire contra-link" href="{CONTRA_URL}" target="_blank" rel="noopener">Hire me</a>
</header>
<main>
  <section class="c-hero wrap">
    <div class="c-hero-grid">
      <div>
        <span class="kicker">{p['kicker']}</span>
        <h1>{p['name']}</h1>
        <p class="tagline">{p['tagline']}</p>
        <p class="lede">{p['summary']}</p>
        <span class="concept">{p['concept']}</span>
      </div>
      <dl class="facts">{facts}</dl>
    </div>
  </section>

  <section class="c-film wrap" id="film" aria-label="The film">
    <div class="{player_cls}" data-chapters='{chapters}' data-duration="{p['duration']}">
      <div class="screen">
        <video src="../../assets/work/{slug}.mp4" poster="../../assets/work/{slug}.jpg" muted playsinline preload="metadata" aria-label="{p['name']} video, {mm(p['duration'])}, no audio"></video>
        <div class="bigplay" aria-hidden="true">{PLAY}</div>
      </div>
      {rail}
      <div class="chaps" aria-label="Chapters"></div>
      <div class="ctrls">
        <button class="cbtn pp" type="button" aria-label="Play">{PLAY}</button>
        <div class="tcode">00:00:00</div>
        <div class="tl" role="slider" tabindex="0" aria-label="Video position" aria-valuemin="0" aria-valuemax="{p['duration']}" aria-valuenow="0"><div class="segs"></div><div class="ph"></div><div class="tip"></div></div>
        <button class="cbtn slow" type="button" aria-pressed="false" title="Half speed, to see the motion detail">0.5×</button>
        <button class="cbtn fs" type="button" aria-label="Fullscreen"><svg viewBox="0 0 24 24"><path d="M3 3h7v2H5v5H3V3zm11 0h7v7h-2V5h-5V3zM3 14h2v5h5v2H3v-7zm16 0h2v7h-7v-2h5v-5z"/></svg></button>
      </div>
    </div>
    <p class="film-note mono"><span>Silent film · captions on screen</span><span class="keys"><kbd>Space</kbd> play · <kbd>←</kbd><kbd>→</kbd> 1s · <kbd>,</kbd><kbd>.</kbd> 1 frame · 0.5× for slow motion</span></p>
  </section>

  <section class="c-brief"><div class="wrap">
    <span class="kicker rv">The brief</span>
    <div class="brief-grid">
      <div class="rv"><h3>The problem</h3><p>{p['problem']}</p></div>
      <div class="rv"><h3>The idea</h3><p>{p['idea']}</p></div>
    </div>
  </div></section>

  <section class="c-beats"><div class="wrap">
    <span class="kicker rv">How the story plays</span>
    <h2 class="rv" style="margin-top:14px">Beat by beat.</h2>
    <div class="beats">{beats}
    </div>
  </div></section>
  {p['special']}
  <section class="c-credits"><div class="wrap credits">
    <div class="rv"><h3>My role</h3><ul>{tags(role)}</ul></div>
    <div class="rv"><h3>Skills</h3><ul>{tags(skills)}</ul></div>
    <div class="rv"><h3>Tools</h3><ul>{tags(tools)}</ul></div>
  </div></section>

  <section class="c-next"><div class="wrap">
    <a class="next" href="../{nxt}/">
      <div class="img"><img src="../../assets/work/{nxt}.jpg" alt="" loading="lazy"></div>
      <div><span class="lbl">Next project</span><h2>{np_['name']} <span class="ar" aria-hidden="true">→</span></h2><p>{np_['kicker']}</p></div>
    </a>
  </div></section>

  <section class="c-cta"><div class="wrap">
    <h2 class="rv">Want one like this for <em>your product?</em></h2>
    <div class="cta-row">
      <a class="btn contra-link" href="{CONTRA_URL}" target="_blank" rel="noopener">Message me on Contra <span aria-hidden="true">→</span></a>
      <a class="btn alt" href="../../#work">See all work</a>
    </div>
  </div></section>
</main>
<footer class="c-foot"><div class="wrap mono"><span>© 2026 Vipin Sao</span><span>AI · Motion · Video</span><a href="../../">Home ↑</a></div></footer>
<script src="../../assets/case.js"></script>
</body>
</html>
"""

for slug in ORDER:
    out = ROOT / "work" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(slug), encoding="utf-8")
    print("wrote", out.relative_to(ROOT))
