# import socket
#
# HOST = ''  # 모든 IP 주소에서 접속 허용
# PORT = 8000
#
#
# def update_html(message):
#     html_content = f"""<!doctype html>
# <html>
# <head>
#     <title>Message Received</title>
#     <meta charset="utf-8" />
#     <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <style type="text/css">
#     body {{
#         background-color: #f0f0f2;
#         margin: 0;
#         padding: 0;
#         font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
#     }}
#     div {{
#         width: 600px;
#         margin: 5em auto;
#         padding: 2em;
#         background-color: #fdfdff;
#         border-radius: 0.5em;
#         box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
#     }}
#     a:link, a:visited {{
#         color: #38488f;
#         text-decoration: none;
#     }}
#     @media (max-width: 700px) {{
#         div {{
#             margin: 0 auto;
#             width: auto;
#         }}
#     }}
#     </style>
# </head>
# <body>
#     <div>
#         <h1>Message Received</h1>
#         <p>{message}</p>
#     </div>
# </body>
# </html>"""
#
#     with open("index.html", "w") as f:
#         f.write(html_content)
#
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     print(f"Server listening on port {PORT}")
#
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             print('Connected by', addr)
#             data = conn.recv(1024)
#             if data:
#                 message = data.decode().strip()
#                 print("Received:", message)
#                 if message.startswith("mipmip"):
#                     # 메시지에서 숫자 추출
#                     number = message[len("mipmip"):]
#                     response = f"lablab{number}"
#                     conn.sendall(response.encode())
#                     print("Sent:", response)
#                     update_html(message)

#////////////////////////웹페이지연동/////////////////////////////
# import socket
# import threading
# import queue
# from http.server import SimpleHTTPRequestHandler, HTTPServer
# import os
#
# TCP_HOST = ''  # 모든 IP 주소에서 접속 허용
# TCP_PORT = 8000  # TCP 포트는 8000
# HTTP_PORT = 8001  # HTTP 포트는 8001로 변경
#
# message_queue = queue.Queue()
#
# def update_html(message):
#     html_content = f"""<!doctype html>
# <html>
# <head>
#     <title>Message Received</title>
#     <meta charset="utf-8" />
#     <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <style type="text/css">
#     body {{
#         background-color: #f0f0f2;
#         margin: 0;
#         padding: 0;
#         font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
#     }}
#     div {{
#         width: 600px;
#         margin: 5em auto;
#         padding: 2em;
#         background-color: #fdfdff;
#         border-radius: 0.5em;
#         box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
#     }}
#     a:link, a:visited {{
#         color: #38488f;
#         text-decoration: none;
#     }}
#     @media (max-width: 700px) {{
#         div {{
#             margin: 0 auto;
#             width: auto;
#         }}
#     }}
#     </style>
# </head>
# <body>
#     <div>
#         <h1>Message Received</h1>
#         <p>{message}</p>
#     </div>
# </body>
# </html>"""
#
#     with open("index.html", "w") as f:
#         f.write(html_content)
#
# class TCPHandler(threading.Thread):
#     def __init__(self, conn, addr):
#         threading.Thread.__init__(self)
#         self.conn = conn
#         self.addr = addr
#
#     def run(self):
#         with self.conn:
#             print('Connected by', self.addr)
#             data = self.conn.recv(1024)
#             if data:
#                 message = data.decode().strip()
#                 print("Received:", message)
#                 if message.startswith("mipmip"):
#                     number = message[len("mipmip"):]
#                     response = f"lablab{number}"
#                     self.conn.sendall(response.encode())
#                     print("Sent:", response)
#                     message_queue.put(message)
#                     update_html(message)
#
# def tcp_server():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((TCP_HOST, TCP_PORT))
#         s.listen()
#         print(f"TCP Server listening on port {TCP_PORT}")
#
#         while True:
#             conn, addr = s.accept()
#             handler = TCPHandler(conn, addr)
#             handler.start()
#
# class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/':
#             self.path = '/index.html'
#         return SimpleHTTPRequestHandler.do_GET(self)
#
# def http_server():
#     os.chdir('.')  # Ensure the server is serving from the current directory
#     httpd = HTTPServer((TCP_HOST, HTTP_PORT), MyHTTPRequestHandler)
#     print(f"HTTP server running on port {HTTP_PORT}")
#     httpd.serve_forever()
#
# if __name__ == "__main__":
#     tcp_thread = threading.Thread(target=tcp_server)
#     tcp_thread.start()
#
#     http_thread = threading.Thread(target=http_server)
#     http_thread.start()
#
#     tcp_thread.join()
#     http_thread.join()

#///////////////////////자동 새로고침


