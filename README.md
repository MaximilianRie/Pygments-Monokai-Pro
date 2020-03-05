# Pygments-Monokai-Pro
Add custom Styles to Pygments like this take on miming "Monokai Pro" (for IPython)

Add the monokai_pro.py file to ```pygments/styles/```
If you want to make your own style just duplicate on of the builin styles and edit it. Make sure to rename the class name!

Edit the pygments/styles/\_\_init\_\_.py file and add a map to your freshly created style to the STYLE_MAP dict like this:
```'displayNameOfStyle': 'submoduleNameOfStyle::ClassNameOfStyle',```

Now you should be able to access this syntax highlighter style by adding 
```c.TerminalInteractiveShell.highlighting_style = "displayNameOfStyle"``` to your IPython config

or by calling 
```%config TerminalInteractiveShell.highlighting_style = "displayNameOfStyle"```  inside of IPython

In this particular example it should look like the Demo.png in the repo.
