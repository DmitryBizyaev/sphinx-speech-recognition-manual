from http.server import *
import json
from sphinx_speech_recognition import decode_audio_file


# обработка GET и POST запросов
class Handler(BaseHTTPRequestHandler):

    # обработка GET запроса
    def do_GET(self): 
        
        # Sending success response code 200
        self.send_response(200)
        self.send_header('content-type', 'text/html') 
        self.end_headers() 
          
        self.wfile.write('<h1>Server is running</h1>'.encode()) 

    # обработка POST запроса
    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        self.wfile.write(f'\n\n -- Content length: {content_length}\n\n\n'.encode('utf-8'))

        print ("content_length: " + str(content_length))
        post_data = self.rfile.read(content_length)

        file_name = "received_data_test.wav" 

        try:
            with open(file_name, 'wb') as file:
                file.write(post_data)

            print("Audio file written")

            response_message = decode_audio_file(file_name)
            print("Audio file transcribed")
        except Exception as e:
            response_message = f"Error saving data: {str(e)}"
        
        

        # Send a response back
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header("Access-Control-Allow-Origin", '*')
        self.end_headers()
        self.wfile.write(response_message.encode('utf-8'))
        print(response_message.encode('utf-8'))
        print("response send")
  
port = HTTPServer(('', 5000), Handler)

print("Server is running")
  
port.serve_forever()
port.server_close()

print("Server stopped")