<strong><h1>OLX Crawler</h1></strong>
<p>The script is designed to extract data from advertisement pages using the Selenium library. It is intended for educational and informational purposes only. To reduce the risk of being blocked by OLX, the crawler's speed is reduced to approximately 1 ad per minute.</p>
<p>The script is used to extract the following data:</p>

<ul>
  <li>Advertisement URL</li>
  <li>Title</li>
  <li>Description</li>
  <li>Publication date</li>
  <li>URLs of all available photos in the ad</li>
  <li>Price</li>
  <li>Seller's name</li>
  <li>Phone number</li>
</ul>
<h2>Getting Started</h2>
<p>Before using the script, you need to:</p>

<ol>
  <li>Install the dependencies. You can do this by running the command <pre><code>pip install -r requirements.txt</code></pre>
  <p>or</p>
  <pre><code>make install</code></pre></li>
  <li>Create a <code>.env</code> file in the <b>olx_selenium_parser</b> folder with variables for your OLX account <b>login</b> and <b>password</b>.</li>
  <pre><code>LOGIN = JohnDoe@gmail.com
PASSWORD = JohnDoe2023</code></pre>
  <li>Download the web browser driver you're using. <p>After downloading, extract the driver from its folder and place it in the <code>driver</code> folder. <b>The code was written and tested on MSEdge browser.</b> If you're using a different browser, you'll need to make slight changes to the code (replace the <code>Edge()</code> and <code>EdgeOptions()</code> class calls with the corresponding ones for your browser and web driver).</p></li>
</ol>
<h2>Example Usage</h2>
<p>Once you've added the web driver and installed all the dependencies, you can run the code and enter the URL of your search query in the console, for example:</p>
<pre><code>https://www.olx.ua/d/uk/transport/legkovye-avtomobili/irpen/?currency=UAH</code></pre>

<p>After that, the code will start its execution (<u>if you have correctly chosen the web driver</u>). All the found links for the given query will be collected and saved in a <code>.txt</code> file in the <b>result</b> folder. Later, in the same folder, you'll find a file with the collected data in <code>JSON</code> format, which will be updated as the script progresses.</p>

<p><b>Once again, I want to emphasize that the script is written solely for educational purposes!</b></p>
