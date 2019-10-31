from django.shortcuts import render

def home(request):
 moise = {
  "title":"this is home page",
  "this is true":True,
  "my_number":123445,
  "my_list":[123,456,789,978,"abc"],
  "my_html":"<h1>hello world</h2>"

 }
 return render(request, 'home/home.html', moise)
