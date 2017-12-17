import http.server
import subprocess

#Type the ip address of the machine you want to close into HOST_NAME
HOST_NAME=''
PORT_NUMBER = 80

class ServerHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        shutdown_button = "<button onclick='Shutdown()' style='height:250px;width:150px'>Shutdown!</button> <script>function Shutdown(){window.location.href = '/shutdown';}</script>"
        cancelshutdown_button = "<button onclick='Cancel()' style='height:250px;width:150px'>Cancel!</button> <script>function Cancel(){window.location.href = '/cancel';}</script>"
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(shutdown_button.encode('utf-8'))
        self.wfile.write(cancelshutdown_button.encode('utf-8'))
        if(self.path=='/shutdown'):
            subprocess.Popen("shutdown /s /t 60",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)

        elif(self.path=='/cancel'):
            subprocess.Popen("shutdown /a",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)


if __name__ == "__main__":
    myserver  =http.server.HTTPServer
    httpobj = myserver((HOST_NAME,PORT_NUMBER),ServerHandler)

    try:
        httpobj.serve_forever()
    except:
        print("sth wrong...")
        httpobj.server_close()
