<h1>Instagram and TikTok saver</h1>

<p>This is a Telegram bot that helps you get content from Instagram and TikTok. Simply send the bot a link to an Instagram or TikTok post and it will send you the post’s content along with its caption and author nickname.</p>

<h2>Getting Started</h2>

<p>Before using the bot, you need to configure the <code>.env</code> file. It should contain all the environment variables used in the <code>main.py</code> file.</p>
<ul>
<li><p><b>TOKEN:</b> You can obtain it by creating a new bot using <a href=“https://t.me/botfather”>BotFather</a> on Telegram.</p></li>

<pre><code>TOKEN = 9876543210:AbC1D2Ef3GHI4KlMnYwzabcdeFGhi567jK</code></pre>

<li><p><b>WEBHOOK_HOST:</b> This is the URL of your webhook. It should be accessible from the internet and capable of receiving incoming requests from Telegram servers. You can use your own domain or obtain a free subdomain from a service like <a href="https://ngrok.com/">ngrok</a>.</p></li>

<pre><code>WEBHOOK_HOST = https://1a94-12-345-678-910.eu.ngrok.io</code></pre>

<li><p><b>WEBHOOK_PATH:</b> This is the path to your webhook on the server. It is appended to the WEBHOOK_HOST to form the full webhook URL. Typically, it is just <code>/webhook</code>.</p></li>

<pre><code>WEBHOOK_PATH = /webhook</code></pre>

<li><p><b>WEBAPP_HOST:</b> This is the IP address on which your server will listen for incoming connections. Usually, it is set to <code>0.0.0.0</code>, which means the server will accept connections from any IP address.</p></li>

<pre><code>WEBAPP_HOST = 0.0.0.0</code></pre>

<li><p><b>WEBAPP_PORT:</b> This is the port on which your server will listen for incoming connections. You can use any available port, but commonly used ports range from 8300 to 8499.</p></li>

<pre><code>WEBAPP_PORT = 8321</code></pre>
</ul>
</p>These variables are used to configure the webhook and start the server to receive updates from Telegram. You need to provide the correct values for these variables to ensure your bot works correctly.</p>











<h2>Example Usage</h2>

<h3>Getting Content from TikTok</h3>

<p>To get content from a TikTok post, simply send the bot a message with the link to the TikTok post. For example:</p>

<pre><code>https://www.tiktok.com/@nick_name/video/12345678910</code></pre>

<p>The bot will then reply with the content and caption of that TikTok post.</p>

<h3>Getting Content from Instagram</h3>

<p>To get content from an Instagram post, simply send the bot a message with the link to the Instagram post. For example:</p>

<pre><code>https://www.instagram.com/reel/AbCd-Q4wEr1/?igshid=MzqlQDB4N2FlZB==</code></pre>

<p>The bot will then reply with the content and caption of that Instagram post.</p>


<h2>Dependencies</h2>

<p>This bot requires the following Python libraries to be installed:</p>

- Python 3.6 or higher
- [instaloader](https://instaloader.github.io/) library
- [aiogram](https://docs.aiogram.dev/) library
- [aiohttp](https://docs.aiohttp.org/) library

<p>To install the dependencies required for this bot, you can utilize the  <code>requirements.txt</code> file in the directory. </p>
<p>Simply run the following command:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<h2>Running the Bot</h2>

<p>To run the bot, simply execute the Python script:</p>

<pre><code>python3 bot.py</code></pre>

<p>The bot will then start running and will be ready to receive messages.</p>