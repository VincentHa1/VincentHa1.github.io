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

with open("data.json", "w") as f:
    json.dump(stats, f)