import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# تحميل متغيرات البيئة من ملف .env
load_dotenv()

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح التشفير (آمن من .env أو مفتاح افتراضي)
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-ضع_مفتاحك_الخاص_هنا')

# وضع التصحيح حسب بيئة التشغيل
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# السماح للمضيفين الموثوقين، مثل Render و localhost
ALLOWED_HOSTS = [
    'h11-2iku.onrender.com',  # رابط Render
    'localhost',
    '127.0.0.1'
]

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'store',
    'orders',

    'cloudinary',
    'cloudinary_storage',
]

# الميدلوير
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# إعدادات المسارات
ROOT_URLCONF = 'h11.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'h11.wsgi.application'

# إعداد قاعدة البيانات من متغير البيئة
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600
    )
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# إعداد الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'h11' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# إعداد الوسائط باستخدام Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dgvoyuawe',
    'API_KEY': '155166337516544',
    'API_SECRET': 'gJJN1t6KXbyiSyPwVMR3gAYrh_I',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# الحقل التلقائي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
