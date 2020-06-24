import webbrowser

webbrowser.open("https://www.python.org/",new=1)

# help(webbrowser)
# chrome = webbrowser.get("chrome %s").open("https://www.python.org/")
# for i in range(10):
#     print(1,2,3,4,5,6,7,8,9, sep="; ",end=" ")
safari = webbrowser.get(using='safari')
safari.open("https://www.python.org/")