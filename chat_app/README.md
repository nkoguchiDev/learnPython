# django チュートリアル

## 環境セットアップ

### python仮想環境作成

```sh
python -m venv .venv
source .venv/bin/activate
```

### 依存関係のインストール

```sh
pip install -r requirements.txt
```

### プロジェクトの作成

```sh
django-admin startproject project
```

### モデルの作成

```sh
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001
python manage.py migrate
```

### superuserの作成

```sh
python manage.py createsuperuser
```

### アプリ起動

```sh
python manage.py runserver
```

### テストの実行

```sh
python manage.py test polls
```

### 新しいアプリの作成

```sh
python manage.py startapp app_name
```