# import socket
# import threading
# import queue
# from http.server import SimpleHTTPRequestHandler, HTTPServer
# import os
#
# TCP_HOST = ''  # 모든 IP 주소에서 접속 허용
# TCP_PORT = 8000  # TCP 포트는 8000
# HTTP_PORT = 8001  # HTTP 포트는 8001로 설정
#
# message_queue = queue.Queue()
#
# def update_html(message):
#     html_content = f"""<!doctype html>
# <html>
# <head>
#     <title>Message Received</title>
#     <meta charset="utf-8" />
#     <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <style type="text/css">
#     body {{
#         background-color: #f0f0f2;
#         margin: 0;
#         padding: 0;
#         font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
#     }}
#     div {{
#         width: 600px;
#         margin: 5em auto;
#         padding: 2em;
#         background-color: #fdfdff;
#         border-radius: 0.5em;
#         box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
#     }}
#     a:link, a:visited {{
#         color: #38488f;
#         text-decoration: none;
#     }}
#     @media (max-width: 700px) {{
#         div {{
#             margin: 0 auto;
#             width: auto;
#         }}
#     }}
#     </style>
#     <script type="text/javascript">
#         // 5초마다 페이지 새로고침
#         setInterval(function() {{
#             window.location.reload();
#         }}, 5000);
#     </script>
# </head>
# <body>
#     <div>
#         <h1>Message Received</h1>
#         <p>{message}</p>
#     </div>
# </body>
# </html>"""
#
#     with open("index.html", "w") as f:
#         f.write(html_content)
#
# class TCPHandler(threading.Thread):
#     def __init__(self, conn, addr):
#         threading.Thread.__init__(self)
#         self.conn = conn
#         self.addr = addr
#
#     def run(self):
#         try:
#             with self.conn:
#                 print('Connected by', self.addr)
#                 data = self.conn.recv(1024)
#                 if data:
#                     message = data.decode().strip()
#                     print("Received:", message)
#                     if message.startswith("mipmip"):
#                         number = message[len("mipmip"):]
#                         response = f"lablab{number}"
#                         self.conn.sendall(response.encode())
#                         print("Sent:", response)
#                         message_queue.put(message)
#                         update_html(message)
#         except Exception as e:
#             print(f"Exception handling client {self.addr}: {e}")
#
# class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
#     def do_GET(self):
#         try:
#             if self.path == '/':
#                 self.path = '/index.html'
#             return SimpleHTTPRequestHandler.do_GET(self)
#         except ConnectionAbortedError:
#             print("Connection aborted by client")
#         except Exception as e:
#             print(f"Exception during GET request: {e}")
#
# def tcp_server():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((TCP_HOST, TCP_PORT))
#         s.listen()
#         print(f"TCP Server listening on port {TCP_PORT}")
#
#         while True:
#             conn, addr = s.accept()
#             handler = TCPHandler(conn, addr)
#             handler.start()
#
# def http_server():
#     os.chdir('.')  # Ensure the server is serving from the current directory
#     httpd = HTTPServer((TCP_HOST, HTTP_PORT), MyHTTPRequestHandler)
#     print(f"HTTP server running on port {HTTP_PORT}")
#     try:
#         httpd.serve_forever()
#     except KeyboardInterrupt:
#         print("Server stopped by user")
#     except Exception as e:
#         print(f"Exception in HTTP server: {e}")
#
# if __name__ == "__main__":
#     tcp_thread = threading.Thread(target=tcp_server)
#     tcp_thread.start()
#
#     http_thread = threading.Thread(target=http_server)
#     http_thread.start()
#
#     tcp_thread.join()
#     http_thread.join()


#///////////////////////큐와 뮤텍스 추가


# import socket
# import threading
# import queue
# from http.server import SimpleHTTPRequestHandler, HTTPServer
# import os
#
# TCP_HOST = ''  # 모든 IP 주소에서 접속 허용
# TCP_PORT = 8000  # TCP 포트는 8000
# HTTP_PORT = 8001  # HTTP 포트는 8001로 설정
#
# message_queue = queue.Queue()
# lock = threading.Lock()
#
# def update_html(message):
#     html_content = f"""<!doctype html>
# <html>
# <head>
#     <title>Message Received</title>
#     <meta charset="utf-8" />
#     <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1" />
#     <style type="text/css">
#     body {{
#         background-color: #f0f0f2;
#         margin: 0;
#         padding: 0;
#         font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
#     }}
#     div {{
#         width: 600px;
#         margin: 5em auto;
#         padding: 2em;
#         background-color: #fdfdff;
#         border-radius: 0.5em;
#         box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
#     }}
#     a:link, a:visited {{
#         color: #38488f;
#         text-decoration: none;
#     }}
#     @media (max-width: 700px) {{
#         div {{
#             margin: 0 auto;
#             width: auto;
#         }}
#     }}
#     </style>
#     <script type="text/javascript">
#         // 5초마다 페이지 새로고침
#         setInterval(function() {{
#             window.location.reload();
#         }}, 5000);
#     </script>
# </head>
# <body>
#     <div>
#         <h1>Message Received</h1>
#         <p>{message}</p>
#     </div>
# </body>
# </html>"""
#
#     with open("index.html", "w") as f:
#         f.write(html_content)
#
# class TCPHandler(threading.Thread):
#     def __init__(self, conn, addr):
#         threading.Thread.__init__(self)
#         self.conn = conn
#         self.addr = addr
#
#     def run(self):
#         try:
#             with self.conn:
#                 print('Connected by', self.addr)
#                 data = self.conn.recv(1024)
#                 if data:
#                     message = data.decode().strip()
#                     print("Received:", message)
#                     if message.startswith("mipmip"):
#                         number = message[len("mipmip"):]
#                         response = f"lablab{number}"
#                         self.conn.sendall(response.encode())
#                         print("Sent:", response)
#                         with lock:
#                             message_queue.put(message)
#         except Exception as e:
#             print(f"Exception handling client {self.addr}: {e}")
#
# class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
#     def do_GET(self):
#         try:
#             if self.path == '/':
#                 self.path = '/index.html'
#             return SimpleHTTPRequestHandler.do_GET(self)
#         except ConnectionAbortedError:
#             print("Connection aborted by client")
#         except Exception as e:
#             print(f"Exception during GET request: {e}")
#
# def tcp_server():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((TCP_HOST, TCP_PORT))
#         s.listen()
#         print(f"TCP Server listening on port {TCP_PORT}")
#
#         while True:
#             conn, addr = s.accept()
#             handler = TCPHandler(conn, addr)
#             handler.start()
#
# def http_server():
#     os.chdir('.')  # Ensure the server is serving from the current directory
#     httpd = HTTPServer((TCP_HOST, HTTP_PORT), MyHTTPRequestHandler)
#     print(f"HTTP server running on port {HTTP_PORT}")
#     try:
#         httpd.serve_forever()
#     except KeyboardInterrupt:
#         print("Server stopped by user")
#     except Exception as e:
#         print(f"Exception in HTTP server: {e}")
#
# def html_updater():
#     while True:
#         message = message_queue.get()
#         with lock:
#             update_html(message)
#
# if __name__ == "__main__":
#     tcp_thread = threading.Thread(target=tcp_server)
#     tcp_thread.start()
#
#     http_thread = threading.Thread(target=http_server)
#     http_thread.start()
#
#     updater_thread = threading.Thread(target=html_updater)
#     updater_thread.start()
#
#     tcp_thread.join()
#     http_thread.join()
#     updater_thread.join()

