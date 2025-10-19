import json

def winrate(wins, loses):
    total = wins + loses
    return f"{wins/total*100:.1f}%" if total > 0 else "0%"

stats = {
    "series_wins": 0, "series_loses": 0,
    "match_wins": 0, "match_loses": 0,
    "bSideW": 0, "bSideL": 0, "rSideW": 0, "rSideL": 0,
    "lp_mid_wins": 0, "lp_mid_loses": 0,
    "lp_adc_wins": 0, "lp_adc_loses": 0
}

def addSeries(result, w, l, bsidew, bsidel, rsidew, rsidel, lpmidw, lpmidl, lpadcw, lpadcl):
    stats["series_wins"] += (result == "w")
    stats["series_loses"] += (result == "l")
    for k, v in zip(["match_wins","match_loses","bSideW","bSideL","rSideW","rSideL","lp_mid_wins","lp_mid_loses","lp_adc_wins","lp_adc_loses"],
                    [w,l,bsidew,rsidew,bsidel,rsidel,lpmidw,lpmidl,lpadcw,lpadcl]):
        stats[k] += v


addSeries("w", 3, 0, 0, 0, 0, 0, 0, 0, 0, 0) #dlcu
addSeries("l", 1, 3, 0, 3, 1, 0, 1, 0, 0, 0) #?
addSeries("w", 2, 1, 1, 0, 1, 0, 0, 0, 0, 0) #sac
addSeries("l", 1, 2, 1, 1, 0, 1, 0, 0, 0, 1) #uvic
addSeries("w",2,1,1,1,1,0,0,0,0,0)#?
addSeries("w",2,0,1,0,1,0,0,0,0,0)#usc
addSeries("l",0,4,0,2,0,0,0,0,0,0)#warmups
addSeries("w",2,0,0,0,2,0,0,0,0,0)#warmups p2

# 4️⃣ Build the HTML string
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>SFU C(UM) Team Stats</title>
</head>
<body>
    <h1 style="text-align: center;">
        <strong>
            <img src="https://html-online.com/editorfiles/tiny/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" />
            SFU C(UM) TEAM STATS
            <img src="https://html-online.com/editorfiles/tiny/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" />
        </strong>
    </h1>

    <h3>WINRATES</h3>
    <p>SERIES W/R: <strong>{winrate(stats['series_wins'], stats['series_loses'])} ({stats['series_wins']}-{stats['series_loses']})</strong></p>
    <p>MATCHES W/R: <strong>{winrate(stats['match_wins'], stats['match_loses'])} ({stats['match_wins']}-{stats['match_loses']})</strong></p>
    <p>RED SIDE W/R: <strong>{winrate(stats['rSideW'], stats['rSideL'])} ({stats['rSideW']}-{stats['rSideL']})</strong></p>
    <p>BLUE SIDE W/R: <strong>{winrate(stats['bSideW'], stats['bSideL'])} ({stats['bSideW']}-{stats['bSideL']})</strong></p>
    <p>LAST PICK MID W/R: <strong>{winrate(stats['lp_mid_wins'], stats['lp_mid_loses'])} ({stats['lp_mid_wins']}-{stats['lp_mid_loses']})</strong></p>
    <p>LAST PICK ADC W/R: <strong>{winrate(stats['lp_adc_wins'], stats['lp_adc_loses'])} ({stats['lp_adc_wins']}-{stats['lp_adc_loses']})</strong></p>

    <h3><strong>CHAMPION STATS</strong></h3>
    <p>wip</p>
</body>
</html>
"""

# 5️⃣ Save it to index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)