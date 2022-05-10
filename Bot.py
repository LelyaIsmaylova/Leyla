<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta http-equiv="Content-Style-Type" content="text/css"/>
<meta name="generator" content="Aspose.Words for .NET 22.5.0"/>
<title/>
<style type="text/css">body { font-family:'Times New Roman'; font-size:12pt }p { margin:0pt }</style>
</head>
<body>
<div>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">bot_token = "default"</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">api_token = "default"</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># key</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">user_city = "Москва"</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># initial city</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">user_city_coords = ('55.7504461', '37.6174943')</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">bot = telebot.TeleBot(bot_token)</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">def city_coords(city: str):</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># returns coordinates of input city in format (latitude, longitude)</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">geolocator = geocoders.Nominatim(user_agent="telebot")</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">latitude = str(geolocator.geocode(city).latitude)</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">longitude = str(geolocator.geocode(city).longitude)</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">return latitude, longitude</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">def get_weather(latitude, longitude, token: str):</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># receives latitude and longitude of the city and returns forecast</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly,alerts&units=metric&lang=ru&appid={token}"</span>
<span style="font-family:'Courier New'; -aw-import:spaces">   </span>
<span style="font-family:'Courier New'"># line</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">request = get(url)</span>
<span style="font-family:'Courier New'; -aw-import:spaces">   </span>
<span style="font-family:'Courier New'"># need an answer</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">data = loads(request.text)</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast = dict()</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['current'] = dict()</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['daily'] = dict()</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># dict in the dict in the massive in the dict</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">params = ['dt', 'temp', 'pressure', 'humidity', 'clouds', 'uvi']</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">for param in params:</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['current'][param] = data['current'][param]</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['current']['weather'] = data['current']['weather'][0]['description']</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">for param in params:</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['daily'][param] = data['daily'][1][param]</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># 0 - is today's forecast, 1 - is tomorrow's forecast</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['daily']['weather'] = data['daily'][1]['weather'][0]['description']</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['timezone_offset'] = data['timezone_offset']</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">return forecast</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">@bot.message_handler(commands=['start'])</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">def start(message):</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># greeting message</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">button = telebot.types.KeyboardButton("Привет 👋")</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">markup.add(button)</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я найду прогноз погоды для указанного города!"</span>
</p>
<p style="text-indent:132.3pt; font-size:10.5pt">
<span style="font-family:'Courier New'">.format(message.from_user), reply_markup=markup)</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">@bot.message_handler(commands=['city'])</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">def city(message):</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># button "/city" function</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">send = bot.send_message(message.chat.id, "Введите город:")</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">bot.register_next_step_handler(send, set_city)</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">def set_city(message):</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># input city</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">global user_city, user_city_coords</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">text = message.text.title()</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">text = text.replace("-", " ")</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">if not text.replace(" ", '').isalpha():</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">send = bot.send_message(message.chat.id, "Неверный формат ввода, используйте кириллицу или латиницу."</span>
</p>
<p style="text-indent:308.75pt; font-size:10.5pt">
<span style="font-family:'Courier New'">"В качестве разделителей в названии используйте пробелы и дефисы.")</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">bot.register_next_step_handler(send, set_city)</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">return</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">try:</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">user_city = text</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">user_city_coords = city_coords(user_city)</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">bot.send_message(message.chat.id, "Установлен город: {0}".format(user_city))</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">except AttributeError:</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">user_city = "Москва"</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">user_city_coords = ('55.7504461', '37.6174943')</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">bot.send_message(message.chat.id, "Проверьте ввод. Данная локация не найдена...")</span>
</p>
<p style="text-indent:50.4pt; font-size:10.5pt">
<span style="font-family:'Courier New'">bot.send_message(message.chat.id, "Установлен город по умолчанию: Москва")</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">@bot.message_handler(commands=['weather'])</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">def send_weather(message):</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># button "/weather" function</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">global user_city, user_city_coords, api_token</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">lat, lon = user_city_coords</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast = get_weather(lat, lon, api_token)</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># tuple</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">current_time = int(forecast['current']['dt']) + int(forecast['timezone_offset'])</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">tomorrow_time = int(forecast['daily']['dt']) + int(forecast['timezone_offset'])</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">current_time = datetime.utcfromtimestamp(current_time).strftime('%d.%m.%Y %H:%M')</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">tomorrow_time = datetime.utcfromtimestamp(tomorrow_time).strftime('%d.%m.%Y')</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['current']['pressure'] = str(int(forecast['current']['pressure']) * 0.75)</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['daily']['pressure'] = str(int(forecast['daily']['pressure']) * 0.75)</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['current']['weather'] = forecast['current']['weather'].capitalize()</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">forecast['daily']['weather'] = forecast['daily']['weather'].capitalize()</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">bot.send_message(message.chat.id, f"Погода в городе {user_city}:\n\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Координаты: ({lat}; {lon})\n\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Местные дата и время: {current_time}\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Температура: {forecast['current']['temp']} °C\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Давление: {forecast['current']['pressure']} мм рт. ст.\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Влажность: {forecast['current']['humidity']}%\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"УФ-индекс: {forecast['current']['uvi']}\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"{forecast['current']['weather']}\n\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Завтра({tomorrow_time}) ожидается:\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Минимальная температура: {forecast['daily']['temp']['min']} °C\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Максимальная температура: {forecast['daily']['temp']['max']} °C\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Утренняя температура: {forecast['daily']['temp']['morn']} °C\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Дневная температура: {forecast['daily']['temp']['day']} °C\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Вечерняя температура: {forecast['daily']['temp']['eve']} °C\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Ночная температура: {forecast['daily']['temp']['night']} °C\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Давление: {forecast['daily']['pressure']} мм рт. ст.\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Влажность: {forecast['daily']['humidity']}%\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"УФ-индекс: {forecast['daily']['uvi']}\n"</span>
</p>
<p style="text-indent:239.45pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"{forecast['daily']['weather']}")</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">@bot.message_handler(commands=['check'])</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">def check_city(message):</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># button "/check" function</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">global user_city</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">bot.send_message(message.chat.id, f"Текущий город: {user_city}")</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">@bot.message_handler(content_types=['text'])</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'">def default_reply(message):</span>
<span style="font-family:'Courier New'; -aw-import:spaces">  </span>
<span style="font-family:'Courier New'"># keyboard's interface</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">button1 = telebot.types.KeyboardButton("/city")</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">button2 = telebot.types.KeyboardButton("/weather")</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">button3 = telebot.types.KeyboardButton("/check")</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">markup.add(button1, button2, button3)</span>
</p>
<p style="text-indent:25.2pt; font-size:10.5pt">
<span style="font-family:'Courier New'">bot.send_message(message.chat.id,</span>
</p>
<p style="text-indent:132.3pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"Введите: \n"</span>
</p>
<p style="text-indent:132.3pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"/city, чтобы указать город\n"</span>
</p>
<p style="text-indent:132.3pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"/weather, чтобы посмотреть погоду в указанном городе (город по умолчанию: Москва)\n"</span>
</p>
<p style="text-indent:132.3pt; font-size:10.5pt">
<span style="font-family:'Courier New'">f"/check, чтобы проверить, какой город сейчас выбран",</span>
</p>
<p style="text-indent:132.3pt; font-size:10.5pt">
<span style="font-family:'Courier New'">reply_markup=markup)</span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
<p style="font-size:10.5pt">
<span style="font-family:'Courier New'; -aw-import:ignore"> </span>
</p>
</div>
</body>
</html>