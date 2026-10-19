"""계정과 최근 게시물 반응 숫자를 insights/latest.json 에 저장 (읽기 전용)."""
import json, os, urllib.request, urllib.parse, urllib.error, time
API = "https://graph.instagram.com/v21.0"
TOKEN = os.environ["IG_TOKEN"].strip()

def get(path, **p):
    p["access_token"] = TOKEN
    try:
        with urllib.request.urlopen(f"{API}/{path}?{urllib.parse.urlencode(p)}", timeout=60) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"error": e.read().decode(errors="replace").replace(TOKEN, "***")[:300]}

out = {"checked_at": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())}
out["account"] = get("me", fields="username,account_type,followers_count,follows_count,media_count")
media = get("me/media", fields="id,caption,media_type,timestamp,permalink,like_count,comments_count", limit=10)
out["media"] = []
for m in media.get("data", []):
    m["caption"] = (m.get("caption") or "")[:30]
    ins = {}
    for metric in ["views", "reach", "saved", "shares", "total_interactions"]:
        r = get(f"{m['id']}/insights", metric=metric)
        ins[metric] = r["data"][0]["values"][0]["value"] if r.get("data") else r.get("error", "")[:120]
    m["insights"] = ins
    out["media"].append(m)
os.makedirs("insights", exist_ok=True)
json.dump(out, open("insights/latest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(json.dumps(out, ensure_ascii=False, indent=2))
