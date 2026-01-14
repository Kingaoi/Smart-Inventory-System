# 🛒 Smart Inventory System (v1.0)
### مشروع نظام إدارة المخزون الذكي

---

## 🌍 Language / اللغة
* [English](#english-version)
* [العربية](#النسخة-العربية)

---

## <a name="english-version"></a> 🇺🇸 English Version

### 📝 Project Overview
A professional Python-based Inventory and Point of Sale (POS) system. It manages user authentication, product entry, and generates a formatted receipt with real-time discounts and timestamps.

### 🧠 Logic & Core Features (By Developer)
The core logic was designed and structured by the developer, including:
* **The Authentication Logic:** A `while` loop managing security attempts.
* **Guest vs. User Mode:** A conditional system to grant different access levels.
* **Data Collection:** Building lists for product names and prices using `while` and `try/except`.
* **Discount Logic:** A business rule that applies 15% off if items exceed 3 or total exceeds $50.

### 🛠️ Technical Enhancements (Assisted by Gemini)
To elevate the code to a professional level, the following was added:
* **Professional Terminology:** Replacing casual phrases with formal business English (e.g., *Inventory Count, Access Granted, Subtotal*).
* **Security Feedback:** Adding the `remaining` attempts counter for a better user experience.
* **Visual UI (ANSI Colors):** Implementing a color-coded system (Red for errors, Green for success, Yellow for totals).
* **Real-time Timestamping:** Integrating the `datetime` module to stamp receipts with the exact local time.
* **Formatting:** Using `.center()` and f-string alignments for a clean output.

---

## <a name="النسخة-العربية"></a> 🇸🇦 النسخة العربية

### 📝 نبذة عن المشروع
نظام إدارة مخزون ومبيعات متكامل بلغة بايثون. يقوم النظام بإدارة تسجيل الدخول، إدخال المنتجات، وإصدار فاتورة منسقة تحتوي على خصومات فورية وختم زمني.

### 🧠 المنطق البرمجي والميزات الأساسية (جهد المطور)
تم بناء الهيكل والمنطق البرمجي بالكامل من قبل المطور، ويشمل ذلك:
* **منطق التحقق:** حلقة `while` التي تدير محاولات الدخول الأمنية.
* **نظام الصلاحيات:** التفريق بين وضع "الضيف" و"المسؤول".
* **جمع البيانات:** بناء مصفوفات لتخزين الأسماء والأسعار باستخدام `try/except` لمنع الانهيار.
* **منطق الخصم:** قاعدة تجارية تطبق خصم 15% إذا زاد عدد المنتجات عن 3 أو زاد المجموع عن 50.

### 🛠️ التحسينات التقنية (بمساعدة Gemini)
لرفع كفاءة الكود إلى المستوى الاحترافي، تم إضافة:
* **المصطلحات المهنية:** تبديل العبارات البسيطة بمصطلحات أعمال رسمية (مثل: *Subtotal, Grand Total*).
* **نظام التنبيه الذكي:** إضافة عداد المحاولات المتبقية `remaining` لتحسين تجربة المستخدم.
* **الواجهة الملونة (ANSI):** تلوين المخرجات (الأحمر للأخطاء، الأخضر للنجاح، والأصفر للمبالغ).
* **الختم الزمني:** ربط مكتبة `datetime` لطباعة الوقت والتاريخ الحقيقي على الفاتورة.
* **تنسيق المخرجات:** استخدام دالة `.center()` وتنسيق النصوص لتظهر كفاتورة حقيقية.

---

## 🚀 How to Run / كيف تشغل البرنامج
1. Copy the code into a file named `Smart-Inventory-System.py`.
2. Open your terminal/command prompt.
3. Run: `python Smart-Inventory-System.py`

---

#### 👨‍💻 Developer / المطور
**Malik Al-Anfous (Kingaoi)**

### 💡 Note for Visitors / ملاحظة للزوار:
* **EN:** This is my first comprehensive project in Python. I am currently a beginner exploring the world of coding. I welcome any feedback, notes, or suggestions to improve my logic and coding style.
* **AR:** هذا هو مشروعي المتكامل الأول بلغة بايثون. أنا حالياً في بداية رحلتي لاستكشاف عالم البرمجة، وأرحب جداً بأي ملاحظات، نصائح، أو اقتراحات لتطوير مهاراتي وتحسين أسلوب كتابتي للكود.

---
*Connect with me on GitHub:* [Kingaoi](https://github.com/Kingaoi)
