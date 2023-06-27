<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>CS GO Discount Monitor Bot</title>
</head>
<body>
  <h1>CS GO Discount Monitor Bot</h1>
  <p>This is a Telegram bot designed to monitor the CS GO weapon skin market for discounts. Currently, it supports 8 categories: gloves, knives, pistols, submachine guns, shotguns, assault rifles, sniper rifles, and machine guns. However, the list of categories can be expanded thanks to the project's convenient structure.</p>
    <h2>Dependencies</h2>
  <ul>
    <li>Python 3.8 or newer</li>
    <li>aiogram 3</li>
    <li>aiohttp</li>
    <li>python-dotenv</li>
  </ul>
    <p>You can install them manually if you haven't already, or use the command <code>make install</code> to install them. The bot can also be run through Makefile using the command <code>make run</code>.</p>
  <h2>Getting Started</h2>
  <p>Before running the bot, you need to create a <code>.env</code> file to store the Telegram bot token. You can obtain the token from <a href=“https://t.me/botfather”>BotFather</a> in Telegram.</p>
  <p>Example:</p>
  <pre><code>TOKEN = 9876543210:AbC1D2Ef3GHI4KlMnYwzabcdeFGhi567jK</code></pre>
  <p>After adding the token, you can start using the bot.</p>
  </b><h3>Discount Percentage</h3></b>
  <p>By default, the minimum discount value is set to 10%. You can use the <code>/discount</code> command to view the current value or change it.</p>
  <b><h3>Price Thresholds</h3></b>
  <p>The bot also has minimum and maximum price thresholds for searching. You can familiarize yourself with them or modify them by using the <code>/min</code> and <code>/max</code> commands respectively.</p>
  <h2>Collecting Market Information</h2>
  <p>To start gathering information from the CS GO skin market, you can enter the <code>/find</code> command or select it from the bot's menu. Then, click the button corresponding to the category you're interested in. Alternatively, you can simply send the bot a relevant keyword for the desired category in the chat, and it will start collecting data immediately.</p>
</body>
</html>