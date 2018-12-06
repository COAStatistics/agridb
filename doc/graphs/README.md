## Install django-extensions

```
$ pip install django-extensions
```

## Install pygraphviz

```
$ pip install pygraphviz
```

## Enable django_extensions

```
INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)
```

## Create graphs via apps

```
$ python manage.py graph_models -e -g -l dot -o livestock.png livestock
$ python manage.py graph_models -e -g -l dot -o welfare.png welfare
$ python manage.py graph_models -e -g -l dot -o smallbig.png smallbig
$ python manage.py graph_models -e -g -l dot -o household.png household
$ python manage.py graph_models -e -g -l dot -o fallow.png fallow
$ python manage.py graph_models -e -g -l dot -o disaster.png disaster
$ python manage.py graph_models -e -g -l dot -o smallbig.png smallbig
```

## References

* [django-extensions](https://github.com/django-extensions/django-extensions)
* [graph_models.md](https://gist.github.com/rg3915/35e999a442a8955e455b)