import requests
import socket
import time

# --- Configuration ---
URL = "https://gold-voice.onrender.com/api/gold"
UDP_IP = "127.0.0.1"     # Target IP (localhost)
UDP_PORT = 54321         # Must match netreceive port
INTERVAL_SECONDS = 3     # How often to fetch & send
# ---------------------

def fetch_and_send_price():
    try:
        # Fetch JSON
        resp = requests.get(URL, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        price = data.get("price")
        if price is None:
            print("Price not found in JSON:", data)
            return

        # Prepare message: just the number as string
        message = str(price)
        message_bytes = message.encode('utf-8')

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message_bytes, (UDP_IP, UDP_PORT))

        print(f"[{time.strftime('%H:%M:%S')}] Sent price {price} to {UDP_IP}:{UDP_PORT}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Starting price → UDP stream")
    while True:
        fetch_and_send_price()
        time.sleep(INTERVAL_SECONDS)