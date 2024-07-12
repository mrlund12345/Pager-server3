from flask import Flask, request, render_template, redirect, url_for
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}


@app.route('/')
def index():
    return '''
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ArYan don here</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

  <style>
    body{
      background-color: #f8f9fa;
    }
    .container{
      max-width: 500px;
      background-color: #fff;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
    .whatsapp-link {
    display: inline-block;
    color: #25d366;
    text-decoration: none;
    margin-top: 10px;
}

.whatsapp-link i {
    margin-right: 5px;
}

  </style>
</head>
<body>
  <header class="header mt-4">
    <h2 class="mb-3">☠ ||| ꜱᴇʀᴠᴇʀ ᴀᴄᴛɪᴠᴇ ||| ☠</h2>
    <img src="/static/images/logo.jpg" alt="ArYan web server" width="300px">
    <h1 class="mt-3">♛ Fuck Tha all server ♛ </h1>
  </header>

  <div class="container">
    <form action="/convo" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="id">Enter Inbox/Convo Id:</label>
        <input type="text" class="form-control" id="id" name="id" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Messages File:</label>
        <input type="file" class="form-control" id="txtFile" name="msgFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="txtFile2">Select Tokens File:</label>
        <input type="file" class="form-control" id="txtFile2" name="tokFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time">Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" name="submit" class="btn btn-primary btn-submit">Submit</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; 2024 Anonymous urf ArYan All Rights Reserved.</p>

    <p>Made with by <a href="https://www.facebook.com/mr.be0001&mibextid=ZbWKwL">FT = ArYan don</a></p>
    <div class="mb-3">
        <a href="https://wa.me/+918824167482" class="whatsapp-link">
            <i class="fab fa-whatsapp"></i> Chat on WhatsApp
        </a>
    </div>
  </footer>
</body>
</html>'''


@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        access_tokens = txt_file.read().decode().splitlines()

        messages_file = request.files['messagesFile']
        messages = messages_file.read().decode().splitlines()

        num_comments = len(messages)
        max_tokens = len(access_tokens)

        post_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
        haters_name = mn
        speed = time_interval

        while True:
            try:
                for message_index in range(num_comments):
                    token_index = message_index % max_tokens
                    access_token = access_tokens[token_index]

                    message = messages[message_index].strip()

                    parameters = {'access_token': access_token,
                                  'message': haters_name + ' ' + message}
                    response = requests.post(
                        post_url, json=parameters, headers=headers)

                    current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                    if response.ok:
                        print("[+] SEND SUCCESSFUL No. {} Convo {}  time{}: Token No.{}".format(
                            message_index + 1, post_url, token_index + 1, haters_name + ' ' + message))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    else:
                        print("[x] Failed to send Convo No. {} Convo {} Token No. {}: {}".format(
                            message_index + 1, post_url, token_index + 1, haters_name + ' ' + message))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    time.sleep(speed)
            except Exception as e:
              
                      
                print(e)
                time.sleep(30)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
