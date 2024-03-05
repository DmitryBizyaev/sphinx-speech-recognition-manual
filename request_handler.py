from http.server import *
from sphinx_speech_recognition import decode_audio_file


# обработка запросов
class Handler(BaseHTTPRequestHandler):

    # обработка GET запроса
    def do_GET(self): 
        
        # ответная отправка "успешного" запроса
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<h1>Server is running</h1>'.encode())


    # обработка POST запроса
    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        print ("content_length: " + str(content_length))
        post_data = self.rfile.read(content_length)

        file_name = "received_data.wav" 

        try:
            with open(file_name, 'wb') as file:
                file.write(post_data)

            print("\naudio file written")

            response_message = decode_audio_file(file_name)
            print("\naudio file transcribed")

        except Exception as e:
            response_message = f"\nerror saving data: {str(e)}"
        
        

        # отправка ответного POST запроса с расшифровкой аудио файла
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header("Access-Control-Allow-Origin", '*')
        self.end_headers()
        self.wfile.write(response_message.encode('utf-8'))
        print(response_message.encode('utf-8'))
        print("\nresponse sent")


    # обработка OPTIONS запроса
    def do_OPTIONS(self):
        
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


def main():

    port = HTTPServer(('', 5000), Handler)
    print("\nserver is running")
      
    port.serve_forever()
    port.server_close()
    
    print("\nserver stopped")


if __name__ == "__main__":
    main()