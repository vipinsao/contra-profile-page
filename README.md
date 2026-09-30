# Vipin Sao, AI Video & Motion Designer

Landing page for my Contra profile: showreel, services, process and contact.

- `index.html`: the home page (showreel, selected work, services, process, contact)
- `work/<project>/`: one case-study page per project (Driftlens, Leftova, Streak '86, Stillwater House)
- `assets/`: web-encoded videos, stills and covers, plus `case.css` / `case.js` shared by the case studies
- `_build/build_cases.py`: generates the case-study pages. Edit the project text there, then run `python3 _build/build_cases.py`

To change the Contra link, edit `CONTRA_URL` in `index.html` and in `_build/build_cases.py` (then re-run the build).
