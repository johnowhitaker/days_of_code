# Days Of Code
> A '100 days of code' style learning project


The goal here is to write small bits of code every weekday. I'm going to try and keep everything in Jupyter notebooks so that I can use NBDev to manade documenting it all and sharing code between days in case I want to build more complex things using building blocks from previous days.

If we're making changes to those files a lot, autoreload comes in handy:

```python
%load_ext autoreload
%autoreload 2
```

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload


Here's a demo function defined in another notebook:

```python
demo_code() # Code defined in 00_core.ipynb, exported to 'core.py' and imported at the top of this NB
```




    'demo'



```python
hw_cairo('this should work')
```


![png](docs/images/output_5_0.png)


Today is a Saturday - but I'm keen to get started and at least lay the foundation so that on Monday I can jump right in rather than starting with all the setup (although it was nice and easy thanks to NBDev - thanks team!)
