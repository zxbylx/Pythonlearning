# TypeError: argument of type 'WindowsPath' is not iterable

将setitng里的代码改一下：

```bash
'NAME': BASE_DIR / 'db.sqlite3',
1
```

改为

```bash
'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
1
```

之后便是：

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
    }
}
123456
```

问题解决