from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="Black Project V3 Core")

# 🐾 إعدادات السيطرة (HATTTAN Admin)
# حط التوكن والآيدي حقك هنا يا شريك
BOT_TOKEN = "ضع_التوكن_هنا"
CHAT_ID = "ضع_الآيدي_هنا"

# 🔑 نظام حماية المفاتيح (HWID-based)
AUTHORIZED_KEYS = {
    "PANTHER-VIP-HATTTAN": {"role": "VIP", "name": "HATTTAN"},
    "USER-DEMO-123": {"role": "User", "name": "Guest"}
}

def send_panther_alert(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"🐾 [BLACK PROJECT V3]\n{msg}"}
    try: requests.post(url, json=payload)
    except: print("Alert Error")

@app.on_event("startup")
async def startup():
    send_panther_alert("⚡ نظام الفهد الأسود استيقظ.. السيرفر المركزي يعمل بنجاح.")

@app.get("/")
def home():
    return {"status": "Active", "owner": "HATTTAN"}

@app.get("/auth/{key}")
async def validate_key(key: str):
    if key in AUTHORIZED_KEYS:
        user = AUTHORIZED_KEYS[key]
        alert = f"👑 دخول المالك: {user['name']}" if user["role"] == "VIP" else f"👤 دخول مشترك: {user['name']}"
        send_panther_alert(alert)
        return {"status": "Access Granted", "role": user["role"], "welcome": user["name"]}
    
    send_panther_alert(f"⚠️ محاولة اختراق بمفتاح خاطئ: {key}")
    raise HTTPException(status_code=403, detail="Access Denied")
