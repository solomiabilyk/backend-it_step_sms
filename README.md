# School Management System (SMS) — Backend

Цей проєкт є бекенд-частиною системи управління школою, розробленою на Django REST Framework. Система дозволяє керувати філіями, студентами, абонементами, розкладом занять та відвідуваністю з гнучким розмежуванням прав доступу (Адміністратор / Викладач).

## 🚀 Стек технологій
* **Framework:** Django 6.0 + Django REST Framework (DRF)
* **Database:** PostgreSQL 16
* **WSGI Server:** Gunicorn 22.0
* **Containerization:** Docker / Docker Compose
* **Authentication:** JWT (SimpleJWT) / Session Auth

---

## 🛠️ Швидкий запуск через Docker (Рекомендовано)

Проєкт повністю контейнеризований. База даних, міграції та вебсервер запускаються автоматично однією командою.

### 1. Клонуйте репозиторій
```bash
git clone <https://github.com/solomiabilyk/backend-it_step_sms.git>
cd backend-it_step_sms