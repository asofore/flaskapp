# استخدم صورة Ubuntu كبداية
FROM ubuntu:22.04

# تثبيت Python وpip
RUN apt-get update && apt-get install -y python3 python3-pip

# إنشاء مجلد العمل
WORKDIR /app

# نسخ ملفات المتطلبات ثم تثبيتها
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# نسخ باقي الملفات الخاصة بالتطبيق
COPY . .

# تعريف الأمر الذي يتم تنفيذه عند تشغيل الحاوية
CMD ["python3", "main.py"]