#//////////////////////키보드 강종 추가

import socket
import threading
import queue
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import keyboard

TCP_HOST = ''  # 모든 IP 주소에서 접속 허용
TCP_PORT = 8000  # TCP 포트는 8000
HTTP_PORT = 8001  # HTTP 포트는 8001로 설정

message_queue = queue.Queue()
lock = threading.Lock()

# 서버 중지 플래그
stop_event = threading.Event()

def update_html(message):
    html_content = f"""<!doctype html>
<html>
<head>
    <title>Message Received</title>
    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {{
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
    }}
    div {{
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }}
    a:link, a:visited {{
        color: #38488f;
        text-decoration: none;
    }}
    @media (max-width: 700px) {{
        div {{
            margin: 0 auto;
            width: auto;
        }}
    }}
    </style>
    <script type="text/javascript">
        // 5초마다 페이지 새로고침
        setInterval(function() {{
            window.location.reload();
        }}, 5000);
    </script>
</head>
<body>
    <div>
        <h1>Message Received</h1>
        <p>{message}</p>
    </div>
</body>
</html>"""

    with open("index.html", "w") as f:
        f.write(html_content)

class TCPHandler(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr

    def run(self):
        try:
            with self.conn:
                print('Connected by', self.addr)
                data = self.conn.recv(1024)
                if data:
                    message = data.decode().strip()
                    print("Received:", message)
                    if message.startswith("mipmip"):
                        number = message[len("mipmip"):]
                        response = f"lablab{number}"
                        self.conn.sendall(response.encode())
                        print("Sent:", response)
                        with lock:
                            message_queue.put(message)
        except Exception as e:
            print(f"Exception handling client {self.addr}: {e}")

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/':
                self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)
        except ConnectionAbortedError:
            print("Connection aborted by client")
        except Exception as e:
            print(f"Exception during GET request: {e}")

def tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((TCP_HOST, TCP_PORT))
        s.listen()
        print(f"TCP Server listening on port {TCP_PORT}")

        while not stop_event.is_set():
            conn, addr = s.accept()
            handler = TCPHandler(conn, addr)
            handler.start()

def http_server():
    os.chdir('.')  # Ensure the server is serving from the current directory
    httpd = HTTPServer((TCP_HOST, HTTP_PORT), MyHTTPRequestHandler)
    print(f"HTTP server running on port {HTTP_PORT}")
    try:
        while not stop_event.is_set():
            httpd.handle_request()
    except KeyboardInterrupt:
        print("Server stopped by user")
    except Exception as e:
        print(f"Exception in HTTP server: {e}")

def html_updater():
    while not stop_event.is_set():
        message = message_queue.get()
        with lock:
            update_html(message)

def stop_server():
    print("Stopping server...")
    stop_event.set()

if __name__ == "__main__":
    tcp_thread = threading.Thread(target=tcp_server)
    tcp_thread.start()

    http_thread = threading.Thread(target=http_server)
    http_thread.start()

    updater_thread = threading.Thread(target=html_updater)
    updater_thread.start()

    print("Press 'q' to stop the server")
    keyboard.wait('q')
    stop_server()

    tcp_thread.join()
    http_thread.join()
    updater_thread.join()
