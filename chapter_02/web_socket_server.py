from aiohttp import web
import socketio

socket_io = socketio.AsyncServer()
app = web.Application()
socket_io.attach(app)


async def index(request):
    await web.Response(text="Hello world from socketio", content_type="text/html")


@socket_io.on("message")
def print_message(socket_id, data):
    print(f"Socket ID: {socket_id}")
    print(f"Data: {data}")


app.router.add_get("/", index)

if __name__ == "__main__":
    web.run_app(app)
