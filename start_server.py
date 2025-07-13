#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
from threading import Timer

# Server configuration
PORT = 8000
HOST = "localhost"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def open_browser():
    """Open browser after a short delay"""
    url = f"http://{HOST}:{PORT}/snake_game.html"
    print(f"\n🐍 Opening Snake '95 in browser...")
    print(f"🌐 Game URL: {url}")
    try:
        webbrowser.open(url)
    except:
        print(f"Could not automatically open browser. Please visit: {url}")

def main():
    # Change to the directory containing the game files
    os.chdir('/workspace')
    
    # Create server
    with socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler) as httpd:
        print("="*60)
        print("🎮 SNAKE '95 LOCAL SERVER")
        print("="*60)
        print(f"📂 Serving files from: {os.getcwd()}")
        print(f"🌐 Server running at: http://{HOST}:{PORT}/")
        print(f"🐍 Snake Game URL: http://{HOST}:{PORT}/snake_game.html")
        print("="*60)
        print("⌨️  Press Ctrl+C to stop the server")
        print("="*60)
        
        # Open browser after 2 seconds
        Timer(2.0, open_browser).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n\n🛑 Server stopped!")
            print("Thanks for playing Snake '95! 🐍")

if __name__ == "__main__":
    main()