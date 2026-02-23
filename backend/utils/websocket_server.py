"""WebSocket server for real-time mobile latency monitoring."""
import asyncio
import threading
import websockets

# Global list to store latency values from mobile clients
mobile_latency_data = []


async def handle_mobile_ping(websocket):
    """Handle incoming WebSocket messages (latency pings from mobile)."""
    async for message in websocket:
        try:
            latency = float(message)
            from datetime import datetime
            mobile_latency_data.append((datetime.now(), latency))
            # Keep only last 100 entries
            if len(mobile_latency_data) > 100:
                mobile_latency_data.pop(0)
            print(f"📱 Mobile latency: {latency:.2f} ms")
        except ValueError:
            pass


async def websocket_server():
    """Run the WebSocket server indefinitely."""
    async with websockets.serve(handle_mobile_ping, "0.0.0.0", 8765):
        await asyncio.Future()  # keep running forever


def start_ws_server():
    """Start WebSocket server in a separate event loop."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(websocket_server())


# Start WebSocket server in a daemon thread
_ws_thread = threading.Thread(target=start_ws_server, daemon=True)
_ws_thread.start()
