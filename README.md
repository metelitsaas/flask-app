# flask-app

Run:
```
uwsgi --ini app/uwsgi.ini --enable-threads
```

Test:
```
curl -v http://0.0.0.0:8000/api/v1/
curl -v -u admin:admin http://0.0.0.0:8000/api/v1/test_data/
```
